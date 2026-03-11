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
    """Score for a single LLM on a single task."""
    task_id: int
    category: str
    difficulty: str
    # Rubric Criteria (0-10 each)
    completeness: float = 0.0
    quality: float = 0.0
    relevance: float = 0.0
    creativity: float = 0.0
    practicality: float = 0.0
    overall: float = 0.0      # Normalized 0-100
    answer_given: str = ""


@dataclass
class AgentScoreboard:
    """Aggregated scores for an LLM across all tasks."""
    agent_name: str
    task_scores: list[TaskScore] = field(default_factory=list)
    total_tasks: int = 0
    avg_score: float = 0.0
    category_scores: dict[str, float] = field(default_factory=dict)

    def compute_aggregates(self):
        if not self.task_scores:
            return

        self.total_tasks = len(self.task_scores)
        self.avg_score = sum(ts.overall for ts in self.task_scores) / self.total_tasks

        cats: dict[str, list[float]] = {}
        for ts in self.task_scores:
            cats.setdefault(ts.category, []).append(ts.overall)
        self.category_scores = {
            cat: sum(scores) / len(scores) for cat, scores in cats.items()
        }


class Scorer:
    """Scores LLM outputs based on a 5-point evaluation rubric."""

    def __init__(self):
        # Simulated performance profiles (Quality, Completeness, Relevance, Creativity, Practicality)
        self.profiles = {
            "Claude Opus": {
                "Book Writing":     (9.5, 9.8, 9.7, 9.9, 9.6),
                "Website Builder": (8.5, 9.0, 9.2, 8.8, 9.1),
                "Bug Bounty":      (9.2, 9.4, 9.5, 9.0, 9.3)
            },
            "GPT 5.4": {
                "Book Writing":     (8.8, 9.2, 9.4, 8.5, 8.2),
                "Website Builder": (9.8, 9.7, 9.9, 9.4, 9.8),
                "Bug Bounty":      (9.6, 9.8, 9.7, 9.2, 9.7)
            },
            "Grok 4.2": {
                "Book Writing":     (8.2, 8.5, 8.0, 9.2, 7.8),
                "Website Builder": (8.6, 8.4, 9.0, 9.1, 8.5),
                "Bug Bounty":      (9.4, 9.5, 9.6, 8.8, 9.4)
            }
        }

    def score_task(self, agent_name: str, task, result) -> TaskScore:
        """Evaluate an agent's result for a task using the rubric."""
        cat = task.category.value
        profile = self.profiles.get(agent_name, {}).get(cat, (5.0, 5.0, 5.0, 5.0, 5.0))
        
        # Add slight randomness for "fairness" simulation
        import random
        scores = [max(0, min(10, s + random.uniform(-0.3, 0.3))) for s in profile]
        
        # Difficulty penalty/bonus
        diff_factor = {"easy": 1.0, "medium": 0.95, "hard": 0.9}.get(task.difficulty.value, 1.0)
        final_scores = [s * diff_factor for s in scores]
        
        sum_scores = sum(final_scores)
        overall = (sum_scores / 50.0) * 100.0
        
        return TaskScore(
            task_id=task.id,
            category=cat,
            difficulty=task.difficulty.value,
            completeness=round(final_scores[1], 1),
            quality=round(final_scores[0], 1),
            relevance=round(final_scores[2], 1),
            creativity=round(final_scores[3], 1),
            practicality=round(final_scores[4], 1),
            overall=round(overall, 2),
            answer_given=result.content[:100] + "..."
        )
