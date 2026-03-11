"""Tests for rubric-based scoring."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.scoring import Scorer, TaskScore, AgentScoreboard
from src.tasks.task import Task, Category, Difficulty, AnswerType
from src.agents.base import AgentResult

class TestScoring:
    def setup_method(self):
        self.scorer = Scorer()

    def test_score_task(self):
        task = Task(1, Category.BOOK_WRITING, Difficulty.EASY, "Q", "Ref")
        result = AgentResult(content="Story content")
        score = self.scorer.score_task("Claude Opus", task, result)
        
        assert isinstance(score, TaskScore)
        assert 0 <= score.overall <= 100
        assert score.quality > 0

    def test_scoreboard_aggregation(self):
        sb = AgentScoreboard(agent_name="Test")
        sb.task_scores = [
            TaskScore(1, "Cat", "easy", overall=90, answer_given="A"),
            TaskScore(2, "Cat", "easy", overall=80, answer_given="B"),
        ]
        sb.compute_aggregates()
        assert sb.avg_score == 85.0
        assert sb.total_tasks == 2
