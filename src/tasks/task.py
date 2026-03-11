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
    EXACT = "exact"
    NUMERIC = "numeric"
    CONTAINS = "contains"
    ONE_OF = "one_of"
    RUBRIC = "rubric"         # Evaluation based on quality criteria


class Category(str, Enum):
    BOOK_WRITING = "Book Writing"
    WEBSITE_BUILDER = "Website Builder"
    BUG_BOUNTY = "Bug Bounty"


@dataclass
class Task:
    """A single benchmark task for LLMs."""
    id: int
    category: Category
    difficulty: Difficulty
    question: str
    expected_answer: str = "" # Reference or criteria description
    answer_type: AnswerType = AnswerType.RUBRIC
    acceptable_answers: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    def __repr__(self) -> str:
        return f"Task(id={self.id}, category='{self.category.value}', difficulty='{self.difficulty.value}')"
