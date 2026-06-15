output "smart_group_ids" {
  value = {
    for i, group in jamfpro_smart_computer_group_v2.this :
    group.name => group.id
  }
  description = "Map of smart group names to their Jamf Pro IDs"
}
