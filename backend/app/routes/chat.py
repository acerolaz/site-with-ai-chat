"""Endpoint de chat avec agent LangChain singleton.

Étape 1 : appel direct à Kimi-K2.6 via AzureAIOpenAIApiChatModel (langchain-azure-ai),
          sans outils, qui renvoie la réponse du modèle. ✓ COMPLÉTÉ

Étape 2 : transformer ça en agent LangChain avec 3 outils branchés sur app/store.py :
          - list_recipes  → retourne la liste actuelle
          - create_recipe → crée une nouvelle recette
          - delete_recipe → supprime par id
          (voir langchain.agents.create_agent)

Étape 3 (stretch) : mémoire conversationnelle pour suivre une session de chat.
"""

from fastapi import APIRouter
from pydantic import BaseModel
from app.agent import get_agent

router = APIRouter(prefix="/chat", tags=["chat"])


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    reply: str


@router.post("", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    """Chat endpoint using singleton agent."""
    try:
        agent = get_agent()
        result = agent.invoke({"messages": [{"role": "user", "content": request.message}]})
        messages = result.get("messages", [])
        reply = messages[-1].content if messages else "No response from agent."
    except Exception as e:
        reply = f"Error: {str(e)}"
    
    return ChatResponse(reply=reply)

