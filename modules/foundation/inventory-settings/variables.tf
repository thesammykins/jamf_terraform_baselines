variable "enable_inventory_settings" {
  type        = bool
  default     = true
  description = "Whether to configure Jamf Pro computer check-in and inventory settings"
}

variable "checkin_frequency_minutes" {
  type        = number
  default     = 15
  description = "Computer check-in frequency in minutes"
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
  default     = "inventory-settings"
  description = "Module name for exemption tracking"
}
