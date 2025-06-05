# Animal Farm Inventory

A simple command-line app to manage your animal farm:
- Track animals by type and breed
- Log feedings and health checkups
- Summarize livestock by type/category

# User stories
- User (farmer) should be able to record, track, update or delete records and animal entries.

# Entities
Animal, Feeding, HealthRecords

# Relationships
Animal -> Feeding : One to many
Animal -> HealthRecords : One to many
Animal -> Output : One to many