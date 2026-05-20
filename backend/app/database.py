"""Configuration SQLAlchemy — engine, session, base déclarative."""

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://recipes:recipes@db:5432/recipes",
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


def get_db():
    """Dépendance FastAPI : fournit une session et la ferme après usage."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
