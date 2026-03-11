"""Tests for paper-aligned hybrid 30/40/30 scoring."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.scoring import Scorer, TaskScore, AgentScoreboard
from src.tasks.task import Task, Category, Difficulty, AnswerType
from src.agents.base import AgentResult


class TestHybridScoring:
    def setup_method(self):
        self.scorer = Scorer()

    def test_hybrid_score_calculation(self):
        task = Task(1, Category.CODING, Difficulty.HARD, "Q", "Ref", AnswerType.HYBRID)
        # Mock result metadata with target factor
        result = AgentResult(content="...", metadata={"target_score_factor": 0.82})
        
        score = self.scorer.score_task("GPT-4 Agent", task, result)
        assert isinstance(score, TaskScore)
        assert 0 <= score.rule_score <= 100
        assert 0 <= score.judge_score <= 100
        assert 0 <= score.human_score <= 100
        # Weighted avg: 30*R + 40*J + 30*H should be in range
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
        assert sb.judge_avg == 65.0
        assert sb.human_avg == 60.0
