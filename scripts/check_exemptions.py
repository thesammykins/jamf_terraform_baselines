#!/usr/bin/env python3
"""Validate exemption declarations across all Terraform modules.

Walks ``modules/compliance/`` and ``modules/foundation/`` looking for
``variables.tf`` files, parses exemption blocks, and checks for:
* Expired exemptions (date past without extension)
* Missing ticket references
* Missing reviewer attribution

Outputs warnings to stderr and optionally produces a JSON report.

Typical usage:
    # Check for expired exemptions (fails if any found)
    python check_exemptions.py \\
        --modules-dir modules/ \\
        --enforce-expiry true

    # Check completeness (warnings only)
    python check_exemptions.py \\
        --modules-dir modules/ \\
        --require-ticket true \\
        --warn-missing-reviewer true

    # Generate JSON report
    python check_exemptions.py \\
        --modules-dir modules/ \\
        --report-json exemptions-report.json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

# Regex to match exemption blocks inside a variables.tf default value.
# Looks for map literals with the exemption object shape.
_EXEMPTION_KEY_RE = re.compile(
    r'"([a-zA-Z0-9_\-]+)"\s*=\s*\{'
)

# Field extractors for exemption block contents
_REASON_RE = re.compile(r'reason\s*=\s*"([^"]*)"')
_TICKET_RE = re.compile(r'ticket\s*=\s*"([^"]*)"')
_RISK_STATUS_RE = re.compile(r'risk_status\s*=\s*"([^"]*)"')
_REVIEWER_RE = re.compile(r'reviewer\s*=\s*"([^"]*)"')
_EXPIRES_RE = re.compile(r'expires\s*=\s*"([^"]*)"')
_REVIEW_DATE_RE = re.compile(r'review_date\s*=\s*"([^"]*)"')

VALID_RISK_STATUSES = {
    "ACCEPTED",
    "TEMPORARY",
    "ACCEPTED_WITH_COMPENSATING_CONTROLS",
    "UNDER_REVIEW",
}


@dataclass
class ExemptionResult:
    """Represents the result of validating a single exemption."""
    rule_id: str
    module: str
    result_type: str  # EXPIRED, WARNING, ERROR, OK
    message: str


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------


def find_variables_files(modules_dir: Path) -> List[Path]:
    """Recursively find all ``variables.tf`` files under the modules directory.

    Args:
        modules_dir: Path to the ``modules/`` directory.

    Returns:
        Sorted list of absolute paths to ``variables.tf`` files.
    """
    files: List[Path] = []
    for tf_file in modules_dir.rglob("variables.tf"):
        files.append(tf_file)
    return sorted(files)


def extract_module_name(file_path: Path) -> str:
    """Derive a human-readable module name from the file path.

    Args:
        file_path: Path to a ``variables.tf`` file.

    Returns:
        Module name like ``compliance/cis_lvl1/macos_26`` or
        ``foundation/security-baseline``.
    """
    parts = file_path.parts
    try:
        modules_idx = parts.index("modules")
        return "/".join(parts[modules_idx + 1 : -1])
    except ValueError:
        return file_path.parent.name


def parse_exemptions(content: str) -> Dict[str, Dict[str, Optional[str]]]:
    try:
        import hcl2
        data = hcl2.loads(content)
    except Exception as e:
        import sys
        print(f"Error parsing HCL: {e}", file=sys.stderr)
        return {}

    variables = data.get("variable", [])
    for var_block in variables:
        for var_name, var_def in var_block.items():
            if var_name.strip('"') == "exemptions":
                default_val = var_def.get("default", {})
                if not isinstance(default_val, dict):
                    return {}
                
                parsed = {}
                for ex_key, ex_data in default_val.items():
                    if not isinstance(ex_data, dict):
                        continue
                    def _get_str(k):
                        v = ex_data.get(k)
                        if isinstance(v, list) and len(v) == 1:
                            v = v[0]
                        return str(v).strip('"') if v is not None else None

                    parsed[ex_key.strip('"')] = {
                        "reason": _get_str("reason"),
                        "ticket": _get_str("ticket"),
                        "risk_status": _get_str("risk_status"),
                        "reviewer": _get_str("reviewer"),
                        "expires": _get_str("expires"),
                        "review_date": _get_str("review_date"),
                    }
                return parsed
    return {}




# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------


def parse_date(date_str: Optional[str]) -> Optional[date]:
    """Attempt to parse an ISO-format date string.

    Args:
        date_str: ISO date string (e.g. ``"2026-06-30"``) or ``None``.

    Returns:
        ``datetime.date`` or ``None`` if parsing fails.
    """
    if not date_str:
        return None
    try:
        return date.fromisoformat(date_str)
    except (ValueError, TypeError):
        return None


def is_exemption_expired(ex_data: Dict[str, Any], today: Optional[date] = None) -> bool:
    """Check if an exemption's expires date is in the past.

    Args:
        ex_data: Exemption dictionary.
        today: Current date override.

    Returns:
        True if the exemption has a valid expires date that is before today.
    """
    if today is None:
        today = date.today()
    expires_str = ex_data.get("expires")
    if not expires_str:
        return False
    expires_date = parse_date(expires_str)
    if expires_date is None:
        return False  # Malformed date fails safe
    return expires_date < today


def check_exemption_completeness(
    ex_data: Dict[str, Any],
    require_ticket: bool = False,
    warn_missing_reviewer: bool = False,
) -> List[str]:
    """Check for completeness of exemption fields.

    Args:
        ex_data: Exemption dictionary.
        require_ticket: If True, warn on missing ticket.
        warn_missing_reviewer: If True, warn on missing reviewer.

    Returns:
        List of warning/error messages.
    """
    issues: List[str] = []
    reason = ex_data.get("reason")
    if not reason or reason.strip() == "":
        issues.append("Missing reason")
    if require_ticket and not ex_data.get("ticket"):
        issues.append("Missing ticket")
    if warn_missing_reviewer and not ex_data.get("reviewer"):
        issues.append("Missing reviewer")
    return issues


def validate_exemptions(
    exemptions: Dict[str, Dict[str, Any]],
    enforce_expiry: bool = False,
    require_ticket: bool = False,
    warn_missing_reviewer: bool = False,
    today: Optional[date] = None,
) -> List[ExemptionResult]:
    """Validate a dictionary of exemptions.

    Args:
        exemptions: Dict of rule_id -> exemption dict.
        enforce_expiry: If True, flag expired as errors/warnings.
        require_ticket: Validate ticket presence.
        warn_missing_reviewer: Validate reviewer presence.
        today: Override today's date.

    Returns:
        List of ExemptionResult items.
    """
    if today is None:
        today = date.today()
    results: List[ExemptionResult] = []
    for rule_id, ex_data in exemptions.items():
        if is_exemption_expired(ex_data, today):
            results.append(
                ExemptionResult(
                    rule_id=rule_id,
                    module="",
                    result_type="EXPIRED" if enforce_expiry else "WARNING",
                    message=f"Exemption expired on {ex_data.get('expires')}",
                )
            )
        issues = check_exemption_completeness(
            ex_data, require_ticket, warn_missing_reviewer
        )
        for issue in issues:
            results.append(
                ExemptionResult(
                    rule_id=rule_id,
                    module="",
                    result_type="WARNING",
                    message=issue,
                )
            )
    return results


def parse_exemptions_from_modules(
    modules_exemptions: Dict[str, Dict[str, Any]]
) -> Dict[str, Dict[str, Any]]:
    """Parse and return exemptions from a raw modules input."""
    return modules_exemptions


def generate_exemption_report(
    modules_exemptions: Dict[str, Dict[str, Any]]
) -> str:
    """Generate a GRC-consumable JSON exemption report string."""
    report: Dict[str, Any] = {}
    timestamp_str = datetime.utcnow().isoformat() + "Z"
    for module_name, exemptions in modules_exemptions.items():
        report[module_name] = {}
        for rule_id, ex_data in exemptions.items():
            entry = dict(ex_data)
            entry["timestamp"] = timestamp_str
            report[module_name][rule_id] = entry
    return json.dumps(report, indent=2)


def check_exemptions(
    modules_dir: Path,
    enforce_expiry: bool = False,
    require_ticket: bool = False,
    warn_missing_reviewer: bool = False,
) -> Tuple[List[Dict[str, Any]], bool]:
    """Walk all modules and validate exemption declarations.

    Args:
        modules_dir: Path to ``modules/`` directory.
        enforce_expiry: If ``True``, exit non-zero when expired exemptions found.
        require_ticket: If ``True``, warn on exemptions missing a ticket.
        warn_missing_reviewer: If ``True``, warn on exemptions missing a reviewer.

    Returns:
        Tuple of ``(report_list, has_errors)`` where ``report_list`` is a
        list of exemption dicts and ``has_errors`` is ``True`` if any
        expired exemptions were found with ``enforce_expiry`` enabled.
    """
    today = date.today()
    variable_files = find_variables_files(modules_dir)
    report: List[Dict[str, Any]] = []
    has_errors = False

    if not variable_files:
        print("Warning: no variables.tf files found", file=sys.stderr)
        return report, has_errors

    for vf_path in variable_files:
        module_name = extract_module_name(vf_path)
        content = vf_path.read_text(encoding="utf-8")
        exemptions = parse_exemptions(content)

        if not exemptions:
            continue

        for ex_key, ex_data in exemptions.items():
            entry: Dict[str, Any] = {
                "module": module_name,
                "rule_id": ex_key,
                "reason": ex_data["reason"],
                "ticket": ex_data["ticket"],
                "risk_status": ex_data["risk_status"],
                "reviewer": ex_data["reviewer"],
                "expires": ex_data["expires"],
                "review_date": ex_data["review_date"],
            }

            # Check expiry
            expires_date = parse_date(ex_data["expires"])
            if expires_date is not None and expires_date < today:
                msg = (
                    f"EXPIRED: {ex_key} in {module_name} expired "
                    f"{ex_data['expires']} (today: {today})"
                )
                if enforce_expiry:
                    print(f"ERROR: {msg}", file=sys.stderr)
                    has_errors = True
                else:
                    print(f"WARNING: {msg}", file=sys.stderr)


            # Check risk status
            if ex_data["risk_status"] not in VALID_RISK_STATUSES:
                msg = f"INVALID RISK STATUS: {ex_data['risk_status']} in {module_name} for rule {ex_key}"
                print(f"ERROR: {msg}", file=sys.stderr)
                has_errors = True

            # Check ticket presence
            if require_ticket and not ex_data.get("ticket"):
                print(
                    f"WARNING: MISSING TICKET: {ex_key} in {module_name}",
                    file=sys.stderr,
                )

            # Check reviewer presence
            if warn_missing_reviewer and not ex_data.get("reviewer"):
                print(
                    f"WARNING: MISSING REVIEWER: {ex_key} in {module_name}",
                    file=sys.stderr,
                )

            report.append(entry)

    return report, has_errors


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def _build_argparser() -> argparse.ArgumentParser:
    """Construct the command-line argument parser."""
    parser = argparse.ArgumentParser(
        description="Validate exemption declarations across Terraform modules.",
    )
    parser.add_argument(
        "--modules-dir",
        required=True,
        type=Path,
        help="Path to modules/ directory",
    )
    parser.add_argument(
        "--enforce-expiry",
        type=bool_flag,
        default=False,
        help="Exit non-zero if any expired exemptions are found",
    )
    parser.add_argument(
        "--require-ticket",
        type=bool_flag,
        default=False,
        help="Warn if any exemption lacks a ticket reference",
    )
    parser.add_argument(
        "--warn-missing-reviewer",
        type=bool_flag,
        default=False,
        help="Warn if any exemption lacks a reviewer",
    )
    parser.add_argument(
        "--report-json",
        type=Path,
        default=None,
        help="Write JSON exemption report to this file",
    )
    return parser


def bool_flag(value: str) -> bool:
    """Parse a CLI boolean flag accepting true/false/yes/no/1/0.

    Args:
        value: String value from CLI.

    Returns:
        Boolean interpretation.

    Raises:
        argparse.ArgumentTypeError: If value is unrecognized.
    """
    if value.lower() in ("true", "yes", "1"):
        return True
    if value.lower() in ("false", "no", "0"):
        return False
    raise argparse.ArgumentTypeError(f"Invalid boolean: {value}")


def main() -> None:
    """Entry point for the exemption checker."""
    parser = _build_argparser()
    args = parser.parse_args()

    modules_dir: Path = args.modules_dir
    enforce_expiry: bool = args.enforce_expiry
    require_ticket: bool = args.require_ticket
    warn_missing_reviewer: bool = args.warn_missing_reviewer
    report_json: Optional[Path] = args.report_json

    if not modules_dir.is_dir():
        print(
            f"Error: modules directory not found: {modules_dir}",
            file=sys.stderr,
        )
        sys.exit(1)

    report, has_errors = check_exemptions(
        modules_dir=modules_dir,
        enforce_expiry=enforce_expiry,
        require_ticket=require_ticket,
        warn_missing_reviewer=warn_missing_reviewer,
    )

    if report_json is not None:
        report_json.parent.mkdir(parents=True, exist_ok=True)
        report_json.write_text(
            json.dumps(report, indent=2), encoding="utf-8"
        )
        print(f"Exemption report written to: {report_json}")

    summary = f"Checked {len(report)} exemption(s)"
    if has_errors:
        print(f"{summary} — expired exemptions found (BLOCKING)", file=sys.stderr)
        sys.exit(1)
    else:
        print(f"{summary} — OK")


if __name__ == "__main__":
    main()
