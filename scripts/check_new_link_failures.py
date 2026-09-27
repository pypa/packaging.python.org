"""Fail when Sphinx reports a URL added by the current PR as broken."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path

URL_RE = re.compile(r"https?://[^\s<>()\[\]{}\"']+")
TRAILING_PUNCTUATION = ".,;:!?`"


def _added_urls(base: str) -> set[str]:
    result = subprocess.run(
        [
            "git",
            "diff",
            "--unified=0",
            "--diff-filter=AM",
            f"{base}...HEAD",
            "--",
            "source",
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    urls: set[str] = set()
    for line in result.stdout.splitlines():
        if not line.startswith("+") or line.startswith("+++"):
            continue
        for match in URL_RE.findall(line[1:]):
            urls.add(match.rstrip(TRAILING_PUNCTUATION))
    return urls


def _broken_urls(report: Path) -> dict[str, str]:
    if not report.is_file():
        raise SystemExit(f"linkcheck report not found: {report}")

    broken: dict[str, str] = {}
    for number, raw_line in enumerate(
        report.read_text(encoding="utf-8").splitlines(), 1
    ):
        if not raw_line.strip():
            continue
        try:
            record = json.loads(raw_line)
        except json.JSONDecodeError as exc:
            raise SystemExit(f"invalid JSON in {report} line {number}: {exc}") from exc
        if record.get("status") != "broken":
            continue
        uri = record.get("uri")
        if isinstance(uri, str):
            broken[uri] = str(record.get("info") or "broken")
    return broken


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", required=True, help="PR base commit SHA")
    parser.add_argument("--report", type=Path, default=Path("build/output.json"))
    args = parser.parse_args()

    added = _added_urls(args.base)
    if not added:
        print("No newly added HTTP(S) links found in source/. ")
        return 0

    broken = _broken_urls(args.report)
    failures = {url: broken[url] for url in sorted(added & broken.keys())}
    if not failures:
        print(f"All {len(added)} newly added HTTP(S) link(s) passed Sphinx linkcheck.")
        return 0

    print("Broken links introduced by this PR:")
    for url, info in failures.items():
        print(f"- {url}: {info}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
