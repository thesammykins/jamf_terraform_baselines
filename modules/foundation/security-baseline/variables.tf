variable "enable_security_baseline" {
  type        = bool
  default     = true
  description = "Whether to deploy the security baseline configuration profiles"
}

variable "screensaver_idle_timeout_minutes" {
  type        = number
  default     = 5
  description = "Number of idle minutes before screensaver activates and requires password"
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
  default     = "security-baseline"
  description = "Module name for exemption tracking"
}
