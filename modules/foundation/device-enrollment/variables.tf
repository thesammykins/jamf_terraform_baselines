variable "enable_device_enrollment" {
  type        = bool
  default     = true
  description = "Whether to configure Automated Device Enrollment settings"
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
  default     = "device-enrollment"
  description = "Module name for exemption tracking"
}
