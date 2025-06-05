from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, date
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker


import sqlite3

#connecting to the SQLite database
conn = sqlite3.connect('animals.db')
#creating a cursor object
cursor = conn.cursor()


#connecting to the database
engine = sqlite3.connect('animals.db')

#creating a session
Session = sessionmaker(bind=engine)




#creating a base classs
Base = declarative_base()

class Category(Base):
    __tablename__ = "animal_types"

    id = Column(Integer, primary_key = True)
    updated_at = Column(Integer, default = datetime.now())


#fastAPI method
def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

     

#creating initial table
class Animal(Base):
    __tablename__ = 'animals'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    species = Column(String, nullable=False)

    def __repr__(self):
        return f"Animal(id={self.id}, name={self.name}, age={self.age}, species={self.species})"


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
