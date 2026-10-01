"""Modèles SQLAlchemy."""

from sqlalchemy import ARRAY, Column, Integer, String

from app.database import Base


class RecipeModel(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    ingredients = Column(ARRAY(String), nullable=False, default=list)
