#set up FastAPI

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Animal, AnimalCreate, AnimalUpdate

#initialize FastAPI 
app = FastAPI()
