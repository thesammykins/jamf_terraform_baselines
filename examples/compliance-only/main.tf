terraform {
  required_version = ">= 1.9.0"
  required_providers {
    jamfplatform = {
      source  = "Jamf-Concepts/jamfplatform"
      version = ">= 0.17.0"
    }
  }
}

provider "jamfplatform" {
  client_id     = var.jamfplatform_client_id
  client_secret = var.jamfplatform_client_secret
  base_url      = var.jamfplatform_base_url
}

# ── CIS Level 1 (macOS 26) ──────────────────────────────────────────
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

# ── DISA STIG (macOS 26) ────────────────────────────────────────────
module "disa_stig_tahoe" {
  source = "../../modules/compliance/disa_stig/macos_26"

  enforcement_mode = "MONITOR"
}
