"""Prompts pour l'agent."""

from langchain_core.prompts import ChatPromptTemplate

SYSTEM_PROMPT = """Tu es un assistant qui aide à répondre à des questions à partir \
d'une base de connaissances locale. Utilise les outils disponibles pour chercher \
l'information puis donne ta réponse en français, claire et sourcée."""


def get_agent_prompt() -> ChatPromptTemplate:
    """Retourne le prompt configuré pour l'agent."""
    return ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ])