"""
Task model for the Agent Arena framework.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class Difficulty(str, Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


class AnswerType(str, Enum):
    HYBRID = "hybrid"         # Rule (30%) + Judge (40%) + Human (30%)


class Category(str, Enum):
    CODING = "Autonomous Coding"
    RESEARCH = "Web Research"
    PLANNING = "Multi-step Planning"
    LOGIC = "Logic & Reasoning"
    DATA = "Data Transformation"


@dataclass
class Task:
    """A single benchmark task for LLMs."""
    id: int
    category: Category
    difficulty: Difficulty
    question: str
    expected_answer: str = ""
    answer_type: AnswerType = AnswerType.HYBRID
    acceptable_answers: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    def __repr__(self) -> str:
        return f"Task(id={self.id}, category='{self.category.value}', difficulty='{self.difficulty.value}')"
