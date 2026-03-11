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
    print("                        🏟️  AGENT ARENA — PROTOTYPE SIMULATION  📊")
    print("=" * 100)
    print("  Aligning repository implementation with the Agent Arena White Paper strategy.")
    print("  Evaluation Model: 30/40/30 Hybrid Prototype (Rule/Judge/Human)")
    print("  Note: Results represent simulated evidence for strategy validation.")
    print("=" * 100)

    # Initialize Aligned Prototype Agents
    agents = [
        Gpt4Agent(),
        Claude3Agent(),
        LangChainAgent()
    ]

    # Load Simulation Tasks (100)
    tasks = get_all_tasks()
    print(f"\n  [✔] Prototype Agents Loaded: {', '.join([a.name for a in agents])}")
    print(f"  [✔] Task Bank (Prototype): {len(tasks)} tasks across 5 paper-aligned domains.")

    # Run Simulation Benchmark
    print("\n  🚀 Executing 100-task simulation study...")
    print("  " + "─" * 60)

    runner = ArenaRunner(agents=agents, tasks=tasks)
    runner.run(verbose=False)

    # Display Simulation Leaderboard
    runner.print_leaderboard()

    print("  [REF] 'python simulation_study.py' for 100-round statistical convergence.")
    print("=" * 100 + "\n")

if __name__ == "__main__":
    main()
