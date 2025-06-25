from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.character import CharacterCreate, CharacterInDB, CharacterUpdate
from app.models.character import Character
from app.database import get_db
from typing import List

router = APIRouter(prefix="/characters", tags=["characters"])

@router.post("/", response_model=CharacterInDB)
def create_character(character: CharacterCreate, db: Session = Depends(get_db)):
    """
    Create a new character.
    
    Args:
        character (CharacterCreate): The character data to create.
        db (Session): Database session dependency.
    
    Returns:
        CharacterInDB: The created character object.
    """
    db_character = Character(
        name=character.name,
        character_class=character.character_class,
        stats=character.stats,
        abilities=character.abilities,
        user_id=None
    )
    db.add(db_character)
    db.commit()
    db.refresh(db_character)
    return db_character

@router.get("/", response_model=List[CharacterInDB])
def list_characters(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieve a list of all characters.
    
    Args:
        skip (int): Number of records to skip for pagination.
        limit (int): Maximum number of records to return.
        db (Session): Database session dependency.
    
    Returns:
        List[CharacterInDB]: List of character objects.
    """
    return db.query(Character).offset(skip).limit(limit).all()

@router.get("/{character_id}", response_model=CharacterInDB)
def get_character(character_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a character by its unique ID.
    
    Args:
        character_id (int): The ID of the character to retrieve.
        db (Session): Database session dependency.
    
    Returns:
        CharacterInDB: The character object if found.
    
    Raises:
        HTTPException: If the character is not found.
    """
    character = db.query(Character).filter(Character.id == character_id).first()
    if not character:
        raise HTTPException(status_code=404, detail="Character not found")
    return character

@router.put("/{character_id}", response_model=CharacterInDB)
def update_character(character_id: int, character: CharacterUpdate, db: Session = Depends(get_db)):
    """
    Update an existing character by its ID.
    
    Args:
        character_id (int): The ID of the character to update.
        character (CharacterUpdate): The updated character data.
        db (Session): Database session dependency.
    
    Returns:
        CharacterInDB: The updated character object.
    
    Raises:
        HTTPException: If the character is not found.
    """
    db_character = db.query(Character).filter(Character.id == character_id).first()
    if not db_character:
        raise HTTPException(status_code=404, detail="Character not found")
    setattr(db_character, "name", character.name)
    setattr(db_character, "character_class", character.character_class)
    setattr(db_character, "stats", character.stats)
    setattr(db_character, "abilities", character.abilities)
    db.commit()
    db.refresh(db_character)
    return db_character

@router.delete("/{character_id}")
def delete_character(character_id: int, db: Session = Depends(get_db)):
    """
    Delete a character by its unique ID.

    Args:
        character_id (int): The ID of the character to delete.
        db (Session): Database session dependency.

    Returns:
        dict: Confirmation of deletion (ok: True).

    Raises:
        HTTPException: If the character is not found.
    """
    db_character = db.query(Character).filter(Character.id == character_id).first()
    if not db_character:
        raise HTTPException(status_code=404, detail="Character not found")
    db.delete(db_character)
    db.commit()
    return {"ok": True}
