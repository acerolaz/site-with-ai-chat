"""Outil de récupération de recette par ID."""

from json import tool

from backend.app.store import Recipe

def get_recipe(recipe_id: int, recipes: dict[int, Recipe]) -> Recipe | None:
    return recipes.get(recipe_id)

@tool("get_recipeById")
def get_recipe_by_id_tool(recipe_id: int, recipes: dict[int, Recipe]) -> Recipe | None:
    """Tool to get a recipe by its ID."""
    return get_recipe(recipe_id, recipes)
