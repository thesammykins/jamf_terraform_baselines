"""Tests for scripts/generate_changelog.py."""

import json
from pathlib import Path

from scripts.generate_changelog import (
    RuleSnapshot,
    compute_module_diff,
    extract_profile_entries,
    extract_rule_ids_from_profile,
    write_changelog_outputs,
)


def _snapshot(
    rule_id: str,
    section: str = "macos",
    metadata_hash: str = "same",
) -> RuleSnapshot:
    return RuleSnapshot(
        id=rule_id,
        title=f"Title for {rule_id}",
        section=section,
        metadata={"title": f"Title for {rule_id}"},
        metadata_hash=metadata_hash,
    )


def _write_rule(
    root: Path,
    rule_id: str,
    *,
    title: str | None = None,
    severity: str = "medium",
    references: dict | None = None,
    odv: dict | None = None,
) -> None:
    rule_path = root / "rules" / "os" / f"{rule_id}.yaml"
    rule_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "id": rule_id,
        "title": title or f"Title for {rule_id}",
        "severity": severity,
        "references": references or {"800-53r5": ["AC-1"]},
        "tags": ["cis_lvl1"],
        "mobileconfig": True,
    }
    if odv is not None:
        payload["odv"] = odv
    lines = []
    for key, value in payload.items():
        if isinstance(value, (dict, list)):
            lines.append(f"{key}: {json.dumps(value)}")
        else:
            lines.append(f'{key}: "{value}"')
    rule_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _write_baseline(root: Path, filename: str, rule_sections: list[tuple[str, list[str]]]) -> None:
    baseline_path = root / "baselines" / filename
    baseline_path.parent.mkdir(parents=True, exist_ok=True)
    lines = ['title: "Fixture baseline"', "profile:"]
    for section, rules in rule_sections:
        lines.append(f'  - section: "{section}"')
        lines.append("    rules:")
        for rule in rules:
            lines.append(f"      - {rule}")
    baseline_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _write_fixture_repo(root: Path) -> None:
    root.mkdir(parents=True, exist_ok=True)
    (root / "VERSION.yaml").write_text(
        'os: "26.0"\nplatform: macOS\nversion: "Tahoe Guidance, Revision 3.0"\n',
        encoding="utf-8",
    )
    _write_baseline(
        root,
        "cis_lvl1.yaml",
        [
            ("macos", ["stable_rule", "added_rule", "changed_rule"]),
            ("systemsettings", ["moved_rule"]),
        ],
    )
    _write_baseline(root, "DISA-STIG.yaml", [("macos", ["stig_rule"])])
    for rule_id in ["stable_rule", "added_rule", "moved_rule", "stig_rule"]:
        _write_rule(root, rule_id)
    _write_rule(
        root,
        "changed_rule",
        severity="high",
        references={"800-53r5": ["AC-2"]},
        odv={"recommended": 900},
    )


def _previous_state() -> dict:
    return {
        "schema_version": 2,
        "branches": {"tahoe": "tahoe_rev2"},
        "modules": {
            "cis_lvl1/macos_26": {
                "rules": {
                    "stable_rule": {
                        "title": "Title for stable_rule",
                        "section": "macos",
                        "metadata": {
                            "title": "Title for stable_rule",
                            "severity": "medium",
                            "references": {"800-53r5": ["AC-1"]},
                            "tags": ["cis_lvl1"],
                            "mobileconfig": "True",
                        },
                        "metadata_hash": "73fbd16308ede8f46ec3890444e7a24c6001b181edef1b35d105aa6671f87fe6",
                    },
                    "changed_rule": {
                        "title": "Title for changed_rule",
                        "section": "macos",
                        "metadata": {
                            "title": "Title for changed_rule",
                            "severity": "medium",
                            "references": {"800-53r5": ["AC-1"]},
                            "tags": ["cis_lvl1"],
                            "mobileconfig": "True",
                        },
                        "metadata_hash": "old-hash",
                    },
                    "moved_rule": {
                        "title": "Title for moved_rule",
                        "section": "macos",
                        "metadata": {
                            "title": "Title for moved_rule",
                            "severity": "medium",
                            "references": {"800-53r5": ["AC-1"]},
                            "tags": ["cis_lvl1"],
                            "mobileconfig": "True",
                        },
                        "metadata_hash": "649816c91d5f15a36074a09df2e37c8e6875a8922deac8770af901ad03dd2a03",
                    },
                    "removed_rule": {
                        "title": "Title for removed_rule",
                        "section": "macos",
                        "metadata": {"title": "Title for removed_rule"},
                        "metadata_hash": "removed-hash",
                    },
                }
            }
        },
    }


