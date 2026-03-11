"""
LLM Benchmark Arena — Main Entry Point

Benchmarks Opus, GPT 5.4, and Grok 4.2 across Book Writing, 
Website Building, and Bug Bounty tasks.
"""

from src.agents import OpusAgent, GptAgent, GrokAgent
from src.tasks import get_all_tasks
from src.arena import ArenaRunner
import os

def main():
    # Set encoding for Windows emoji support
    os.environ['PYTHONIOENCODING'] = 'utf-8'
    
    print()
    print("🏆  LLM BENCHMARK ARENA — Opus vs GPT 5.4 vs Grok 4.2  🏆")
    print()

    # Create agents
    agents = [
        OpusAgent(),
        GptAgent(),
        GrokAgent(),
    ]

    print(f"  Models loaded: {len(agents)}")
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
    print("\n  Starting benchmark evaluation...")
    print("  " + "─" * 60)

    runner = ArenaRunner(agents=agents, tasks=tasks)
    runner.run(verbose=True)

    # Print the leaderboard
    runner.print_leaderboard()


if __name__ == "__main__":
    main()
