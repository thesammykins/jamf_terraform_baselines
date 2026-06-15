output "category_ids" {
  value = {
    for i, cat in jamfpro_category.this :
    cat.name => cat.id
  }
  description = "Map of category names to their Jamf Pro IDs"
}
