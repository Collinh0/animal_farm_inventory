#For  holding classes acting as blueprint for CRUD methods
from pydantic import BaseModel
from typing import Optional, List
from datetime import date


#Feeding
class FeedingBase(BaseModel):
    date: date
    food: str
    quantity: str

class FeedingCreate(FeedingBase):
    animal_id: int

class FeedingResponse(FeedingBase):
    id: int
    class Config:
        orm_mode = True


#Health
class HealthRecordBase(BaseModel):
    date: date
    notes: str

class HealthRecordCreate(HealthRecordBase):
    animal_id: int

class HealthRecordResponse(HealthRecordBase):
    id: int
    class Config:
        orm_mode = True


#Animal 
class AnimalBase(BaseModel):
    name: str
    animal_type: str
    breed: Optional[str] = None

class AnimalCreate(AnimalBase):
    pass

class AnimalResponse(AnimalBase):
    id: int
    feedings: List[FeedingResponse] = []
    health_records: List[HealthRecordResponse] = []

    class Config:
        orm_mode = True #enable Pydantic to read datafrom dicts & SQLAlchemy models -> so you can return DB objects directly from FastAPI endpoints.





