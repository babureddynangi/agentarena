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
        Run all agents on all tasks and return scored results.
        """
        # Collect raw results: {agent_name: [(task, result, elapsed_time), ...]}
        raw_results: dict[str, list[tuple[Task, AgentResult, float]]] = {}

        for agent in self.agents:
            raw_results[agent.name] = []
            for task in self.tasks:
                start = time.perf_counter()
                result = agent.solve(task)
                elapsed = time.perf_counter() - start
                raw_results[agent.name].append((task, result, elapsed))

                if verbose:
                    correct = self._is_correct(task, result)
                    status = "✓" if correct else "✗"
                    print(f"  {status} {agent.name} | Task {task.id:2d} | "
                          f"Answer: {result.answer[:40]:<40} | "
                          f"Expected: {task.expected_answer}")

        # Score each agent
        self.scoreboards = []
        for agent in self.agents:
            scoreboard = self._score_agent(agent.name, raw_results)
            self.scoreboards.append(scoreboard)

        # Sort by overall score (descending)
        self.scoreboards.sort(key=lambda sb: sb.overall_score, reverse=True)
        return self.scoreboards

    def _is_correct(self, task: Task, result: AgentResult) -> bool:
        """Quick check if result is correct."""
        score = self.scorer.check_accuracy(
            result.answer, task.expected_answer,
            task.answer_type, task.acceptable_answers
        )
        return score >= 100.0

    def _score_agent(self, agent_name: str,
                     raw_results: dict[str, list[tuple[Task, AgentResult, float]]]
                     ) -> AgentScoreboard:
        """Compute full scoreboard for one agent."""
        scoreboard = AgentScoreboard(agent_name=agent_name)

        agent_results = raw_results[agent_name]

        for i, (task, result, elapsed) in enumerate(agent_results):
            # Accuracy
            accuracy = self.scorer.check_accuracy(
                result.answer, task.expected_answer,
                task.answer_type, task.acceptable_answers
            )

            # Speed: compare with same task across all agents
            times = {
                name: results[i][2]
                for name, results in raw_results.items()
            }
            speed_scores = self.scorer.compute_speed_scores(times)
            speed = speed_scores.get(agent_name, 50.0)

            # Efficiency: compare steps across all agents for same task
            steps = {
                name: results[i][1].steps_taken
                for name, results in raw_results.items()
            }
            eff_scores = self.scorer.compute_efficiency_scores(steps)
            efficiency = eff_scores.get(agent_name, 50.0)

            # Overall weighted score
            overall = self.scorer.compute_overall(accuracy, speed, efficiency)

            cat = task.category.value if hasattr(task.category, "value") else task.category
            diff = task.difficulty.value if hasattr(task.difficulty, "value") else task.difficulty

            task_score = TaskScore(
                task_id=task.id,
                category=cat,
                difficulty=diff,
                accuracy=accuracy,
                speed=speed,
                efficiency=efficiency,
                overall=overall,
                answer_given=result.answer,
                expected_answer=task.expected_answer,
                correct=accuracy >= 100.0,
            )
            scoreboard.task_scores.append(task_score)

        scoreboard.compute_aggregates()
        return scoreboard

    def print_leaderboard(self):
        """Print a beautifully formatted leaderboard to console."""
        if not self.scoreboards:
            print("No results. Run the arena first.")
            return

        print()
        print("=" * 90)
        print("                        🏟️  AGENT ARENA — FINAL LEADERBOARD  🏟️")
        print("=" * 90)

        # Medals
        medals = ["🥇", "🥈", "🥉"]

        for rank, sb in enumerate(self.scoreboards):
            medal = medals[rank] if rank < len(medals) else f"#{rank + 1}"
            print()
            print(f"  {medal}  {sb.agent_name}")
            print(f"  {'─' * 60}")
            print(f"  Overall Score:  {sb.overall_score:6.2f} / 100")
            print(f"  Accuracy:       {sb.avg_accuracy:6.2f} / 100  "
                  f"({sb.total_correct}/{sb.total_tasks} correct)")
            print(f"  Speed:          {sb.avg_speed:6.2f} / 100")
            print(f"  Efficiency:     {sb.avg_efficiency:6.2f} / 100")

        # Category breakdown
        print()
        print("─" * 90)
        print("  📊  CATEGORY BREAKDOWN")
        print("─" * 90)
        print()

        categories = list(self.scoreboards[0].category_scores.keys())
        header = f"  {'Category':<30}"
        for sb in self.scoreboards:
            header += f" {sb.agent_name:>18}"
        print(header)
        print(f"  {'─' * (30 + 18 * len(self.scoreboards) + len(self.scoreboards))}")

        for cat in categories:
            row = f"  {cat:<30}"
            for sb in self.scoreboards:
                score = sb.category_scores.get(cat, 0.0)
                row += f" {score:>17.2f}"
            print(row)

        # Task-by-task details
        print()
        print("─" * 90)
        print("  📋  TASK-BY-TASK RESULTS")
        print("─" * 90)
        print()

        header = f"  {'Task':>4} {'Category':<26} {'Diff':<7}"
        for sb in self.scoreboards:
            name_short = sb.agent_name[:12]
            header += f" {name_short:>13}"
        print(header)
        print(f"  {'─' * (4 + 26 + 7 + 14 * len(self.scoreboards))}")

        num_tasks = len(self.scoreboards[0].task_scores)
        for i in range(num_tasks):
            ts0 = self.scoreboards[0].task_scores[i]
            row = f"  {ts0.task_id:>4} {ts0.category:<26} {ts0.difficulty:<7}"
            for sb in self.scoreboards:
                ts = sb.task_scores[i]
                mark = "✓" if ts.correct else "✗"
                row += f" {mark} {ts.overall:>9.1f}"
            print(row)

        print()
        print("=" * 90)
        winner = self.scoreboards[0]
        print(f"  🏆  WINNER: {winner.agent_name} with {winner.overall_score:.2f} points!")
        print("=" * 90)
        print()
