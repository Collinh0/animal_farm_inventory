from datetime import date


class AnimalFeeder:
    def __init__(self):
        self.fed_today = {}

    def feed(self, animal_id, name):
        today = date.today()
        if animal_id not in self.fed_today:
            self.fed_today[animal_id] = {}
        self.fed_today[animal_id][name] = today
        print(f"Fed {name} (ID: {animal_id}) on {today}.")  #Feed the animal and record the feeding date.
   

class Cattle:
    def __init__(self, gender, name, age):
        self.id = id
        self.name = name
        self.age = age
    __tablename__ = 'cattle'


def __repr__(self):
        return f"Cattle(id={self.id}, name={self.name}, age={self.age})"

class Sheep:
    def __init__(self,breed, name, age):
        self.id = id
        self.breed = breed
        self.name = name
        self.age = age

    __tablename__ = 'sheep'

def __repr__(self): 
        return f"Sheep(id={self.id}, breed={self.breed}, name={self.name}, age={self.age})"

class Goat:
    def __init__(self, breed, name, age):
        self.id = id
        self.breed = breed
        self.name = name
        self.age = age

    __tablename__ = 'goat'

def __repr__(self):
        return f"Goat(id={self.id}, breed={self.breed}, name={self.name}, age={self.age})"
class pet:
    def __init__(self, species, name, age):
        self.id = id
        self.species = species
        self.name = name
        self.age = age

    __tablename__ = 'pet'