"""Tests for Agent Arena Prototype hybrid 30/40/30 scoring."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.scoring.scorer import AgentArenaScorer, TaskScore, AgentScoreboard
from src.tasks.task import Task, Category, Difficulty, AnswerType
from src.agents.base import AgentResult


class TestAgentArenaScoring:
    def setup_method(self):
        self.scorer = AgentArenaScorer()

    def test_structural_rule_matching(self):
        task = Task(1, Category.CODING, Difficulty.HARD, "Q", "Ref", AnswerType.HYBRID)
        
        # Missing markers
        r1 = AgentResult(content="Hello", metadata={})
        score1 = self.scorer.score_task("Test", task, r1)
        assert score1.rule_score == 0.0
        
        # All markers + coding bonus
        r2 = AgentResult(content="Methodology: X. Execution: Y. Confidence: Z. import os", metadata={})
        score2 = self.scorer.score_task("Test", task, r2)
        assert score2.rule_score > 99.0

    def test_prototype_score_calculation(self):
        task = Task(1, Category.CODING, Difficulty.HARD, "Q", "Ref", AnswerType.HYBRID)
        result = AgentResult(content="Methodology: X. Execution: Y. Confidence: Z.", 
                             metadata={"target_score_factor": 0.82})
        
        score = self.scorer.score_task("GPT-4", task, result)
        assert isinstance(score, TaskScore)
        assert score.is_simulation is True
        assert 0 <= score.overall <= 100

    def test_scoreboard_aggregates(self):
        sb = AgentScoreboard(agent_name="Test")
        sb.task_scores = [
            TaskScore(1, "Cat", rule_score=80, judge_score=85, human_score=80, overall=82),
            TaskScore(2, "Cat", rule_score=40, judge_score=45, human_score=40, overall=42),
        ]
        sb.compute_aggregates()
        assert sb.avg_score == 62.0
        assert sb.rule_avg == 60.0
