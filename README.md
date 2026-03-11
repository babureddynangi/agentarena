# 🏟️ Agent Arena

![Project Badge](https://img.shields.io/badge/project-agentarena-blue.svg)
![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Tests](https://img.shields.io/badge/tests-47%20passed-brightgreen.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

**A modular framework for developing, testing, and evaluating AI agents.** Three agents compete on 30 tasks across 5 categories, scored on accuracy, speed, and efficiency.

---

## ✨ Features

- **3 Distinct Agents** with different problem-solving strategies
- **30 Tasks** across 5 categories (Math, Text, Code, Reasoning, Knowledge)
- **Weighted Scoring** — Accuracy (60%), Speed (25%), Efficiency (15%)
- **Formatted Leaderboard** with category breakdowns and task-by-task results
- **47 Unit & Integration Tests** via pytest
- **Self-contained** — no API keys required

---

## 🤖 Agents

| Agent | Strategy | Strengths | Trade-offs |
|-------|----------|-----------|------------|
| **ReAct Agent** | Thought → Action → Observation loop with tools (calculator, string ops, knowledge lookup) | Most accurate on complex multi-step tasks | Slowest, most steps |
| **Chain-of-Thought Agent** | Structured "let me think step by step" reasoning | Good accuracy on reasoning tasks | Moderate speed |
| **Direct Agent** | Pattern matching and heuristics for immediate answers | Fastest execution | Least accurate on hard tasks |

---

## 📋 30 Tasks

| Category | Tasks | Difficulty | Examples |
|----------|-------|------------|---------|
| **Math & Logic** | 1–6 | 2E / 2M / 2H | Sum, product, factorial, sqrt, Fibonacci, prime counting |
| **Text Processing** | 7–12 | 2E / 2M / 2H | Word count, uppercase, vowels, reverse, unique words, palindrome |
| **Code Understanding** | 13–18 | 2E / 2M / 2H | Python output prediction (arithmetic, recursion, list comprehensions) |
| **Reasoning** | 19–24 | 2E / 2M / 2H | Day calculations, syllogisms, bat-and-ball, widget puzzles |
| **Knowledge & Trivia** | 25–30 | 2E / 2M / 2H | Chemical symbols, capitals, planets, Python creator, Moon landing |

---

## 📁 Project Structure

```
agentarena/
├── main.py                     # CLI entry point
├── src/
│   ├── agents/
│   │   ├── base.py             # BaseAgent + AgentResult
│   │   ├── react_agent.py      # ReAct Agent (tool-use)
│   │   ├── cot_agent.py        # Chain-of-Thought Agent
│   │   └── direct_agent.py     # Direct Agent (zero-shot)
│   ├── tasks/
│   │   ├── task.py             # Task model + enums
│   │   └── task_bank.py        # 30 task definitions
│   ├── scoring/
│   │   └── scorer.py           # Scoring engine
│   └── arena/
│       └── runner.py           # Arena orchestrator + leaderboard
├── tests/
│   ├── test_agents.py          # Agent unit tests
│   ├── test_tasks.py           # Task bank validation
│   ├── test_scoring.py         # Scoring engine tests
│   └── test_arena.py           # Integration tests
├── docs/
│   ├── QUICKSTART.md
│   └── ARCHITECTURE.md
├── requirements.txt
└── pytest.ini
```

---

## 🚀 Installation

```bash
git clone https://github.com/babureddynangi/agentarena.git
cd agentarena
pip install -r requirements.txt
```

---

## ▶️ Usage

### Run the Arena

```bash
python main.py
```

This runs all 3 agents against all 30 tasks and outputs a formatted leaderboard.

> **Windows note:** If you see encoding errors with emojis, run with:
> ```powershell
> $env:PYTHONIOENCODING='utf-8'; python main.py
> ```

### Run Tests

```bash
pytest -ra -q
```

---

## 🏆 Sample Results

```
                    AGENT ARENA — FINAL LEADERBOARD

  🥇  Direct Agent            — 71.45 / 100  (24/30 correct)
  🥈  Chain-of-Thought Agent  — 70.29 / 100  (28/30 correct)
  🥉  ReAct Agent             — 56.00 / 100  (28/30 correct)
```

> Direct Agent wins overall due to speed and efficiency bonuses despite lower accuracy.
> ReAct and CoT are more accurate (28/30) but slower with more reasoning steps.

---

## 🧪 Scoring System

| Metric | Weight | How It Works |
|--------|--------|-------------|
| **Accuracy** | 60% | Exact match, numeric tolerance, substring, or multiple-choice |
| **Speed** | 25% | Fastest agent per task gets 100, others scaled relative to slowest |
| **Efficiency** | 15% | Fewer reasoning steps = higher score |

---

## 🤝 Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for guidelines on how to contribute.

---

## 📄 License

This project is open source and available under the MIT License.