from dataclasses import dataclass, field
import random


@dataclass
class TaskScore:
    """Score for an agent on a single task using the 30/40/30 Hybrid Model."""
    task_id: int
    category: str
    rule_score: float = 0.0   # 30% — Hard checks
    judge_score: float = 0.0  # 40% — LLM-as-Judge
    human_score: float = 0.0  # 30% — Qualitative
    overall: float = 0.0      # Weighted composite 0-100
    answer_preview: str = ""


@dataclass
class AgentScoreboard:
    """Aggregated empirical results for an agent."""
    agent_name: str
    task_scores: list[TaskScore] = field(default_factory=list)
    avg_score: float = 0.0
    category_scores: dict[str, float] = field(default_factory=dict)
    rule_avg: float = 0.0
    judge_avg: float = 0.0
    human_avg: float = 0.0

    def compute_aggregates(self):
        if not self.task_scores:
            return

        n = len(self.task_scores)
        self.avg_score = sum(ts.overall for ts in self.task_scores) / n
        self.rule_avg = sum(ts.rule_score for ts in self.task_scores) / n
        self.judge_avg = sum(ts.judge_score for ts in self.task_scores) / n
        self.human_avg = sum(ts.human_score for ts in self.task_scores) / n

        cats: dict[str, list[float]] = {}
        for ts in self.task_scores:
            cats.setdefault(ts.category, []).append(ts.overall)
        self.category_scores = {
            cat: sum(scores) / len(scores) for cat, scores in cats.items()
        }


class Scorer:
    """
    Hybrid Scorer (30/40/30) as specified in the Agent Arena White Paper.
    
    Weights:
      - Rule-based (30%): Binary/Deterministic checks.
      - LLM Judge (40%): Evaluation of reasoning and planning coherence.
      - Human Eval (30%): Qualitative 'vibes' and usability check.
    """

    def score_task(self, agent_name: str, task, result) -> TaskScore:
        target = result.metadata.get("target_score_factor", 0.5)
        
        # Rule Score (30%) — high variance, hard checks
        rule_raw = self._simulate_rule_score(target)
        
        # Judge Score (40%) — more stable, reasoning check
        judge_raw = self._simulate_judge_score(target)
        
        # Human Score (30%) — qualitative, conservative
        human_raw = self._simulate_human_score(target)
        
        # Weighted Overall (0-100)
        overall = (rule_raw * 0.3) + (judge_raw * 0.4) + (human_raw * 0.3)
        
        return TaskScore(
            task_id=task.id,
            category=task.category.value,
            rule_score=round(rule_raw, 2),
            judge_score=round(judge_raw, 2),
            human_score=round(human_raw, 2),
            overall=round(overall, 2),
            answer_preview=result.content[:60] + "..."
        )

    def _simulate_rule_score(self, target: float) -> float:
        # Rules are either right or wrong mostly, but across 20 tasks they average out
        base = target * 100
        return max(0, min(100, base + random.uniform(-15, 15)))

    def _simulate_judge_score(self, target: float) -> float:
        # LLM Judges are slightly more optimistic but consistent
        base = target * 100
        return max(0, min(100, (base * 1.05) + random.uniform(-5, 5)))

    def _simulate_human_score(self, target: float) -> float:
        # Humans are often harsher or more conservative
        base = target * 100
        return max(0, min(100, (base * 0.9) + random.uniform(-10, 10)))
