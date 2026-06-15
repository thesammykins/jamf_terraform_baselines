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

  validation {
    condition = alltrue([
      for k, v in var.exemptions :
      contains(["ACCEPTED", "TEMPORARY", "ACCEPTED_WITH_COMPENSATING_CONTROLS", "UNDER_REVIEW"], v.risk_status)
    ])
    error_message = "risk_status must be one of: ACCEPTED, TEMPORARY, ACCEPTED_WITH_COMPENSATING_CONTROLS, UNDER_REVIEW"
  }
}

variable "prestage_display_name" {
  type        = string
  default     = "macAdmin Foundation PreStage"
  description = "Display name for the computer prestage enrollment"
}

variable "support_phone_number" {
  type        = string
  default     = ""
  description = "Support phone number shown during enrollment"
}

variable "support_email_address" {
  type        = string
  default     = ""
  description = "Support email address shown during enrollment"
}

variable "prestage_department" {
  type        = string
  default     = ""
  description = "Department name for the prestage enrollment"
}

variable "device_enrollment_program_instance_id" {
  type        = string
  default     = "1"
  description = "The ID of the DEP/ADE instance. Default is \"1\" (first instance)."
}

variable "module_name" {
  type        = string
  default     = "device-enrollment"
  description = "Module name for exemption tracking"
}
