#For  holding classes acting as blueprint for CRUD methods
from pydantic import BaseModel


class AnimalSchema(BaseModel):
    name: str
    age: int
    species: str
    animal_id: int



