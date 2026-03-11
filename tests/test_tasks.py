"""Tests for the 100-task prototype evaluation bank."""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.tasks import get_all_tasks
from src.tasks.task import Category


class TestPrototypeTaskBank:
    def test_total_task_count(self):
        tasks = get_all_tasks()
        assert len(tasks) == 100

    def test_domain_distribution(self):
        tasks = get_all_tasks()
        cats = [t.category for t in tasks]
        
        # 20 tasks per category
        assert cats.count(Category.CODING) == 20
        assert cats.count(Category.RESEARCH) == 20
        assert cats.count(Category.PLANNING) == 20
        assert cats.count(Category.LOGIC) == 20
        assert cats.count(Category.DATA) == 20
