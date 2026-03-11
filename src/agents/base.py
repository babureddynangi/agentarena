"""
Base agent class and result model for the Agent Arena framework.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any


@dataclass
class AgentResult:
    """Result returned by an agent after solving a task."""
    answer: str
    reasoning_trace: list[str] = field(default_factory=list)
    steps_taken: int = 0
    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def has_answer(self) -> bool:
        return self.answer is not None and self.answer.strip() != ""


class BaseAgent(ABC):
    """Abstract base class for all agents in the arena."""

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

        Args:
            task: A Task object with question, category, expected_answer, etc.

        Returns:
            AgentResult with the agent's answer, reasoning trace, and step count.
        """
        pass

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name='{self._name}')"
