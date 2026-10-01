"""Configuration et constantes du projet."""

import os
from dotenv import load_dotenv

load_dotenv()

# Variables d'environnement
API_KEY = os.getenv("ANTHROPIC_API_KEY")

# Chemins
KB_PATH = "./data/kb.json"

# Modèle LLM
MODEL_NAME = "claude-haiku-4-5"

# Messages
WELCOME_MESSAGE = "Assistant prêt. Posez une question (Ctrl+C pour quitter)."
QUESTION_PROMPT = "Question: "
ANSWER_PREFIX = "Réponse: "
GOODBYE_MESSAGE = "À bientôt!"
ENTRY_NOT_FOUND_MSG = "Entrée '{query}' non trouvée dans la base de connaissances."