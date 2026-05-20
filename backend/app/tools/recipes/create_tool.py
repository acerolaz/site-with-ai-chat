"""Outil de création de recette."""

import json
from langchain_core.tools import tool
from app.store import create_recipe as store_create_recipe, RecipeCreate


@tool
def create_recipe_tool(name: str, ingredients: list[str]) -> str:
    """Tool to create a new recipe."""
    recipe = store_create_recipe(RecipeCreate(name=name, ingredients=ingredients))
    return json.dumps({"id": recipe.id, "name": recipe.name, "ingredients": recipe.ingredients})