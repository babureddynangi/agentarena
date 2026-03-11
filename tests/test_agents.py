"""Tests for all three agent implementations."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.agents import ReActAgent, ChainOfThoughtAgent, DirectAgent, AgentResult
from src.tasks.task import Task, Category, Difficulty, AnswerType


def _sample_task():
    return Task(
        id=99,
        category=Category.MATH_LOGIC,
        difficulty=Difficulty.EASY,
        question="What is the sum of 10 and 20?",
        expected_answer="30",
        answer_type=AnswerType.NUMERIC,
    )


def _sample_text_task():
    return Task(
        id=98,
        category=Category.TEXT_PROCESSING,
        difficulty=Difficulty.EASY,
        question='How many words are in the sentence "hello beautiful world"?',
        expected_answer="3",
        answer_type=AnswerType.NUMERIC,
    )


class TestReActAgent:
    def test_instantiation(self):
        agent = ReActAgent()
        assert agent.name == "ReAct Agent"
        assert "tool" not in agent.name.lower() or True  # just check it exists

    def test_returns_agent_result(self):
        agent = ReActAgent()
        result = agent.solve(_sample_task())
        assert isinstance(result, AgentResult)
        assert result.has_answer
        assert result.steps_taken > 0
        assert len(result.reasoning_trace) > 0

    def test_math_accuracy(self):
        agent = ReActAgent()
        result = agent.solve(_sample_task())
        assert float(result.answer) == 30.0

    def test_text_accuracy(self):
        agent = ReActAgent()
        result = agent.solve(_sample_text_task())
        assert result.answer == "3"


class TestChainOfThoughtAgent:
    def test_instantiation(self):
        agent = ChainOfThoughtAgent()
        assert agent.name == "Chain-of-Thought Agent"

    def test_returns_agent_result(self):
        agent = ChainOfThoughtAgent()
        result = agent.solve(_sample_task())
        assert isinstance(result, AgentResult)
        assert result.has_answer
        assert result.steps_taken > 0

    def test_math_accuracy(self):
        agent = ChainOfThoughtAgent()
        result = agent.solve(_sample_task())
        assert float(result.answer) == 30.0

    def test_text_accuracy(self):
        agent = ChainOfThoughtAgent()
        result = agent.solve(_sample_text_task())
        assert result.answer == "3"


class TestDirectAgent:
    def test_instantiation(self):
        agent = DirectAgent()
        assert agent.name == "Direct Agent"

    def test_returns_agent_result(self):
        agent = DirectAgent()
        result = agent.solve(_sample_task())
        assert isinstance(result, AgentResult)
        assert result.has_answer
        assert result.steps_taken >= 1

    def test_math_accuracy(self):
        agent = DirectAgent()
        result = agent.solve(_sample_task())
        assert float(result.answer) == 30.0

    def test_is_fastest(self):
        """Direct agent should take fewer steps."""
        task = _sample_task()
        react = ReActAgent().solve(task)
        direct = DirectAgent().solve(task)
        assert direct.steps_taken <= react.steps_taken
