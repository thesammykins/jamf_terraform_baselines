# Software Updates — deploys configuration profile for macOS update
# deferral, auto-download, auto-install, and Rapid Security Response settings.

resource "jamfpro_macos_configuration_profile_plist" "software_update" {
  count = (
    var.enable_software_updates &&
    !contains(keys(var.exemptions), "software_updates")
  ) ? 1 : 0

  name                = "macAdmin Foundation — Software Updates"
  description         = "Configures macOS software update deferral and auto-install policies. Managed by Terraform."
  level               = "System"
  distribution_method = "Install Automatically"
  redeploy_on_update  = "Newly Assigned"
  user_removable      = false
  payloads            = templatefile("${path.module}/templates/software-update.mobileconfig.tftpl", {
    major_deferral_days          = var.software_update_major_deferral_days
    minor_deferral_days          = var.software_update_minor_deferral_days
    rapid_security_response      = var.rapid_security_response_enabled
  })
  payload_validate    = true

  scope {
    all_computers = true
    all_jss_users = false
  }
}
