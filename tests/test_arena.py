"""Integration test for Agent Arena Prototype simulation."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.agents import Gpt4Agent, Claude3Agent, LangChainAgent
from src.arena import ArenaRunner


class TestAgentArenaPrototype:
    def test_simulation_run_completes(self):
        agents = [Gpt4Agent(), Claude3Agent(), LangChainAgent()]
        runner = ArenaRunner(agents=agents)
        
        # Check task count
        assert len(runner.tasks) == 100
        
        # Run subset
        runner.tasks = runner.tasks[:5]
        scoreboards = runner.run()
        
        assert len(scoreboards) == 3
        assert "Agent Arena" in runner.__class__.__doc__
        # Results should be sorted by simulation performance
        assert scoreboards[0].agent_name == "GPT-4 Agent"
