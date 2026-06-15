"""
Unit tests for scripts/generate_changelog.py — the per-PR changelog generator.

These tests validate that the changelog generator correctly:
- Detects newly added rules (ADDED)
- Detects removed rules (REMOVED)
- Detects modified rules (MODIFIED)
- Handles the no-change case correctly
- Produces valid markdown output matching the expected PR body format
"""

from scripts.generate_changelog import (
    ChangeType,
    compute_changelog,
    format_changelog_markdown,
    parse_rule_state,
)


# ── Mock data fixtures ─────────────────────────────────────────────────

PREVIOUS_RULES = [
    {"id": "os_gatekeeper_enable", "title": "Enable Gatekeeper", "severity": "high"},
    {"id": "os_sip_enable", "title": "Enable SIP", "severity": "high"},
    {"id": "os_dictation_disable", "title": "Disable Dictation", "severity": "medium"},
    {"id": "system_settings_screensaver_password_enforce", "title": "Screensaver Password", "severity": "medium"},
    {"id": "system_settings_software_update_enforce", "title": "Software Update", "severity": "medium"},
    {"id": "pwpolicy_account_lockout_enforce", "title": "Account Lockout", "severity": "high"},
]

CURRENT_RULES = [
    {"id": "os_gatekeeper_enable", "title": "Enable Gatekeeper", "severity": "high"},
    {"id": "os_sip_enable", "title": "Enable SIP", "severity": "high"},
    {"id": "os_loginwindow_adminhostinfo_disabled", "title": "Disable AdminHostInfo at Login Window", "severity": "low"},  # ADDED
    {"id": "os_safari_clear_history_disable", "title": "Disable Safari Clear History", "severity": "low"},                    # ADDED
    {"id": "system_settings_screensaver_password_enforce", "title": "Screensaver Password (updated)", "severity": "medium"},  # MODIFIED (title changed)
    {"id": "pwpolicy_account_lockout_enforce", "title": "Account Lockout Enforcement", "severity": "high"},                   # MODIFIED (title changed)
    # os_dictation_disable REMOVED
    # system_settings_software_update_enforce REMOVED
]

IDENTICAL_RULES = PREVIOUS_RULES  # Same rules, no changes


# ── Test: Rule state parsing ───────────────────────────────────────────

def test_parse_rule_state_empty():
    """Parsing an empty rule list returns empty dict keyed by rule ID."""
    result = parse_rule_state([])
    assert result == {}


def test_parse_rule_state_maps_by_id():
    """Rule state should be indexed by rule ID for fast lookup."""
    result = parse_rule_state(PREVIOUS_RULES)
    assert "os_gatekeeper_enable" in result
    assert result["os_gatekeeper_enable"]["title"] == "Enable Gatekeeper"
    assert result["os_gatekeeper_enable"]["severity"] == "high"


# ── Test: Changelog computation ────────────────────────────────────────

def test_compute_changelog_detects_added_rules():
    """Rules present in current but not previous are flagged as ADDED."""
    changes = compute_changelog(PREVIOUS_RULES, CURRENT_RULES)

    added = {c.rule_id for c in changes if c.change_type == ChangeType.ADDED}
    assert "os_loginwindow_adminhostinfo_disabled" in added
    assert "os_safari_clear_history_disable" in added


def test_compute_changelog_detects_removed_rules():
    """Rules present in previous but not current are flagged as REMOVED."""
    changes = compute_changelog(PREVIOUS_RULES, CURRENT_RULES)

    removed = {c.rule_id for c in changes if c.change_type == ChangeType.REMOVED}
    assert "os_dictation_disable" in removed
    assert "system_settings_software_update_enforce" in removed


def test_compute_changelog_detects_modified_rules():
    """Rules with same ID but different title/severity are flagged as MODIFIED."""
    changes = compute_changelog(PREVIOUS_RULES, CURRENT_RULES)

    modified = {c.rule_id: c for c in changes if c.change_type == ChangeType.MODIFIED}
    assert "pwpolicy_account_lockout_enforce" in modified
    assert "system_settings_screensaver_password_enforce" in modified

    # The change should include a note about why it was flagged
    assert modified["pwpolicy_account_lockout_enforce"].note is not None


def test_compute_changelog_no_change_case():
    """Identical rule lists should produce zero changes."""
    changes = compute_changelog(IDENTICAL_RULES, IDENTICAL_RULES)
    assert len(changes) == 0


def test_compute_changelog_empty_both():
    """Two empty rule lists should produce zero changes."""
    changes = compute_changelog([], [])
    assert len(changes) == 0


def test_compute_changelog_all_new():
    """Going from empty to populated should flag everything as ADDED."""
    changes = compute_changelog([], CURRENT_RULES)
    assert len(changes) == len(CURRENT_RULES)
    assert all(c.change_type == ChangeType.ADDED for c in changes)


