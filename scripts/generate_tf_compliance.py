#!/usr/bin/env python3
"""Generate Terraform compliance modules from NIST mSCP baseline YAML.

Reads mSCP baseline and rule YAML definitions and produces Terraform HCL
modules under ``modules/compliance/{baseline_key}/macos_{version_major}/``.
Each module references the Jamf Platform Compliance Benchmark Engine
(`jamfplatform_cbengine_benchmark`) with per-rule enable/disable and
organization-defined-value (ODV) overrides exposed as Terraform variables.

Typical usage:
    python generate_tf_compliance.py \\
        --mscp-path /tmp/mscp \\
        --output modules/compliance \\
        --branch all

Output per baseline × version:
    main.tf        – device group, cbengine data source, benchmark resource
    variables.tf   – enforcement_mode, disabled_rules, rule_overrides,
                     exemptions, baseline/macOS metadata
    outputs.tf     – benchmark_id, exemption_report
    README.md      – baseline description, rule count, framework info
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

SUPPORTED_BASELINES: Dict[str, Dict[str, str]] = {
    "800-53r5_high": {
        "display_name": "NIST SP 800-53 Rev 5 — High",
        "category": "government",
    },
    "800-53r5_moderate": {
        "display_name": "NIST SP 800-53 Rev 5 — Moderate",
        "category": "government",
    },
    "800-53r5_low": {
        "display_name": "NIST SP 800-53 Rev 5 — Low",
        "category": "government",
    },
    "800-53r5_privacy": {
        "display_name": "NIST SP 800-53 Rev 5 — Privacy",
        "category": "government",
    },
    "800-171": {
        "display_name": "NIST SP 800-171 Rev 3",
        "category": "government",
    },
    "disa_stig": {
        "display_name": "DISA macOS STIG",
        "category": "government",
    },
    "cmmc_lvl1": {
        "display_name": "CMMC 2.0 — Level 1",
        "category": "government",
    },
    "cmmc_lvl2": {
        "display_name": "CMMC 2.0 — Level 2",
        "category": "government",
    },
    "cnssi-1253_high": {
        "display_name": "CNSSI 1253 — High",
        "category": "government",
    },
    "cnssi-1253_moderate": {
        "display_name": "CNSSI 1253 — Moderate",
        "category": "government",
    },
    "cnssi-1253_low": {
        "display_name": "CNSSI 1253 — Low",
        "category": "government",
    },
    "nlmapgov_base": {
        "display_name": "Netherlands BIO — Base",
        "category": "government",
    },
    "nlmapgov_plus": {
        "display_name": "Netherlands BIO — Plus",
        "category": "government",
    },
    "cis_lvl1": {
        "display_name": "CIS macOS Benchmark — Level 1",
        "category": "industry",
    },
    "cis_lvl2": {
        "display_name": "CIS macOS Benchmark — Level 2",
        "category": "industry",
    },
    "cisv8": {
        "display_name": "CIS Controls v8",
        "category": "industry",
    },
}

SUPPORTED_VERSIONS: Dict[str, Dict[str, str]] = {
    "14": {"name": "Sonoma", "min": "14.0", "branch": "sonoma"},
    "15": {"name": "Sequoia", "min": "15.0", "branch": "sequoia"},
    "26": {"name": "Tahoe", "min": "26.0", "branch": "tahoe"},
}

RULE_DIRS: List[str] = [
    "audit",
    "auth",
    "icloud",
    "os",
    "pwpolicy",
    "system_settings",
    "supplemental",
    "inherent",
]

# ---------------------------------------------------------------------------
# YAML helpers (imported lazily so the script is importable without PyYAML)
# ---------------------------------------------------------------------------


def _import_yaml() -> Any:
    """Lazily import PyYAML so the module is importable for type-checking."""
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
# Path resolution
# ---------------------------------------------------------------------------


def resolve_rules_dir(mscp_path: Path) -> Path:
    """Resolve the mSCP rules directory, handling nested layouts.

    Args:
        mscp_path: Root of the cloned mSCP repository.

    Returns:
        Absolute path to the ``rules/`` directory.
    """
    direct = mscp_path / "rules"
    if direct.is_dir():
        return direct
    # Some mSCP container layouts nest under a subdirectory
    for candidate in mscp_path.iterdir():
        if candidate.is_dir() and (candidate / "rules").is_dir():
            return candidate / "rules"
    return direct


def resolve_baselines_dir(mscp_path: Path) -> Path:
    """Resolve the mSCP baselines directory.

    Args:
        mscp_path: Root of the cloned mSCP repository.

    Returns:
        Absolute path to the ``baselines/`` directory.
    """
    direct = mscp_path / "baselines"
    if direct.is_dir():
        return direct
    for candidate in mscp_path.iterdir():
        if candidate.is_dir() and (candidate / "baselines").is_dir():
            return candidate / "baselines"
    return direct


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------


def parse_version_yaml(mscp_path: Path) -> Dict[str, str]:
    """Extract current branch and revision from VERSION.yaml.

    Args:
        mscp_path: Root of the cloned mSCP repository.

    Returns:
        Dict with keys ``branch`` and ``revision`` (defaults to "unknown").
    """
    yaml = _import_yaml()
    version_file = mscp_path / "VERSION.yaml"
    if not version_file.is_file():
        return {"branch": "unknown", "revision": "unknown"}
    with open(version_file, "r", encoding="utf-8") as fh:
        data: Dict[str, Any] = yaml.safe_load(fh) or {}
    return {
        "branch": str(data.get("branch", "unknown")),
        "revision": str(data.get("revision", "unknown")),
    }


def parse_baseline_yaml(baseline_path: Path) -> Dict[str, Any]:
    """Parse a single baseline YAML and return its profile sections + rules.

    Args:
        baseline_path: Path to a ``baselines/{key}.yaml`` file.

    Returns:
        Dict with ``profile`` key containing sections and rule IDs.
    """
    yaml = _import_yaml()
    with open(baseline_path, "r", encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


def find_rule_yaml(rules_dir: Path, rule_id: str) -> Optional[Path]:
    """Search for a rule YAML file by rule ID across all rule subdirectories.

    Args:
        rules_dir: Resolved path to the ``rules/`` directory.
        rule_id: Rule identifier (e.g. ``os_gatekeeper_enable``).

    Returns:
        Path to the rule YAML file, or ``None`` if not found.
    """
    for subdir in RULE_DIRS:
        candidate = rules_dir / subdir / f"{rule_id}.yaml"
        if candidate.is_file():
            return candidate
    # Fallback: recursive search
    for candidate in rules_dir.rglob(f"{rule_id}.yaml"):
        return candidate
    return None


def parse_rule_yaml(rule_path: Path) -> Dict[str, Any]:
    """Parse a single rule YAML file and return its metadata.

    Args:
        rule_path: Path to a ``rules/{dir}/{id}.yaml`` file.

    Returns:
        Dict with keys: ``title``, ``discussion``, ``severity``,
        ``references``, ``platforms``.
    """
    yaml = _import_yaml()
    with open(rule_path, "r", encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


def extract_rules_from_baseline(
    baseline_data: Dict[str, Any],
    rules_dir: Path,
    macos_version_major: str,
    macos_branch: str,
) -> List[Dict[str, Any]]:
    """Extract and enrich rule metadata from a parsed baseline.

    For each rule ID in the baseline profile, cross-reference its rule
    YAML to pull title, discussion, severity, references, and
    version-specific enforcement info.

    Args:
        baseline_data: Parsed baseline YAML.
        rules_dir: Resolved path to the ``rules/`` directory.
        macos_version_major: e.g. ``"14"``.
        macos_branch: e.g. ``"sonoma"``.

    Returns:
        List of rule dicts ready for Terraform resource generation.
    """
    profile: Dict[str, Any] = baseline_data.get("profile", {})
    sections: List[Dict[str, Any]] = profile.get("section", [])
    rules: List[Dict[str, Any]] = []

    for section in sections:
        section_rules: List[str] = section.get("rules", [])
        for rule_id in section_rules:
            rule_path = find_rule_yaml(rules_dir, rule_id)
            title = rule_id
            discussion = ""
            severity = "medium"
            references: Dict[str, Any] = {}
            platforms_info: Dict[str, Any] = {}

            if rule_path is not None:
                rule_data = parse_rule_yaml(rule_path)
                title = rule_data.get("title", rule_id)
                discussion = rule_data.get("discussion", "")
                severity = rule_data.get("severity", "medium")
                references = rule_data.get("references", {})
                platforms_raw: Dict[str, Any] = rule_data.get("platforms", {})
                macos_info: Any = platforms_raw.get("macOS")
                if isinstance(macos_info, list):
                    for entry in macos_info:
                        if isinstance(entry, dict):
                            platforms_info = entry
                            break

            rules.append(
                {
                    "id": rule_id,
                    "title": title,
                    "discussion": discussion,
                    "severity": severity,
                    "references": references,
                    "platforms": platforms_info,
                }
            )

    return rules


# ---------------------------------------------------------------------------
# HCL generation helpers
# ---------------------------------------------------------------------------


def _hcl_escape(value: str) -> str:
    """Escape a string value for safe inclusion in HCL double-quoted strings.

    Args:
        value: Raw string.

    Returns:
        Escaped string safe for HCL interpolation.
    """
    return value.replace("\\", "\\\\").replace('"', '\\"')


def _hcl_map_literal(d: Dict[str, str], indent: int = 4) -> str:
    """Format a Python dict as an HCL map literal.

    Args:
        d: String-keyed dict.
        indent: Number of spaces for indentation.

    Returns:
        HCL map literal string.
    """
    if not d:
        return "{}"
    pad = " " * indent
    inner = ",\n".join(
        f'{pad}{k} = "{_hcl_escape(v)}"' for k, v in d.items()
    )
    return "{\n" + inner + "\n}"


def _hcl_list_literal(items: List[str], indent: int = 4) -> str:
    """Format a list of strings as an HCL list literal.

    Args:
        items: List of string values.
        indent: Number of spaces for indentation.

    Returns:
        HCL list literal string.
    """
    if not items:
        return "[]"
    pad = " " * indent
    inner = ",\n".join(f'{pad}"{_hcl_escape(i)}"' for i in items)
    return "[\n" + inner + "\n]"


def generate_main_tf(
    baseline_key: str,
    baseline_display_name: str,
    macos_version_major: str,
    macos_version_min: str,
    macos_branch: str,
    mscp_revision: str,
    rules: List[Dict[str, Any]],
) -> str:
    """Generate ``main.tf`` HCL content for a compliance module.

    Produces:
    * A ``locals`` block with all rule metadata.
    * A device group resource targeting the macOS version.
    * A ``jamfplatform_cbengine_rules`` data source.
    * A ``jamfplatform_cbengine_benchmark`` resource.

    Args:
        baseline_key: e.g. ``"cis_lvl1"``.
        baseline_display_name: Human-readable display name.
        macos_version_major: e.g. ``"26"``.
        macos_version_min: e.g. ``"26.0"``.
        macos_branch: mSCP branch name e.g. ``"tahoe"``.
        mscp_revision: mSCP release tag e.g. ``"tahoe_rev2"``.
        rules: List of enriched rule dicts.

    Returns:
        HCL string for ``main.tf``.
    """
    rules_json = json.dumps(
        [
            {
                "id": r["id"],
                "title": r["title"],
                "severity": r["severity"],
            }
            for r in rules
        ],
        indent=4,
    )

    return f'''# Compliance Baseline: {baseline_display_name}
# macOS {macos_version_major} ({macos_version_min}+)
# mSCP branch: {macos_branch}  revision: {mscp_revision}
# Generated by scripts/generate_tf_compliance.py — DO NOT EDIT DIRECTLY

locals {{
  # All rules for this baseline (id, title, severity)
  all_rules = {rules_json}

  enabled_rules = {{
    for rule in local.all_rules :
    rule.id => rule
    if !contains(var.disabled_rules, rule.id) && !contains(keys(var.exemptions), rule.id)
  }}
}}

# ---------------------------------------------------------------------------
# Device group — targets macOS {macos_version_major} devices
# ---------------------------------------------------------------------------
resource "jamfplatform_device_group" "this" {{
  name        = "${{var.baseline_display_name}} — macOS ${{var.macos_version}}"
  group_type  = "smart"
  device_type = "computer"
  criteria = [{{
    criteria = "Operating System Version"
    operator = "greater than or equal"
    value    = var.macos_version_min
  }}]
}}

# ---------------------------------------------------------------------------
# Compliance Benchmark Engine — rule metadata from mSCP
# ---------------------------------------------------------------------------
data "jamfplatform_cbengine_rules" "this" {{
  baseline_id = var.baseline_id
}}

# ---------------------------------------------------------------------------
# Benchmark resource — all rules enabled by default, with per-rule overrides
# ---------------------------------------------------------------------------
resource "jamfplatform_cbengine_benchmark" "this" {{
  title              = var.baseline_display_name
  description        = "${{var.baseline_display_name}} — mSCP ${{var.mscp_branch}} @ ${{var.mscp_revision}} — Managed by Terraform"
  source_baseline_id = var.baseline_id

  sources = [for s in data.jamfplatform_cbengine_rules.this.sources : {{
    branch   = s.branch
    revision = s.revision
  }}]

  rules = [
    for r in data.jamfplatform_cbengine_rules.this.rules : {{
      id      = r.id
      enabled = contains(keys(local.enabled_rules), r.id)
      odv_value = try(var.rule_overrides[r.id].odv_value, null)
    }}
  ]

  target_device_group = jamfplatform_device_group.this.id
  enforcement_mode    = var.enforcement_mode
}}
'''


def generate_variables_tf(
    baseline_key: str,
    baseline_display_name: str,
    macos_version_major: str,
    macos_version_min: str,
    macos_branch: str,
    mscp_revision: str,
    rule_count: int,
) -> str:
    """Generate ``variables.tf`` with all module input variables.

    Includes: enforcement_mode, disabled_rules, rule_overrides, exemptions,
    baseline metadata, and macOS version info.

    Args:
        baseline_key: e.g. ``"cis_lvl1"``.
        baseline_display_name: Human-readable display name.
        macos_version_major: e.g. ``"26"``.
        macos_version_min: e.g. ``"26.0"``.
        macos_branch: mSCP branch name.
        mscp_revision: mSCP release tag.
        rule_count: Number of rules in the baseline.

    Returns:
        HCL string for ``variables.tf``.
    """
    return f'''# Variables for {baseline_display_name} — macOS {macos_version_major}
# Generated by scripts/generate_tf_compliance.py — DO NOT EDIT DIRECTLY

# ---------------------------------------------------------------------------
# Enforcement
# ---------------------------------------------------------------------------
variable "enforcement_mode" {{
  type        = string
  default     = "MONITOR"
  description = "Enforcement mode for the compliance benchmark"

  validation {{
    condition     = contains(["MONITOR", "MONITOR_AND_ENFORCE"], var.enforcement_mode)
    error_message = "enforcement_mode must be MONITOR or MONITOR_AND_ENFORCE"
  }}
}}

# ---------------------------------------------------------------------------
# Rule management
# ---------------------------------------------------------------------------
variable "disabled_rules" {{
  type        = list(string)
  default     = []
  description = "Rule IDs to permanently disable (non-compliance decision)"
}}

variable "rule_overrides" {{
  type = map(object({{
    odv_value = optional(string)
  }}))
  default     = {{}}
  description = "Organization-Defined Value (ODV) overrides per rule"
}}

# ---------------------------------------------------------------------------
# Exemptions
# ---------------------------------------------------------------------------
variable "exemptions" {{
  type = map(object({{
    reason                = string
    ticket                = optional(string)
    risk_status           = string
    compensating_controls = optional(string)
    reviewer              = optional(string)
    review_date           = optional(string)
    expires               = optional(string)
  }}))
  default     = {{}}
  description = "Exemptions with audit justification for compliance tracking"

  validation {{
    condition = alltrue([
      for k, v in var.exemptions :
      contains(["ACCEPTED", "TEMPORARY", "ACCEPTED_WITH_COMPENSATING_CONTROLS", "UNDER_REVIEW"], v.risk_status)
    ])
    error_message = "risk_status must be one of: ACCEPTED, TEMPORARY, ACCEPTED_WITH_COMPENSATING_CONTROLS, UNDER_REVIEW"
  }}
}}

# ---------------------------------------------------------------------------
# Baseline metadata (set by generator, not user-overridable)
# ---------------------------------------------------------------------------
variable "baseline_id" {{
  type        = string
  default     = "{baseline_key}"
  description = "mSCP baseline identifier"
}}

variable "baseline_display_name" {{
  type        = string
  default     = "{_hcl_escape(baseline_display_name)}"
  description = "Human-readable baseline name"
}}

variable "mscp_branch" {{
  type        = string
  default     = "{macos_branch}"
  description = "mSCP git branch for this macOS version"
}}

variable "mscp_revision" {{
  type        = string
  default     = "{mscp_revision}"
  description = "mSCP release revision (tag)"
}}

variable "macos_version" {{
  type        = string
  default     = "{macos_version_major}"
  description = "macOS major version number"
}}

variable "macos_version_min" {{
  type        = string
  default     = "{macos_version_min}"
  description = "Minimum macOS version for device group targeting"
}}

variable "rule_count" {{
  type        = number
  default     = {rule_count}
  description = "Number of rules in this baseline"
}}
'''


def generate_outputs_tf(
    baseline_key: str,
    baseline_display_name: str,
) -> str:
    """Generate ``outputs.tf`` with benchmark ID and exemption report.

    Args:
        baseline_key: e.g. ``"cis_lvl1"``.
        baseline_display_name: Human-readable display name.

    Returns:
        HCL string for ``outputs.tf``.
    """
    return f'''# Outputs for {baseline_display_name}
# Generated by scripts/generate_tf_compliance.py — DO NOT EDIT DIRECTLY

output "benchmark_id" {{
  value       = jamfplatform_cbengine_benchmark.this.id
  description = "ID of the created benchmark resource"
}}

output "exemption_report" {{
  value = {{
    for k, v in var.exemptions : k => merge(v, {{
      module        = var.baseline_id
      macos_version = var.macos_version
      timestamp     = timestamp()
    }})
  }}
  description = "Active exemptions with audit justification"
}}
'''


def generate_readme(
    baseline_key: str,
    baseline_display_name: str,
    category: str,
    macos_version_major: str,
    macos_version_min: str,
    macos_branch: str,
    mscp_revision: str,
    rule_count: int,
    rules: List[Dict[str, Any]],
) -> str:
    """Generate ``README.md`` with baseline description and metadata.

    Args:
        baseline_key: Baseline identifier.
        baseline_display_name: Human-readable name.
        category: ``"government"``, ``"industry"``, or ``"international"``.
        macos_version_major: macOS major version.
        macos_version_min: Minimum macOS version string.
        macos_branch: mSCP branch name.
        mscp_revision: mSCP release tag.
        rule_count: Number of rules.
        rules: List of enriched rule dicts.

    Returns:
        Markdown string.
    """
    severity_counts: Dict[str, int] = {}
    for r in rules:
        sev = r.get("severity", "medium")
        severity_counts[sev] = severity_counts.get(sev, 0) + 1

    sev_lines = "\n".join(
        f"- **{s}**: {c} rules" for s, c in sorted(severity_counts.items())
    )

    return f"""# {baseline_display_name} — macOS {macos_version_major}

