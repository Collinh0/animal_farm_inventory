from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from models import Animal
from schemas import AnimalSchema



#initialize FastAPI 
app = FastAPI

# In-memory "database"
animals_db = []

#CRUD operations
"""
FastAPI uvicorn --> uvicorn animals:app --reload 
http://127.0.0.1:8000
"""

# Create
@app.post("/animals/", response_model=Animal)
def create_animal(animal: Animal):
    animals_db.append(animal)
    return animal

# Read all
@app.get("/animals/", response_model=str[Animal])
def get_animals():
    return animals_db

# Read one
@app.get("/animals/{animal_id}", response_model=Animal)
def get_animal(animal_id: int):
    for animal in animals_db:
        if animal.id == animal_id:
            return animal


# Update
@app.put("/animals/{animal_id}", response_model=Animal)
def update_animal(animal_id: int, updated_animal: Animal):
    for index, animal in enumerate(animals_db):
        if animal.id == animal_id:
            animals_db[index] = updated_animal
            return updated_animal
   

# Delete
@app.delete("/animals/{animal_id}")
def delete_animal(animal_id: int):
    for index, animal in enumerate(animals_db):
        if animal.id == animal_id:
            del animals_db[index]
            return {"message": "Animal removed"}

