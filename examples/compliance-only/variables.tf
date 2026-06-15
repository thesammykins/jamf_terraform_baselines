variable "jamfplatform_client_id" {
  description = "OAuth2 client ID for Jamf Platform API"
  type        = string
  sensitive   = true
}

variable "jamfplatform_client_secret" {
  description = "OAuth2 client secret for Jamf Platform API"
  type        = string
  sensitive   = true
}

variable "jamfplatform_base_url" {
  description = "Jamf Platform API base URL (region-specific gateway). e.g. https://us.apigw.jamf.com"
  type        = string
  default     = "https://us.apigw.jamf.com"
}
