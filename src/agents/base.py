"""
Base agent class and result model for the Agent Arena framework.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any


@dataclass
class AgentResult:
    """Result returned by an agent after solving a task."""
    content: str
    metadata: dict[str, Any] = field(default_factory=dict)
    
    @property
    def has_content(self) -> bool:
        return self.content is not None and self.content.strip() != ""


class BaseAgent(ABC):
    """Abstract base class for all LLM agents in the arena."""

    def __init__(self, name: str, description: str):
        self._name = name
        self._description = description

    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return self._description

    @abstractmethod
    def solve(self, task) -> AgentResult:
        """
        Solve the given task and return an AgentResult.
        """
        pass

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self._name}')"
