"""Integration test — Runs the full arena and validates output."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.agents import ReActAgent, ChainOfThoughtAgent, DirectAgent
from src.tasks import get_all_tasks
from src.arena import ArenaRunner


class TestArenaRunner:
    def test_full_run_completes(self):
        agents = [ReActAgent(), ChainOfThoughtAgent(), DirectAgent()]
        runner = ArenaRunner(agents=agents)
        scoreboards = runner.run()
        assert len(scoreboards) == 3

    def test_scoreboards_are_sorted(self):
        agents = [ReActAgent(), ChainOfThoughtAgent(), DirectAgent()]
        runner = ArenaRunner(agents=agents)
        scoreboards = runner.run()
        scores = [sb.overall_score for sb in scoreboards]
        assert scores == sorted(scores, reverse=True)

    def test_all_tasks_scored(self):
        agents = [ReActAgent(), ChainOfThoughtAgent(), DirectAgent()]
        runner = ArenaRunner(agents=agents)
        scoreboards = runner.run()
        for sb in scoreboards:
            assert sb.total_tasks == 30

    def test_scores_in_valid_range(self):
        agents = [ReActAgent(), ChainOfThoughtAgent(), DirectAgent()]
        runner = ArenaRunner(agents=agents)
        scoreboards = runner.run()
        for sb in scoreboards:
            assert 0 <= sb.overall_score <= 100
            assert 0 <= sb.avg_accuracy <= 100
            for ts in sb.task_scores:
                assert 0 <= ts.overall <= 100

    def test_category_breakdown_exists(self):
        agents = [ReActAgent(), ChainOfThoughtAgent(), DirectAgent()]
        runner = ArenaRunner(agents=agents)
        scoreboards = runner.run()
        for sb in scoreboards:
            assert len(sb.category_scores) == 5

    def test_custom_task_subset(self):
        """Test running with a subset of tasks."""
        agents = [ReActAgent(), DirectAgent()]
        tasks = get_all_tasks()[:5]
        runner = ArenaRunner(agents=agents, tasks=tasks)
        scoreboards = runner.run()
        assert len(scoreboards) == 2
        for sb in scoreboards:
            assert sb.total_tasks == 5
