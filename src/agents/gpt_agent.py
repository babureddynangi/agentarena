"""
GPT 5.4 Agent — Structured, broad, and technical.
"""

from .base import BaseAgent, AgentResult


class GptAgent(BaseAgent):
    """GPT 5.4 simulated agent."""

    def __init__(self):
        super().__init__(
            name="GPT 5.4",
            description="Broad general knowledge, strong instruction following, and world-class coding."
        )

    def solve(self, task) -> AgentResult:
        cat = task.category.value
        content = ""

        if cat == "Book Writing":
            content = self._simulate_book_writing(task)
        elif cat == "Website Builder":
            content = self._simulate_website_builder(task)
        elif cat == "Bug Bounty":
            content = self._simulate_bug_bounty(task)
        else:
            content = "Simulated GPT 5.4 response."

        return AgentResult(content=content)

    def _simulate_book_writing(self, task):
        return (
            "London’s streets were slick with shadows. Elias felt the weight of the letter in his pocket, "
            "a crisp ivory square that burned like a secret. Every step on the cobblestones echoed, "
            "a sharp staccato rhythm that seemed to broadcast his arrival to the silent houses lining the lane."
        )

    def _simulate_website_builder(self, task):
        return (
            "<!DOCTYPE html>\n<html lang='en'>\n<head>\n"
            "<meta charset='UTF-8'>\n<title>GPT Landing Page</title>\n"
            "<style>\nbody { font-family: Arial; padding: 20px; }\n"
            ".header { display: flex; justify-content: space-between; }\n"
            "</style>\n</head>\n<body>\n"
            "<div class='header'>Logo | Nav Items</div>\n<h1>Future Tech</h1>\n"
            "</body>\n</html>"
        )

    def _simulate_bug_bounty(self, task):
        return (
            "Vulnerability: SQL Injection in Search Field.\n"
            "Impact: Critical. Potential data exfiltration of all user tables.\n"
            "Fix: Use parameterized queries (Prepared Statements)."
        )
