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
  client_id     = var.jamfpro_client_id
  client_secret = var.jamfpro_client_secret
  instance_fqdn = var.jamfpro_instance_fqdn
}

module "foundation" {
  source = "../../modules/foundation"

  enable_categories              = true
  enable_os_version_smart_groups = true
  enable_security_baseline       = true
  enable_software_updates        = true
  enable_pppc_screen_capture     = true
  enable_pppc_accessibility      = true
  enable_device_enrollment       = true
  enable_inventory_settings      = true

  exemptions = {
    "device_enrollment" = {
      reason      = "ADE token not yet provisioned — will re-enable in Q3"
      ticket      = "IT-7823"
      risk_status = "TEMPORARY"
    }
  }
}
