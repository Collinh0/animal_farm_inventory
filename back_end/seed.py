#for debugging
#from animals import animals_db
from datetime import date
from db import engine, SessionLocal
from models import Base, Feeding, HealthRecord, Animal


print(Animal.__tablename__) # return: animals

# Seed test -> animals

Base.metadata.create_all(bind=engine)  # -> Create all tables

# Open the DB session
db = SessionLocal()

# Create test animals
bessie = Animal(name="Bessie", animal_type="Cow", breed="Jersey")
clucky = Animal(name="Clucky", animal_type="Chicken", breed="Leghorn")
goaty = Animal(name="Goaty", animal_type="Goat", breed="Boer")

db.add_all([bessie, clucky, goaty])
db.commit()

# Adding feedings and health records
feeding1 = Feeding(date=date(2024, 6, 1), food="Grass", quantity="10kg", animal_id=bessie.id)
feeding2 = Feeding(date=date(2024, 6, 2), food="Grains", quantity="500g", animal_id=clucky.id)

health1 = HealthRecord(date=date(2024, 5, 20), notes="Vaccinated for foot-and-mouth", animal_id=bessie.id)
health2 = HealthRecord(date=date(2024, 5, 25), notes="Dewormed", animal_id=goaty.id)

db.add_all([feeding1, feeding2, health1, health2])
db.commit()

#  Done
print("Database seeded successfully.")
db.close()




