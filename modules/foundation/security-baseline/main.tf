# Security Baseline — deploys essential macOS security configuration profiles
# for FileVault encryption, firewall, screensaver lock, and Gatekeeper.

resource "jamfpro_macos_configuration_profile_plist" "filevault" {
  count = (
    var.enable_security_baseline &&
    !contains(keys(var.exemptions), "filevault")
  ) ? 1 : 0

  name                = "Security Baseline — FileVault"
  description         = "Enforces FileVault full-disk encryption. Managed by Terraform."
  level               = "System"
  distribution_method = "Install Automatically"
  redeploy_on_update  = "Newly Assigned"
  user_removable      = false
  payloads            = templatefile("${path.module}/templates/filevault.mobileconfig.tftpl", {})
  payload_validate    = true

  scope {
    all_computers = true
    all_jss_users = false
  }
}

resource "jamfpro_macos_configuration_profile_plist" "firewall" {
  count = (
    var.enable_security_baseline &&
    !contains(keys(var.exemptions), "firewall")
  ) ? 1 : 0

  name                = "Security Baseline — Firewall"
  description         = "Enables firewall with stealth mode and signed application access. Managed by Terraform."
  level               = "System"
  distribution_method = "Install Automatically"
  redeploy_on_update  = "Newly Assigned"
  user_removable      = false
  payloads            = templatefile("${path.module}/templates/firewall.mobileconfig.tftpl", {})
  payload_validate    = true

  scope {
    all_computers = true
    all_jss_users = false
  }
}

resource "jamfpro_macos_configuration_profile_plist" "screensaver" {
  count = (
    var.enable_security_baseline &&
    !contains(keys(var.exemptions), "screensaver")
  ) ? 1 : 0

  name                = "Security Baseline — Screensaver"
  description         = "Enforces screensaver password after idle timeout. Managed by Terraform."
  level               = "System"
  distribution_method = "Install Automatically"
  redeploy_on_update  = "Newly Assigned"
  user_removable      = false
  payloads = templatefile("${path.module}/templates/screensaver.mobileconfig.tftpl", {
    idle_timeout_minutes = var.screensaver_idle_timeout_minutes
  })
  payload_validate = true

  scope {
    all_computers = true
    all_jss_users = false
  }
}

resource "jamfpro_macos_configuration_profile_plist" "gatekeeper" {
  count = (
    var.enable_security_baseline &&
    !contains(keys(var.exemptions), "gatekeeper")
  ) ? 1 : 0

  name                = "Security Baseline — Gatekeeper"
  description         = "Restricts app execution to App Store and identified developers. Managed by Terraform."
  level               = "System"
  distribution_method = "Install Automatically"
  redeploy_on_update  = "Newly Assigned"
  user_removable      = false
  payloads            = templatefile("${path.module}/templates/gatekeeper.mobileconfig.tftpl", {})
  payload_validate    = true

  scope {
    all_computers = true
    all_jss_users = false
  }
}
