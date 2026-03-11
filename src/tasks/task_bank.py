"""
Task Bank — 100 empirical tasks aligned with the White Paper.
Domains: Coding, Research, Planning, Logic, Data (20 tasks each).
"""

from .task import Task, Category, Difficulty, AnswerType


def get_all_tasks() -> list[Task]:
    """Return 100 benchmark tasks."""
    tasks = []
    
    # Generate 20 tasks per category
    categories = [
        (Category.CODING, "Implement a {feat} in Python using {lib}."),
        (Category.RESEARCH, "Analyze the market trends for {field} in 2024."),
        (Category.PLANNING, "Develop a 5-step deployment plan for a {app}."),
        (Category.LOGIC, "Solve the complex logic puzzle involving {count} variables."),
        (Category.DATA, "Transform the raw {fmt} data into a structured JSON schema.")
    ]
    
    task_id = 1
    for cat, template in categories:
        for i in range(20):
            diff = Difficulty.EASY if i < 6 else (Difficulty.MEDIUM if i < 14 else Difficulty.HARD)
            
            # Simulated specific prompt
            question = template.format(
                feat=f"feature_{i}", lib="standard libraries", field=f"sector_{i}", 
                app=f"microservice_{i}", count=i+2, fmt="CSV"
            )
            
            tasks.append(
                Task(
                    id=task_id,
                    category=cat,
                    difficulty=diff,
                    question=question,
                    expected_answer=f"Criteria for task {task_id}",
                    answer_type=AnswerType.HYBRID
                )
            )
            task_id += 1
            
    return tasks


def get_tasks_by_category(category: Category) -> list[Task]:
    """Return tasks for a specific category."""
    return [t for t in get_all_tasks() if t.category == category]
