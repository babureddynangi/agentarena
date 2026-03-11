"""
Grok 4.2 Agent — Direct, edgy, and fast.
"""

from .base import BaseAgent, AgentResult


class GrokAgent(BaseAgent):
    """Grok 4.2 simulated agent."""

    def __init__(self):
        super().__init__(
            name="Grok 4.2",
            description="Direct, anti-woke, and highly technical. Designed to be funny and real."
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
            content = "Simulated Grok 4.2 response."

        return AgentResult(content=content)

    def _simulate_book_writing(self, task):
        return (
            "The city was a mess. Fog everywhere, as if the sky was embarrassed to see London. "
            "Elias was walking, brooding about stuff only detectives in noir novels care about. "
            "Someone was following him. Probably. They always are, aren't they?"
        )

    def _simulate_website_builder(self, task):
        return (
            "<main>\n  <h1>No BS Landing Page</h1>\n"
            "  <button onclick='buy()'>Get Grokked</button>\n"
            "</main>\n<style>\n  h1 { color: #f00; font-size: 5rem; }\n</style>"
        )

    def _simulate_bug_bounty(self, task):
        return (
            "Found it. You're storing passwords in plain text like it's 1995. "
            "Fix: Hash your stuff. Use Argon2. Stop being lazy."
        )
