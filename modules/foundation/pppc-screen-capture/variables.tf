variable "enable_pppc_screen_capture" {
  type        = bool
  default     = true
  description = "Whether to deploy the PPPC screen capture configuration profile"
}

variable "pppc_tools" {
  type        = list(string)
  default     = ["Zoom", "Slack", "Microsoft Teams", "Google Chrome", "Webex"]
  description = "List of tool names to grant screen capture access (must match keys in pppc-bundle-ids.yaml)"
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
  default     = "pppc-screen-capture"
  description = "Module name for exemption tracking"
}
