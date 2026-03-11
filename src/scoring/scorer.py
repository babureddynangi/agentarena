from dataclasses import dataclass, field
import random
import re


@dataclass
class TaskScore:
    """Score for an agent on a single task using the 30/40/30 Hybrid Prototype Model."""
    task_id: int
    category: str
    rule_score: float = 0.0   # 30% — Hard structural checks
    judge_score: float = 0.0  # 40% — Simulated Reasoning Analysis
    human_score: float = 0.0  # 30% — Simulated Alignment/Utility
    overall: float = 0.0      # Weighted composite 0-100
    answer_preview: str = ""
    is_simulation: bool = True


@dataclass
class AgentScoreboard:
    """Aggregated simulation results for an agent."""
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


class AgentArenaScorer:
    """
    Agent Arena Structural Hybrid Scorer (Prototype Engine).
    
    Implements a structural 30/40/30 weight model:
      - Rule (30%): Pattern matching for required structural components.
      - Judge (40%): Simulation of qualitative reasoning evaluation.
      - Human (30%): Simulation of subjective utility.
    """

    def score_task(self, agent_name: str, task, result) -> TaskScore:
        target = result.metadata.get("target_score_factor", 0.5)
        content = result.content
        
        # 1. Rule Score (30%) - Structural validation
        rule_raw = self._eval_structural_rules(content, task.category)
        
        # 2. Judge Score (40%) - Simulated reasoning depth
        judge_raw = self._simulate_judge_score(target, content)
        
        # 3. Human Score (30%) - Simulated alignment
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
            answer_preview=content[:60].replace("\n", " ") + "...",
            is_simulation=True
        )

    def _eval_structural_rules(self, content: str, category) -> float:
        """Structural rule checking using pattern matching markers."""
        score = 0
        markers = ["Methodology:", "Execution:", "Confidence:"]
        
        for m in markers:
            if m.lower() in content.lower():
                score += 33.3
        
        # Bonus for category-specific keywords
        if "coding" in category.value.lower() and "import" in content.lower():
            score += 10
        if "research" in category.value.lower() and "analysis" in content.lower():
            score += 10
            
        return min(100.0, score)

    def _simulate_judge_score(self, target: float, content: str) -> float:
        # Penalize short content as a 'structural' signal
        length_penalty = 1.0 if len(content) > 100 else 0.7
        base = target * 100 * length_penalty
        return max(0, min(100, base + random.uniform(-5, 5)))

    def _simulate_human_score(self, target: float) -> float:
        base = target * 100
        return max(0, min(100, base + random.uniform(-10, 10)))
