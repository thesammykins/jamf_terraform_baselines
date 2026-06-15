"""
Unit tests for scripts/generate_tf_compliance.py — the Variant A code generator.

These tests validate that the compliance module generator:
- Maintains the correct set of supported baselines (17) and macOS versions (3)
- Correctly parses mSCP baseline YAML definitions into structured rule data
- Generates valid HCL (Terraform configuration) from parsed rule data
- Creates the expected module directory structure for all baseline × version combos
"""

import json
import os
import tempfile
from pathlib import Path
from unittest.mock import MagicMock, mock_open, patch

import pytest

from scripts.generate_tf_compliance import (
    SUPPORTED_BASELINES,
    SUPPORTED_VERSIONS,
    generate_main_tf,
    generate_outputs_tf,
    generate_variables_tf,
    parse_baseline_yaml,
    extract_rules_from_baseline,
    write_module,
)

# ── Constants from spec ────────────────────────────────────────────────

EXPECTED_BASELINE_COUNT = 17  # All 17 NIST mSCP baselines including hicp_lp
EXPECTED_VERSION_COUNT = 3    # Sonoma (14), Sequoia (15), Tahoe (26)


# ── Test: SUPPORTED_BASELINES ──────────────────────────────────────────

def test_supported_baselines_count():
    """SUPPORTED_BASELINES must contain exactly 17 entries matching the spec."""
    count = len(SUPPORTED_BASELINES)
    assert count == EXPECTED_BASELINE_COUNT, (
        f"Expected {EXPECTED_BASELINE_COUNT} baselines, found {count}"
    )


def test_supported_baselines_keys():
    """Verify all expected baseline keys are present with correct metadata."""
    expected_keys = {
        "800-53r5_high",
        "800-53r5_moderate",
        "800-53r5_low",
        "800-53r5_privacy",
        "800-171",
        "disa_stig",
        "cmmc_lvl1",
        "cmmc_lvl2",
        "cnssi-1253_high",
        "cnssi-1253_moderate",
        "cnssi-1253_low",
        "nlmapgov_base",
        "nlmapgov_plus",
        "hicp_lp",
        "cis_lvl1",
        "cis_lvl2",
        "cisv8",
    }
    actual_keys = set(SUPPORTED_BASELINES.keys())
    assert actual_keys == expected_keys

    # Each entry must have a display_name and category
    for key, entry in SUPPORTED_BASELINES.items():
        assert "display_name" in entry, f"{key} missing 'display_name'"
        assert "category" in entry, f"{key} missing 'category'"
        assert entry["category"] in ("government", "industry", "international"), (
            f"{key}: unexpected category '{entry['category']}'"
        )


# ── Test: SUPPORTED_VERSIONS ───────────────────────────────────────────

def test_supported_versions_count():
    """SUPPORTED_VERSIONS must contain exactly 3 macOS versions."""
    count = len(SUPPORTED_VERSIONS)
    assert count == EXPECTED_VERSION_COUNT, (
        f"Expected {EXPECTED_VERSION_COUNT} versions, found {count}"
    )


def test_supported_versions_structure():
    """Each version entry must have name, min, and branch fields."""
    expected_version_keys = {"14", "15", "26"}
    assert set(SUPPORTED_VERSIONS.keys()) == expected_version_keys

    # macOS 14 = Sonoma
    assert SUPPORTED_VERSIONS["14"]["name"] == "Sonoma"
    assert SUPPORTED_VERSIONS["14"]["min"] == "14.0"
    assert SUPPORTED_VERSIONS["14"]["branch"] == "sonoma"

    # macOS 15 = Sequoia
    assert SUPPORTED_VERSIONS["15"]["name"] == "Sequoia"
    assert SUPPORTED_VERSIONS["15"]["min"] == "15.0"
    assert SUPPORTED_VERSIONS["15"]["branch"] == "sequoia"

    # macOS 26 = Tahoe
    assert SUPPORTED_VERSIONS["26"]["name"] == "Tahoe"
    assert SUPPORTED_VERSIONS["26"]["min"] == "26.0"
    assert SUPPORTED_VERSIONS["26"]["branch"] == "tahoe"


# ── Test: YAML parsing ─────────────────────────────────────────────────

MOCK_BASELINE_YAML = """
profile:
  - section: os
    rules:
      - os_gatekeeper_enable
      - os_sip_enable
      - os_dictation_disable
  - section: system_settings
    rules:
      - system_settings_time_server_configure
      - system_settings_screensaver_password_enforce
"""


def test_parse_baseline_yaml_rules():
    """Baseline YAML should be parsed correctly into the profile sections and rules structure."""
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_file = Path(tmpdir) / "baseline.yaml"
        tmp_file.write_text(MOCK_BASELINE_YAML, encoding="utf-8")
        
        result = parse_baseline_yaml(tmp_file)

        assert "profile" in result
        profile = result["profile"]
        assert len(profile) == 2
        assert profile[0]["section"] == "os"
        assert profile[0]["rules"] == [
            "os_gatekeeper_enable",
            "os_sip_enable",
            "os_dictation_disable",
        ]


def test_parse_baseline_yaml_empty():
    """Empty baseline YAML should return an empty dict or parse cleanly."""
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_file = Path(tmpdir) / "baseline.yaml"
        tmp_file.write_text("", encoding="utf-8")
        result = parse_baseline_yaml(tmp_file)
        assert result == {}


# ── Test: HCL generation ───────────────────────────────────────────────

