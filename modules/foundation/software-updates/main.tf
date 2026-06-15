# Software Updates — manages macOS software update policy via DDM Managed Software Updates.
#
# NOTE: The legacy com.apple.SoftwareUpdate configuration profile payload is DEPRECATED
# in macOS 26 (Tahoe) and REMOVED in macOS 27 (Golden Gate). Apple requires transitioning
# to declarative software update management via DDM (com.apple.configuration.softwareupdate.settings).
#
# This module enables Jamf Pro's Managed Software Updates feature toggle (DDM-backed).
# A legacy profile fallback is available via var.use_legacy_profile for migration windows.
#
# Reference: https://support.apple.com/en-au/124963
# Migration deadline: Before upgrading fleet to macOS 27 (Golden Gate, expected Sep 2026).

# Enable the Managed Software Update feature in Jamf Pro (required for DDM updates).
# This is a singleton toggle — only one should exist per Jamf Pro instance.
# OPERATOR NOTE: Set manage_feature_toggle = true on ONE deployment of this module
# (typically the first one). Subsequent deployments should set it to false.
resource "jamfpro_managed_software_update_feature_toggle" "enable" {
  count = (
    var.enable_software_updates &&
    var.manage_feature_toggle &&
    !contains(keys(var.exemptions), "software_updates")
  ) ? 1 : 0

  toggle = true
}

# DDM-native Managed Software Update plans — one per macOS version smart group.
# These use Apple's com.apple.configuration.softwareupdate.settings DDM declaration.
# Requires the feature toggle (above) to be enabled on the Jamf Pro instance.
# Targets version-specific smart computer groups from the os-version-smart-groups module.
resource "jamfpro_managed_software_update" "ddm_plans" {
  for_each = var.smart_group_ids

  update_action = var.ddm_update_action
  version_type  = var.ddm_version_type

  group {
    group_id    = each.value
    object_type = "COMPUTER_GROUP"
  }

  max_deferrals = var.ddm_max_deferrals
}

# Legacy configuration profile (DEPRECATED) — for macOS 25 and earlier compatibility.
# Uses the com.apple.SoftwareUpdate payload which is REMOVED in macOS 27 (Golden Gate).
# Set var.use_legacy_profile = true to enable this fallback path during migration.
resource "jamfpro_macos_configuration_profile_plist" "software_update_legacy" {
  count = (
    var.enable_software_updates &&
    var.use_legacy_profile &&
    !contains(keys(var.exemptions), "software_updates")
  ) ? 1 : 0

  name                = "[DEPRECATED] macAdmin Foundation — Software Updates (Legacy)"
  description         = "DEPRECATED — Uses com.apple.SoftwareUpdate payload which is removed in macOS 27. Transition to DDM Managed Software Updates. Managed by Terraform."
  level               = "System"
  distribution_method = "Install Automatically"
  redeploy_on_update  = "Newly Assigned"
  user_removable      = false
  payloads = templatefile("${path.module}/templates/software-update.mobileconfig.tftpl", {
    major_deferral_days     = var.software_update_major_deferral_days
    minor_deferral_days     = var.software_update_minor_deferral_days
    rapid_security_response = var.rapid_security_response_enabled
  })
  payload_validate = true

  scope {
    all_computers = true
    all_jss_users = false
  }

  lifecycle {
    create_before_destroy = true
  }
}
