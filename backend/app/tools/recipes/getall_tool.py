"""Outil de récupération de recettes."""

import json
from langchain_core.tools import tool
from app.store import list_recipes as store_list_recipes


@tool
def list_recipes_tool() -> str:
    """Tool to list all recipes in the store."""
    recipes = store_list_recipes()
    if not recipes:
        return "Aucunes recettes trouvées."
    
    return json.dumps([{"id": r.id, "name": r.name, "ingredients": r.ingredients} for r in recipes])