def test_extract_rule_ids_from_list_profile():
    baseline_data = {
        "profile": [
            {"section": "macos", "rules": ["os_gatekeeper_enable"]},
            {
                "section": "systemsettings",
                "rules": ["system_settings_screensaver_timeout_enforce"],
            },
        ]
    }

    assert extract_rule_ids_from_profile(baseline_data) == [
        "os_gatekeeper_enable",
        "system_settings_screensaver_timeout_enforce",
    ]
    assert extract_profile_entries(baseline_data)[1]["section"] == "systemsettings"


def test_extract_rule_ids_from_legacy_dict_profile():
    baseline_data = {
        "profile": {
            "section": [
                {"section": "macos", "rules": ["os_gatekeeper_enable"]},
                {"section": "auth", "rules": ["auth_smartcard_allow"]},
            ]
        }
    }

    assert extract_rule_ids_from_profile(baseline_data) == [
        "os_gatekeeper_enable",
        "auth_smartcard_allow",
    ]
    assert extract_profile_entries(baseline_data)[1]["section"] == "auth"


def test_compute_module_diff_reports_only_real_changes():
    previous = {
        "stable": _snapshot("stable"),
        "moved": _snapshot("moved", section="old"),
        "changed": _snapshot("changed", metadata_hash="old"),
        "removed": _snapshot("removed"),
    }
    current = {
        "stable": _snapshot("stable"),
        "moved": _snapshot("moved", section="new"),
        "changed": _snapshot("changed", metadata_hash="new"),
        "added": _snapshot("added"),
    }

    diff = compute_module_diff(
        baseline_key="cis_lvl1",
        display_name="CIS Level 1",
        macos_version="26",
        previous_rules=previous,
        current_rules=current,
    )

    assert [rule.id for rule in diff.added] == ["added"]
    assert [rule.id for rule in diff.removed] == ["removed"]
    assert [rule.id for rule in diff.moved] == ["moved"]
    assert [rule.id for rule in diff.metadata_changed] == ["changed"]
    assert "stable" not in {rule.id for rule in diff.metadata_changed}


def test_write_changelog_outputs_with_fixture_repo(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    mscp_path = tmp_path / "mscp"
    _write_fixture_repo(mscp_path)
    state_path = tmp_path / ".ci" / "mscp-rule-state.json"
    state_path.parent.mkdir()
    state_path.write_text(json.dumps(_previous_state()), encoding="utf-8")

    result = write_changelog_outputs(
        mscp_path=mscp_path,
        branch="tahoe",
        full_output=None,
        summary_output=tmp_path / "changelog-summary.md",
        summary_limit=20_000,
    )

    full_path = tmp_path / "docs" / "compliance-changelogs" / "tahoe_tahoe_rev3.md"
    summary_path = tmp_path / "changelog-summary.md"
    assert full_path.is_file()
    assert summary_path.is_file()
    assert len(summary_path.read_text(encoding="utf-8")) < 20_000

    summary = summary_path.read_text(encoding="utf-8")
    assert "Full changelog" in summary
    assert "docs/compliance-changelogs/tahoe_tahoe_rev3.md" in summary
    assert "CIS macOS Benchmark" in summary

    full = full_path.read_text(encoding="utf-8")
    assert "ADDED" in full
    assert "REMOVED" in full
    assert "MOVED" in full
    assert "METADATA_CHANGED" in full
    assert "Baseline State Initialized" in full
    assert any(diff.baseline_key == "cis_lvl1" for diff in result.module_diffs)
    assert any(diff.baseline_key == "disa_stig" for diff in result.initialized_modules)

    state = json.loads(state_path.read_text(encoding="utf-8"))
    assert state["schema_version"] == 2
    assert state["branches"]["tahoe"] == "tahoe_rev3"
    assert "metadata_hash" in state["modules"]["cis_lvl1/macos_26"]["rules"]["stable_rule"]


def test_large_summary_stays_under_limit(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    mscp_path = tmp_path / "mscp"
    _write_fixture_repo(mscp_path)
    rules = [f"added_rule_{idx}" for idx in range(300)]
    _write_baseline(mscp_path, "cis_lvl2.yaml", [("macos", rules)])
    for rule_id in rules:
        _write_rule(mscp_path, rule_id)

    write_changelog_outputs(
        mscp_path=mscp_path,
        branch="tahoe",
        full_output=None,
        summary_output=tmp_path / "changelog-summary.md",
        summary_limit=4_000,
    )

    assert len((tmp_path / "changelog-summary.md").read_text(encoding="utf-8")) <= 4_000


def test_workflow_uses_summary_body_and_full_changelog_artifact():
    workflow = Path(".github/workflows/compliance-update.yml").read_text(
        encoding="utf-8"
    )

    assert "--summary-output changelog-summary.md" in workflow
    assert "body-path: changelog-summary.md" in workflow
    assert "--output changelog.md" not in workflow
    assert "test -f .ci/mscp-revision-state.json" in workflow
    assert "test -f .ci/mscp-rule-state.json" in workflow
    assert "test -f changelog-summary.md" in workflow
    assert "docs/compliance-changelogs" in workflow
