"""Outil de suppression de recettes."""

from langchain_core.tools import tool
from app.store import delete_recipe as store_delete_recipe


@tool
def delete_recipe_tool(recipe_id: int) -> str:
    """Tool to delete a recipe by its ID."""
    success = store_delete_recipe(recipe_id)
    return f"Recipe {recipe_id} {'deleted successfully' if success else 'not found'}."