variable "enable_intelligence_settings" {
  type        = bool
  default     = true
  description = "Whether to deploy Apple Intelligence management profiles"
}

variable "use_legacy_profile" {
  type        = bool
  default     = false
  description = "Whether to deploy the DEPRECATED com.apple.applicationaccess legacy profile (macOS 25–26.3). When false, uses DDM-native declaration (macOS 26.4+)."
}

# -- Core Apple Intelligence feature toggles --

variable "allow_apple_intelligence_report" {
  type        = bool
  default     = false
  description = "Allow users to generate Apple Intelligence Report. Available only in DDM path (macOS 26.4+)."
}

variable "allow_genmoji" {
  type        = bool
  default     = false
  description = "Allow Genmoji creation. Disabled by default for enterprise compliance."
}

variable "allow_image_playground" {
  type        = bool
  default     = false
  description = "Allow Image Playground AI image generation. Disabled by default for enterprise compliance."
}

variable "allow_image_wand" {
  type        = bool
  default     = false
  description = "Allow Image Wand AI image generation in Notes. Disabled by default for enterprise compliance."
}

variable "allow_personalized_handwriting" {
  type        = bool
  default     = false
  description = "Allow Personalized Handwriting Results. Disabled by default for enterprise compliance."
}

variable "allow_visual_intelligence_summary" {
  type        = bool
  default     = false
  description = "Allow Visual Intelligence Summary. Available only in DDM path (macOS 26.4+)."
}

variable "allow_writing_tools" {
  type        = bool
  default     = true
  description = "Allow Writing Tools (proofreading, rewriting, summarization). Enabled by default."
}

# -- Per-app feature toggles --

variable "allow_mail_smart_replies" {
  type        = bool
  default     = false
  description = "Allow Smart Replies in Mail. Available only in DDM path (macOS 26.4+)."
}

variable "allow_mail_summary" {
  type        = bool
  default     = true
  description = "Allow email thread summarization in Mail."
}

variable "allow_notes_transcription" {
  type        = bool
  default     = false
  description = "Allow audio transcription in Notes."
}

variable "allow_notes_transcription_summary" {
  type        = bool
  default     = false
  description = "Allow transcription summaries in Notes."
}

variable "allow_safari_summary" {
  type        = bool
  default     = true
  description = "Allow content summarization in Safari. Available only in DDM path (macOS 26.4+)."
}

# -- On-device enforcement --

variable "force_on_device_dictation" {
  type        = bool
  default     = true
  description = "Force on-device-only dictation (no cloud processing). Available only in DDM path (macOS 26.4+)."
}

variable "force_on_device_translation" {
  type        = bool
  default     = true
  description = "Force on-device-only translation (no cloud processing). Available only in DDM path (macOS 26.4+)."
}

# -- Standard module scaffolding --

variable "exemptions" {
  type = map(object({
    reason                = string
    ticket                = optional(string)
    risk_status           = string
    compensating_controls = optional(string)
    reviewer              = optional(string)
    review_date           = optional(string)
    expires               = optional(string)
  }))
  default     = {}
  description = "Foundation module exemptions with audit justification"

  validation {
    condition = alltrue([
      for k, v in var.exemptions :
      contains(["ACCEPTED", "TEMPORARY", "ACCEPTED_WITH_COMPENSATING_CONTROLS", "UNDER_REVIEW"], v.risk_status)
    ])
    error_message = "risk_status must be one of: ACCEPTED, TEMPORARY, ACCEPTED_WITH_COMPENSATING_CONTROLS, UNDER_REVIEW"
  }
}

variable "module_name" {
  type        = string
  default     = "intelligence-settings"
  description = "Module name for exemption tracking"
}
