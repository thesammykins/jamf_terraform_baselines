# Device Enrollment — configures Automated Device Enrollment (ADE) settings
# to skip setup assistant panes and enforce MDM enrollment.

resource "jamfpro_enrollment_settings" "device_enrollment" {
  count = (
    var.enable_device_enrollment &&
    !contains(keys(var.exemptions), "device_enrollment")
  ) ? 1 : 0

  # Skip setup assistant panes for streamlined enrollment
  skip_apple_id             = true
  skip_siri                 = true
  skip_touch_id             = true
  skip_screen_time          = true
  skip_privacy              = true
  skip_icloud_storage       = true
  skip_filevault            = true
  skip_display_tone         = true
  skip_true_tone            = true
  skip_appearance           = true

  # MDM enrollment enforcement
  require_mdm_enrollment    = true
  disallow_mdm_profile_removal = true
}
