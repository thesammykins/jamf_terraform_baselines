"""
Unit tests for scripts/generate_changelog.py — the per-PR changelog generator.

These tests validate that the changelog generator correctly:
- Detects newly added rules (ADDED)
- Detects removed rules (REMOVED)
- Groups common rules as candidates for modification (MODIFIED)
- Handles the no-change case correctly
- Produces valid markdown output matching the expected PR body format
"""

from scripts.generate_changelog import (
    compute_diff,
    generate_changelog_markdown,
)

# ── Mock data fixtures ─────────────────────────────────────────────────

PREVIOUS_RULES = [
    "os_gatekeeper_enable",
    "os_sip_enable",
    "os_dictation_disable",
    "system_settings_screensaver_password_enforce",
    "system_settings_software_update_enforce",
    "pwpolicy_account_lockout_enforce",
]

CURRENT_RULES = [
    "os_gatekeeper_enable",
    "os_sip_enable",
    "os_loginwindow_adminhostinfo_disabled",  # ADDED
    "os_safari_clear_history_disable",       # ADDED
    "system_settings_screensaver_password_enforce",
    "pwpolicy_account_lockout_enforce",
    # os_dictation_disable REMOVED
    # system_settings_software_update_enforce REMOVED
]

IDENTICAL_RULES = PREVIOUS_RULES  # Same rules, no changes


# ── Test: Changelog computation ────────────────────────────────────────

def test_compute_diff_detects_added_rules():
    """Rules present in current but not previous are flagged as ADDED."""
    added, removed, common = compute_diff(PREVIOUS_RULES, CURRENT_RULES)
    assert "os_loginwindow_adminhostinfo_disabled" in added
    assert "os_safari_clear_history_disable" in added


def test_compute_diff_detects_removed_rules():
    """Rules present in previous but not current are flagged as REMOVED."""
    added, removed, common = compute_diff(PREVIOUS_RULES, CURRENT_RULES)
    assert "os_dictation_disable" in removed
    assert "system_settings_software_update_enforce" in removed


def test_compute_diff_no_change_case():
    """Identical rule lists should produce zero added and removed changes."""
    added, removed, common = compute_diff(IDENTICAL_RULES, IDENTICAL_RULES)
    assert len(added) == 0
    assert len(removed) == 0
    assert len(common) == len(IDENTICAL_RULES)


def test_compute_diff_empty_both():
    """Two empty rule lists should produce zero changes."""
    added, removed, common = compute_diff([], [])
    assert len(added) == 0
    assert len(removed) == 0
    assert len(common) == 0


def test_compute_diff_all_new():
    """Going from empty to populated should flag everything as ADDED."""
    added, removed, common = compute_diff([], CURRENT_RULES)
    assert len(added) == len(CURRENT_RULES)
    assert len(removed) == 0
    assert len(common) == 0


def test_compute_diff_all_removed():
    """Going from populated to empty should flag everything as REMOVED."""
    added, removed, common = compute_diff(PREVIOUS_RULES, [])
    assert len(added) == 0
    assert len(removed) == len(PREVIOUS_RULES)
    assert len(common) == 0


# ── Test: Markdown output ──────────────────────────────────────────────

def test_generate_changelog_markdown_structure():
    """Output markdown must follow the expected PR body format."""
    added, removed, modified = compute_diff(PREVIOUS_RULES, CURRENT_RULES)
    
    rule_titles = {
        "os_gatekeeper_enable": "Enable Gatekeeper",
        "os_sip_enable": "Enable SIP",
        "os_loginwindow_adminhostinfo_disabled": "Disable AdminHostInfo",
        "os_safari_clear_history_disable": "Disable Safari History",
        "system_settings_screensaver_password_enforce": "Screensaver Password",
        "pwpolicy_account_lockout_enforce": "Account Lockout",
    }

    markdown = generate_changelog_markdown(
        baseline_key="cis_lvl1",
        ver_major="26",
        ver_meta={"name": "Tahoe", "branch": "tahoe"},
        old_revision="tahoe_rev1",
        new_revision="tahoe_rev2",
        added=added,
        removed=removed,
        modified=modified,
        rule_titles=rule_titles,
    )

    # Header with baseline name and version range
    assert "CIS macOS Benchmark — Level 1" in markdown
    assert "macOS 26" in markdown
    assert "tahoe_rev1" in markdown
    assert "tahoe_rev2" in markdown

    # Markdown table header
    assert "| Change" in markdown
    assert "| Rule ID" in markdown or "|--------" in markdown

    # Each change type should appear in the table
    assert "ADDED" in markdown
    assert "REMOVED" in markdown
    assert "MODIFIED" in markdown


def test_generate_changelog_markdown_no_changes():
    """No-change case should produce a clear 'none' message in the table."""
    markdown = generate_changelog_markdown(
        baseline_key="cis_lvl1",
        ver_major="26",
        ver_meta={"name": "Tahoe", "branch": "tahoe"},
        old_revision="tahoe_rev1",
        new_revision="tahoe_rev2",
        added=[],
        removed=[],
        modified=[],
        rule_titles={},
    )

    assert "none" in markdown.lower()
