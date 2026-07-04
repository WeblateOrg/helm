#!/usr/bin/env python3
"""Bump chart version for Renovate Weblate image updates."""

from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

CHART_PATH = Path("charts/weblate/Chart.yaml")
README_PATH = Path("charts/weblate/README.md")
VALUES_PATH = Path("charts/weblate/values.yaml")

ALLOWED_PATHS = {
    CHART_PATH.as_posix(),
    README_PATH.as_posix(),
    VALUES_PATH.as_posix(),
}
REQUIRED_PATHS = {
    CHART_PATH.as_posix(),
    VALUES_PATH.as_posix(),
}


def run_git(*args: str) -> str:
    completed = subprocess.run(
        ("git", *args),
        check=True,
        capture_output=True,
        text=True,
    )
    return completed.stdout


def git_show(base_ref: str, path: Path) -> str:
    return run_git("show", f"origin/{base_ref}:{path.as_posix()}")


def root_scalar(chart: str, key: str) -> str:
    match = re.search(
        rf"^{re.escape(key)}:\s*([^\s#]+).*$",
        chart,
        flags=re.MULTILINE,
    )
    if match is None:
        raise SystemExit(f"Unable to find top-level {key!r} in Chart.yaml")
    return match.group(1).strip("'\"")


def bump_patch(version: str) -> str:
    match = re.fullmatch(r"(\d+)\.(\d+)\.(\d+)", version)
    if match is None:
        raise SystemExit(f"Unsupported chart version: {version}")
    major, minor, patch = match.groups()
    return f"{major}.{minor}.{int(patch) + 1}"


def changed_paths(base_ref: str) -> set[str]:
    return set(
        run_git(
            "diff",
            "--name-only",
            "--diff-filter=ACMRT",
            f"origin/{base_ref}...HEAD",
        ).splitlines()
    )


def update_chart_version(chart: str, target_version: str) -> str:
    new_chart, count = re.subn(
        r"^(version:\s*)[^\s#]+(.*)$",
        lambda match: f"{match.group(1)}{target_version}{match.group(2)}",
        chart,
        count=1,
        flags=re.MULTILINE,
    )
    if count != 1:
        raise SystemExit("Unable to update chart version in Chart.yaml")
    return new_chart


def update_readme_badge(readme: str, target_version: str) -> str:
    version_badge = (
        f"![Version: {target_version}]"
        f"(https://img.shields.io/badge/Version-{target_version}"
        "-informational?style=flat-square)"
    )
    new_readme, count = re.subn(
        r"!\[Version: [^\]]+\]\("
        r"https://img\.shields\.io/badge/Version-[^-)]*"
        r"-informational\?style=flat-square\)",
        version_badge,
        readme,
        count=1,
    )
    if count != 1:
        raise SystemExit("Unable to update chart version badge in README.md")
    return new_readme


def main() -> int:
    base_ref = os.environ["BASE_REF"]
    changed = changed_paths(base_ref)
    unexpected = changed - ALLOWED_PATHS

    if unexpected:
        print(
            "Skipping chart version bump; unexpected changed paths: "
            + ", ".join(sorted(unexpected))
        )
        return 0

    if not REQUIRED_PATHS.issubset(changed):
        print(
            "Skipping chart version bump; Weblate Chart.yaml and values.yaml "
            "changes were not both detected."
        )
        return 0

    base_chart = git_show(base_ref, CHART_PATH)
    head_chart = CHART_PATH.read_text(encoding="utf-8")

    base_app_version = root_scalar(base_chart, "appVersion")
    head_app_version = root_scalar(head_chart, "appVersion")
    if base_app_version == head_app_version:
        print("Skipping chart version bump; appVersion did not change.")
        return 0

    base_chart_version = root_scalar(base_chart, "version")
    head_chart_version = root_scalar(head_chart, "version")
    target_chart_version = bump_patch(base_chart_version)
    if head_chart_version not in {base_chart_version, target_chart_version}:
        raise SystemExit(
            f"Unexpected chart version {head_chart_version}; expected "
            f"{base_chart_version} or {target_chart_version}."
        )

    new_chart = update_chart_version(head_chart, target_chart_version)
    readme = README_PATH.read_text(encoding="utf-8")
    new_readme = update_readme_badge(readme, target_chart_version)

    CHART_PATH.write_text(new_chart, encoding="utf-8")
    README_PATH.write_text(new_readme, encoding="utf-8")

    if head_chart_version == target_chart_version:
        print(f"Chart version already set to {target_chart_version}.")
    else:
        print(
            f"Bumped chart version from {head_chart_version} to {target_chart_version}."
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
