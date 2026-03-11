"""
Task Bank — 30 tasks across 5 categories for the Agent Arena.

Categories:
  1. Math & Logic        (tasks 1–6)
  2. Text Processing     (tasks 7–12)
  3. Code Understanding  (tasks 13–18)
  4. Reasoning           (tasks 19–24)
  5. Knowledge & Trivia  (tasks 25–30)

Each category has 2 easy, 2 medium, and 2 hard tasks.
"""

from .task import Task, Category, Difficulty, AnswerType


def get_all_tasks() -> list[Task]:
    """Return all 30 tasks."""
    return (
        _math_tasks()
        + _text_tasks()
        + _code_tasks()
        + _reasoning_tasks()
        + _knowledge_tasks()
    )


def get_tasks_by_category(category: Category) -> list[Task]:
    """Return tasks for a specific category."""
    return [t for t in get_all_tasks() if t.category == category]


# ═══════════════════════════════════════════════════════════════════
# Category 1: Math & Logic
# ═══════════════════════════════════════════════════════════════════

def _math_tasks() -> list[Task]:
    return [
        Task(
            id=1,
            category=Category.MATH_LOGIC,
            difficulty=Difficulty.EASY,
            question="What is the sum of 15 and 27?",
            expected_answer="42",
            answer_type=AnswerType.NUMERIC,
        ),
        Task(
            id=2,
            category=Category.MATH_LOGIC,
            difficulty=Difficulty.EASY,
            question="What is the product of 8 and 7?",
            expected_answer="56",
            answer_type=AnswerType.NUMERIC,
        ),
        Task(
            id=3,
            category=Category.MATH_LOGIC,
            difficulty=Difficulty.MEDIUM,
            question="What is the factorial of 6?",
            expected_answer="720",
            answer_type=AnswerType.NUMERIC,
        ),
        Task(
            id=4,
            category=Category.MATH_LOGIC,
            difficulty=Difficulty.MEDIUM,
            question="What is the square root of 144?",
            expected_answer="12",
            answer_type=AnswerType.NUMERIC,
        ),
        Task(
            id=5,
            category=Category.MATH_LOGIC,
            difficulty=Difficulty.HARD,
            question="What is the 10th number in the Fibonacci sequence? (1, 1, 2, 3, 5, ...)",
            expected_answer="55",
            answer_type=AnswerType.NUMERIC,
        ),
        Task(
            id=6,
            category=Category.MATH_LOGIC,
            difficulty=Difficulty.HARD,
            question="How many prime numbers are there between 1 and 50?",
            expected_answer="15",
            answer_type=AnswerType.NUMERIC,
        ),
    ]


# ═══════════════════════════════════════════════════════════════════
# Category 2: Text Processing
# ═══════════════════════════════════════════════════════════════════

def _text_tasks() -> list[Task]:
    return [
        Task(
            id=7,
            category=Category.TEXT_PROCESSING,
            difficulty=Difficulty.EASY,
            question='How many words are in the sentence "The quick brown fox jumps over the lazy dog"?',
            expected_answer="9",
            answer_type=AnswerType.NUMERIC,
        ),
        Task(
            id=8,
            category=Category.TEXT_PROCESSING,
            difficulty=Difficulty.EASY,
            question='Convert the following to uppercase: "hello world"',
            expected_answer="HELLO WORLD",
            answer_type=AnswerType.EXACT,
        ),
        Task(
            id=9,
            category=Category.TEXT_PROCESSING,
            difficulty=Difficulty.MEDIUM,
            question='How many vowels are in the word "extraordinary"?',
            expected_answer="6",
            answer_type=AnswerType.NUMERIC,
        ),
        Task(
            id=10,
            category=Category.TEXT_PROCESSING,
            difficulty=Difficulty.MEDIUM,
            question='Reverse the characters in the string "Python"',
            expected_answer="nohtyP",
            answer_type=AnswerType.EXACT,
        ),
        Task(
            id=11,
            category=Category.TEXT_PROCESSING,
            difficulty=Difficulty.HARD,
            question='How many unique words are in "the cat sat on the mat and the cat played on the mat"?',
            expected_answer="7",
            answer_type=AnswerType.NUMERIC,
        ),
        Task(
            id=12,
            category=Category.TEXT_PROCESSING,
            difficulty=Difficulty.HARD,
            question='Is "racecar" a palindrome? Answer Yes or No.',
            expected_answer="Yes",
            answer_type=AnswerType.EXACT,
            acceptable_answers=["Yes", "yes", "YES"],
        ),
    ]


# ═══════════════════════════════════════════════════════════════════
# Category 3: Code Understanding
# ═══════════════════════════════════════════════════════════════════

