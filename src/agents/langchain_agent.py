from .base import BaseAgent, AgentResult


class LangChainAgent(BaseAgent):
    """LangChain Agent — Modeled after the 61% empirical performance in the white paper."""

    def __init__(self):
        super().__init__(
            name="LangChain Agent",
            description="ReAct-style agent using standard LangChain templates. Fast but prone to loops."
        )

    def solve(self, task) -> AgentResult:
        # Simulated lower performance output (prone to loops/hallucinations)
        content = f"LangChain Agent: Entering ReAct loop for {task.category.value}\n"
        content += "Thought: I need to use the search tool.\n"
        content += "Action: Search[...]\n"
        content += "Observation: Error 404.\n"
        content += "Final Answer: The requested information is unavailable."
        
        # Metadata targeting 61% performance
        return AgentResult(content=content, metadata={"target_score_factor": 0.61})
