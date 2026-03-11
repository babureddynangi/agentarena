"""
Final Entry Point — Aligned with Agent Arena White Paper.
Runs the 100-task empirical study comparing GPT-4, Claude-3, and LangChain.
"""

import os
from src.agents import Gpt4Agent, Claude3Agent, LangChainAgent
from src.tasks import get_all_tasks
from src.arena import ArenaRunner

def main():
    # Set encoding for Windows emoji support
    os.environ['PYTHONIOENCODING'] = 'utf-8'
    
    print("\n" + "=" * 100)
    print("                        🏟️  AGENT ARENA — EMPIRICAL STUDY RUNNER  📊")
    print("=" * 100)
    print("  Aligning repository implementation with the White Paper testing strategy.")
    print("  Evaluation Model: 30/40/30 Hybrid (Rule/Judge/Human)")
    print("=" * 100)

    # Initialize Agents
    agents = [
        Gpt4Agent(),
        Claude3Agent(),
        LangChainAgent()
    ]

    # Load 100 Tasks
    tasks = get_all_tasks()
    print(f"\n  [✔] Agents Loaded: {', '.join([a.name for a in agents])}")
    print(f"  [✔] Empirical Task Bank Loaded: {len(tasks)} tasks across 5 domains.")

    # Run Benchmark
    print("\n  🚀 Executing 100-task benchmark study...")
    print("  " + "─" * 60)

    runner = ArenaRunner(agents=agents, tasks=tasks)
    runner.run(verbose=False)

    # Display Results
    runner.print_leaderboard()

    print("  [TIP] Run 'python simulation_study.py' for the 500-round statistical analysis.")
    print("=" * 100 + "\n")

if __name__ == "__main__":
    main()
