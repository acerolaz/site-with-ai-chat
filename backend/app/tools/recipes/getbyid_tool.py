"""Outil de récupération de recette par ID."""

import json
from langchain_core.tools import tool
from app.store import get_recipe as store_get_recipe


@tool
def get_recipe_by_id_tool(recipe_id: int) -> str:
    """Tool to get a recipe by its ID."""
    recipe = store_get_recipe(recipe_id)
    if recipe is None:
        return f"Recipe with ID {recipe_id} not found."
    
    return json.dumps({"id": recipe.id, "name": recipe.name, "ingredients": recipe.ingredients})
