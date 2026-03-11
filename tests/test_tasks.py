"""Tests for the task model and task bank."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.tasks import Task, get_all_tasks, get_tasks_by_category
from src.tasks.task import Category, Difficulty, AnswerType


class TestTaskModel:
    def test_create_task(self):
        t = Task(
            id=1,
            category=Category.MATH_LOGIC,
            difficulty=Difficulty.EASY,
            question="What is 1+1?",
            expected_answer="2",
        )
        assert t.id == 1
        assert t.category == Category.MATH_LOGIC
        assert t.difficulty == Difficulty.EASY

    def test_default_answer_type(self):
        t = Task(id=1, category=Category.MATH_LOGIC, difficulty=Difficulty.EASY,
                 question="Q", expected_answer="A")
        assert t.answer_type == AnswerType.EXACT


class TestTaskBank:
    def test_total_tasks(self):
        tasks = get_all_tasks()
        assert len(tasks) == 30

    def test_unique_ids(self):
        tasks = get_all_tasks()
        ids = [t.id for t in tasks]
        assert len(ids) == len(set(ids)), "Task IDs must be unique"

    def test_all_categories_covered(self):
        tasks = get_all_tasks()
        categories = set(t.category for t in tasks)
        assert len(categories) == 5, f"Expected 5 categories, got {len(categories)}"

    def test_six_tasks_per_category(self):
        for cat in Category:
            cat_tasks = get_tasks_by_category(cat)
            assert len(cat_tasks) == 6, f"{cat.value} has {len(cat_tasks)} tasks, expected 6"

    def test_difficulty_distribution(self):
        tasks = get_all_tasks()
        for cat in Category:
            cat_tasks = [t for t in tasks if t.category == cat]
            diffs = [t.difficulty for t in cat_tasks]
            assert diffs.count(Difficulty.EASY) == 2
            assert diffs.count(Difficulty.MEDIUM) == 2
            assert diffs.count(Difficulty.HARD) == 2

    def test_all_tasks_have_questions(self):
        for task in get_all_tasks():
            assert task.question.strip(), f"Task {task.id} has empty question"
            assert task.expected_answer.strip(), f"Task {task.id} has empty expected_answer"

    def test_get_tasks_by_category(self):
        math_tasks = get_tasks_by_category(Category.MATH_LOGIC)
        assert len(math_tasks) == 6
        assert all(t.category == Category.MATH_LOGIC for t in math_tasks)
