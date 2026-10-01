"""Outil de suppression de recettes."""

from langchain_core.tools import tool
from app.store import delete_recipe as store_delete_recipe


@tool
def delete_recipe_tool(recipe_id: int) -> dict:
    """Outil pour supprimer une recette par son identifiant."""
    success = store_delete_recipe(recipe_id)
    return {
        "success": success,
        "recipe_id": recipe_id,
        "message": (
            f"Recette {recipe_id} supprimée avec succès."
            if success
            else f"Recette {recipe_id} introuvable."
        ),
    }