"""Outil de récupération de recettes."""

from json import tool

from backend.app.store import Recipe


def list_recipes(recipes: dict[int, Recipe]) -> list[str]:
    return [r.value() for r in recipes.values()]

@tool("list_recipes")
def list_recipes_tool() -> list[str]:
    """Tool to list all recipes in the store."""
    recipes = list_recipes()
    if not recipes:
        return "Aucunes recettes trouvées."
    
    return recipes