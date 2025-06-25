import os
import sys

# Asegurar que el directorio actual esté en PYTHONPATH
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from sqlalchemy.orm import sessionmaker
from app.database import engine
from models.character import Character

# Crear sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

# Insertar datos iniciales
initial_data = [
    {
        "name": "Warrior Template",
        "character_class": "Warrior",
        "stats": {"hp": 100, "damage": 15},
        "abilities": ["Slash", "Block"],
        "user_id": None
    },
    {
        "name": "Mage Template",
        "character_class": "Mage",
        "stats": {"hp": 50, "damage": 25},
        "abilities": ["Fireball", "Teleport"],
        "user_id": None
    }
]

for data in initial_data:
    character = Character(**data)
    session.add(character)

session.commit()
session.close()

print("Datos iniciales insertados correctamente.")
