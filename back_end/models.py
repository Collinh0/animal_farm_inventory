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

     
#SQLAlchemy & ORM

class Animal(Base):
    __tablename__ = 'animals'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    animal_type = Column(String, nullable=False)  # e.g., Cow, Chicken
    breed = Column(String)

    feedings = relationship("Feeding", back_populates="animal", cascade="all, delete")
    health_records = relationship("HealthRecord", back_populates="animal", cascade="all, delete")

    def __repr__(self):
        return f"<Animal(name='{self.name}', type='{self.animal_type}', breed='{self.breed}')>"


class Feeding(Base):
    __tablename__ = 'feedings'

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    food = Column(String, nullable=False)
    quantity = Column(String, nullable=False)  
    animal_id = Column(Integer, ForeignKey('animals.id'))

    animal = relationship("Animal", back_populates="feedings")

    def __repr__(self):
        return f"<Feeding(animal_id={self.animal_id}, food='{self.food}', date={self.date})>"


class HealthRecord(Base):
    __tablename__ = 'health_records'

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    notes = Column(String, nullable=False)  
    animal_id = Column(Integer, ForeignKey('animals.id'))

    animal = relationship("Animal", back_populates="health_records")

    def __repr__(self):
        return f"<HealthRecord(animal_id={self.animal_id}, date={self.date}, notes='{self.notes}')>"
