#!/usr/bin/env python3
"""Generate reviewer-friendly changelogs for mSCP baseline updates.

The workflow needs two artifacts:

* a concise PR body that stays well below GitHub's body limit
* a full committed changelog for audit/review of large upstream releases

The durable state file stores rule IDs, sections, and comparable metadata so
future releases can report real additions/removals/moves/metadata changes
instead of flooding the PR with every common rule.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

try:
    from generate_tf_compliance import (  # type: ignore[import-untyped]
        BASELINE_FILENAME_MAP,
        SUPPORTED_BASELINES,
        SUPPORTED_VERSIONS,
        find_rule_yaml,
        parse_baseline_yaml,
        parse_rule_yaml,
        parse_version_yaml,
        resolve_baselines_dir,
        resolve_rules_dir,
    )
except ImportError:
    try:
        from scripts.generate_tf_compliance import (
            BASELINE_FILENAME_MAP,
            SUPPORTED_BASELINES,
            SUPPORTED_VERSIONS,
            find_rule_yaml,
            parse_baseline_yaml,
            parse_rule_yaml,
            parse_version_yaml,
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


STATE_FILE = ".ci/mscp-rule-state.json"
DEFAULT_SUMMARY_LIMIT = 20_000
SUMMARY_SAMPLE_LIMIT = 12
TRACKED_METADATA_FIELDS = (
    "title",
    "severity",
    "references",
    "odv",
    "mobileconfig",
    "tags",
)


@dataclass
class RuleSnapshot:
    """Comparable rule state for one rule in one baseline."""

    id: str
    title: str
    section: str
    metadata: Dict[str, Any]
    metadata_hash: str


@dataclass
class ModuleDiff:
    """Rule changes for one baseline and macOS version."""

    baseline_key: str
    display_name: str
    macos_version: str
    initialized: bool = False
    added: List[RuleSnapshot] = field(default_factory=list)
    removed: List[RuleSnapshot] = field(default_factory=list)
    moved: List[RuleSnapshot] = field(default_factory=list)
    metadata_changed: List[RuleSnapshot] = field(default_factory=list)

    @property
    def module_key(self) -> str:
        return f"{self.baseline_key}/macos_{self.macos_version}"

    @property
    def changed_count(self) -> int:
        return (
            len(self.added)
            + len(self.removed)
            + len(self.moved)
            + len(self.metadata_changed)
        )

    @property
    def rule_count(self) -> int:
        return len({rule.id for rule in self.current_rules})

    @property
    def current_rules(self) -> List[RuleSnapshot]:
        return self.added + self.moved + self.metadata_changed


@dataclass
class ChangelogResult:
    """All output data for a changelog run."""

    branch: str
    old_revision: str
    new_revision: str
    full_changelog_path: Path
    summary_path: Path
    module_diffs: List[ModuleDiff]
    initialized_modules: List[ModuleDiff]


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


def _json_hash(data: Dict[str, Any]) -> str:
    """Return a stable hash for comparable metadata."""
    payload = json.dumps(data, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _normalise_revision(version_info: Dict[str, str], branch: str) -> str:
    """Return the release tag-like revision used in artifact names."""
    revision = str(version_info.get("revision", "unknown"))
    if revision.startswith(f"{branch}_rev"):
        return revision

    match = re.search(r"rev(?:ision)?\s*([0-9]+(?:\.[0-9]+)?)", revision, re.I)
    if match:
        value = match.group(1).split(".")[0]
        return f"{branch}_rev{value}"

    match = re.search(r"([0-9]+)(?:\.[0-9]+)?$", revision)
    if match:
        return f"{branch}_rev{match.group(1)}"

    return revision


def _display_revision(value: str) -> str:
    """Use a readable placeholder for missing previous state."""
    return value if value else "none"


def _safe_artifact_stem(branch: str, revision: str) -> str:
    """Build a filesystem-safe changelog basename."""
    raw = f"{branch}_{revision}"
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", raw).strip("_") or "mscp_update"


def extract_profile_entries(baseline_data: Dict[str, Any]) -> List[Dict[str, str]]:
    """Flatten supported mSCP baseline profile shapes to rule/section entries."""
    profile: Any = baseline_data.get("profile", [])
    entries: List[Dict[str, str]] = []

    if isinstance(profile, list):
        for entry in profile:
            if isinstance(entry, dict):
                section = str(entry.get("section", "unknown"))
                rules = entry.get("rules", [])
                if isinstance(rules, list):
                    entries.extend(
                        {"id": str(rule_id), "section": section}
                        for rule_id in rules
                    )
    elif isinstance(profile, dict):
        sections = profile.get("section", [])
        if isinstance(sections, list):
            for section_entry in sections:
                if isinstance(section_entry, dict):
                    section = str(section_entry.get("section", "unknown"))
                    rules = section_entry.get("rules", [])
                    if isinstance(rules, list):
                        entries.extend(
                            {"id": str(rule_id), "section": section}
                            for rule_id in rules
                        )

    return entries


def extract_rule_ids_from_profile(baseline_data: Dict[str, Any]) -> List[str]:
    """Extract rule IDs from supported mSCP baseline profile shapes."""
    return [entry["id"] for entry in extract_profile_entries(baseline_data)]


def _tracked_metadata(rule_data: Dict[str, Any]) -> Dict[str, Any]:
    """Return the rule metadata fields that should affect changelog diffs."""
    return {
        key: rule_data.get(key)
        for key in TRACKED_METADATA_FIELDS
        if key in rule_data
    }


def build_rule_snapshots(
    baseline_data: Dict[str, Any],
    rules_dir: Path,
) -> Dict[str, RuleSnapshot]:
    """Build comparable rule snapshots for a baseline."""
    snapshots: Dict[str, RuleSnapshot] = {}

    for entry in extract_profile_entries(baseline_data):
        rule_id = entry["id"]
        rule_path = find_rule_yaml(rules_dir, rule_id)
        rule_data: Dict[str, Any] = {}
        if rule_path is not None:
            rule_data = parse_rule_yaml(rule_path)

        title = str(rule_data.get("title", rule_id))
        metadata = _tracked_metadata(rule_data)
        snapshots[rule_id] = RuleSnapshot(
            id=rule_id,
            title=title,
            section=entry["section"],
            metadata=metadata,
            metadata_hash=_json_hash(metadata),
        )

    return snapshots


def _state_module_to_snapshots(module_data: Any) -> Dict[str, RuleSnapshot]:
    """Read one module from either legacy or structured state."""
    if isinstance(module_data, list):
        return {
            str(rule_id): RuleSnapshot(
                id=str(rule_id),
                title=str(rule_id),
                section="unknown",
                metadata={},
                metadata_hash="",
            )
            for rule_id in module_data
        }

    if not isinstance(module_data, dict):
        return {}

    rules = module_data.get("rules", {})
    if not isinstance(rules, dict):
        return {}

    snapshots: Dict[str, RuleSnapshot] = {}
    for rule_id, rule_data in rules.items():
        if not isinstance(rule_data, dict):
            continue
        metadata = rule_data.get("metadata", {})
        if not isinstance(metadata, dict):
            metadata = {}
        snapshots[str(rule_id)] = RuleSnapshot(
            id=str(rule_id),
            title=str(rule_data.get("title", rule_id)),
            section=str(rule_data.get("section", "unknown")),
            metadata=metadata,
            metadata_hash=str(rule_data.get("metadata_hash", "")),
        )
    return snapshots


def load_previous_state(state_path: Path = Path(STATE_FILE)) -> Dict[str, Any]:
    """Load the previous structured rule state, falling back to git history."""
    if state_path.is_file():
        try:
            with state_path.open("r", encoding="utf-8") as fh:
                loaded: Dict[str, Any] = json.load(fh)
            return loaded
        except (json.JSONDecodeError, OSError):
            pass

    return _read_previous_state_from_git()


def _read_previous_state_from_git() -> Dict[str, Any]:
    """Read the rule state file from HEAD if it exists."""
    try:
        result = subprocess.run(
            ["git", "--no-pager", "show", f"HEAD:{STATE_FILE}"],
            capture_output=True,
            text=True,
            cwd=Path.cwd(),
            check=False,
        )
        if result.returncode == 0 and result.stdout.strip():
            loaded: Dict[str, Any] = json.loads(result.stdout)
            return loaded
    except (subprocess.SubprocessError, FileNotFoundError, json.JSONDecodeError):
        pass
    return {}


def _previous_modules(previous_state: Dict[str, Any]) -> Dict[str, Any]:
    """Return module state supporting legacy and v2 state shapes."""
    modules = previous_state.get("modules")
    if isinstance(modules, dict):
        return modules
    return previous_state


def _previous_revision(previous_state: Dict[str, Any], branch: str) -> str:
    """Read previous revision for a branch from rule state when available."""
    branches = previous_state.get("branches")
    if isinstance(branches, dict):
        value = branches.get(branch)
        if value is not None:
            return str(value)
    return ""


def _snapshot_to_state(snapshot: RuleSnapshot) -> Dict[str, Any]:
    """Serialize a rule snapshot to durable JSON state."""
    return {
        "title": snapshot.title,
        "section": snapshot.section,
        "metadata": snapshot.metadata,
        "metadata_hash": snapshot.metadata_hash,
    }


def compute_module_diff(
    baseline_key: str,
    display_name: str,
    macos_version: str,
    previous_rules: Dict[str, RuleSnapshot],
    current_rules: Dict[str, RuleSnapshot],
) -> ModuleDiff:
    """Compare previous and current rule snapshots for one module."""
    diff = ModuleDiff(
        baseline_key=baseline_key,
        display_name=display_name,
        macos_version=macos_version,
        initialized=not previous_rules,
    )

    previous_ids = set(previous_rules)
    current_ids = set(current_rules)

    if diff.initialized:
        return diff

    for rule_id in sorted(current_ids - previous_ids):
        diff.added.append(current_rules[rule_id])

    for rule_id in sorted(previous_ids - current_ids):
        diff.removed.append(previous_rules[rule_id])

    for rule_id in sorted(previous_ids & current_ids):
        previous = previous_rules[rule_id]
        current = current_rules[rule_id]
        if previous.section != current.section:
            diff.moved.append(current)
        elif previous.metadata_hash != current.metadata_hash:
            diff.metadata_changed.append(current)

    return diff


def generate_state(
    branch: str,
    revision: str,
    modules: Dict[str, Dict[str, RuleSnapshot]],
    previous_state: Dict[str, Any],
) -> Dict[str, Any]:
    """Build the durable rule state payload."""
    previous_branches = previous_state.get("branches", {})
    branches = dict(previous_branches) if isinstance(previous_branches, dict) else {}
    branches[branch] = revision

    return {
        "schema_version": 2,
        "branches": branches,
        "modules": {
            module_key: {
                "rules": {
                    rule_id: _snapshot_to_state(snapshot)
                    for rule_id, snapshot in sorted(rule_snapshots.items())
                }
            }
            for module_key, rule_snapshots in sorted(modules.items())
        },
    }


def _table_rows(rules: Iterable[RuleSnapshot], change: str) -> List[str]:
    """Format full changelog rows for a change group."""
    return [
        f"| {change} | `{rule.id}` | {rule.title} | {rule.section} |"
        for rule in rules
    ]


def generate_full_changelog_markdown(result: ChangelogResult) -> str:
    """Format the complete detailed changelog artifact."""
    lines = [
        f"# mSCP Compliance Changelog: {result.branch} {result.new_revision}",
        "",
        f"- **Branch**: `{result.branch}`",
        f"- **Previous revision**: `{_display_revision(result.old_revision)}`",
        f"- **New revision**: `{result.new_revision}`",
        f"- **Modules initialized**: {len(result.initialized_modules)}",
        f"- **Modules with changes**: {len(result.module_diffs)}",
        "",
        "## Summary by Baseline",
        "",
        "| Baseline | macOS | Added | Removed | Moved | Metadata changed |",
        "|----------|-------|-------|---------|-------|------------------|",
    ]

    if not result.module_diffs and not result.initialized_modules:
        lines.append("| *(none)* | *(none)* | 0 | 0 | 0 | 0 |")

    for diff in result.module_diffs:
        lines.append(
            "| "
            f"{diff.display_name} | {diff.macos_version} | "
            f"{len(diff.added)} | {len(diff.removed)} | {len(diff.moved)} | "
            f"{len(diff.metadata_changed)} |"
        )

    if result.initialized_modules:
        lines.extend(["", "## Baseline State Initialized", ""])
        for diff in result.initialized_modules:
            lines.append(
                f"- {diff.display_name} macOS {diff.macos_version}: "
                "first tracked state captured; future runs will report deltas."
            )

    for diff in result.module_diffs:
        lines.extend(
            [
                "",
                f"## {diff.display_name} (macOS {diff.macos_version})",
                "",
                "| Change | Rule ID | Title | Section |",
                "|--------|---------|-------|---------|",
            ]
        )
        rows: List[str] = []
        rows.extend(_table_rows(diff.added, "ADDED"))
        rows.extend(_table_rows(diff.removed, "REMOVED"))
        rows.extend(_table_rows(diff.moved, "MOVED"))
        rows.extend(_table_rows(diff.metadata_changed, "METADATA_CHANGED"))
        lines.extend(rows or ["| *(none)* | *(none)* | *(none)* | *(none)* |"])

    lines.append("")
    return "\n".join(lines)


def _sample_rules(rules: List[RuleSnapshot]) -> str:
    """Return a concise comma-separated sample of rule IDs."""
    if not rules:
        return "none"
    sample = [f"`{rule.id}`" for rule in rules[:SUMMARY_SAMPLE_LIMIT]]
    if len(rules) > SUMMARY_SAMPLE_LIMIT:
        sample.append(f"... +{len(rules) - SUMMARY_SAMPLE_LIMIT} more")
    return ", ".join(sample)


def _risk_notes(module_diffs: List[ModuleDiff]) -> List[str]:
    """Build short reviewer risk notes from the diff shape."""
    notes: List[str] = []
    if any(diff.removed for diff in module_diffs):
        notes.append("Rules were removed from at least one baseline; review exemptions and expectations.")
    if any(diff.added for diff in module_diffs):
        notes.append("New rules were added; review default enablement and possible operational impact.")
    if any(diff.metadata_changed for diff in module_diffs):
        notes.append("Rule metadata changed; review ODV/reference/severity-sensitive controls.")
    if any(diff.moved for diff in module_diffs):
        notes.append("Rules moved sections; verify generated grouping remains reviewable.")
    return notes


def generate_summary_markdown(result: ChangelogResult, max_chars: int) -> str:
    """Format a concise PR body summary under a fixed character budget."""
    full_path = result.full_changelog_path.as_posix()
    total_added = sum(len(diff.added) for diff in result.module_diffs)
    total_removed = sum(len(diff.removed) for diff in result.module_diffs)
    total_moved = sum(len(diff.moved) for diff in result.module_diffs)
    total_metadata = sum(len(diff.metadata_changed) for diff in result.module_diffs)

    lines = [
        f"# mSCP {result.branch} Compliance Update",
        "",
        f"- **Previous revision**: `{_display_revision(result.old_revision)}`",
        f"- **New revision**: `{result.new_revision}`",
        f"- **Full changelog**: [{full_path}]({full_path})",
        f"- **Initialized modules**: {len(result.initialized_modules)}",
        f"- **Modules with changes**: {len(result.module_diffs)}",
        "",
        "## Totals",
        "",
        "| Added | Removed | Moved | Metadata changed |",
        "|-------|---------|-------|------------------|",
        f"| {total_added} | {total_removed} | {total_moved} | {total_metadata} |",
        "",
        "## Review Notes",
        "",
    ]

    notes = _risk_notes(result.module_diffs)
    lines.extend([f"- {note}" for note in notes] or ["- No rule deltas detected."])

    if result.initialized_modules:
        lines.extend(
            [
                "- Rule-state tracking was initialized for one or more modules; "
                "future releases will report exact deltas.",
            ]
        )

    lines.extend(
        [
            "",
            "## Baseline Summary",
            "",
            "| Baseline | macOS | Added | Removed | Moved | Metadata changed |",
            "|----------|-------|-------|---------|-------|------------------|",
        ]
    )

    for diff in result.module_diffs:
        candidate = (
            "| "
            f"{diff.display_name} | {diff.macos_version} | "
            f"{len(diff.added)} | {len(diff.removed)} | {len(diff.moved)} | "
            f"{len(diff.metadata_changed)} |"
        )
        if len("\n".join(lines + [candidate])) > max_chars:
            lines.append("| *(truncated)* | *(see full changelog)* | - | - | - | - |")
            break
        lines.append(candidate)

    lines.extend(["", "## Notable Samples", ""])
    if result.module_diffs:
        for diff in result.module_diffs[:8]:
            block = [
                f"### {diff.display_name} (macOS {diff.macos_version})",
                f"- Added: {_sample_rules(diff.added)}",
                f"- Removed: {_sample_rules(diff.removed)}",
                f"- Moved: {_sample_rules(diff.moved)}",
                f"- Metadata changed: {_sample_rules(diff.metadata_changed)}",
                "",
            ]
            if len("\n".join(lines + block)) > max_chars:
                lines.append("Additional samples omitted; see the full changelog.")
                break
            lines.extend(block)
    else:
        lines.append("No rule deltas detected.")

    summary = "\n".join(lines).rstrip() + "\n"
    if len(summary) > max_chars:
        footer = f"\n\nFull details: [{full_path}]({full_path})\n"
        summary = summary[: max_chars - len(footer) - 32].rstrip()
        summary += "\n\nSummary truncated for GitHub body size." + footer
    return summary


def _target_versions(branch: str) -> Iterable[tuple[str, Dict[str, str]]]:
    """Yield supported versions matching a branch filter."""
    for version, metadata in SUPPORTED_VERSIONS.items():
        if branch == "all" or metadata["branch"] == branch:
            yield version, metadata


def build_changelog_result(
    mscp_path: Path,
    branch: str,
    full_changelog_path: Path,
    summary_path: Path,
) -> tuple[ChangelogResult, Dict[str, Any]]:
    """Compute changelog result and next durable state."""
    baselines_dir = resolve_baselines_dir(mscp_path)
    rules_dir = resolve_rules_dir(mscp_path)
    version_info = parse_version_yaml(mscp_path)
    effective_branch = branch if branch != "all" else version_info.get("branch", "all")
    new_revision = _normalise_revision(version_info, effective_branch)

    previous_state = load_previous_state()
    previous_modules = _previous_modules(previous_state)
    old_revision = _previous_revision(previous_state, effective_branch)

    current_modules: Dict[str, Dict[str, RuleSnapshot]] = {}
    module_diffs: List[ModuleDiff] = []
    initialized_modules: List[ModuleDiff] = []

    for baseline_key, baseline_meta in SUPPORTED_BASELINES.items():
        baseline_file = baselines_dir / BASELINE_FILENAME_MAP.get(
            baseline_key, f"{baseline_key}.yaml"
        )
        if not baseline_file.is_file():
            continue

        baseline_data = parse_baseline_yaml(baseline_file)
        current_rules = build_rule_snapshots(baseline_data, rules_dir)

        for version, version_meta in _target_versions(branch):
            module_key = f"{baseline_key}/macos_{version}"
            current_modules[module_key] = current_rules
            previous_rules = _state_module_to_snapshots(
                previous_modules.get(module_key, {})
            )
            diff = compute_module_diff(
                baseline_key=baseline_key,
                display_name=baseline_meta["display_name"],
                macos_version=version,
                previous_rules=previous_rules,
                current_rules=current_rules,
            )
            if diff.initialized:
                initialized_modules.append(diff)
            elif diff.changed_count > 0:
                module_diffs.append(diff)

    result = ChangelogResult(
        branch=effective_branch,
        old_revision=old_revision,
        new_revision=new_revision,
        full_changelog_path=full_changelog_path,
        summary_path=summary_path,
        module_diffs=module_diffs,
        initialized_modules=initialized_modules,
    )
    next_state = generate_state(
        branch=effective_branch,
        revision=new_revision,
        modules=current_modules,
        previous_state=previous_state,
    )
    return result, next_state


def write_changelog_outputs(
    mscp_path: Path,
    branch: str,
    full_output: Optional[Path],
    summary_output: Path,
    summary_limit: int = DEFAULT_SUMMARY_LIMIT,
) -> ChangelogResult:
    """Generate and write full changelog, summary, and durable state."""
    version_info = parse_version_yaml(mscp_path)
    effective_branch = branch if branch != "all" else version_info.get("branch", "all")
    revision = _normalise_revision(version_info, effective_branch)
    if full_output is None:
        stem = _safe_artifact_stem(effective_branch, revision)
        full_output = Path("docs/compliance-changelogs") / f"{stem}.md"

    result, next_state = build_changelog_result(
        mscp_path=mscp_path,
        branch=branch,
        full_changelog_path=full_output,
        summary_path=summary_output,
    )

    full_changelog = generate_full_changelog_markdown(result)
    summary = generate_summary_markdown(result, summary_limit)

    full_output.parent.mkdir(parents=True, exist_ok=True)
    full_output.write_text(full_changelog, encoding="utf-8")

    summary_output.parent.mkdir(parents=True, exist_ok=True)
    summary_output.write_text(summary, encoding="utf-8")

    state_path = Path(STATE_FILE)
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(
        json.dumps(next_state, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    print(f"Full changelog written to: {full_output}")
    print(f"Summary written to: {summary_output}")
    print(f"Rule state written to: {state_path}")
    return result


def _build_argparser() -> argparse.ArgumentParser:
    """Construct the command-line argument parser."""
    parser = argparse.ArgumentParser(
        description="Generate full and summary changelogs between mSCP revisions.",
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
        help="mSCP branch to generate changelog for (tahoe, sequoia, sonoma, or all)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Path to write the full markdown changelog",
    )
    parser.add_argument(
        "--summary-output",
        type=Path,
        default=Path("changelog-summary.md"),
        help="Path to write the concise PR summary markdown",
    )
    parser.add_argument(
        "--summary-limit",
        type=int,
        default=DEFAULT_SUMMARY_LIMIT,
        help="Maximum PR summary characters",
    )
    return parser


def main() -> None:
    """Entry point for the changelog generator."""
    parser = _build_argparser()
    args = parser.parse_args()

    mscp_path: Path = args.mscp_path
    if not mscp_path.is_dir():
        print(f"Error: mSCP path does not exist: {mscp_path}", file=sys.stderr)
        sys.exit(1)

    write_changelog_outputs(
        mscp_path=mscp_path,
        branch=args.branch,
        full_output=args.output,
        summary_output=args.summary_output,
        summary_limit=args.summary_limit,
    )


if __name__ == "__main__":
    main()
