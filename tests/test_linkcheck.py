import json
import re
import subprocess
import sys
from contextlib import contextmanager
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread

import pytest

from scripts.linkcheck import (
    baseline_patterns,
    prepare_baseline,
    read_report,
    summarize,
)

ROOT = Path(__file__).resolve().parents[1]


def write_report(path, records):
    path.write_text("".join(json.dumps(record) + "\n" for record in records))


@pytest.mark.parametrize("status", ["working", "broken", "redirected", "ignored"])
def test_exact_external_urls(tmp_path, status):
    url = "https://example.org/docs_(v1)?a=1&b=2"
    report = tmp_path / "output.json"
    write_report(
        report,
        [
            {"uri": url, "status": status},
            {"uri": url, "status": status},
            {"uri": "/local/file", "status": "working"},
            {"uri": "mailto:docs@example.org", "status": "unchecked"},
        ],
    )
    patterns = baseline_patterns(report)
    assert len(patterns) == 1
    assert re.match(patterns[0], url)
    for other in (
        url + "#missing-anchor",
        url + "&new=value",
        url + "/new-page",
        url.replace("example.org", "exampleXorg"),
        url + "\n",
        "/local/file",
    ):
        assert not re.match(patterns[0], other)


@pytest.mark.parametrize(
    "content", ["not JSON", "[]", "null", "{}", '{"uri": 1, "status": "broken"}']
)
def test_invalid_reports(tmp_path, content):
    report = tmp_path / "output.json"
    report.write_text(content)
    with pytest.raises(ValueError, match="output.json:1:"):
        read_report(report)


def test_missing_and_empty_reports(tmp_path):
    report = tmp_path / "output.json"
    with pytest.raises(FileNotFoundError):
        read_report(report)
    report.write_text("\n")
    assert baseline_patterns(report) == []


def test_summary(tmp_path):
    report, summary = tmp_path / "output.json", tmp_path / "summary.md"
    write_report(
        report,
        [
            {"uri": "https://example.org/ok", "status": "working"},
            {"uri": "https://example.org/<bad>", "status": "broken", "info": "404"},
            {"uri": "https://example.org/slow", "status": "timeout"},
        ],
    )
    summary.write_text("Existing summary\n")
    summarize(report, summary)
    text = summary.read_text()
    assert text.startswith("Existing summary\n")
    assert "2 failing URLs" in text
    assert "&lt;bad&gt;" in text
    assert "https://example.org/slow" in text
    assert "https://example.org/ok" not in text


@pytest.fixture
def server():
    requests = []

    class Handler(BaseHTTPRequestHandler):
        def do_HEAD(self):
            requests.append(self.path)
            self.send_response(200 if self.path.startswith("/ok") else 404)
            self.end_headers()

        def log_message(self, *args):
            pass

    with ThreadingHTTPServer(("127.0.0.1", 0), Handler) as http:
        thread = Thread(target=http.serve_forever, daemon=True)
        thread.start()
        try:
            yield f"http://127.0.0.1:{http.server_port}", requests
        finally:
            http.shutdown()
            thread.join()


def documentation(directory, text, *, base=False):
    source = directory / "source"
    source.mkdir()
    configuration = (
        "import os, sys\n"
        f"sys.path.insert(0, {str(ROOT)!r})\n"
        "from pathlib import Path\n"
        "from scripts.linkcheck import baseline_patterns\n"
        "linkcheck_ignore = []\n"
        "if baseline := os.getenv('LINKCHECK_BASELINE'):\n"
        "    linkcheck_ignore = baseline_patterns(Path(baseline))\n"
        "linkcheck_retries = 1\n"
        "linkcheck_timeout = 2\n"
    )
    if base:
        configuration += (
            "assert not os.getenv('LINKCHECK_BASELINE')\n"
            "assert not os.getenv('LINKCHECK_BASE_REF')\n"
        )
    (source / "conf.py").write_text(configuration)
    (source / "index.rst").write_text("Links\n=====\n\n" + text)
    return source


