"""Outil de création de recette."""

from json import tool

from backend.app.store import Recipe, RecipeCreate

def create_recipe(data: RecipeCreate,  recipes: dict[int, Recipe]) -> Recipe:
    new_id = max(recipes.keys()) + 1 if recipes else 1
    recipie = Recipe(id=new_id, name=data.name, ingredients=data.ingredients)
    recipes[new_id] = recipie
    return recipie

@tool("create_recipe")
def create_recipie_tool(data: RecipeCreate, recipes: dict[int, Recipe]) -> Recipe:
    """Tool to create a new recipe."""
    return create_recipe(data, recipes)