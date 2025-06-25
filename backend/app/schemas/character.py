from pydantic import BaseModel
from typing import List, Dict, Optional

class CharacterBase(BaseModel):
    name: str
    character_class: str
    stats: Dict[str, int]
    abilities: List[str]

class CharacterCreate(CharacterBase):
    pass

class CharacterUpdate(CharacterBase):
    pass

class CharacterInDB(CharacterBase):
    id: int
    user_id: Optional[int]

    class Config:
        orm_mode = True

class CharacterClassTemplate(BaseModel):
    name: str
    character_class: str
    stats: Dict[str, int]
    abilities: List[str]
