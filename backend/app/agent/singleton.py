"""Singleton agent instance."""

from .builder import build_agent

_agent_instance = None


def get_agent():
    """Get or create the singleton agent instance."""
    global _agent_instance
    if _agent_instance is None:
        _agent_instance = build_agent()
    return _agent_instance
