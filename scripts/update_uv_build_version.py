# /// script
# requires-python = ">= 3.12"
# dependencies = [
#     "httpx>=0.28.1,<0.29",
#     "packaging>=25.0",
# ]
# ///
import os
import re
from pathlib import Path

import httpx
from packaging.utils import parse_wheel_filename
from packaging.version import Version


def main():
    response = httpx.get(
        "https://pypi.org/simple/uv-build/",
        headers={"Accept": "application/vnd.pypi.simple.v1+json"},
    )
    response.raise_for_status()
    data = response.json()
    current_release = None
    for file in data["files"]:
        if not file["filename"].endswith(".whl"):
            continue
        _name, version, _build, _tags = parse_wheel_filename(file["filename"])
        if version.is_prerelease:
            continue
        if current_release is None or version > current_release:
            current_release = version

    [major, minor, _patch] = current_release.release
    if major != 0:
        raise NotImplementedError("The script needs to be updated for uv 1.x")
    upper_bound = Version(f"{major}.{minor + 1}.{0}")

    repository_root = Path(__file__).parent.parent
    existing = repository_root.joinpath(
        "source/shared/build-backend-tabs.rst"
    ).read_text()
    replacement = f'requires = ["uv_build >= {current_release}, <{upper_bound}"]'
    searcher = re.compile(re.escape('requires = ["uv_build') + ".*" + re.escape('"]'))
    if not searcher.search(existing):
        raise RuntimeError("Could not `uv-build` entry")
    updated = searcher.sub(replacement, existing)

    if existing != updated:
        print("Updating source/shared/build-backend-tabs.rst")
        Path("source/shared/build-backend-tabs.rst").write_text(updated)
        if github_output := os.environ.get("GITHUB_OUTPUT"):
            with open(github_output, "a") as f:
                f.write(f"version={current_release}\n")
                f.write("updated=true\n")
    else:
        print("Already up-to-date source/shared/build-backend-tabs.rst")
        if github_output := os.environ.get("GITHUB_OUTPUT"):
            with open(github_output, "a") as f:
                f.write("updated=false\n")


if __name__ == "__main__":
    main()
