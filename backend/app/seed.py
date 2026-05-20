"""Données initiales — insère les recettes de démarrage si la table est vide."""

from app.database import SessionLocal
from app.models import RecipeModel


def seed_db() -> None:
    with SessionLocal() as db:
        if db.query(RecipeModel).count() == 0:
            db.add_all([
                RecipeModel(
                    name="Tarte aux pommes",
                    ingredients=["pommes", "pâte brisée", "sucre", "cannelle"],
                ),
                RecipeModel(
                    name="Quiche lorraine",
                    ingredients=["pâte brisée", "lardons", "œufs", "crème fraîche"],
                ),
            ])
            db.commit()
