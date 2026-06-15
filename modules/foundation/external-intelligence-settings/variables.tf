variable "enable_external_intelligence_settings" {
  type        = bool
  default     = true
  description = "Whether to deploy external intelligence (third-party AI) management profiles"
}

variable "use_legacy_profile" {
  type        = bool
  default     = false
  description = "Whether to deploy the DEPRECATED com.apple.applicationaccess legacy profile (macOS 25–26.3). When false, uses DDM-native declaration (macOS 26.4+)."
}

variable "enable_external_intelligence" {
  type        = bool
  default     = false
  description = "Allow external intelligence integrations (e.g. ChatGPT). Disabled by default for enterprise data protection."
}

variable "allow_external_intelligence_sign_in" {
  type        = bool
  default     = false
  description = "Allow users to sign in to external intelligence services (e.g. ChatGPT account). When disabled, forces anonymous mode. Disabled by default."
}

variable "allowed_workspace_ids" {
  type        = list(string)
  default     = []
  description = "List of allowed external intelligence workspace IDs. If set, only these workspaces can be used. Only available in DDM path. Empty list means no workspace restriction."
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
}

variable "module_name" {
  type        = string
  default     = "external-intelligence-settings"
  description = "Module name for exemption tracking"
}
