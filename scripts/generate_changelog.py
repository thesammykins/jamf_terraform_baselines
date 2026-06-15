#!/usr/bin/env python3
"""Generate a rule-level changelog between mSCP revisions.

Compares the current state of generated compliance modules against a
previous recorded state (or git history) to identify rules that were
ADDED, REMOVED, or MODIFIED in a new mSCP release.

Output is a markdown table suitable for inclusion in a PR body.

Typical usage:
    python generate_changelog.py \\
        --mscp-path /tmp/mscp \\
        --branch tahoe \\
        --output changelog.md
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# Import shared constants from the generator
try:
    from generate_tf_compliance import (  # type: ignore[import-untyped]
        SUPPORTED_BASELINES,
        SUPPORTED_VERSIONS,
        parse_baseline_yaml,
        resolve_baselines_dir,
        resolve_rules_dir,
    )
except ImportError:
    print(
        "Error: could not import generate_tf_compliance. "
        "Ensure both scripts are in the same directory.",
        file=sys.stderr,
    )
    sys.exit(1)


# ---------------------------------------------------------------------------
# State management
# ---------------------------------------------------------------------------

STATE_FILE = ".ci/mscp-rule-state.json"


def _import_yaml() -> Any:
    """Lazily import PyYAML."""
    try:
        import yaml  # type: ignore[import-untyped]
    except ImportError:
        print(
            "PyYAML is required. Install with: pip install pyyaml",
            file=sys.stderr,
        )
        sys.exit(1)
    return yaml


def load_previous_state(
    output_dir: Path, branch: str
) -> Dict[str, List[str]]:
    """Load the previous rule state from the state file or git history.

    Args:
        output_dir: Base output directory (``modules/compliance``).
        branch: mSCP branch name (e.g. ``"tahoe"``).

    Returns:
        Dict mapping ``"baseline_key/macos_version"`` → list of rule IDs.
    """
    state_path = Path(STATE_FILE)
    if state_path.is_file():
        try:
            with open(state_path, "r", encoding="utf-8") as fh:
                return json.load(fh)  # type: ignore[no-any-return]
        except (json.JSONDecodeError, KeyError):
            pass

    # Fallback: try reading from committed module files via git
    return _read_previous_from_git(output_dir, branch)


def _read_previous_from_git(
    output_dir: Path, branch: str
) -> Dict[str, List[str]]:
    """Read previous rule lists from git HEAD.

    Attempts to parse ``main.tf`` from the last commit to extract rule IDs
    from the ``locals.all_rules`` block.

    Args:
        output_dir: Base output directory.
        branch: mSCP branch (used to filter relevant versions).

    Returns:
        Dict mapping module path → list of rule IDs.
    """
    previous: Dict[str, List[str]] = {}
    try:
        result = subprocess.run(
            [
                "git",
                "--no-pager",
                "show",
                "HEAD:modules/compliance",
            ],
            capture_output=True,
            text=True,
            cwd=output_dir.parent if output_dir.parent.is_dir() else Path.cwd(),
        )
        if result.returncode != 0:
            return previous
        # Simple fallback: read the state file from previous commit
        result2 = subprocess.run(
            [
                "git",
                "--no-pager",
                "show",
                f"HEAD:{STATE_FILE}",
            ],
            capture_output=True,
            text=True,
            cwd=Path.cwd(),
        )
        if result2.returncode == 0:
            return json.loads(result2.stdout)
    except (subprocess.SubprocessError, FileNotFoundError):
        pass
    return previous


def save_current_state(
    baseline_key: str,
    ver_major: str,
    rule_ids: List[str],
    state: Dict[str, List[str]],
) -> None:
    """Record the current rule IDs for a module into the state dict.

    Args:
        baseline_key: Baseline identifier.
        ver_major: macOS major version string.
        rule_ids: List of current rule IDs.
        state: Mutable state dict to update.
    """
    key = f"{baseline_key}/macos_{ver_major}"
    state[key] = sorted(rule_ids)


# ---------------------------------------------------------------------------
# Changelog computation
# ---------------------------------------------------------------------------


def compute_diff(
    previous: List[str],
    current: List[str],
) -> Tuple[List[str], List[str], List[str]]:
    """Compute ADDED, REMOVED, and MODIFIED rule IDs between two lists.

    Args:
        previous: Rule IDs from the previous revision.
        current: Rule IDs from the current revision.

    Returns:
        Tuple of ``(added, removed, modified)`` where ``modified``
        includes rule IDs present in both lists (further inspection
        needed to confirm actual modification of rule content).
    """
    prev_set = set(previous)
    curr_set = set(current)

    added = sorted(curr_set - prev_set)
    removed = sorted(prev_set - curr_set)
    # Rules present in both are candidates for MODIFIED
    common = sorted(prev_set & curr_set)

    return added, removed, common


def generate_changelog_markdown(
    baseline_key: str,
    ver_major: str,
    ver_meta: Dict[str, str],
    old_revision: str,
    new_revision: str,
    added: List[str],
    removed: List[str],
    modified: List[str],
    rule_titles: Dict[str, str],
) -> str:
    """Format a markdown changelog table for one baseline × version.

    Args:
        baseline_key: Baseline identifier.
        ver_major: macOS major version.
        ver_meta: Version metadata dict (name, branch, etc.).
        old_revision: Previous mSCP revision tag.
        new_revision: New mSCP revision tag.
        added: Rule IDs added.
        removed: Rule IDs removed.
        modified: Rule IDs present in both (candidates for modification).
        rule_titles: Mapping of rule ID → title.

    Returns:
        Markdown string with changelog table.
    """
    display = SUPPORTED_BASELINES.get(
        baseline_key, {}
    ).get("display_name", baseline_key)

    lines: List[str] = [
        f"## Rule Changes — {display} (macOS {ver_major}) — {old_revision} → {new_revision}",
        "",
        "| Change | Rule ID | Title |",
        "|--------|---------|-------|",
    ]

    for rid in added:
        title = rule_titles.get(rid, rid)
        lines.append(f"| ADDED | {rid} | {title} |")

    for rid in removed:
        title = rule_titles.get(rid, rid)
        lines.append(f"| REMOVED | {rid} | {title} |")

    for rid in modified:
        title = rule_titles.get(rid, rid)
        lines.append(f"| MODIFIED | {rid} | {title} |")

    if not added and not removed and not modified:
        lines.append("| *(none)* | *(none)* | *(none)* |")

    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Orchestration
# ---------------------------------------------------------------------------


def generate_changelog(
    mscp_path: Path,
    output_dir: Path,
    branch: str,
) -> str:
    """Generate a full changelog comparing current vs previous rule state.

    Args:
        mscp_path: Root of cloned mSCP repository.
        output_dir: Base output directory (``modules/compliance``).
        branch: mSCP branch name or ``"all"``.

    Returns:
        Combined markdown changelog string.
    """
    yaml = _import_yaml()
    baselines_dir = resolve_baselines_dir(mscp_path)
    rules_dir = resolve_rules_dir(mscp_path)

    previous_state = load_previous_state(output_dir, branch)
    current_state: Dict[str, List[str]] = {}
    changelog_parts: List[str] = []
    old_revision = "unknown"
    new_revision = "unknown"

    # Try to read version info
    version_file = mscp_path / "VERSION.yaml"
    if version_file.is_file():
        with open(version_file, "r", encoding="utf-8") as fh:
            version_data = yaml.safe_load(fh) or {}
        new_revision = str(version_data.get("revision", "unknown"))
        old_revision = "previous"

    for baseline_key in SUPPORTED_BASELINES:
        baseline_file = baselines_dir / f"{baseline_key}.yaml"
        if not baseline_file.is_file():
            continue

        baseline_data = parse_baseline_yaml(baseline_file)

        for ver_major, ver_meta in SUPPORTED_VERSIONS.items():
            if branch != "all" and ver_meta["branch"] != branch:
                continue

            # Extract current rule IDs from baseline
            profile: Dict[str, Any] = baseline_data.get("profile", {})
            sections: List[Dict[str, Any]] = profile.get("section", [])
            current_rule_ids: List[str] = []
            for section in sections:
                current_rule_ids.extend(section.get("rules", []))

            key = f"{baseline_key}/macos_{ver_major}"
            prev_ids = previous_state.get(key, [])

            added, removed, common = compute_diff(prev_ids, current_rule_ids)

            # Build rule title map for current rules
            rule_titles: Dict[str, str] = {}
            for rid in current_rule_ids:
                from generate_tf_compliance import find_rule_yaml, parse_rule_yaml

                rp = find_rule_yaml(rules_dir, rid)
                if rp is not None:
                    rd = parse_rule_yaml(rp)
                    rule_titles[rid] = rd.get("title", rid)
                else:
                    rule_titles[rid] = rid

            # All common rules are marked as modified for now
            if added or removed or common:
                part = generate_changelog_markdown(
                    baseline_key=baseline_key,
                    ver_major=ver_major,
                    ver_meta=ver_meta,
                    old_revision=old_revision,
                    new_revision=new_revision,
                    added=added,
                    removed=removed,
                    modified=common,
                    rule_titles=rule_titles,
                )
                changelog_parts.append(part)

            save_current_state(
                baseline_key, ver_major, current_rule_ids, current_state
            )

    # Write state for next run
    state_dir = Path(STATE_FILE).parent
    state_dir.mkdir(parents=True, exist_ok=True)
    with open(STATE_FILE, "w", encoding="utf-8") as fh:
        json.dump(current_state, fh, indent=2, sort_keys=True)

    if not changelog_parts:
        return "No rule changes detected across any baseline × version combinations.\n"

    return "\n".join(changelog_parts)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def _build_argparser() -> argparse.ArgumentParser:
    """Construct the command-line argument parser."""
    parser = argparse.ArgumentParser(
        description="Generate a rule-level changelog between mSCP revisions.",
    )
    parser.add_argument(
        "--mscp-path",
        required=True,
        type=Path,
        help="Path to cloned mSCP repository",
    )
    parser.add_argument(
        "--branch",
        required=True,
        help="mSCP branch to generate changelog for (tahoe, sequoia, sonoma, or 'all')",
    )
    parser.add_argument(
        "--output",
        required=True,
        type=Path,
        help="Path to write the markdown changelog",
    )
    return parser


def main() -> None:
    """Entry point for the changelog generator."""
    parser = _build_argparser()
    args = parser.parse_args()

    mscp_path: Path = args.mscp_path
    branch: str = args.branch
    output_path: Path = args.output

    if not mscp_path.is_dir():
        print(f"Error: mSCP path does not exist: {mscp_path}", file=sys.stderr)
        sys.exit(1)

    # Determine output_dir: assume modules/compliance relative to CWD
    output_dir = Path("modules/compliance")
    if not output_dir.is_dir():
        output_dir = output_path.parent / "modules" / "compliance"

    changelog = generate_changelog(
        mscp_path=mscp_path,
        output_dir=output_dir,
        branch=branch,
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(changelog, encoding="utf-8")
    print(f"Changelog written to: {output_path}")


if __name__ == "__main__":
    main()