def sphinx(source, output):
    return subprocess.run(
        [
            sys.executable,
            "-m",
            "sphinx",
            "-q",
            "-b",
            "linkcheck",
            "-d",
            str(output / "doctrees"),
            str(source),
            str(output),
        ],
        capture_output=True,
        text=True,
        check=False,
    )


def test_sphinx_checks_only_new_urls(tmp_path, server, monkeypatch):
    url, requests = server
    monkeypatch.delenv("LINKCHECK_BASELINE", raising=False)
    source = documentation(tmp_path, f"{url}/old-broken\n\n{url}/ok\n")
    full = tmp_path / "full"
    assert sphinx(source, full).returncode == 1
    assert "/old-broken" in requests

    monkeypatch.setenv("LINKCHECK_BASELINE", str(full / "output.json"))
    requests.clear()
    with (source / "index.rst").open("a") as stream:
        stream.write(f"\n{url}/ok?new\n")
    result = sphinx(source, tmp_path / "filtered")
    assert result.returncode == 0, result.stdout + result.stderr
    assert requests == ["/ok?new"]

    requests.clear()
    with (source / "index.rst").open("a") as stream:
        stream.write(f"\n{url}/new-broken\n")
    assert sphinx(source, tmp_path / "new-broken").returncode == 1
    assert "/new-broken" in requests
    assert "/old-broken" not in requests


def git(*args):
    return subprocess.check_output(["git", *args], text=True).strip()


@contextmanager
def repository(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    git("init", "-q")
    git("add", "source")
    git(
        "-c",
        "user.name=Test",
        "-c",
        "user.email=test@example.org",
        "commit",
        "-qm",
        "Docs",
    )
    yield git("rev-parse", "HEAD")
    assert git("worktree", "list", "--porcelain").count("worktree ") == 1


def test_generate_baseline_and_reuse_cache(tmp_path, server, monkeypatch):
    url, requests = server
    documentation(tmp_path, f"{url}/old-broken\n", base=True)
    report = tmp_path / "cache" / "baseline.jsonl"
    with repository(tmp_path, monkeypatch) as base:
        monkeypatch.setenv("LINKCHECK_BASELINE", "must-not-be-read")
        monkeypatch.setenv("LINKCHECK_BASE_REF", "must-not-be-read")
        prepare_baseline(base, report)
        assert read_report(report)[0]["uri"] == f"{url}/old-broken"
        assert "/old-broken" in requests
        requests.clear()
        prepare_baseline(base, report)
        assert not requests


def test_baseline_failure_cleans_up_worktree(tmp_path, monkeypatch):
    source = documentation(tmp_path, "No links.\n")
    (source / "conf.py").write_text("raise RuntimeError('broken configuration')\n")
    with repository(tmp_path, monkeypatch) as base:
        report = tmp_path / "baseline.jsonl"
        with pytest.raises(subprocess.CalledProcessError):
            prepare_baseline(base, report)
        assert not report.exists()


def test_fetch_baseline_in_shallow_checkout(tmp_path, server, monkeypatch):
    url, _ = server
    original = tmp_path / "original"
    original.mkdir()
    source = documentation(original, f"{url}/old-broken\n", base=True)
    with repository(original, monkeypatch) as base:
        (source / "index.rst").write_text("Current\n=======\n\nNo links.\n")
        git("add", "source")
        git(
            "-c",
            "user.name=Test",
            "-c",
            "user.email=test@example.org",
            "commit",
            "-qm",
            "Change docs",
        )
        checkout = tmp_path / "shallow"
        git("clone", "--depth=1", original.as_uri(), str(checkout))
        with monkeypatch.context() as context:
            context.chdir(checkout)
            with pytest.raises(subprocess.CalledProcessError):
                git("cat-file", "-e", base)
            report = tmp_path / "baseline.jsonl"
            prepare_baseline(base, report)
            assert read_report(report)[0]["uri"] == f"{url}/old-broken"
            assert git("worktree", "list", "--porcelain").count("worktree ") == 1
