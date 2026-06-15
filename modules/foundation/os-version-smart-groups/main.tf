# OS Version Smart Groups — creates smart computer groups for targeting
# compliance baselines and policies by macOS version.

locals {
  os_groups = {
    "macOS 14 — Sonoma" = {
      os_version = "14.0"
    }
    "macOS 15 — Sequoia" = {
      os_version = "15.0"
    }
    "macOS 26 — Tahoe" = {
      os_version = "26.0"
    }
    "macOS — Unsupported" = {
      os_version = "13.9"
    }
  }

  group_keys = keys(local.os_groups)
}

resource "jamfpro_smart_computer_group" "this" {
  count = (
    var.enable_smart_groups &&
    !contains(keys(var.exemptions), "os_version_smart_groups")
  ) ? length(local.group_keys) : 0

  name = local.group_keys[count.index]

  criteria {
    name         = "Operating System Version"
    search_type  = "greater than or equal"
    search_value = local.os_groups[local.group_keys[count.index]].os_version
  }
}
