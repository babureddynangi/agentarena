"""
Arena Runner — Orchestrates the agent competition.

Loads all tasks, runs each agent on every task, collects results,
scores them, and outputs a formatted leaderboard.
"""

import time
from ..agents.base import BaseAgent, AgentResult
from ..tasks.task import Task
from ..tasks.task_bank import get_all_tasks
from ..scoring.scorer import Scorer, TaskScore, AgentScoreboard


class ArenaRunner:
    """Runs all agents against all tasks and produces a scored leaderboard."""

    def __init__(self, agents: list[BaseAgent], tasks: list[Task] | None = None):
        self.agents = agents
        self.tasks = tasks or get_all_tasks()
        self.scorer = Scorer()
        self.scoreboards: list[AgentScoreboard] = []

    def run(self, verbose: bool = False) -> list[AgentScoreboard]:
        """
        Run all LLMs on all tasks and return scored results.
        """
        self.scoreboards = []
        for agent in self.agents:
            print(f"  Benchmarking {agent.name}...")
            scoreboard = AgentScoreboard(agent_name=agent.name)
            
            for task in self.tasks:
                result = agent.solve(task)
                task_score = self.scorer.score_task(agent.name, task, result)
                scoreboard.task_scores.append(task_score)
                
                if verbose:
                    print(f"    - Task {task.id:2d} ({task.category.value}): {task_score.overall}/100")

            scoreboard.compute_aggregates()
            self.scoreboards.append(scoreboard)

        # Sort by overall score (descending)
        self.scoreboards.sort(key=lambda sb: sb.avg_score, reverse=True)
        return self.scoreboards

    def print_leaderboard(self):
        """Print a beautifully formatted LLM Benchmark leaderboard."""
        if not self.scoreboards:
            print("No results. Run the arena first.")
            return

        print()
        print("=" * 100)
        print("                        🏆  LLM BENCHMARK ARENA — RESULTS  🏆")
        print("=" * 100)

        medals = ["🥇", "🥈", "🥉"]

        for rank, sb in enumerate(self.scoreboards):
            medal = medals[rank] if rank < len(medals) else f"#{rank + 1}"
            print()
            print(f"  {medal}  {sb.agent_name}")
            print(f"  {'─' * 60}")
            print(f"  Average Benchmark Score: {sb.avg_score:6.2f} / 100")

        # Category breakdown
        print()
        print("─" * 100)
        print("  📊  CATEGORY BREAKDOWN (Average Score per Category)")
        print("─" * 100)
        print()

        categories = list(self.scoreboards[0].category_scores.keys())
        header = f"  {'Category':<30}"
        for sb in self.scoreboards:
            header += f" {sb.agent_name:>20}"
        print(header)
        print(f"  {'─' * (30 + 21 * len(self.scoreboards))}")

        for cat in categories:
            row = f"  {cat:<30}"
            for sb in self.scoreboards:
                score = sb.category_scores.get(cat, 0.0)
                row += f" {score:>19.2f}"
            print(row)

        print()
        print("=" * 100)
        winner = self.scoreboards[0]
        print(f"  👑  LEADER: {winner.agent_name} with {winner.avg_score:.2f} points!")
        print("=" * 100)
        print()
