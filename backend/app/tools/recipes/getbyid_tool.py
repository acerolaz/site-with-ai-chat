"""Outil de récupération de recette par ID."""

import json
from langchain_core.tools import tool
from app.store import get_recipe as store_get_recipe


@tool
def get_recipe_by_id_tool(recipe_id: int) -> str:
    """Outil pour récupérer une recette par son ID."""
    recipe = store_get_recipe(recipe_id)
    if recipe is None:
        return json.dumps(
            {
                "success": False,
                "error": f"Recette avec l'ID {recipe_id} introuvable."
            },
            ensure_ascii=False,
        )

    return json.dumps(
        {
            "success": True,
            "recipe": {
                "id": recipe.id,
                "name": recipe.name,
                "ingredients": recipe.ingredients,
            },
        },
        ensure_ascii=False,
    )
