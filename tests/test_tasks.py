"""Tests for the new LLM benchmark task bank."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.tasks import get_all_tasks, get_tasks_by_category
from src.tasks.task import Category, Difficulty


class TestTaskBank:
    def test_total_tasks(self):
        tasks = get_all_tasks()
        assert len(tasks) == 30

    def test_categories(self):
        tasks = get_all_tasks()
        cats = set(t.category for t in tasks)
        assert Category.BOOK_WRITING in cats
        assert Category.WEBSITE_BUILDER in cats
        assert Category.BUG_BOUNTY in cats

    def test_count_per_category(self):
        assert len(get_tasks_by_category(Category.BOOK_WRITING)) == 10
        assert len(get_tasks_by_category(Category.WEBSITE_BUILDER)) == 10
        assert len(get_tasks_by_category(Category.BUG_BOUNTY)) == 10