def _code_tasks() -> list[Task]:
    return [
        Task(
            id=13,
            category=Category.CODE_UNDERSTANDING,
            difficulty=Difficulty.EASY,
            question='What is the output of the following Python code?\n```python\nprint(3 + 4)\n```',
            expected_answer="7",
            answer_type=AnswerType.NUMERIC,
        ),
        Task(
            id=14,
            category=Category.CODE_UNDERSTANDING,
            difficulty=Difficulty.EASY,
            question='What is the output of the following Python code?\n```python\nprint(len("hello"))\n```',
            expected_answer="5",
            answer_type=AnswerType.NUMERIC,
        ),
        Task(
            id=15,
            category=Category.CODE_UNDERSTANDING,
            difficulty=Difficulty.MEDIUM,
            question='What is the output of the following Python code?\n```python\nx = [1, 2, 3, 4, 5]\nprint(sum(x))\n```',
            expected_answer="15",
            answer_type=AnswerType.NUMERIC,
        ),
        Task(
            id=16,
            category=Category.CODE_UNDERSTANDING,
            difficulty=Difficulty.MEDIUM,
            question='What is the output of the following Python code?\n```python\ndef factorial(n):\n    if n <= 1:\n        return 1\n    return n * factorial(n - 1)\nprint(factorial(5))\n```',
            expected_answer="120",
            answer_type=AnswerType.NUMERIC,
        ),
        Task(
            id=17,
            category=Category.CODE_UNDERSTANDING,
            difficulty=Difficulty.HARD,
            question='What is the output of the following Python code?\n```python\nresult = [x**2 for x in range(1, 6)]\nprint(sum(result))\n```',
            expected_answer="55",
            answer_type=AnswerType.NUMERIC,
        ),
        Task(
            id=18,
            category=Category.CODE_UNDERSTANDING,
            difficulty=Difficulty.HARD,
            question='What is the output of the following Python code?\n```python\ndef fib(n):\n    a, b = 0, 1\n    for _ in range(n):\n        a, b = b, a + b\n    return a\nprint(fib(8))\n```',
            expected_answer="21",
            answer_type=AnswerType.NUMERIC,
        ),
    ]


# ═══════════════════════════════════════════════════════════════════
# Category 4: Reasoning & Common Sense
# ═══════════════════════════════════════════════════════════════════

def _reasoning_tasks() -> list[Task]:
    return [
        Task(
            id=19,
            category=Category.REASONING,
            difficulty=Difficulty.EASY,
            question="If today is Monday, what day will it be after 3 days?",
            expected_answer="Thursday",
            answer_type=AnswerType.EXACT,
        ),
        Task(
            id=20,
            category=Category.REASONING,
            difficulty=Difficulty.EASY,
            question="If today is Friday, what day was it 2 days before?",
            expected_answer="Wednesday",
            answer_type=AnswerType.EXACT,
        ),
        Task(
            id=21,
            category=Category.REASONING,
            difficulty=Difficulty.MEDIUM,
            question="All roses are flowers. All flowers need water. Do roses need water? Answer Yes or No.",
            expected_answer="Yes",
            answer_type=AnswerType.EXACT,
            acceptable_answers=["Yes", "yes", "YES"],
        ),
        Task(
            id=22,
            category=Category.REASONING,
            difficulty=Difficulty.MEDIUM,
            question="If today is Wednesday, what day will it be after 10 days?",
            expected_answer="Saturday",
            answer_type=AnswerType.EXACT,
        ),
        Task(
            id=23,
            category=Category.REASONING,
            difficulty=Difficulty.HARD,
            question="A bat and a ball cost $1.10 in total. The bat costs $1.00 more than the ball. How much does the ball cost in cents?",
            expected_answer="5",
            answer_type=AnswerType.NUMERIC,
        ),
        Task(
            id=24,
            category=Category.REASONING,
            difficulty=Difficulty.HARD,
            question="If it takes 5 machines 5 minutes to make 5 widgets, how many minutes would it take 100 machines to make 100 widgets?",
            expected_answer="5",
            answer_type=AnswerType.NUMERIC,
        ),
    ]


# ═══════════════════════════════════════════════════════════════════
# Category 5: Knowledge & Trivia
# ═══════════════════════════════════════════════════════════════════

def _knowledge_tasks() -> list[Task]:
    return [
        Task(
            id=25,
            category=Category.KNOWLEDGE,
            difficulty=Difficulty.EASY,
            question="What is the chemical symbol for water?",
            expected_answer="H2O",
            answer_type=AnswerType.EXACT,
        ),
        Task(
            id=26,
            category=Category.KNOWLEDGE,
            difficulty=Difficulty.EASY,
            question="What is the largest planet in our solar system?",
            expected_answer="Jupiter",
            answer_type=AnswerType.EXACT,
        ),
        Task(
            id=27,
            category=Category.KNOWLEDGE,
            difficulty=Difficulty.MEDIUM,
            question="What is the chemical symbol for gold?",
            expected_answer="Au",
            answer_type=AnswerType.EXACT,
        ),
        Task(
            id=28,
            category=Category.KNOWLEDGE,
            difficulty=Difficulty.MEDIUM,
            question="What is the capital of Japan?",
            expected_answer="Tokyo",
            answer_type=AnswerType.EXACT,
        ),
        Task(
            id=29,
            category=Category.KNOWLEDGE,
            difficulty=Difficulty.HARD,
            question="Who created the Python programming language?",
            expected_answer="Guido van Rossum",
            answer_type=AnswerType.CONTAINS,
        ),
        Task(
            id=30,
            category=Category.KNOWLEDGE,
            difficulty=Difficulty.HARD,
            question="In what year did the first Moon landing occur?",
            expected_answer="1969",
            answer_type=AnswerType.EXACT,
        ),
    ]
