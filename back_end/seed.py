#for debugging
from models import Animal
from models import AnimalFeeder
from animals import animals_db


print(Animal.__tablename__) # return: animals

# Seed test -> animals
animals_db.append(Animal(id=1, name="Belga", animal_type="Cattle", breed="Jersey"))
animals_db.append(Animal(id=2, name="Clark", animal_type="Chicken", breed="Leghorn"))

print("Seed data added:")
for a in animals_db:
    print(a)



