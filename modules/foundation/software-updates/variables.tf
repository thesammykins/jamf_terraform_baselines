variable "enable_software_updates" {
  type        = bool
  default     = true
  description = "Whether to deploy the software update configuration profile"
}

variable "software_update_major_deferral_days" {
  type        = number
  default     = 90
  description = "Number of days to defer major macOS upgrades"
}

variable "software_update_minor_deferral_days" {
  type        = number
  default     = 14
  description = "Number of days to defer minor macOS updates"
}

variable "rapid_security_response_enabled" {
  type        = bool
  default     = true
  description = "Whether Rapid Security Response updates are enabled"
}

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
  default     = "software-updates"
  description = "Module name for exemption tracking"
}
