"""Prepare exact-URL linkcheck baselines and summarize monitoring reports."""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


def read_report(path: Path) -> list[dict]:
    """Read Sphinx's JSONL report, rejecting unusable cache entries."""
    records = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{number}: invalid JSON") from exc
        if (
            not isinstance(record, dict)
            or not isinstance(record.get("uri"), str)
            or not record["uri"]
            or not isinstance(record.get("status"), str)
        ):
            raise ValueError(f"{path}:{number}: invalid linkcheck record")
        records.append(record)
    return records


def baseline_patterns(path: Path) -> list[str]:
    """Ignore known external URLs, without ignoring new suffixes or local links."""
    urls = {
        record["uri"]
        for record in read_report(path)
        if record["uri"].startswith(("http://", "https://"))
    }
    print(f"Linkcheck baseline: {len(urls)} known external URLs from {path}")
    return [r"\A" + re.escape(url) + r"\Z" for url in sorted(urls)]


def copy_report(source: Path, destination: Path) -> None:
    read_report(source)
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, destination)


def prepare_baseline(base: str, report: Path) -> None:
    """Use the cached report or generate one at the exact base revision."""
    if not re.fullmatch(r"[0-9a-f]{40}", base):
        raise ValueError("The linkcheck base must be a full Git commit SHA")
    if report.exists():
        read_report(report)
        print(f"Linkcheck baseline cache hit: {base}")
        return

    print(f"Linkcheck baseline cache miss: generating report for {base}", flush=True)
    if subprocess.run(
        ["git", "cat-file", "-e", f"{base}^{{commit}}"],
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    ).returncode:
        subprocess.run(
            ["git", "fetch", "--no-tags", "--depth=1", "origin", base], check=True
        )

    with tempfile.TemporaryDirectory(prefix="linkcheck-baseline-") as directory:
        temporary = Path(directory)
        checkout = temporary / "checkout"
        output = temporary / "report"
        subprocess.run(
            ["git", "worktree", "add", "--detach", str(checkout), base], check=True
        )
        try:
            env = os.environ.copy()
            env.pop("LINKCHECK_BASELINE", None)
            env.pop("LINKCHECK_BASE_REF", None)
            result = subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "sphinx",
                    "-b",
                    "linkcheck",
                    "-d",
                    str(temporary / "doctrees"),
                    "-n",
                    "-W",
                    "--keep-going",
                    "source",
                    str(output),
                ],
                cwd=checkout,
                env=env,
                check=False,
            )
            # Sphinx returns 1 for broken links or warnings. Those do not change
            # which URLs existed at the base revision; a report is still required.
            if result.returncode not in (0, 1):
                result.check_returncode()
            copy_report(output / "output.json", report)
        finally:
            subprocess.run(
                ["git", "worktree", "remove", "--force", str(checkout)], check=True
            )


def summarize(report: Path, summary: Path) -> None:
    records = read_report(report)
    failures = [r for r in records if r["status"] in {"broken", "timeout"}]
    lines = ["## Full linkcheck", "", f"{len(failures)} failing URLs.", ""]
    for record in failures:
        uri = html.escape(record["uri"])
        info = html.escape(str(record.get("info", record["status"]))).replace("\n", " ")
        lines.append(f"- <code>{uri}</code>: {info}")
    with summary.open("a", encoding="utf-8") as stream:
        stream.write("\n".join(lines) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    prepare = commands.add_parser("prepare")
    prepare.add_argument("--base", required=True)
    prepare.add_argument("--report", type=Path, required=True)
    publish = commands.add_parser("publish")
    publish.add_argument("--report", type=Path, required=True)
    publish.add_argument("--baseline", type=Path, required=True)
    summary = commands.add_parser("summarize")
    summary.add_argument("--report", type=Path, required=True)
    summary.add_argument("--summary", type=Path, required=True)
    args = parser.parse_args()
    if args.command == "prepare":
        prepare_baseline(args.base, args.report.resolve())
    elif args.command == "publish":
        copy_report(args.report, args.baseline)
    else:
        summarize(args.report, args.summary)


if __name__ == "__main__":
    main()
