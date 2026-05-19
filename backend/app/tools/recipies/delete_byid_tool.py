"""Outil de suppression de recettes."""

from json import tool

from backend.app.store import Recipe

def delete_recipe(recipe_id: int, recipes: dict[int, Recipe]) -> bool:
    return recipes.pop(recipe_id, None) is not None

@tool("delete_recipeById")
def deleteById_recipie(recipe_id: int, recipes: dict[int, Recipe]) -> bool:
    """Tool to delete a recipe by its ID."""
    return delete_recipe(recipe_id, recipes)