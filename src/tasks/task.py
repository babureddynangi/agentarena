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
    EXACT = "exact"           # Must match exactly (case-insensitive)
    NUMERIC = "numeric"       # Must be numerically equal (with tolerance)
    CONTAINS = "contains"     # Answer must contain the expected string
    ONE_OF = "one_of"         # Answer must be one of several acceptable answers


class Category(str, Enum):
    MATH_LOGIC = "Math & Logic"
    TEXT_PROCESSING = "Text Processing"
    CODE_UNDERSTANDING = "Code Understanding"
    REASONING = "Reasoning & Common Sense"
    KNOWLEDGE = "Knowledge & Trivia"


@dataclass
class Task:
    """A single task for agents to solve."""
    id: int
    category: Category
    difficulty: Difficulty
    question: str
    expected_answer: str
    answer_type: AnswerType = AnswerType.EXACT
    acceptable_answers: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    def __repr__(self) -> str:
        return f"Task(id={self.id}, category='{self.category.value}', difficulty='{self.difficulty.value}')"
