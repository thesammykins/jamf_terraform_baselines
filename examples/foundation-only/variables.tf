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
