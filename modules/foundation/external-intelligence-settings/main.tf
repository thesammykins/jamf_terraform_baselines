# External Intelligence Settings — manages third-party AI integration
# (ChatGPT and similar services) via DDM declarations.
#
# DDM-NATIVE PATH (macOS 26.4+, iOS 26.4+):
# Uses com.apple.configuration.external-intelligence.settings declaration payload.
# Controls: enable/disable external AI, sign-in, workspace allowlisting.
#
# LEGACY PATH (macOS 25 – 26.3):
# Uses com.apple.applicationaccess restriction keys:
# allowExternalIntelligenceIntegrations, allowExternalIntelligenceIntegrationsSignIn.
# Set var.use_legacy_profile = true to enable this fallback.
#
# Reference: https://github.com/apple/device-management (declarative/configurations/external-intelligence.settings.yaml)
# Migration deadline: Before upgrading fleet past macOS 26.3.

resource "jamfpro_macos_configuration_profile_plist" "external_intelligence_ddm" {
  count = (
    var.enable_external_intelligence_settings &&
    !var.use_legacy_profile &&
    !contains(keys(var.exemptions), "external_intelligence_settings")
  ) ? 1 : 0

  name                = "macAdmin Foundation — External Intelligence Settings (DDM)"
  description         = "Manages third-party AI integration (ChatGPT, etc.) via DDM declaration. macOS 26.4+ required. Managed by Terraform."
  level               = "System"
  distribution_method = "Install Automatically"
  redeploy_on_update  = "Newly Assigned"
  user_removable      = false
  payloads = templatefile("${path.module}/templates/external-intelligence-ddm.mobileconfig.tftpl", {
    enabled               = var.enable_external_intelligence
    allow_sign_in         = var.allow_external_intelligence_sign_in
    allowed_workspace_ids = var.allowed_workspace_ids
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

# Legacy fallback (DEPRECATED) — for macOS 25 through 26.3 compatibility.
# Uses com.apple.applicationaccess restriction keys.
# Does NOT support workspace allowlisting.
resource "jamfpro_macos_configuration_profile_plist" "external_intelligence_legacy" {
  count = (
    var.enable_external_intelligence_settings &&
    var.use_legacy_profile &&
    !contains(keys(var.exemptions), "external_intelligence_settings")
  ) ? 1 : 0

  name                = "[LEGACY] macAdmin Foundation — External Intelligence Settings"
  description         = "DEPRECATED — Uses com.apple.applicationaccess restrictions. Transition to DDM in macOS 26.4+. Managed by Terraform."
  level               = "System"
  distribution_method = "Install Automatically"
  redeploy_on_update  = "Newly Assigned"
  user_removable      = false
  payloads = templatefile("${path.module}/templates/external-intelligence-legacy.mobileconfig.tftpl", {
    enabled       = var.enable_external_intelligence
    allow_sign_in = var.allow_external_intelligence_sign_in
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
