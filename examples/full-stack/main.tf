terraform {
  required_version = ">= 1.9.0"
  required_providers {
    jamfplatform = {
      source  = "Jamf-Concepts/jamfplatform"
      version = ">= 0.17.0"
    }
    jamfpro = {
      source  = "deploymenttheory/jamfpro"
      version = ">= 0.36.0"
    }
  }
}

# ── Provider: Jamf Platform (Variant A — Compliance) ─────────────────
provider "jamfplatform" {
  client_id     = var.jamfplatform_client_id
  client_secret = var.jamfplatform_client_secret
  base_url      = var.jamfplatform_base_url
}

# ── Provider: Jamf Pro (Variant B — Foundation) ──────────────────────
provider "jamfpro" {
  client_id             = var.jamfpro_client_id
  client_secret         = var.jamfpro_client_secret
  jamfpro_instance_fqdn = var.jamfpro_instance_fqdn
  auth_method           = "oauth2"
}

# ─────────────────────────────────────────────────────────────────────
# Variant A — Compliance Baselines
# ─────────────────────────────────────────────────────────────────────

# CIS Level 1 — macOS 26 (Tahoe)
module "cis_l1_tahoe" {
  source = "../../modules/compliance/cis_lvl1/macos_26"

  enforcement_mode = "MONITOR_AND_ENFORCE"

  exemptions = {
    "os_dictation_disable" = {
      reason      = "Clinical staff require dictation for EHR workflows"
      ticket      = "SEC-4521"
      risk_status = "ACCEPTED"
    }
  }
}

# DISA STIG — macOS 26 (Tahoe)
module "disa_stig_tahoe" {
  source = "../../modules/compliance/disa_stig/macos_26"

  enforcement_mode = "MONITOR"
}

# NIST 800-53 Moderate — macOS 26 (Tahoe)
module "nist_80053_moderate_tahoe" {
  source = "../../modules/compliance/800-53r5_moderate/macos_26"

  enforcement_mode = "MONITOR_AND_ENFORCE"

  # Override organization-defined values where needed
  rule_overrides = {
    "system_settings_time_server_configure" = {
      odv_value = "ntp.example.com"
    }
  }

  exemptions = {
    "icloud_keychain_disable" = {
      reason      = "Users need iCloud Keychain for cross-device password sync in BYOD-optional program"
      ticket      = "GRC-2026-014"
      risk_status = "ACCEPTED"
      reviewer    = "jane.doe@example.com"
      review_date = "2026-12-01"
    }
    "os_iphone_mirroring_disable" = {
      reason                = "Engineering team uses iPhone mirroring for iOS app testing on Mac"
      ticket                = "ENG-4412"
      risk_status           = "ACCEPTED_WITH_COMPENSATING_CONTROLS"
      compensating_controls = "iPhone Mirroring restricted to Developer VLAN (subnet 10.88.0.0/16) via network segmentation; only enrolled corporate iPhones permitted"
      reviewer              = "security-team@example.com"
    }
    "system_settings_bluetooth_disable" = {
      reason      = "Bluetooth required for wireless peripherals in open-plan office"
      ticket      = "IT-9012"
      risk_status = "TEMPORARY"
      expires     = "2026-09-30"
      reviewer    = "ciso@example.com"
    }
  }
}

# ─────────────────────────────────────────────────────────────────────
# Variant B — macAdmin Foundation
# ─────────────────────────────────────────────────────────────────────

# ── Variant B Submodules ────────────────────────────────────────────

module "categories" {
  source = "../../modules/foundation/categories"

  enable_categories = true
}

module "os_version_smart_groups" {
  source = "../../modules/foundation/os-version-smart-groups"

  enable_smart_groups = true
}

module "security_baseline" {
  source = "../../modules/foundation/security-baseline"

  enable_security_baseline         = true
  screensaver_idle_timeout_minutes = 5
}

module "software_updates" {
  source = "../../modules/foundation/software-updates"

  enable_software_updates             = true
  manage_feature_toggle               = true
  use_legacy_profile                  = false
  ddm_update_action                   = "DOWNLOAD_INSTALL_ALLOW_DEFERRAL"
  ddm_version_type                    = "LATEST_MAJOR"
  ddm_max_deferrals                   = 3
  software_update_major_deferral_days = 90
  software_update_minor_deferral_days = 14
  rapid_security_response_enabled     = true

  smart_group_ids = module.os_version_smart_groups.smart_group_ids
}

module "pppc_screen_capture" {
  source = "../../modules/foundation/pppc-screen-capture"

  enable_pppc_screen_capture = true
  pppc_tools                 = ["Zoom", "Slack", "Microsoft Teams", "Google Chrome", "Webex"]
}

module "pppc_accessibility" {
  source = "../../modules/foundation/pppc-accessibility"

  enable_pppc_accessibility = true
  pppc_tools                = ["Zoom", "Slack", "Microsoft Teams", "Dropbox"]
}

module "device_enrollment" {
  source = "../../modules/foundation/device-enrollment"

  enable_device_enrollment = false

  exemptions = {
    "device_enrollment" = {
      reason      = "ADE token not yet provisioned — will re-enable in Q3"
      ticket      = "IT-7823"
      risk_status = "TEMPORARY"
      expires     = "2026-09-30"
    }
  }
}

module "inventory_settings" {
  source = "../../modules/foundation/inventory-settings"

  enable_inventory_settings = true
  checkin_frequency_minutes = 15
}

module "intelligence_settings" {
  source = "../../modules/foundation/intelligence-settings"

  enable_intelligence_settings = true
  use_legacy_profile           = false

  allow_writing_tools         = true
  allow_mail_summary          = true
  allow_safari_summary        = true
  force_on_device_dictation   = true
  force_on_device_translation = true
}

module "external_intelligence_settings" {
  source = "../../modules/foundation/external-intelligence-settings"

  enable_external_intelligence_settings = true
  use_legacy_profile                    = false

  enable_external_intelligence        = false
  allow_external_intelligence_sign_in = false
}