MOCK_RULES = [
    {
        "id": "os_gatekeeper_enable",
        "title": "Enable Gatekeeper",
        "severity": "high",
        "discussion": "Gatekeeper discussion",
        "cce": {"macos_26": "CCE-91002"},
    },
    {
        "id": "os_sip_enable",
        "title": "Enable System Integrity Protection",
        "severity": "high",
        "discussion": "SIP discussion",
        "cce": {"macos_26": "CCE-91003"},
    },
    {
        "id": "os_dictation_disable",
        "title": "Disable Dictation",
        "severity": "medium",
        "discussion": "Dictation discussion",
        "cce": {"macos_26": "CCE-91004"},
    },
]


def test_generate_main_tf_produces_valid_hcl():
    """Generated main.tf must contain required resource blocks and locals."""
    hcl = generate_main_tf(
        baseline_key="cis_lvl1",
        baseline_display_name="CIS Level 1",
        macos_version_major="26",
        macos_version_min="26.0",
        macos_branch="tahoe",
        mscp_revision="tahoe_rev2",
        rules=MOCK_RULES,
    )

    # Required blocks
    assert 'locals {' in hcl
    assert 'all_rules' in hcl
    assert 'enabled_rules' in hcl
    assert 'resource "jamfplatform_device_group" "this"' in hcl
    assert 'data "jamfplatform_cbengine_rules" "this"' in hcl
    assert 'resource "jamfplatform_cbengine_benchmark" "this"' in hcl

    # Metadata references
    assert "CIS Level 1" in hcl
    assert "macOS 26" in hcl or "macos_26" in hcl
    assert "tahoe" in hcl
    assert "tahoe_rev2" in hcl

    # All rule IDs should appear in the all_rules local
    assert '"os_gatekeeper_enable"' in hcl
    assert '"os_sip_enable"' in hcl
    assert '"os_dictation_disable"' in hcl


def test_generate_main_tf_with_empty_rules():
    """Generating with an empty rule list should still produce valid HCL skeleton."""
    hcl = generate_main_tf(
        baseline_key="cis_lvl1",
        baseline_display_name="CIS Level 1",
        macos_version_major="26",
        macos_version_min="26.0",
        macos_branch="tahoe",
        mscp_revision="tahoe_rev2",
        rules=[],
    )

    assert 'resource "jamfplatform_device_group"' in hcl
    assert 'data "jamfplatform_cbengine_rules"' in hcl
    assert 'resource "jamfplatform_cbengine_benchmark"' in hcl
    assert "all_rules = []" in hcl or "all_rules = [" in hcl


def test_generate_variables_tf():
    """variables.tf must declare enforcement_mode, exemptions, and rule_overrides."""
    hcl = generate_variables_tf(
        baseline_key="cis_lvl1",
        baseline_display_name="CIS Level 1",
        macos_version_major="26",
        macos_version_min="26.0",
        macos_branch="tahoe",
        mscp_revision="tahoe_rev2",
        rule_count=len(MOCK_RULES),
    )

    assert 'variable "enforcement_mode"' in hcl
    assert 'variable "exemptions"' in hcl
    assert 'variable "rule_overrides"' in hcl
    assert '"MONITOR"' in hcl or "MONITOR" in hcl
    assert "exemptions" in hcl.lower()


def test_generate_outputs_tf():
    """outputs.tf must expose benchmark_id, device_group_id, and exemptions."""
    hcl = generate_outputs_tf(
        baseline_key="cis_lvl1",
        baseline_display_name="CIS Level 1",
    )

    assert 'output "benchmark_id"' in hcl
    assert 'output "device_group_id"' in hcl
    assert 'output "exemptions"' in hcl


# ── Test: Module directory structure ───────────────────────────────────

def test_write_module():
    """write_module must write all files in the correct baseline/version layout."""
    with tempfile.TemporaryDirectory() as tmpdir:
        output_base = Path(tmpdir) / "modules" / "compliance"

        write_module(
            output_dir=output_base,
            baseline_key="cis_lvl1",
            baseline_display_name="CIS Level 1",
            category="industry",
            macos_version_major="26",
            macos_version_min="26.0",
            macos_branch="tahoe",
            mscp_revision="tahoe_rev2",
            rules=MOCK_RULES,
        )

        # Check that all expected files were created
        expected_dir = output_base / "cis_lvl1" / "macos_26"
        assert expected_dir.exists()
        assert (expected_dir / "main.tf").exists()
        assert (expected_dir / "variables.tf").exists()
        assert (expected_dir / "outputs.tf").exists()
        assert (expected_dir / "versions.tf").exists()
        assert (expected_dir / "README.md").exists()


def test_generated_hcl_uses_terraform_conventions():
    """Generated HCL should follow Terraform formatting conventions."""
    hcl = generate_main_tf(
        baseline_key="cis_lvl1",
        baseline_display_name="CIS Level 1",
        macos_version_major="26",
        macos_version_min="26.0",
        macos_branch="tahoe",
        mscp_revision="tahoe_rev2",
        rules=MOCK_RULES,
    )

    # No hard tabs
    assert "\t" not in hcl, "HCL should not contain tab characters"

    # Resource names use underscores, not hyphens
    assert "jamfplatform_device_group" in hcl
    assert "jamfplatform_cbengine_benchmark" in hcl

    # Strings use double quotes (Terraform standard)
    assert '"this"' in hcl
    assert "= {" in hcl  # HCL block-opening brace on same line
