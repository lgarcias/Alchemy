from fastapi import FastAPI
from app.api.v1 import character as v1_character

app = FastAPI()

app.include_router(v1_character.router, prefix="/api/v1")
