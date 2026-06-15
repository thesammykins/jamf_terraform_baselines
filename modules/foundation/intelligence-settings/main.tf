# Intelligence Settings — manages Apple Intelligence features via DDM declarations.
#
# DDM-NATIVE PATH (macOS 26.4+, iOS 26.4+):
# Uses com.apple.configuration.intelligence.settings declaration payload.
# Controls: Genmoji, Image Playground, Writing Tools, Image Wand, per-app
# Mail/Notes/Safari AI features, and on-device-only dictation/translation.
#
# LEGACY PATH (macOS 25 – 26.3):
# Uses com.apple.applicationaccess restriction keys for partial coverage.
# Set var.use_legacy_profile = true to enable this fallback.
#
# Reference: https://github.com/apple/device-management (declarative/configurations/intelligence.settings.yaml)
# Migration deadline: Before upgrading fleet past macOS 26.3.

resource "jamfpro_macos_configuration_profile_plist" "intelligence_ddm" {
  count = (
    var.enable_intelligence_settings &&
    !var.use_legacy_profile &&
    !contains(keys(var.exemptions), "intelligence_settings")
  ) ? 1 : 0

  name                = "macAdmin Foundation — Apple Intelligence Settings (DDM)"
  description         = "Manages Apple Intelligence features via DDM declaration. macOS 26.4+ required. Managed by Terraform."
  level               = "System"
  distribution_method = "Install Automatically"
  redeploy_on_update  = "Newly Assigned"
  user_removable      = false
  payloads = templatefile("${path.module}/templates/intelligence-settings-ddm.mobileconfig.tftpl", {
    allow_apple_intelligence_report   = var.allow_apple_intelligence_report
    allow_genmoji                     = var.allow_genmoji
    allow_image_playground            = var.allow_image_playground
    allow_image_wand                  = var.allow_image_wand
    allow_personalized_handwriting    = var.allow_personalized_handwriting
    allow_visual_intelligence_summary = var.allow_visual_intelligence_summary
    allow_writing_tools               = var.allow_writing_tools
    allow_mail_smart_replies          = var.allow_mail_smart_replies
    allow_mail_summary                = var.allow_mail_summary
    allow_notes_transcription         = var.allow_notes_transcription
    allow_notes_transcription_summary = var.allow_notes_transcription_summary
    allow_safari_summary              = var.allow_safari_summary
    force_on_device_dictation         = var.force_on_device_dictation
    force_on_device_translation       = var.force_on_device_translation
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
# Uses com.apple.applicationaccess restriction keys with partial feature coverage.
# Does NOT cover: Apple Intelligence Report, Visual Intelligence Summary,
# Mail Smart Replies, Safari Summary, on-device-only controls.
resource "jamfpro_macos_configuration_profile_plist" "intelligence_legacy" {
  count = (
    var.enable_intelligence_settings &&
    var.use_legacy_profile &&
    !contains(keys(var.exemptions), "intelligence_settings")
  ) ? 1 : 0

  name                = "[LEGACY] macAdmin Foundation — Apple Intelligence Settings"
  description         = "DEPRECATED — Uses com.apple.applicationaccess restrictions. Transition to DDM in macOS 26.4+. Managed by Terraform."
  level               = "System"
  distribution_method = "Install Automatically"
  redeploy_on_update  = "Newly Assigned"
  user_removable      = false
  payloads = templatefile("${path.module}/templates/intelligence-settings-legacy.mobileconfig.tftpl", {
    allow_genmoji                     = var.allow_genmoji
    allow_image_playground            = var.allow_image_playground
    allow_image_wand                  = var.allow_image_wand
    allow_writing_tools               = var.allow_writing_tools
    allow_personalized_handwriting    = var.allow_personalized_handwriting
    allow_mail_summary                = var.allow_mail_summary
    allow_notes_transcription         = var.allow_notes_transcription
    allow_notes_transcription_summary = var.allow_notes_transcription_summary
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
