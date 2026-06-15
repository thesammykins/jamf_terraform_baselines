# ── Jamf Platform (Variant A — Compliance) ───────────────────────────
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

# ── Jamf Pro (Variant B — Foundation) ────────────────────────────────
variable "jamfpro_client_id" {
  description = "OAuth2 client ID for Jamf Pro API"
  type        = string
  sensitive   = true
}

variable "jamfpro_client_secret" {
  description = "OAuth2 client secret for Jamf Pro API"
  type        = string
  sensitive   = true
}

variable "jamfpro_instance_fqdn" {
  description = "Fully qualified domain name of the Jamf Pro instance. e.g. myorg.jamfcloud.com"
  type        = string
}
