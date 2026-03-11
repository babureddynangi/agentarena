"""Integration test for LLM Benchmark Arena."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.agents import OpusAgent, GptAgent, GrokAgent
from src.arena import ArenaRunner


class TestArenaIntegration:
    def test_full_benchmark_run(self):
        agents = [OpusAgent(), GptAgent(), GrokAgent()]
        runner = ArenaRunner(agents=agents)
        scoreboards = runner.run()
        
        assert len(scoreboards) == 3
        # Should be sorted
        assert scoreboards[0].avg_score >= scoreboards[1].avg_score
        assert scoreboards[1].avg_score >= scoreboards[2].avg_score
