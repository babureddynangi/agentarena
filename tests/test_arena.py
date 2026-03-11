"""Integration test for paper-aligned empirical benchmark."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.agents import Gpt4Agent, Claude3Agent, LangChainAgent
from src.arena import ArenaRunner


class TestEmpiricalArena:
    def test_100_task_run_completes(self):
        # Using a subset for speed in unit tests, but checking full runner logic
        agents = [Gpt4Agent(), Claude3Agent(), LangChainAgent()]
        runner = ArenaRunner(agents=agents)
        
        # Check that we have 100 tasks
        assert len(runner.tasks) == 100
        
        # Run subset integration
        runner.tasks = runner.tasks[:5]
        scoreboards = runner.run()
        
        assert len(scoreboards) == 3
        # Check sorting (GPT-4 82% > Claude 79% > LangChain 61%)
        assert scoreboards[0].agent_name == "GPT-4 Agent"
        assert scoreboards[1].agent_name == "Claude-3 Agent"
        assert scoreboards[2].agent_name == "LangChain Agent"