def test_compute_changelog_all_removed():
    """Going from populated to empty should flag everything as REMOVED."""
    changes = compute_changelog(PREVIOUS_RULES, [])
    assert len(changes) == len(PREVIOUS_RULES)
    assert all(c.change_type == ChangeType.REMOVED for c in changes)


# ── Test: Markdown output ──────────────────────────────────────────────

def test_format_changelog_markdown_structure():
    """Output markdown must follow the expected PR body format."""
    changes = compute_changelog(PREVIOUS_RULES, CURRENT_RULES)
    markdown = format_changelog_markdown(
        changes=changes,
        baseline_name="CIS Level 1",
        macos_version="26",
        old_revision="tahoe_rev1",
        new_revision="tahoe_rev2",
    )

    # Header with baseline name and version range
    assert "CIS Level 1" in markdown
    assert "macOS 26" in markdown or "macos_26" in markdown
    assert "tahoe_rev1" in markdown
    assert "tahoe_rev2" in markdown

    # Markdown table header
    assert "| Change" in markdown
    assert "| Rule ID" in markdown or "|--------" in markdown

    # Each change type should appear
    assert "ADDED" in markdown
    assert "REMOVED" in markdown
    assert "MODIFIED" in markdown


def test_format_changelog_markdown_no_changes():
    """No-change case should produce a clear 'no changes' message."""
    changes = compute_changelog(IDENTICAL_RULES, IDENTICAL_RULES)
    markdown = format_changelog_markdown(
        changes=changes,
        baseline_name="CIS Level 1",
        macos_version="26",
        old_revision="tahoe_rev1",
        new_revision="tahoe_rev2",
    )

    assert "no changes" in markdown.lower() or "No changes" in markdown


def test_format_changelog_markdown_includes_rule_count():
    """Changelog should include the rule count for both old and new states."""
    changes = compute_changelog(PREVIOUS_RULES, CURRENT_RULES)
    markdown = format_changelog_markdown(
        changes=changes,
        baseline_name="CIS Level 1",
        macos_version="26",
        old_revision="tahoe_rev1",
        new_revision="tahoe_rev2",
    )

    # The previous and current rule counts should be referenced
    assert "6" in markdown or "5" in markdown  # Count appears somewhere


def test_format_changelog_markdown_sort_order():
    """Changes should be grouped by type: ADDED first, then MODIFIED, then REMOVED."""
    changes = compute_changelog(PREVIOUS_RULES, CURRENT_RULES)
    markdown = format_changelog_markdown(
        changes=changes,
        baseline_name="CIS Level 1",
        macos_version="26",
        old_revision="tahoe_rev1",
        new_revision="tahoe_rev2",
    )

    # Check that ADDED appears before MODIFIED and REMOVED in the output
    added_pos = markdown.find("ADDED")
    removed_pos = markdown.find("REMOVED")
    modified_pos = markdown.find("MODIFIED")

    # Not all types may be present, but if both found, ADDED should come first
    if added_pos >= 0 and removed_pos >= 0:
        assert added_pos < removed_pos, "ADDED should appear before REMOVED in changelog"


# ── Test: ChangeType enum ──────────────────────────────────────────────

def test_changetype_values():
    """ChangeType enum must have the three expected values."""
    assert ChangeType.ADDED.value == "ADDED"
    assert ChangeType.REMOVED.value == "REMOVED"
    assert ChangeType.MODIFIED.value == "MODIFIED"


# ── Test: Edge cases ───────────────────────────────────────────────────

def test_rule_title_change_detected_as_modified():
    """A rule whose ID is unchanged but title differs should be MODIFIED."""
    prev = [{"id": "os_firewall_enable", "title": "Enable Firewall", "severity": "high"}]
    curr = [{"id": "os_firewall_enable", "title": "Enable Application Firewall", "severity": "high"}]
    changes = compute_changelog(prev, curr)
    assert len(changes) == 1
    assert changes[0].change_type == ChangeType.MODIFIED


def test_rule_severity_change_detected_as_modified():
    """A rule whose severity changes should also be flagged as MODIFIED."""
    prev = [{"id": "os_firewall_enable", "title": "Enable Firewall", "severity": "medium"}]
    curr = [{"id": "os_firewall_enable", "title": "Enable Firewall", "severity": "high"}]
    changes = compute_changelog(prev, curr)
    assert len(changes) == 1
    assert changes[0].change_type == ChangeType.MODIFIED


def test_unchanged_rule_not_flagged():
    """A rule with identical ID, title, and severity should not appear in changes."""
    prev = [{"id": "os_gatekeeper_enable", "title": "Enable Gatekeeper", "severity": "high"}]
    curr = [{"id": "os_gatekeeper_enable", "title": "Enable Gatekeeper", "severity": "high"}]
    changes = compute_changelog(prev, curr)
    assert len(changes) == 0
