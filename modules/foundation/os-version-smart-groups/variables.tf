variable "enable_smart_groups" {
  type        = bool
  default     = true
  description = "Whether to create OS version smart computer groups"
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
  default     = "os-version-smart-groups"
  description = "Module name for exemption tracking"
}
