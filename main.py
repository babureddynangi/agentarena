"""
Agent Arena — Main Entry Point

Run the full arena competition between 3 agents on 30 tasks.
Usage: python main.py
"""

from src.agents import ReActAgent, ChainOfThoughtAgent, DirectAgent
from src.tasks import get_all_tasks
from src.arena import ArenaRunner


def main():
    print()
    print("🏟️  Agent Arena — Initializing...")
    print()

    # Create agents
    agents = [
        ReActAgent(),
        ChainOfThoughtAgent(),
        DirectAgent(),
    ]

    print(f"  Agents loaded: {len(agents)}")
    for agent in agents:
        print(f"    • {agent.name}: {agent.description}")

    # Load tasks
    tasks = get_all_tasks()
    print(f"\n  Tasks loaded: {len(tasks)}")

    categories = {}
    for t in tasks:
        cat = t.category.value
        categories[cat] = categories.get(cat, 0) + 1
    for cat, count in categories.items():
        print(f"    • {cat}: {count} tasks")

    # Run the arena
    print("\n  Running competition...")
    print("  " + "─" * 50)

    runner = ArenaRunner(agents=agents, tasks=tasks)
    runner.run(verbose=True)

    # Print the leaderboard
    runner.print_leaderboard()


if __name__ == "__main__":
    main()
