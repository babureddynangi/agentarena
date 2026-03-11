from .base import BaseAgent, AgentResult


class LangChainAgent(BaseAgent):
    """LangChain Agent — Prototype Configuration."""

    def __init__(self):
        super().__init__(
            name="LangChain Agent",
            description="Deterministic ReAct loop simulation."
        )

    def solve(self, task) -> AgentResult:
        content = f"LangChain Agent: Entering ReAct loop for {task.category.value}\n"
        content += "Thought: I need to use the search tool.\n"
        content += "Execution: Calling Tool[Search]...\n"
        content += "Methodology: Zero-shot pattern matching.\n"
        content += "Final Answer: Information retrieved but lacks nuance."
        
        return AgentResult(content=content, metadata={"target_score_factor": 0.61})
