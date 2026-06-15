terraform {
  required_version = ">= 1.9.0"
  required_providers {
    jamfpro = {
      source  = "deploymenttheory/jamfpro"
      version = ">= 0.36.0"
    }
  }
}

provider "jamfpro" {
  client_id             = var.jamfpro_client_id
  client_secret         = var.jamfpro_client_secret
  jamfpro_instance_fqdn = var.jamfpro_instance_fqdn
  auth_method           = "oauth2"
}

# ── Foundation Module: Categories ────────────────────────────────────
module "categories" {
  source = "../../modules/foundation/categories"

  enable_categories = true
}

# ── Foundation Module: OS Version Smart Groups ────────────────────────
module "os_version_smart_groups" {
  source = "../../modules/foundation/os-version-smart-groups"

  enable_smart_groups = true
}

# ── Foundation Module: Security Baseline ──────────────────────────────
module "security_baseline" {
  source = "../../modules/foundation/security-baseline"

  enable_security_baseline         = true
  screensaver_idle_timeout_minutes = 5
}

# ── Foundation Module: Software Updates (DDM-native) ─────────────────
module "software_updates" {
  source = "../../modules/foundation/software-updates"

  enable_software_updates             = true
  manage_feature_toggle               = true  # First deployment — manages the singleton toggle
  use_legacy_profile                  = false # DDM-native path only
  ddm_update_action                   = "DOWNLOAD_INSTALL_ALLOW_DEFERRAL"
  ddm_version_type                    = "LATEST_MAJOR"
  ddm_max_deferrals                   = 3
  software_update_major_deferral_days = 90
  software_update_minor_deferral_days = 14
  rapid_security_response_enabled     = true

  smart_group_ids = module.os_version_smart_groups.smart_group_ids
}

# ── Foundation Module: PPPC Screen Capture ────────────────────────────
module "pppc_screen_capture" {
  source = "../../modules/foundation/pppc-screen-capture"

  enable_pppc_screen_capture = true
  pppc_tools                 = ["Zoom", "Slack", "Microsoft Teams", "Google Chrome", "Webex"]
}

# ── Foundation Module: PPPC Accessibility ─────────────────────────────
module "pppc_accessibility" {
  source = "../../modules/foundation/pppc-accessibility"

  enable_pppc_accessibility = true
  pppc_tools                = ["Zoom", "Slack", "Microsoft Teams", "Dropbox"]
}

# ── Foundation Module: Device Enrollment (PreStage) ───────────────────
module "device_enrollment" {
  source = "../../modules/foundation/device-enrollment"

  enable_device_enrollment = false # ADE token not yet provisioned

  exemptions = {
    "device_enrollment" = {
      reason      = "ADE token not yet provisioned — will re-enable in Q3"
      ticket      = "IT-7823"
      risk_status = "TEMPORARY"
    }
  }
}

# ── Foundation Module: Inventory Settings ─────────────────────────────
module "inventory_settings" {
  source = "../../modules/foundation/inventory-settings"

  enable_inventory_settings = true
  checkin_frequency_minutes = 15
}

# ── Foundation Module: Intelligence Settings (DDM-native) ────────────
module "intelligence_settings" {
  source = "../../modules/foundation/intelligence-settings"

  enable_intelligence_settings = true
  use_legacy_profile           = false # DDM-native path (macOS 26.4+)

  # Enterprise defaults: disable generative AI, enable productivity tools
  allow_writing_tools         = true
  allow_mail_summary          = true
  allow_safari_summary        = true
  force_on_device_dictation   = true
  force_on_device_translation = true
}

# ── Foundation Module: External Intelligence Settings (DDM-native) ───
module "external_intelligence_settings" {
  source = "../../modules/foundation/external-intelligence-settings"

  enable_external_intelligence_settings = true
  use_legacy_profile                    = false # DDM-native path (macOS 26.4+)

  # Enterprise default: block third-party AI services
  enable_external_intelligence        = false
  allow_external_intelligence_sign_in = false
}
