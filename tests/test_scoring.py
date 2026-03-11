"""Tests for the scoring engine."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.scoring import Scorer, TaskScore, AgentScoreboard


class TestAccuracyChecking:
    def setup_method(self):
        self.scorer = Scorer()

    def test_exact_match(self):
        assert self.scorer.check_accuracy("hello", "hello", "exact") == 100.0

    def test_exact_match_case_insensitive(self):
        assert self.scorer.check_accuracy("Hello", "hello", "exact") == 100.0

    def test_exact_mismatch(self):
        assert self.scorer.check_accuracy("world", "hello", "exact") == 0.0

    def test_numeric_exact(self):
        assert self.scorer.check_accuracy("42", "42", "numeric") == 100.0

    def test_numeric_with_float(self):
        assert self.scorer.check_accuracy("42.0", "42", "numeric") == 100.0

    def test_numeric_wrong(self):
        assert self.scorer.check_accuracy("99", "42", "numeric") == 0.0

    def test_contains_match(self):
        assert self.scorer.check_accuracy("Guido van Rossum", "Guido van Rossum", "contains") == 100.0

    def test_contains_partial(self):
        assert self.scorer.check_accuracy("Hello World", "World", "contains") == 100.0

    def test_contains_mismatch(self):
        assert self.scorer.check_accuracy("Hello", "World", "contains") == 0.0

    def test_one_of_match(self):
        assert self.scorer.check_accuracy("Yes", "Yes", "one_of", ["yes", "YES"]) == 100.0

    def test_one_of_alternative(self):
        assert self.scorer.check_accuracy("YES", "Yes", "one_of", ["yes", "YES"]) == 100.0

    def test_empty_answer(self):
        assert self.scorer.check_accuracy("", "hello", "exact") == 0.0


class TestSpeedScoring:
    def setup_method(self):
        self.scorer = Scorer()

    def test_fastest_gets_100(self):
        times = {"A": 0.01, "B": 0.05, "C": 0.10}
        scores = self.scorer.compute_speed_scores(times)
        assert scores["A"] == max(scores.values())

    def test_slowest_gets_lowest(self):
        times = {"A": 0.01, "B": 0.05, "C": 0.10}
        scores = self.scorer.compute_speed_scores(times)
        assert scores["C"] == min(scores.values())


class TestEfficiencyScoring:
    def setup_method(self):
        self.scorer = Scorer()

    def test_fewest_steps_gets_highest(self):
        steps = {"A": 1, "B": 3, "C": 5}
        scores = self.scorer.compute_efficiency_scores(steps)
        assert scores["A"] == max(scores.values())

    def test_most_steps_gets_lowest(self):
        steps = {"A": 1, "B": 3, "C": 5}
        scores = self.scorer.compute_efficiency_scores(steps)
        assert scores["C"] == min(scores.values())


class TestOverallScoring:
    def setup_method(self):
        self.scorer = Scorer()

    def test_perfect_score(self):
        overall = self.scorer.compute_overall(100.0, 100.0, 100.0)
        assert overall == 100.0

    def test_zero_score(self):
        overall = self.scorer.compute_overall(0.0, 0.0, 0.0)
        assert overall == 0.0

    def test_accuracy_weighted_highest(self):
        # With only accuracy = 100, the rest zero
        overall = self.scorer.compute_overall(100.0, 0.0, 0.0)
        assert overall == 60.0  # 60% weight


class TestAgentScoreboard:
    def test_compute_aggregates(self):
        sb = AgentScoreboard(agent_name="Test")
        sb.task_scores = [
            TaskScore(task_id=1, category="Math", difficulty="easy",
                      accuracy=100, speed=80, efficiency=90, overall=92, correct=True),
            TaskScore(task_id=2, category="Math", difficulty="medium",
                      accuracy=0, speed=60, efficiency=70, overall=30, correct=False),
        ]
        sb.compute_aggregates()
        assert sb.total_correct == 1
        assert sb.total_tasks == 2
        assert sb.avg_accuracy == 50.0
        assert sb.overall_score == 61.0
