"""Constructeur de l'agent."""

from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_anthropic import ChatAnthropic
from config import API_KEY, MODEL_NAME
from agent.prompts import get_agent_prompt
from tools.recipies import create_tool, delete_byid_tool, get_byid_tool, getall_tool


def build_agent() -> AgentExecutor:
    """Construit et retourne l'agent exécuteur."""
    llm = ChatAnthropic(model=MODEL_NAME, api_key=API_KEY)
    tools = [create_tool, delete_byid_tool, get_byid_tool, getall_tool]
    prompt = get_agent_prompt()
    agent = create_tool_calling_agent(llm, tools, prompt)
    return AgentExecutor(agent=agent, tools=tools, verbose=True)