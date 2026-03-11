"""
Scoring engine for the Agent Arena.

Evaluates agents on:
  - Accuracy  (60% weight) — correctness of the answer
  - Speed     (25% weight) — time relative to the slowest agent
  - Efficiency (15% weight) — fewer reasoning steps = higher score
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class TaskScore:
    """Score for a single agent on a single task."""
    task_id: int
    category: str
    difficulty: str
    accuracy: float = 0.0     # 0–100
    speed: float = 0.0        # 0–100
    efficiency: float = 0.0   # 0–100
    overall: float = 0.0      # Weighted composite 0–100
    answer_given: str = ""
    expected_answer: str = ""
    correct: bool = False


@dataclass
class AgentScoreboard:
    """Aggregated scores for one agent across all tasks."""
    agent_name: str
    task_scores: list[TaskScore] = field(default_factory=list)
    total_correct: int = 0
    total_tasks: int = 0
    avg_accuracy: float = 0.0
    avg_speed: float = 0.0
    avg_efficiency: float = 0.0
    overall_score: float = 0.0
    category_scores: dict[str, float] = field(default_factory=dict)

    def compute_aggregates(self):
        """Compute aggregate scores from individual task scores."""
        if not self.task_scores:
            return

        self.total_tasks = len(self.task_scores)
        self.total_correct = sum(1 for ts in self.task_scores if ts.correct)
        self.avg_accuracy = sum(ts.accuracy for ts in self.task_scores) / self.total_tasks
        self.avg_speed = sum(ts.speed for ts in self.task_scores) / self.total_tasks
        self.avg_efficiency = sum(ts.efficiency for ts in self.task_scores) / self.total_tasks
        self.overall_score = sum(ts.overall for ts in self.task_scores) / self.total_tasks

        # Category breakdown
        cats: dict[str, list[float]] = {}
        for ts in self.task_scores:
            cats.setdefault(ts.category, []).append(ts.overall)
        self.category_scores = {
            cat: sum(scores) / len(scores) for cat, scores in cats.items()
        }


class Scorer:
    """Scores agent results against expected answers."""

    WEIGHT_ACCURACY = 0.60
    WEIGHT_SPEED = 0.25
    WEIGHT_EFFICIENCY = 0.15

    def __init__(self, numeric_tolerance: float = 0.01):
        self.numeric_tolerance = numeric_tolerance

    def check_accuracy(self, answer: str, expected: str, answer_type: str,
                       acceptable_answers: list[str] | None = None) -> float:
        """
        Check if the answer is correct. Returns 100.0 for correct, 0.0 for wrong.
        """
        if not answer or not answer.strip():
            return 0.0

        answer = answer.strip()
        expected = expected.strip()
        at = answer_type if isinstance(answer_type, str) else answer_type.value

        if at == "exact":
            if answer.lower() == expected.lower():
                return 100.0
            if acceptable_answers:
                for acc in acceptable_answers:
                    if answer.lower() == acc.strip().lower():
                        return 100.0
            return 0.0

        elif at == "numeric":
            try:
                a = float(answer)
                e = float(expected)
                if abs(a - e) <= self.numeric_tolerance:
                    return 100.0
                # Partial credit for close answers
                if e != 0 and abs((a - e) / e) < 0.1:
                    return 50.0
            except (ValueError, TypeError):
                pass
            return 0.0

        elif at == "contains":
            if expected.lower() in answer.lower():
                return 100.0
            return 0.0

        elif at == "one_of":
            all_options = [expected] + (acceptable_answers or [])
            for opt in all_options:
                if answer.lower() == opt.strip().lower():
                    return 100.0
            return 0.0

        return 0.0

    def compute_speed_scores(self, times: dict[str, float]) -> dict[str, float]:
        """
        Compute speed scores: fastest gets 100, others scaled relative to max time.
        """
        if not times:
            return {}

        max_time = max(times.values())
        if max_time == 0:
            return {name: 100.0 for name in times}

        return {
            name: round(max(0, (1 - t / max_time) * 100), 2) if max_time > 0 else 100.0
            for name, t in times.items()
        }

    def compute_efficiency_scores(self, steps: dict[str, int]) -> dict[str, float]:
        """
        Compute efficiency scores: fewer steps = higher score.
        """
        if not steps:
            return {}

        max_steps = max(steps.values())
        if max_steps == 0:
            return {name: 100.0 for name in steps}

        return {
            name: round(max(0, (1 - s / max_steps) * 100), 2) if max_steps > 0 else 100.0
            for name, s in steps.items()
        }

    def compute_overall(self, accuracy: float, speed: float, efficiency: float) -> float:
        """Compute weighted overall score."""
        return round(
            accuracy * self.WEIGHT_ACCURACY
            + speed * self.WEIGHT_SPEED
            + efficiency * self.WEIGHT_EFFICIENCY,
            2
        )
