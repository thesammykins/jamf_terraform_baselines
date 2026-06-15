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

variable "manage_feature_toggle" {
  type        = bool
  default     = false
  description = "Whether this module deployment should manage the Jamf Pro Managed Software Update feature toggle. Set to true on only ONE deployment per Jamf Pro instance."
}

variable "use_legacy_profile" {
  type        = bool
  default     = false
  description = "Whether to deploy the DEPRECATED com.apple.SoftwareUpdate legacy configuration profile for macOS 25 and earlier. Set to true only during migration."
}

variable "smart_group_ids" {
  type        = map(string)
  default     = {}
  description = "Map of smart group names to Jamf Pro group IDs for DDM update plan targeting. Use output from the os-version-smart-groups module."
}

variable "ddm_update_action" {
  type        = string
  default     = "DOWNLOAD_INSTALL_ALLOW_DEFERRAL"
  description = "DDM update action. Valid values: DOWNLOAD_INSTALL_ALLOW_DEFERRAL, DOWNLOAD_INSTALL_RESTART, DOWNLOAD_INSTALL_SHUTDOWN, DOWNLOAD_ONLY."

  validation {
    condition = contains([
      "DOWNLOAD_INSTALL_ALLOW_DEFERRAL",
      "DOWNLOAD_INSTALL_RESTART",
      "DOWNLOAD_INSTALL_SHUTDOWN",
      "DOWNLOAD_ONLY"
    ], var.ddm_update_action)
    error_message = "ddm_update_action must be one of: DOWNLOAD_INSTALL_ALLOW_DEFERRAL, DOWNLOAD_INSTALL_RESTART, DOWNLOAD_INSTALL_SHUTDOWN, DOWNLOAD_ONLY."
  }
}

variable "ddm_version_type" {
  type        = string
  default     = "LATEST_MAJOR"
  description = "DDM version type to target. Valid values: LATEST_MAJOR, LATEST_MINOR, SPECIFIC_VERSION, CUSTOM_VERSION."

  validation {
    condition = contains([
      "LATEST_MAJOR",
      "LATEST_MINOR",
      "SPECIFIC_VERSION",
      "CUSTOM_VERSION"
    ], var.ddm_version_type)
    error_message = "ddm_version_type must be one of: LATEST_MAJOR, LATEST_MINOR, SPECIFIC_VERSION, CUSTOM_VERSION."
  }
}

variable "ddm_max_deferrals" {
  type        = number
  default     = 3
  description = "Maximum number of times a user can defer a DDM-managed update (only used when update_action is DOWNLOAD_INSTALL_ALLOW_DEFERRAL)."
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