## Overview

- **Baseline key**: `{baseline_key}`
- **Category**: {category}
- **macOS version**: {macos_version_major} ({macos_version_min}+)
- **mSCP branch**: `{macos_branch}`
- **mSCP revision**: `{mscp_revision}`
- **Rule count**: {rule_count}

## Severity distribution

{sev_lines}

## Usage

```hcl
module "{baseline_key}_macos_{macos_version_major}" {{
  source = "./modules/compliance/{baseline_key}/macos_{macos_version_major}"

  enforcement_mode = "MONITOR_AND_ENFORCE"

  # Override organization-defined values
  rule_overrides = {{
    "example_rule_id" = {{
      odv_value = "your-value-here"
    }}
  }}

  # Exempt rules with justification
  exemptions = {{
    "example_rule_id" = {{
      reason      = "Operational requirement"
      ticket      = "SEC-XXXX"
      risk_status = "ACCEPTED"
    }}
  }}
}}
```

## Important

This module is **auto-generated** by `scripts/generate_tf_compliance.py`.
Do not edit files in this directory directly — changes will be overwritten
on the next CI run.

To add or remove rules, modify the generator script or update the upstream
mSCP baseline definition at https://github.com/usnistgov/macos_security.
"""


# ---------------------------------------------------------------------------
# File I/O
# ---------------------------------------------------------------------------


def write_module(
    output_dir: Path,
    baseline_key: str,
    baseline_display_name: str,
    category: str,
    macos_version_major: str,
    macos_version_min: str,
    macos_branch: str,
    mscp_revision: str,
    rules: List[Dict[str, Any]],
) -> None:
    """Write a complete Terraform module to the output directory.

    Creates: ``main.tf``, ``variables.tf``, ``outputs.tf``, ``README.md``.

    Args:
        output_dir: Base output directory (e.g. ``modules/compliance``).
        baseline_key: Baseline identifier.
        baseline_display_name: Human-readable name.
        category: Baseline category.
        macos_version_major: macOS major version.
        macos_version_min: Minimum macOS version string.
        macos_branch: mSCP branch name.
        mscp_revision: mSCP release tag.
        rules: List of enriched rule dicts.
    """
    module_dir = output_dir / baseline_key / f"macos_{macos_version_major}"
    module_dir.mkdir(parents=True, exist_ok=True)

    main_tf = generate_main_tf(
        baseline_key=baseline_key,
        baseline_display_name=baseline_display_name,
        macos_version_major=macos_version_major,
        macos_version_min=macos_version_min,
        macos_branch=macos_branch,
        mscp_revision=mscp_revision,
        rules=rules,
    )
    (module_dir / "main.tf").write_text(main_tf, encoding="utf-8")

    variables_tf = generate_variables_tf(
        baseline_key=baseline_key,
        baseline_display_name=baseline_display_name,
        macos_version_major=macos_version_major,
        macos_version_min=macos_version_min,
        macos_branch=macos_branch,
        mscp_revision=mscp_revision,
        rule_count=len(rules),
    )
    (module_dir / "variables.tf").write_text(variables_tf, encoding="utf-8")

    outputs_tf = generate_outputs_tf(
        baseline_key=baseline_key,
        baseline_display_name=baseline_display_name,
    )
    (module_dir / "outputs.tf").write_text(outputs_tf, encoding="utf-8")

    readme = generate_readme(
        baseline_key=baseline_key,
        baseline_display_name=baseline_display_name,
        category=category,
        macos_version_major=macos_version_major,
        macos_version_min=macos_version_min,
        macos_branch=macos_branch,
        mscp_revision=mscp_revision,
        rule_count=len(rules),
        rules=rules,
    )
    (module_dir / "README.md").write_text(readme, encoding="utf-8")


# ---------------------------------------------------------------------------
# Orchestration
# ---------------------------------------------------------------------------


def generate_all(
    mscp_path: Path,
    output_dir: Path,
    branch_filter: Optional[str] = None,
    baseline_filter: Optional[str] = None,
    version_filter: Optional[str] = None,
) -> List[str]:
    """Generate compliance modules for all baseline × version combinations.

    Args:
        mscp_path: Root of cloned mSCP repository.
        output_dir: Base output directory.
        branch_filter: If set, only process this mSCP branch (e.g. ``"tahoe"``).
        baseline_filter: If set, only process this baseline key.
        version_filter: If set, only process this macOS major version.

    Returns:
        List of generated module directory paths.
    """
    yaml = _import_yaml()
    rules_dir = resolve_rules_dir(mscp_path)
    baselines_dir = resolve_baselines_dir(mscp_path)
    version_info = parse_version_yaml(mscp_path)

    generated: List[str] = []

    for baseline_key, baseline_meta in SUPPORTED_BASELINES.items():
        if baseline_filter is not None and baseline_key != baseline_filter:
            continue

        baseline_file = baselines_dir / f"{baseline_key}.yaml"
        if not baseline_file.is_file():
            print(
                f"Warning: baseline file not found: {baseline_file}",
                file=sys.stderr,
            )
            continue

        baseline_data = parse_baseline_yaml(baseline_file)

        for ver_major, ver_meta in SUPPORTED_VERSIONS.items():
            if version_filter is not None and ver_major != version_filter:
                continue
            if branch_filter is not None and branch_filter != "all" and ver_meta["branch"] != branch_filter:
                continue

            rules = extract_rules_from_baseline(
                baseline_data=baseline_data,
                rules_dir=rules_dir,
                macos_version_major=ver_major,
                macos_branch=ver_meta["branch"],
            )

            mscp_revision = version_info.get("revision", "unknown")

            module_dir = str(
                output_dir / baseline_key / f"macos_{ver_major}"
            )

            write_module(
                output_dir=output_dir,
                baseline_key=baseline_key,
                baseline_display_name=baseline_meta["display_name"],
                category=baseline_meta["category"],
                macos_version_major=ver_major,
                macos_version_min=ver_meta["min"],
                macos_branch=ver_meta["branch"],
                mscp_revision=mscp_revision,
                rules=rules,
            )

            generated.append(module_dir)
            print(f"Generated: {module_dir} ({len(rules)} rules)")

    return generated


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def _build_argparser() -> argparse.ArgumentParser:
    """Construct the command-line argument parser."""
    parser = argparse.ArgumentParser(
        description="Generate Terraform compliance modules from NIST mSCP baselines.",
    )
    parser.add_argument(
        "--mscp-path",
        required=True,
        type=Path,
        help="Path to cloned mSCP repository",
    )
    parser.add_argument(
        "--output",
        required=True,
        type=Path,
        help="Base output directory for generated modules (e.g. modules/compliance)",
    )
    parser.add_argument(
        "--branch",
        default="all",
        help="mSCP branch to process (tahoe, sequoia, sonoma, or 'all')",
    )
    parser.add_argument(
        "--baseline",
        default=None,
        help="Process only this baseline key (e.g. cis_lvl1)",
    )
    parser.add_argument(
        "--version",
        default=None,
        help="Process only this macOS major version (e.g. 26)",
    )
    return parser


def main() -> None:
    """Entry point for the compliance module generator."""
    parser = _build_argparser()
    args = parser.parse_args()

    mscp_path: Path = args.mscp_path
    output_dir: Path = args.output
    branch_filter: Optional[str] = args.branch
    baseline_filter: Optional[str] = args.baseline
    version_filter: Optional[str] = args.version

    if not mscp_path.is_dir():
        print(f"Error: mSCP path does not exist: {mscp_path}", file=sys.stderr)
        sys.exit(1)

    output_dir.mkdir(parents=True, exist_ok=True)

    generated = generate_all(
        mscp_path=mscp_path,
        output_dir=output_dir,
        branch_filter=None if branch_filter == "all" else branch_filter,
        baseline_filter=baseline_filter,
        version_filter=version_filter,
    )

    if not generated:
        print("No modules generated. Check baseline files and filters.", file=sys.stderr)
        sys.exit(1)

    print(f"\nDone. {len(generated)} module(s) generated.")


if __name__ == "__main__":
    main()
