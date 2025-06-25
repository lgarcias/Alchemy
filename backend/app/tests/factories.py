from factory.alchemy import SQLAlchemyModelFactory
from factory.faker import Faker
from app.models.character import Character
from app.database import SessionLocal
from sqlalchemy.orm import scoped_session

# Ensure SessionLocal is instantiated properly
session = scoped_session(SessionLocal)

class CharacterFactory(SQLAlchemyModelFactory):
    class Meta: # type: ignore
        model = Character
        sqlalchemy_session = session

    name = Faker("name")
    character_class = Faker("word", ext_word_list=["Alchemist", "Warrior"])
    stats = {
        "hp": 10,
        "damage": 2,
        "defense": 1,
        "speed": 3
    }
    abilities = ["Potion Mastery", "Transmute"]
