"""Endpoint de chat avec agent LangChain singleton + mémoire de session.

Étape 1 : appel direct à Kimi-K2.6 via AzureAIOpenAIApiChatModel. ✓ COMPLÉTÉ
Étape 2 : agent LangChain avec outils recettes. ✓ COMPLÉTÉ
Étape 3 : mémoire conversationnelle par session_id (thread_id LangGraph). ✓ COMPLÉTÉ
"""

import time
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.agent import get_agent

router = APIRouter(prefix="/chat", tags=["chat"])

_MAX_RETRIES = 3
_RETRY_DELAY = 2.0  # seconds (doubles each attempt)


class ChatRequest(BaseModel):
    message: str
    session_id: str = "default"


class ChatResponse(BaseModel):
    reply: str


@router.post("", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    """Chat endpoint using singleton agent with per-session memory."""
    agent = get_agent()
    config = {"configurable": {"thread_id": request.session_id}}
    delay = _RETRY_DELAY

    print(f"Received chat request: {request.message} (session: {request.session_id})")

    for attempt in range(_MAX_RETRIES):
        try:
            result = agent.invoke(
                {"messages": [{"role": "user", "content": request.message}]},
                config=config,
            )
            messages = result.get("messages", [])
            reply = messages[-1].content if messages else "No response from agent."
            return ChatResponse(reply=reply)
        except Exception as e:
            err = str(e)
            is_rate_limit = "429" in err or "capacity" in err.lower()
            if is_rate_limit and attempt < _MAX_RETRIES - 1:
                time.sleep(delay)
                delay *= 2
                continue
            raise HTTPException(status_code=429 if is_rate_limit else 500, detail=err)

