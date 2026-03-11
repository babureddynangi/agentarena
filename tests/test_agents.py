"""Tests for paper-aligned LLM agents."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.agents import Gpt4oAgent, Claude35SonnetAgent, Llama3_1Agent, AgentResult
from src.tasks.task import Task, Category, Difficulty, AnswerType


def _sample_task():
    return Task(
        id=99,
        category=Category.CODING,
        difficulty=Difficulty.MEDIUM,
        question="Write a script.",
        expected_answer="Criteria",
        answer_type=AnswerType.HYBRID,
    )


class TestAlignedAgents:
    def test_gpt4o_performance_metadata(self):
        agent = Gpt4oAgent()
        result = agent.solve(_sample_task())
        assert result.metadata["target_score_factor"] == 0.82
        assert "GPT-4o" in result.content

    def test_claude35_sonnet_performance_metadata(self):
        agent = Claude35SonnetAgent()
        result = agent.solve(_sample_task())
        assert result.metadata["target_score_factor"] == 0.79
        assert "Claude 3.5 Sonnet" in result.content

    def test_llama3_1_performance_metadata(self):
        agent = Llama3_1Agent()
        result = agent.solve(_sample_task())
        assert result.metadata["target_score_factor"] == 0.61
        assert "Llama 3.1 70B" in result.content
