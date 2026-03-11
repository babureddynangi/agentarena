"""
Claude Opus Agent — Creative, nuanced, and safe.
"""

from .base import BaseAgent, AgentResult


class OpusAgent(BaseAgent):
    """Claude Opus simulated agent."""

    def __init__(self):
        super().__init__(
            name="Claude Opus",
            description="Creative, nuanced, and safe. Excels at high-stakes reasoning and literature."
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
            content = "Simulated Opus response."

        return AgentResult(content=content)

    def _simulate_book_writing(self, task):
        return (
            "The fog clung to the cobblestones like a forgotten memory, cold and damp. "
            "Elias pulled his collar tighter, the scent of parched parchment and damp copper "
            "filling his lungs. London was a city of secrets, but even the stones seemed to weep "
            "tonight as the clock at St. Jude's chattered its rhythmic warning into the void."
        )

    def _simulate_website_builder(self, task):
        return (
            "<!DOCTYPE html>\n<html>\n<head>\n<style>\n"
            "body { font-family: 'Inter', sans-serif; background: #fafafa; }\n"
            ".container { max-width: 1200px; margin: 0 auto; }\n"
            "</style>\n</head>\n<body>\n"
            "<nav>Menu</nav>\n<main>Welcome to the Opus Page</main>\n"
            "</body>\n</html>"
        )

    def _simulate_bug_bounty(self, task):
        return (
            "Analysis: The endpoint /api/user/profile is vulnerable to IDOR. "
            "Recommendation: Ensure that the session user ID matches the requested resource ID."
        )
