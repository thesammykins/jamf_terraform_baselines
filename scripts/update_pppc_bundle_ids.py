#!/usr/bin/env python3
"""Validate and report on PPPC bundle identifier files.

Reads ``pppc-bundle-ids.yaml`` files from foundation PPPC modules,
validates bundle IDs against the reverse-DNS format expected by Apple's
Privacy Preferences Policy Control (PPPC) framework, checks that common
tools have correct bundle IDs, and outputs a validation report.

Typical usage:
    # Validate only (read-only)
    python update_pppc_bundle_ids.py \\
        --pppc-dir modules/foundation/ \\
        --validate-only

    # Validate and report (always validate-only in current version)
    python update_pppc_bundle_ids.py \\
        --pppc-dir modules/foundation/
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

# Reverse-DNS bundle identifier pattern per Apple conventions
BUNDLE_ID_RE = re.compile(
    r"^[a-zA-Z_][a-zA-Z0-9_]*(\.[a-zA-Z_][a-zA-Z0-9_]*)+$"
)

# Well-known bundle IDs for common collaboration tools
# Used to validate that the correct identifiers are present
KNOWN_BUNDLE_IDS: Dict[str, str] = {
    "Zoom": "us.zoom.xos",
    "Slack": "com.tinyspeck.slackmacgap",
    "Microsoft Teams": "com.microsoft.teams2",
    "Google Chrome": "com.google.Chrome",
    "Webex": "Cisco-Systems.Spark",
}

# Alternative bundle IDs that are also acceptable
ALTERNATE_BUNDLE_IDS: Dict[str, List[str]] = {
    "Microsoft Teams": [
        "com.microsoft.teams",
        "com.microsoft.teams2",
    ],
    "Webex": [
        "Cisco-Systems.Spark",
        "com.cisco.webexmeetingsapp",
    ],
}


# ---------------------------------------------------------------------------
# YAML helpers
# ---------------------------------------------------------------------------


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


# ---------------------------------------------------------------------------
# File discovery
# ---------------------------------------------------------------------------


def find_pppc_bundle_files(pppc_dir: Path) -> List[Path]:
    """Find all ``pppc-bundle-ids.yaml`` files under the PPPC modules directory.

    Args:
        pppc_dir: Path to foundation modules directory (e.g.
            ``modules/foundation/``).

    Returns:
        Sorted list of absolute paths to PPPC bundle ID files.
    """
    files: List[Path] = []
    for yaml_file in pppc_dir.rglob("pppc-bundle-ids.yaml"):
        files.append(yaml_file)
    return sorted(files)


def read_bundle_ids(file_path: Path) -> Dict[str, Any]:
    """Parse a ``pppc-bundle-ids.yaml`` file.

    Expected YAML structure::

        tools:
          "Tool Name":
            bundle_id: "com.example.tool"
            display_name: "Tool Name"

    Args:
        file_path: Path to a PPPC bundle ID YAML file.

    Returns:
        Parsed dict, or empty dict on error.
    """
    yaml = _import_yaml()
    try:
        with open(file_path, "r", encoding="utf-8") as fh:
            data = yaml.safe_load(fh)
        return data or {}
    except Exception as exc:
        print(
            f"Warning: could not parse {file_path}: {exc}",
            file=sys.stderr,
        )
        return {}


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------


def validate_bundle_id(bundle_id: str) -> Tuple[bool, str]:
    """Validate a single bundle ID against reverse-DNS format.

    Args:
        bundle_id: The bundle identifier string to check.

    Returns:
        Tuple of ``(is_valid, reason)``.
    """
    if not bundle_id:
        return False, "empty bundle ID"
    if not BUNDLE_ID_RE.match(bundle_id):
        return False, (
            f"invalid format: '{bundle_id}' does not match "
            "reverse-DNS pattern (e.g. com.example.app)"
        )
    if len(bundle_id) > 255:
        return False, f"bundle ID too long ({len(bundle_id)} chars, max 255)"
    return True, "valid"


def check_known_tools(
    tools: Dict[str, Dict[str, str]],
    module_path: Path,
) -> List[str]:
    """Verify that well-known tools have expected bundle IDs.

    Args:
        tools: Dict of tool name → {bundle_id, ...}.
        module_path: Path to the module for reporting.

    Returns:
        List of warning/error messages.
    """
    messages: List[str] = []

    for tool_name, expected_id in KNOWN_BUNDLE_IDS.items():
        if tool_name in tools:
            actual_id = tools[tool_name].get("bundle_id", "")
            if actual_id != expected_id:
                alternates = ALTERNATE_BUNDLE_IDS.get(tool_name, [])
                if actual_id not in alternates:
                    messages.append(
                        f"WARNING: {module_path}: {tool_name} bundle ID "
                        f"is '{actual_id}', expected '{expected_id}'"
                    )

    return messages


def validate_module(
    file_path: Path,
) -> Tuple[List[Dict[str, str]], List[str]]:
    """Validate all bundle IDs in a single PPPC module.

    Args:
        file_path: Path to a ``pppc-bundle-ids.yaml`` file.

    Returns:
        Tuple of ``(results, warnings)`` where ``results`` is a list of
        per-tool validation dicts and ``warnings`` is a list of messages.
    """
    data = read_bundle_ids(file_path)
    tools: Dict[str, Dict[str, str]] = data.get("tools", {})

    results: List[Dict[str, str]] = []
    warnings: List[str] = []

    for tool_name, tool_data in tools.items():
        bundle_id = tool_data.get("bundle_id", "")
        is_valid, reason = validate_bundle_id(bundle_id)

        results.append(
            {
                "tool": tool_name,
                "bundle_id": bundle_id,
                "valid": str(is_valid),
                "reason": reason,
            }
        )

        if not is_valid:
            warnings.append(
                f"ERROR: {file_path}: {tool_name}: {reason}"
            )

    # Check against known tools
    known_warnings = check_known_tools(tools, file_path.parent)
    warnings.extend(known_warnings)

    return results, warnings


# ---------------------------------------------------------------------------
# Orchestration
# ---------------------------------------------------------------------------


def validate_all(
    pppc_dir: Path,
    validate_only: bool = True,
) -> Tuple[Dict[str, Any], List[str]]:
    """Validate PPPC bundle IDs across all foundation PPPC modules.

    Args:
        pppc_dir: Path to foundation modules directory.
        validate_only: If ``True``, only report findings without making
            changes. (Currently always True — update support is planned.)

    Returns:
        Tuple of ``(report, all_warnings)``.
    """
    files = find_pppc_bundle_files(pppc_dir)

    if not files:
        return {"modules": [], "total_tools": 0, "errors": 0}, [
            "No PPPC bundle ID files found"
        ]

    report: Dict[str, Any] = {"modules": [], "total_tools": 0, "errors": 0}
    all_warnings: List[str] = []

    for file_path in files:
        results, warnings = validate_module(file_path)
        module_name = file_path.parent.name

        module_report: Dict[str, Any] = {
            "module": module_name,
            "path": str(file_path),
            "tools": results,
            "tool_count": len(results),
            "invalid_count": sum(
                1 for r in results if r["valid"] != "True"
            ),
        }
        report["modules"].append(module_report)
        report["total_tools"] += len(results)
        report["errors"] += module_report["invalid_count"]

        all_warnings.extend(warnings)

    return report, all_warnings


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def _build_argparser() -> argparse.ArgumentParser:
    """Construct the command-line argument parser."""
    parser = argparse.ArgumentParser(
        description="Validate PPPC bundle identifiers in foundation modules.",
    )
    parser.add_argument(
        "--pppc-dir",
        required=True,
        type=Path,
        help="Path to foundation modules directory (e.g. modules/foundation/)",
    )
    parser.add_argument(
        "--validate-only",
        action="store_true",
        default=True,
        help="Only validate bundle IDs; do not modify files (default)",
    )
    return parser


def main() -> None:
    """Entry point for the PPPC bundle ID validator."""
    parser = _build_argparser()
    args = parser.parse_args()

    pppc_dir: Path = args.pppc_dir
    validate_only: bool = args.validate_only

    if not pppc_dir.is_dir():
        print(
            f"Error: PPPC directory not found: {pppc_dir}",
            file=sys.stderr,
        )
        sys.exit(1)

    report, warnings = validate_all(pppc_dir, validate_only=validate_only)

    # Print warnings
    for w in warnings:
        print(w, file=sys.stderr)

    # Print summary
    print(f"\nPPPC Bundle ID Validation Report")
    print(f"=" * 40)
    print(f"Modules checked: {len(report['modules'])}")
    print(f"Total tools:     {report['total_tools']}")
    print(f"Invalid IDs:     {report['errors']}")

    if report["errors"] > 0:
        print(f"\nDetailed results:")
        for mod in report["modules"]:
            if mod["invalid_count"] > 0:
                print(f"\n  Module: {mod['module']} ({mod['path']})")
                for tool in mod["tools"]:
                    if tool["valid"] != "True":
                        print(
                            f"    ✗ {tool['tool']}: {tool['reason']}"
                        )
                for tool in mod["tools"]:
                    if tool["valid"] == "True":
                        print(
                            f"    ✓ {tool['tool']}: {tool['bundle_id']}"
                        )

    if warnings:
        print(f"\n{len(warnings)} warning(s) found.", file=sys.stderr)
    else:
        print("\nAll bundle IDs validated successfully.")

    # Exit non-zero if there are invalid bundle IDs
    if report["errors"] > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
