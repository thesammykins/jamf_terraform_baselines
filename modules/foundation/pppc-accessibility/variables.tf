variable "enable_pppc_accessibility" {
  type        = bool
  default     = true
  description = "Whether to deploy the PPPC accessibility configuration profile"
}

variable "pppc_tools" {
  type        = list(string)
  default     = ["Zoom", "Slack", "Microsoft Teams", "Google Chrome", "Webex"]
  description = "List of tool names to grant accessibility access (must match keys in pppc-bundle-ids.yaml)"
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
  default     = "pppc-accessibility"
  description = "Module name for exemption tracking"
}
