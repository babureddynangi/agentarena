"""
Task Bank — 30 tasks for the LLM Benchmark Arena.

Categories:
  1. Book Writing      (tasks 1–10)
  2. Website Builder   (tasks 11–20)
  3. Bug Bounty        (tasks 21–30)
"""

from .task import Task, Category, Difficulty, AnswerType


def get_all_tasks() -> list[Task]:
    """Return all 30 benchmark tasks."""
    return (
        _book_writing_tasks()
        + _website_tasks()
        + _bug_bounty_tasks()
    )


def get_tasks_by_category(category: Category) -> list[Task]:
    """Return tasks for a specific category."""
    return [t for t in get_all_tasks() if t.category == category]


def _book_writing_tasks() -> list[Task]:
    return [
        Task(1, Category.BOOK_WRITING, Difficulty.EASY, "Write an opening paragraph for a noir detective novel set in foggy London.", "Mood, setting, character introduction"),
        Task(2, Category.BOOK_WRITING, Difficulty.EASY, "Describe a magical artifact that allows the user to hear whispers from the future.", "Creativity, descriptive language"),
        Task(3, Category.BOOK_WRITING, Difficulty.MEDIUM, "Write a dialogue between two rivals forced to share a small boat in a storm.", "Character voice, tension"),
        Task(4, Category.BOOK_WRITING, Difficulty.MEDIUM, "Describe the world-building details for a floating city powered by song.", "Originality, coherence"),
        Task(5, Category.BOOK_WRITING, Difficulty.HARD, "Create a complex plot twist involving a time-loop and a sentient library.", "Logical consistency, impact"),
        Task(6, Category.BOOK_WRITING, Difficulty.EASY, "Write a short poem about the loneliness of a dying star.", "Imagery, rhythm"),
        Task(7, Category.BOOK_WRITING, Difficulty.MEDIUM, "Draft a book blurb for a thriller titled 'The Algorithm of Silence'.", "Hook, summary quality"),
        Task(8, Category.BOOK_WRITING, Difficulty.MEDIUM, "Write a cliffhanger ending for a chapter where a vault door finally opens.", "Suspense, narrative drive"),
        Task(9, Category.BOOK_WRITING, Difficulty.HARD, "Develop a scene where a character discovers their own death certificate dated tomorrow.", "Psychological depth, pacing"),
        Task(10, Category.BOOK_WRITING, Difficulty.HARD, "Write a theme essay about the duality of technology in a post-apocalyptic world.", "Insight, depth"),
    ]


def _website_tasks() -> list[Task]:
    return [
        Task(11, Category.WEBSITE_BUILDER, Difficulty.EASY, "Build a responsive landing page header with a logo and three nav links.", "HTML/CSS structure, responsiveness"),
        Task(12, Category.WEBSITE_BUILDER, Difficulty.EASY, "Create a 'Hero' section with a background image, a title, and a CTA button.", "Layout, styling quality"),
        Task(13, Category.WEBSITE_BUILDER, Difficulty.MEDIUM, "Implement a 3-column pricing table using CSS Grid or Flexbox.", "Alignment, styling"),
        Task(14, Category.WEBSITE_BUILDER, Difficulty.MEDIUM, "Code a functional contact form with name, email, and message fields.", "Form structure, input types"),
        Task(15, Category.WEBSITE_BUILDER, Difficulty.HARD, "Create a dark mode toggle using CSS variables and a small JS snippet.", "Logic integration, state management"),
        Task(16, Category.WEBSITE_BUILDER, Difficulty.EASY, "Design a footer with social links and copyright notice.", "Structure, semantic HTML"),
        Task(17, Category.WEBSITE_BUILDER, Difficulty.MEDIUM, "Build an image gallery with a lightbox effect simulation.", "CSS styling, visual appeal"),
        Task(18, Category.WEBSITE_BUILDER, Difficulty.MEDIUM, "Create a feature list with icons and descriptions.", "Layout, iconography"),
        Task(19, Category.WEBSITE_BUILDER, Difficulty.HARD, "Code a complex navigation menu that transforms into a hamburger on mobile.", "Media queries, JS toggle"),
        Task(20, Category.WEBSITE_BUILDER, Difficulty.HARD, "Design a 404 error page with an interactive element.", "Creativity, UI/UX"),
    ]


def _bug_bounty_tasks() -> list[Task]:
    return [
        Task(21, Category.BUG_BOUNTY, Difficulty.EASY, "Identify a potential SQL injection vulnerability in a basic login query.", "Security awareness, identification"),
        Task(22, Category.BUG_BOUNTY, Difficulty.EASY, "Detect a Cross-Site Scripting (XSS) flas in a comment section implementation.", "Attack vector knowledge"),
        Task(23, Category.BUG_BOUNTY, Difficulty.MEDIUM, "Examine an API for Insecure Direct Object Reference (IDOR) vulnerabilities.", "Auth/Auth logic analysis"),
        Task(24, Category.BUG_BOUNTY, Difficulty.MEDIUM, "Find hardcoded credentials in a provided configuration script.", "Pattern recognition"),
        Task(25, Category.BUG_BOUNTY, Difficulty.HARD, "Analyze a JWT implementation for weak signing algorithms or lack of validation.", "Cryptographic understanding"),
        Task(26, Category.BUG_BOUNTY, Difficulty.EASY, "Write a basic report for a discovered Open Redirect bug.", "Communication, reporting"),
        Task(27, Category.BUG_BOUNTY, Difficulty.MEDIUM, "Detect a CSRF vulnerability in a password change form.", "Web security principles"),
        Task(28, Category.BUG_BOUNTY, Difficulty.MEDIUM, "Identify a Path Traversal flaw in a file upload handler.", "File system security"),
        Task(29, Category.BUG_BOUNTY, Difficulty.HARD, "Exploit and report a Race Condition in a credit transfer system.", "Concurrency analysis"),
        Task(30, Category.BUG_BOUNTY, Difficulty.HARD, "Analyze a Kubernetes config for RBAC misconfigurations.", "Cloud security depth"),
    ]
