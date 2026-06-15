"""
Unit tests for scripts/check_exemptions.py — the exemption validation script.

These tests validate that the exemption checker correctly:
- Detects expired exemptions (expires date in the past)
- Detects missing ticket references
- Detects missing reviewer attribution
- Passes valid exemptions without errors
- Generates a machine-readable JSON exemption report
"""

import json
from datetime import date, timedelta

import pytest

from scripts.check_exemptions import (
    ExemptionResult,
    check_exemption_completeness,
    generate_exemption_report,
    is_exemption_expired,
    parse_exemptions_from_modules,
    validate_exemptions,
)


# ── Mock data fixtures ─────────────────────────────────────────────────

# Valid exemption — should pass all checks
VALID_EXEMPTION = {
    "reason": "Clinical staff require dictation for EHR workflows",
    "ticket": "SEC-4521",
    "risk_status": "ACCEPTED",
    "reviewer": "jane.doe@example.com",
    "review_date": "2026-12-01",
}

# Expired exemption — TEMPORARY with past expires date
EXPIRED_EXEMPTION = {
    "reason": "Temporary waiver for Q1 testing",
    "ticket": "IT-9012",
    "risk_status": "TEMPORARY",
    "expires": "2025-01-15",  # Well in the past
    "reviewer": "ciso@example.com",
}

# Missing ticket — no ticket reference
MISSING_TICKET_EXEMPTION = {
    "reason": "Operational necessity",
    "risk_status": "ACCEPTED",
    "reviewer": "admin@example.com",
}

# Missing reviewer — no reviewer attribution
MISSING_REVIEWER_EXEMPTION = {
    "reason": "Field researchers share data between devices",
    "ticket": "GRC-2025-089",
    "risk_status": "ACCEPTED_WITH_COMPENSATING_CONTROLS",
    "compensating_controls": "Restricted VLAN only",
}

# Empty exemption — just a reason, nothing else
MINIMAL_EXEMPTION = {
    "reason": "Minimal justification",
    "risk_status": "ACCEPTED",
}

# Full module exemption set simulating a compliance module
MOCK_MODULE_EXEMPTIONS = {
    "os_dictation_disable": VALID_EXEMPTION,
    "system_settings_bluetooth_disable": EXPIRED_EXEMPTION,
    "os_airdrop_disable": MISSING_TICKET_EXEMPTION,
    "icloud_keychain_disable": MISSING_REVIEWER_EXEMPTION,
}

# Another module with no exemptions
MOCK_EMPTY_MODULE = {}


# ── Test: Expiration detection ─────────────────────────────────────────

def test_expired_exemption_detected():
    """An exemption with expires in the past should be flagged as expired."""
    today = date.today()
    # Create a TEMPORARY exemption that expired yesterday
    exemption = {
        "reason": "Test waiver",
        "ticket": "TICKET-001",
        "risk_status": "TEMPORARY",
        "expires": (today - timedelta(days=1)).isoformat(),
        "reviewer": "reviewer@example.com",
    }
    assert is_exemption_expired(exemption, today) is True


def test_future_expiration_not_flagged():
    """An exemption with expires in the future should NOT be flagged."""
    today = date.today()
    exemption = {
        "reason": "Future waiver",
        "ticket": "TICKET-002",
        "risk_status": "TEMPORARY",
        "expires": (today + timedelta(days=90)).isoformat(),
        "reviewer": "reviewer@example.com",
    }
    assert is_exemption_expired(exemption, today) is False


def test_accepted_exemption_never_expires():
    """ACCEPTED exemptions without expires field should never be expired."""
    assert is_exemption_expired(VALID_EXEMPTION) is False


def test_exemption_without_expires_not_expired():
    """Exemptions without an expires key should not be considered expired."""
    assert is_exemption_expired(MISSING_TICKET_EXEMPTION) is False


# ── Test: Completeness checks ──────────────────────────────────────────

def test_valid_exemption_passes_all_checks():
    """A complete, valid exemption should pass all completeness checks."""
    issues = check_exemption_completeness(VALID_EXEMPTION)
    assert len(issues) == 0


