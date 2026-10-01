"""Variables d'environnement et chargement de la base de connaissances."""

import os
import json
from dotenv import load_dotenv

from config import DEFAULT_MODEL, KB_PATH

load_dotenv()

ENDPOINT = os.getenv("AZURE_AI_INFERENCE_ENDPOINT")
API_KEY = os.getenv("AZURE_AI_INFERENCE_API_KEY")
MODEL = os.getenv("AZURE_AI_INFERENCE_MODEL", DEFAULT_MODEL)

with open(KB_PATH, "r", encoding="utf-8") as f:
    KB = json.load(f)
