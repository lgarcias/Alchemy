from sqlalchemy import Column, Integer, String, JSON
from app.models import Base

class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    character_class = Column(String, nullable=False)
    stats = Column(JSON, nullable=False)  # Example: {"hp": 10, "damage": 2, ...}
    abilities = Column(JSON, nullable=False)  # Example: ["passive_1", "active_1"]
    user_id = Column(Integer, index=True)  # ForeignKey can be added when User model exists
