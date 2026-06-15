terraform {
  required_version = ">= 1.9.0"
  required_providers {
    jamfpro = {
      source  = "deploymenttheory/jamfpro"
      version = ">= 0.36.0"
    }
  }
}
