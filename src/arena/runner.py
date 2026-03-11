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
        """Print the empirical leaderboard with 30/40/30 hybrid breakdowns."""
        if not self.scoreboards:
            print("No results. Run the arena first.")
            return

        print()
        print("=" * 100)
        print("                        📊  AGENT ARENA — EMPIRICAL LEADERBOARD  📊")
        print("                        (Hybrid 30/40/30 Rule/Judge/Human Model)")
        print("=" * 100)

        medals = ["🥇", "🥈", "🥉"]

        for rank, sb in enumerate(self.scoreboards):
            medal = medals[rank] if rank < len(medals) else f"#{rank + 1}"
            print()
            print(f"  {medal}  {sb.agent_name:<20} | Score: {sb.avg_score:6.2f}%")
            print(f"  {'─' * 60}")
            print(f"      [Rule-Based: {sb.rule_avg:5.1f}%]  "
                  f"[LLM-Judge: {sb.judge_avg:5.1f}%]  "
                  f"[Human-Eval: {sb.human_avg:5.1f}%]")

        # Category breakdown
        print()
        print("─" * 100)
        print("  🎯  DOMAIN PERFORMANCE (Category Breakdowns)")
        print("─" * 100)
        print()

        categories = list(self.scoreboards[0].category_scores.keys())
        header = f"  {'Domain':<25}"
        for sb in self.scoreboards:
            name_short = sb.agent_name.split()[0]
            header += f" {name_short:>18}"
        print(header)
        print(f"  {'─' * (25 + 19 * len(self.scoreboards))}")

        for cat in categories:
            row = f"  {cat:<25}"
            for sb in self.scoreboards:
                score = sb.category_scores.get(cat, 0.0)
                row += f" {score:>17.2f}%"
            print(row)

        print()
        print("=" * 100)
        winner = self.scoreboards[0]
        print(f"  🏆  WINNER: {winner.agent_name} with {winner.avg_score:.2f}% Empirical Accuracy")
        print("=" * 100)
        print()