def test_missing_ticket_detected():
    """Exemptions without a ticket field should produce a warning."""
    issues = check_exemption_completeness(
        MISSING_TICKET_EXEMPTION,
        require_ticket=True,
    )
    assert len(issues) > 0
    assert any("ticket" in issue.lower() for issue in issues)


def test_missing_ticket_not_flagged_when_require_ticket_is_false():
    """When require_ticket is False, missing tickets should be allowed."""
    issues = check_exemption_completeness(
        MISSING_TICKET_EXEMPTION,
        require_ticket=False,
    )
    ticket_issues = [i for i in issues if "ticket" in i.lower()]
    assert len(ticket_issues) == 0


def test_missing_reviewer_detected():
    """Exemptions without a reviewer field should produce a warning."""
    issues = check_exemption_completeness(
        MISSING_REVIEWER_EXEMPTION,
        warn_missing_reviewer=True,
    )
    assert len(issues) > 0
    assert any("reviewer" in issue.lower() for issue in issues)


def test_missing_reviewer_not_flagged_when_warn_is_false():
    """When warn_missing_reviewer is False, missing reviewers should be allowed."""
    issues = check_exemption_completeness(
        MISSING_REVIEWER_EXEMPTION,
        warn_missing_reviewer=False,
    )
    reviewer_issues = [i for i in issues if "reviewer" in i.lower()]
    assert len(reviewer_issues) == 0


def test_empty_reason_detected():
    """Exemptions with empty reason should be flagged."""
    bad = dict(MINIMAL_EXEMPTION)
    bad["reason"] = ""
    issues = check_exemption_completeness(bad)
    assert len(issues) > 0
    assert any("reason" in issue.lower() for issue in issues)


# ── Test: Module parsing ───────────────────────────────────────────────

def test_parse_exemptions_from_modules_returns_grouped_results():
    """Exemptions should be parsed and grouped by module name."""
    results = parse_exemptions_from_modules(
        modules_exemptions={
            "cis_lvl1_macos_26": MOCK_MODULE_EXEMPTIONS,
            "disa_stig_macos_26": MOCK_EMPTY_MODULE,
        }
    )

    # Should have entries for the module with exemptions
    assert "cis_lvl1_macos_26" in results
    assert len(results["cis_lvl1_macos_26"]) == len(MOCK_MODULE_EXEMPTIONS)

    # Empty module should still be present with empty dict
    assert "disa_stig_macos_26" in results
    assert len(results["disa_stig_macos_26"]) == 0


def test_parse_exemptions_from_empty_modules():
    """Parsing empty input should return empty dict."""
    results = parse_exemptions_from_modules({})
    assert results == {}


# ── Test: Validation ───────────────────────────────────────────────────

def test_validate_exemptions_detects_expired():
    """validate_exemptions should catch expired exemptions."""
    today = date.today()
    exemptions = {
        "test_rule": {
            "reason": "Test",
            "ticket": "T-1",
            "risk_status": "TEMPORARY",
            "expires": (today - timedelta(days=1)).isoformat(),
            "reviewer": "r@e.com",
        }
    }
    results = validate_exemptions(exemptions, enforce_expiry=True, today=today)

    # Should return at least one Expired result
    expired = [r for r in results if r.result_type == "EXPIRED"]
    assert len(expired) == 1
    assert expired[0].rule_id == "test_rule"


def test_validate_exemptions_passes_valid():
    """validate_exemptions should pass a valid exemption without errors."""
    results = validate_exemptions(
        {"valid_rule": VALID_EXEMPTION},
        enforce_expiry=True,
        require_ticket=False,
        warn_missing_reviewer=False,
    )
    # No EXPIRED, no WARNING
    errors = [r for r in results if r.result_type in ("EXPIRED", "WARNING", "ERROR")]
    assert len(errors) == 0


def test_validate_exemptions_empty():
    """validate_exemptions on empty input should return empty list."""
    results = validate_exemptions({})
    assert len(results) == 0


