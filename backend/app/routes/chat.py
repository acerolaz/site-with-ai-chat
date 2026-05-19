"""Endpoint de chat avec appel direct à Kimi-K2.6.

Étape 1 : appel direct à Kimi-K2.6 via AzureAIOpenAIApiChatModel (langchain-azure-ai),
          sans outils, qui renvoie la réponse du modèle. ✓ COMPLÉTÉ

Étape 2 : transformer ça en agent LangChain avec 3 outils branchés sur app/store.py :
          - list_recipes  → retourne la liste actuelle
          - create_recipe → crée une nouvelle recette
          - delete_recipe → supprime par id
          (voir langchain.agents.create_agent)

Étape 3 (stretch) : mémoire conversationnelle pour suivre une session de chat.
"""

import os
from backend.app.agent.builder import build_agent
from backend.app.agent.config import ANSWER_PREFIX, QUESTION_PROMPT, WELCOME_MESSAGE
from fastapi import APIRouter
from pydantic import BaseModel
from langchain_azure_ai.chat_models import AzureAIOpenAIApiChatModel
from langchain_core.messages import HumanMessage

router = APIRouter(prefix="/chat", tags=["chat"])


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    reply: str


@router.post("", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    """Chat endpoint Anthropic."""
    agent = build_agent()
    print(WELCOME_MESSAGE)
    try:
            user_input = input(f"\n{QUESTION_PROMPT}").strip()
            answer = agent.invoke({"input": user_input})
            reply = f"\n{ANSWER_PREFIX}{answer['output']}" if answer else "No response from model."
    except Exception as e:
        reply = f"Error: {str(e)}"
    
    return ChatResponse(reply=reply)

