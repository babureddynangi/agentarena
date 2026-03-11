"""
Arena Runner — Orchestrates the agent competition.

Loads all tasks, runs each agent on every task, collects results,
scores them, and outputs a formatted leaderboard.
"""

import time
from ..agents.base import BaseAgent, AgentResult
from ..tasks.task import Task
from ..tasks.task_bank import get_all_tasks
from ..scoring.scorer import AgentArenaScorer, TaskScore, AgentScoreboard


class ArenaRunner:
    """Orchestrates the Agent Arena Prototype simulation benchmark."""

    def __init__(self, agents: list[BaseAgent], tasks: list[Task] | None = None):
        self.agents = agents
        self.tasks = tasks or get_all_tasks()
        self.scorer = AgentArenaScorer()
        self.scoreboards: list[AgentScoreboard] = []

    def run(self, verbose: bool = False) -> list[AgentScoreboard]:
        """
        Run Agent Arena simulation study.
        """
        self.scoreboards = []
        for agent in self.agents:
            if verbose:
                print(f"  Simulating {agent.name}...")
            scoreboard = AgentScoreboard(agent_name=agent.name)
            
            for task in self.tasks:
                result = agent.solve(task)
                task_score = self.scorer.score_task(agent.name, task, result)
                scoreboard.task_scores.append(task_score)

            scoreboard.compute_aggregates()
            self.scoreboards.append(scoreboard)

        # Sort by overall score (descending)
        self.scoreboards.sort(key=lambda sb: sb.avg_score, reverse=True)
        return self.scoreboards

    def print_leaderboard(self):
        """Print the Agent Arena Prototype Simulation Leaderboard."""
        if not self.scoreboards:
            print("No simulation results. Run the arena first.")
            return

        print()
        print("=" * 100)
        print("                        🏟️  AGENT ARENA — PROTOTYPE LEADERBOARD  📊")
        print("                        (Simulation Study Evidence Layer)")
        print("=" * 100)

        medals = ["🥇", "🥈", "🥉"]

        for rank, sb in enumerate(self.scoreboards):
            medal = medals[rank] if rank < len(medals) else f"#{rank + 1}"
            print()
            print(f"  {medal}  {sb.agent_name:<20} | Score: {sb.avg_score:6.2f}%")
            print(f"  {'─' * 60}")
            print(f"      [Rule-Based: {sb.rule_avg:5.1f}%]  "
                  f"[Sim-Judge: {sb.judge_avg:5.1f}%]  "
                  f"[Sim-Human: {sb.human_avg:5.1f}%]")

        # Category breakdown
        print()
        print("─" * 100)
        print("  🎯  PROTOTYPE DOMAIN PERFORMANCE (Mean Simulation Scores)")
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
        print(f"  🏆  LEADER (Simulation): {winner.agent_name} with {winner.avg_score:.2f}% Convergence")
        print("  Note: Results reflect prototype simulation logic, not production evaluation logs.")
        print("=" * 100)
        print()
