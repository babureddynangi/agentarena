"""Tests for LLM agent implementations."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.agents import OpusAgent, GptAgent, GrokAgent, AgentResult
from src.tasks.task import Task, Category, Difficulty, AnswerType


def _sample_task(cat=Category.BOOK_WRITING):
    return Task(
        id=99,
        category=cat,
        difficulty=Difficulty.EASY,
        question="Write something.",
        expected_answer="Criteria",
        answer_type=AnswerType.RUBRIC,
    )


class TestLLMAgents:
    def test_opus_solve(self):
        agent = OpusAgent()
        result = agent.solve(_sample_task())
        assert isinstance(result, AgentResult)
        assert result.has_content
        assert "fog" in result.content.lower()

    def test_gpt_solve(self):
        agent = GptAgent()
        result = agent.solve(_sample_task(Category.WEBSITE_BUILDER))
        assert isinstance(result, AgentResult)
        assert result.has_content
        assert "html" in result.content.lower()

    def test_grok_solve(self):
        agent = GrokAgent()
        result = agent.solve(_sample_task(Category.BUG_BOUNTY))
        assert isinstance(result, AgentResult)
        assert result.has_content
        assert "plain text" in result.content.lower()