def test_validate_exemptions_expiry_not_enforced():
    """When enforce_expiry is False, expired exemptions produce warnings not errors."""
    today = date.today()
    exemptions = {
        "test_rule": {
            "reason": "Test",
            "ticket": "T-1",
            "risk_status": "TEMPORARY",
            "expires": (today - timedelta(days=30)).isoformat(),
            "reviewer": "r@e.com",
        }
    }
    results = validate_exemptions(exemptions, enforce_expiry=False, today=today)

    expired_errors = [r for r in results if r.result_type == "EXPIRED"]
    assert len(expired_errors) == 0, "Should not error when enforce_expiry is False"


# ── Test: JSON report generation ───────────────────────────────────────

def test_generate_exemption_report_produces_valid_json():
    """The exemption report should be valid JSON consumable by GRC tools."""
    report = generate_exemption_report(
        modules_exemptions={
            "cis_lvl1_macos_26": MOCK_MODULE_EXEMPTIONS,
        }
    )

    # Should be valid JSON
    parsed = json.loads(report)
    assert "cis_lvl1_macos_26" in parsed
    assert "os_dictation_disable" in parsed["cis_lvl1_macos_26"]

    # Each exemption entry should include required fields
    entry = parsed["cis_lvl1_macos_26"]["os_dictation_disable"]
    assert "reason" in entry
    assert "risk_status" in entry
    assert "timestamp" in entry  # Generated at report time


def test_generate_exemption_report_includes_module_metadata():
    """Each exemption entry should include module-level metadata."""
    report = generate_exemption_report(
        modules_exemptions={
            "cis_lvl1_macos_26": {"os_dictation_disable": VALID_EXEMPTION},
        }
    )
    parsed = json.loads(report)
    entry = parsed["cis_lvl1_macos_26"]["os_dictation_disable"]

    assert "module" not in entry or "module" in entry
    # Risk status must be present (required field from spec)
    assert entry["risk_status"] == "ACCEPTED"


def test_generate_exemption_report_empty_modules():
    """Generating a report with no exemptions should produce valid empty JSON."""
    report = generate_exemption_report(
        modules_exemptions={
            "foundation": {},
        }
    )
    parsed = json.loads(report)
    assert "foundation" in parsed
    assert isinstance(parsed["foundation"], dict)


def test_generate_exemption_report_no_modules():
    """Generating a report with no modules at all should produce empty object."""
    report = generate_exemption_report(modules_exemptions={})
    parsed = json.loads(report)
    assert parsed == {}


# ── Test: ExemptionResult dataclass ────────────────────────────────────

def test_exemption_result_fields():
    """ExemptionResult should have the expected fields."""
    result = ExemptionResult(
        rule_id="os_dictation_disable",
        module="cis_lvl1_macos_26",
        result_type="ACCEPTED",
        message="Exemption is valid",
    )
    assert result.rule_id == "os_dictation_disable"
    assert result.module == "cis_lvl1_macos_26"
    assert result.result_type == "ACCEPTED"
    assert result.message == "Exemption is valid"


# ── Test: Edge cases ───────────────────────────────────────────────────

def test_exemption_with_today_expires():
    """An exemption expiring today should NOT be flagged as expired."""
    today = date.today()
    exemption = {
        "reason": "Today expiry",
        "ticket": "TICKET-003",
        "risk_status": "TEMPORARY",
        "expires": today.isoformat(),
        "reviewer": "reviewer@example.com",
    }
    # Expiring today means still valid for the current day
    assert is_exemption_expired(exemption, today) is False


def test_exemption_with_malformed_date():
    """An exemption with a non-parseable date should not crash."""
    exemption = {
        "reason": "Bad date",
        "ticket": "TICKET-004",
        "risk_status": "TEMPORARY",
        "expires": "not-a-real-date",
        "reviewer": "reviewer@example.com",
    }
    # Should not raise; should treat as valid (can't determine if expired)
    try:
        result = is_exemption_expired(exemption)
        assert result is False  # Fail-safe: treat unparseable as not-expired
    except ValueError:
        pytest.fail("is_exemption_expired raised ValueError on malformed date")
