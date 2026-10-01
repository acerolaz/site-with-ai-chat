"""Store PostgreSQL pour les recettes via SQLAlchemy."""

from pydantic import BaseModel

from app.database import SessionLocal
from app.models import RecipeModel


class Recipe(BaseModel):
    id: int
    name: str
    ingredients: list[str]

    model_config = {"from_attributes": True}


class RecipeCreate(BaseModel):
    name: str
    ingredients: list[str]


def list_recipes() -> list[Recipe]:
    with SessionLocal() as db:
        rows = db.query(RecipeModel).all()
        return [Recipe.model_validate(r) for r in rows]


def get_recipe(recipe_id: int) -> Recipe | None:
    with SessionLocal() as db:
        row = db.get(RecipeModel, recipe_id)
        return Recipe.model_validate(row) if row else None


def create_recipe(data: RecipeCreate) -> Recipe:
    with SessionLocal() as db:
        row = RecipeModel(name=data.name, ingredients=data.ingredients)
        db.add(row)
        db.commit()
        db.refresh(row)
        return Recipe.model_validate(row)


def delete_recipe(recipe_id: int) -> bool:
    with SessionLocal() as db:
        row = db.get(RecipeModel, recipe_id)
        if row is None:
            return False
        db.delete(row)
        db.commit()
        return True
