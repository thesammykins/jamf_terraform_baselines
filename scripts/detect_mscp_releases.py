#!/usr/bin/env python3
"""Poll the GitHub releases API for new NIST mSCP release tags.

Reads a local state file (``.ci/mscp-revision-state.json``) tracking the
last-seen revision per mSCP branch, queries the GitHub releases API, and
emits a JSON file listing any branches with new releases.

Typical usage:
    python detect_mscp_releases.py \\
        --state-file .ci/mscp-revision-state.json \\
        --output new-releases.json

Output JSON shape:
    {
      "branches": [
        {
          "branch": "tahoe",
          "new_tag": "tahoe_rev3",
          "previous_revision": "tahoe_rev2",
          "released_at": "2026-06-10T00:00:00Z"
        }
      ]
    }
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

GITHUB_API_RELEASES = (
    "https://api.github.com/repos/usnistgov/macos_security/releases"
)

# mSCP branches we track, mapped to their release tag prefix
MSCP_BRANCHES: Dict[str, str] = {
    "sonoma": "sonoma",
    "sequoia": "sequoia",
    "tahoe": "tahoe",
}

DEFAULT_PAGE_SIZE = 100


# ---------------------------------------------------------------------------
# GitHub API helpers
# ---------------------------------------------------------------------------


def fetch_releases() -> List[Dict[str, Any]]:
    """Fetch the mSCP releases list from the GitHub API.

    Handles pagination to retrieve all releases.

    Returns:
        List of release dicts from the GitHub API.

    Raises:
        SystemExit: If the API request fails.
    """
    releases: List[Dict[str, Any]] = []
    page = 1

    while True:
        url = f"{GITHUB_API_RELEASES}?per_page={DEFAULT_PAGE_SIZE}&page={page}"
        req = urllib.request.Request(
            url,
            headers={
                "Accept": "application/vnd.github+json",
                "User-Agent": "jamf-mscp-tf-release-detector/1.0",
            },
        )

        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            print(
                f"Error: GitHub API returned {exc.code}: {exc.reason}",
                file=sys.stderr,
            )
            sys.exit(1)
        except urllib.error.URLError as exc:
            print(
                f"Error: could not reach GitHub API: {exc.reason}",
                file=sys.stderr,
            )
            sys.exit(1)

        if not data:
            break

        releases.extend(data)
        page += 1

    return releases


def find_latest_tag_for_branch(
    releases: List[Dict[str, Any]],
    branch_prefix: str,
) -> Optional[Dict[str, Any]]:
    """Find the most recent release tag matching a branch prefix.

    Tags are matched by prefix (e.g. ``tahoe_rev`` matches the ``tahoe`` branch).

    Args:
        releases: List of release dicts from GitHub API.
        branch_prefix: e.g. ``"tahoe"``, used to match tag names.

    Returns:
        Most recent matching release dict, or ``None``.
    """
    pattern = re.compile(rf"^{re.escape(branch_prefix)}_rev(\d+)$")
    best: Optional[Dict[str, Any]] = None
    best_rev = -1

    for release in releases:
        # Skip drafts and prereleases
        if release.get("draft", False):
            continue
        tag: str = release.get("tag_name", "")
        match = pattern.match(tag)
        if match:
            rev_num = int(match.group(1))
            if rev_num > best_rev:
                best_rev = rev_num
                best = release

    return best


# ---------------------------------------------------------------------------
# State file management
# ---------------------------------------------------------------------------


def load_state(state_path: Path) -> Dict[str, str]:
    """Load the last-known revision state per branch.

    Args:
        state_path: Path to ``.ci/mscp-revision-state.json``.

    Returns:
        Dict mapping branch name → last-seen tag string.
    """
    if not state_path.is_file():
        return {}
    try:
        with open(state_path, "r", encoding="utf-8") as fh:
            data: Dict[str, Any] = json.load(fh)
        return data.get("branches", {})  # type: ignore[no-any-return]
    except (json.JSONDecodeError, KeyError):
        return {}


def save_state(state_path: Path, state: Dict[str, str]) -> None:
    """Write updated revision state back to disk.

    Args:
        state_path: Path to write.
        state: Updated branch → tag mapping.
    """
    state_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "branches": state,
        "last_checked": datetime.now(timezone.utc).isoformat(),
    }
    with open(state_path, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2, sort_keys=True)


# ---------------------------------------------------------------------------
# Detection logic
# ---------------------------------------------------------------------------


def detect_new_releases(
    state: Dict[str, str],
    releases: List[Dict[str, Any]],
) -> Dict[str, Any]:
    """Compare GitHub releases against last-known state to find new tags.

    Args:
        state: Last-known branch → tag mapping.
        releases: Full list of GitHub release dicts.

    Returns:
        Dict suitable for JSON output with ``branches`` array.
    """
    new_branches: List[Dict[str, Any]] = []
    updated_state = dict(state)

    for branch_name, prefix in MSCP_BRANCHES.items():
        latest = find_latest_tag_for_branch(releases, prefix)
        if latest is None:
            continue

        new_tag: str = latest.get("tag_name", "")
        previous = state.get(branch_name)

        if previous is None:
            # First run: record but don't report as new
            updated_state[branch_name] = new_tag
            print(
                f"First detection for {branch_name}: recorded {new_tag}",
                file=sys.stderr,
            )
        elif new_tag != previous:
            new_branches.append(
                {
                    "branch": branch_name,
                    "new_tag": new_tag,
                    "previous_revision": previous,
                    "released_at": latest.get("published_at", ""),
                }
            )
            updated_state[branch_name] = new_tag
            print(
                f"New release for {branch_name}: {previous} → {new_tag}",
                file=sys.stderr,
            )
        else:
            print(
                f"No new release for {branch_name}: still at {new_tag}",
                file=sys.stderr,
            )

    return {"branches": updated_state, "new_releases": new_branches}


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def _build_argparser() -> argparse.ArgumentParser:
    """Construct the command-line argument parser."""
    parser = argparse.ArgumentParser(
        description="Poll GitHub releases API for new NIST mSCP release tags.",
    )
    parser.add_argument(
        "--state-file",
        required=True,
        type=Path,
        help="Path to .ci/mscp-revision-state.json",
    )
    parser.add_argument(
        "--output",
        required=True,
        type=Path,
        help="Path to write new-releases.json",
    )
    return parser


def main() -> None:
    """Entry point for the mSCP release detector."""
    parser = _build_argparser()
    args = parser.parse_args()

    state_path: Path = args.state_file
    output_path: Path = args.output

    state = load_state(state_path)
    releases = fetch_releases()

    result = detect_new_releases(state, releases)

    # Write new-releases.json with just the new releases array
    new_releases_only = result["new_releases"]

    # Also output individual branch tags for CI matrix use
    for item in new_releases_only:
        branch = item["branch"]
        result[f"{branch}_tag"] = item["new_tag"]

    # Update state file
    save_state(state_path, result["branches"])

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=2, sort_keys=True)

    print(f"Release detection written to: {output_path}")
    if new_releases_only:
        print(f"New releases found: {len(new_releases_only)}")
    else:
        print("No new releases detected.")


if __name__ == "__main__":
    main()
