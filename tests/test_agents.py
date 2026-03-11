"""Tests for paper-aligned LLM agents."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.agents import Gpt4Agent, Claude3Agent, LangChainAgent, AgentResult
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
    def test_gpt4_performance_metadata(self):
        agent = Gpt4Agent()
        result = agent.solve(_sample_task())
        assert result.metadata["target_score_factor"] == 0.82
        assert "GPT-4" in result.content

    def test_claude3_performance_metadata(self):
        agent = Claude3Agent()
        result = agent.solve(_sample_task())
        assert result.metadata["target_score_factor"] == 0.79
        assert "Claude-3" in result.content

    def test_langchain_performance_metadata(self):
        agent = LangChainAgent()
        result = agent.solve(_sample_task())
        assert result.metadata["target_score_factor"] == 0.61
        assert "LangChain" in result.content
