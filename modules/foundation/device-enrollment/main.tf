# Device Enrollment — configures Computer PreStage enrollment settings
# to skip setup assistant panes and enforce MDM enrollment via ADE/DEP.
#
# Uses the real jamfpro_computer_prestage_enrollment resource with the
# skip_setup_items block. All skip keys match the provider schema exactly.

resource "jamfpro_computer_prestage_enrollment" "device_enrollment" {
  count = (
    var.enable_device_enrollment &&
    !contains(keys(var.exemptions), "device_enrollment")
  ) ? 1 : 0

  display_name                            = var.prestage_display_name
  mandatory                               = true
  mdm_removable                           = false
  support_phone_number                    = var.support_phone_number
  support_email_address                   = var.support_email_address
  department                              = var.prestage_department
  default_prestage                        = false
  enrollment_site_id                      = "-1"
  keep_existing_site_membership           = false
  keep_existing_location_information      = false
  require_authentication                  = false
  authentication_prompt                   = "Sign in to your organization account"
  prevent_activation_lock                 = false
  enable_device_based_activation_lock     = false
  device_enrollment_program_instance_id   = var.device_enrollment_program_instance_id
  enrollment_customization_id             = "0"
  site_id                                 = "-1"
  auto_advance_setup                      = true
  language                                = ""
  region                                  = ""
  install_profiles_during_setup           = true
  custom_package_ids                      = []
  prestage_installed_profile_ids          = []
  prestage_minimum_os_target_version_type = "NO_ENFORCEMENT"
  rotate_recovery_lock_password           = false
  recovery_lock_password_type             = "RANDOM"
  enable_recovery_lock                    = false
  custom_package_distribution_point_id    = "-1"

  skip_setup_items {
    accessibility               = true
    additional_privacy_settings = true
    appearance                  = true
    apple_id                    = true
    biometric                   = true
    diagnostics                 = true
    display_tone                = true # DEPRECATED — removed in future macOS
    enable_lockdown_mode        = true
    file_vault                  = false # Allow FileVault prompt
    icloud_diagnostics          = true
    icloud_storage              = true
    intelligence                = true
    location                    = true
    os_showcase                 = true
    payment                     = true
    privacy                     = true
    registration                = true
    restore                     = true
    screen_time                 = true
    siri                        = true
    software_update             = true
    terms_of_address            = true
    tos                         = true
    wallpaper                   = true
    welcome                     = true
  }

  location_information {
    username      = ""
    realname      = ""
    phone         = ""
    email         = ""
    room          = ""
    position      = ""
    department_id = "-1"
    building_id   = "-1"
  }

  account_settings {
    prefill_account_user_name                    = ""
    prefill_account_full_name                    = ""
    prefill_type                                 = "CUSTOM"
    admin_username                               = ""
    admin_password                               = ""
    local_admin_account_enabled                  = false
    local_user_managed                           = false
    prefill_primary_account_info_feature_enabled = false
    prevent_prefill_info_from_modification       = false
    payload_configured                           = false
    user_account_type                            = "STANDARD"
    hidden_admin_account                         = false
  }

  purchasing_information {
    leased             = false
    purchased          = true
    apple_care_id      = ""
    po_number          = ""
    vendor             = ""
    purchase_price     = ""
    life_expectancy    = 0
    purchasing_account = ""
    purchasing_contact = ""
    lease_date         = "1970-01-01"
    po_date            = "1970-01-01"
    warranty_date      = "1970-01-01"
  }
}
