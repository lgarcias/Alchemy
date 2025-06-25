from models.base_characters import Alchemist, Warrior
from models.character import Character
from database import SessionLocal

# Crear plantillas de personajes base

def create_base_characters():
    db = SessionLocal()
    # Alchemist
    alchemist = Alchemist(name="Alchemist Template")
    db.add(Character(
        name=alchemist.name,
        character_class="Alchemist",
        stats=alchemist.stats,
        abilities=alchemist.abilities,
        user_id=None
    ))
    # Warrior
    warrior = Warrior(name="Warrior Template")
    db.add(Character(
        name=warrior.name,
        character_class="Warrior",
        stats=warrior.stats,
        abilities=warrior.abilities,
        user_id=None
    ))
    db.commit()
    db.close()
    print("Plantillas de personajes base creadas.")

if __name__ == "__main__":
    create_base_characters()
