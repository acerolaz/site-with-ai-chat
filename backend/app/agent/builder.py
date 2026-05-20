"""Constructeur de l'agent."""

import os
from langchain.agents import create_agent
from langchain_azure_ai.chat_models import AzureAIOpenAIApiChatModel
from .prompts import SYSTEM_PROMPT
from app.tools.recipes import create_recipe_tool, list_recipes_tool, delete_recipe_tool, get_recipe_by_id_tool


def build_agent():
    """Construit et retourne l'agent LangChain 1.x."""
    llm = AzureAIOpenAIApiChatModel(
        endpoint=os.getenv("AZURE_AI_INFERENCE_ENDPOINT", ""),
        credential=os.getenv("AZURE_AI_INFERENCE_API_KEY", ""),
        model=os.getenv("AZURE_AI_INFERENCE_MODEL", ""),
    )
    tools = [create_recipe_tool, list_recipes_tool, delete_recipe_tool, get_recipe_by_id_tool]
    return create_agent(llm, tools=tools, system_prompt=SYSTEM_PROMPT)