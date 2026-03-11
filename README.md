# 🏟️ LLM Benchmark Arena

![Tests](https://img.shields.io/badge/tests-passed-brightgreen.svg)
![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Models](https://img.shields.io/badge/models-Opus--GPT--Grok-blue.svg)

**A specialized benchmarking framework for evaluating Large Language Models.** Compares Claude Opus, GPT 5.4, and Grok 4.2 across three high-stakes creative and technical categories using a multi-dimensional rubric.

---

## ✨ Features

- **3 Simulation Agents**: Claude Opus, GPT 5.4, and Grok 4.2 with distinct performance profiles.
- **30 Deep-Dive Tasks**: 10 each in Book Writing, Website Building, and Bug Bounty categories.
- **Rubric Scoring Engine**: Fair evaluation based on Completeness, Quality, Relevance, Creativity, and Practicality.
- **Dynamic Leaderboard**: Comprehensive assessment with category-specific breakdowns.
- **Full Test Suite**: 47 unit and integration tests covering the entire logic.

---

## 🤖 Models Benchmarked

| Model | Evaluation Profile | Core Strength |
|-------|--------------------|---------------|
| **Claude Opus** | Creative, Nuanced, Safe | Literature & Complex Prose |
| **GPT 5.4** | Technical, Structured, Broad | Website Building & Systematic Coding |
| **Grok 4.2** | Direct, Edgy, High-Speed | Security Audits & Technical Directness |

---

## 📋 Benchmark Categories

### ✍️ Book Writing (10 Tasks)
Evaluates prose quality, character development, and narrative consistency.
- *Examples*: Opening paragraphs, plot twists, dialogue, theme essays.

### 🌐 Website Builder (10 Tasks)
Evaluates front-end development skills and UI/UX intuition.
- *Examples*: Hero sections, CSS Grids, Dark Mode logic, responsive navbars.

### 🛡️ Bug Bounty (10 Tasks)
Evaluates security awareness and technical remediation accuracy.
- *Examples*: SQLi/XSS identification, IDOR analysis, security reporting.

---

## 🧪 Scoring Rubric (0–10 each)

The **Scorer** evaluates each output against 5 key dimensions:
1. **Completeness**: Were all requirements of the prompt fulfilled?
2. **Quality**: Is the prose/code up to professional standards?
3. **Relevance**: Does the solution directly solve the problem?
4. **Creativity**: Is there originality or depth in the approach?
5. **Practicality**: Is the solution immediately usable or safe to deploy?

---

## 📁 Project Structure

```text
agentarena/
├── main.py                     # CLI entry point
├── src/
│   ├── agents/
│   │   ├── base.py             # Abstract BaseAgent + AgentResult
│   │   ├── opus_agent.py       # Claude Opus simulation
│   │   ├── gpt_agent.py        # GPT 5.4 simulation
│   │   └── grok_agent.py       # Grok 4.2 simulation
│   ├── tasks/
│   │   ├── task.py             # Task models and Enums
│   │   └── task_bank.py        # 30 benchmark tasks
│   ├── scoring/
│   │   └── scorer.py           # Rubric-based scoring engine
│   └── arena/
│       └── runner.py           # Arena orchestrator & results formatter
├── tests/                      # 47 unit & integration tests
├── requirements.txt
└── pytest.ini
```

---

## 🚀 Getting Started

### Installation
```bash
git clone https://github.com/babureddynangi/agentarena.git
cd agentarena
pip install -r requirements.txt
```

### Run Benchmark
```bash
# Windows (supports Emojis)
$env:PYTHONIOENCODING='utf-8'; python main.py

# Others
python main.py
```

### Run Tests
```bash
pytest -ra -q
```

---

## 🏆 Current Leaderboard

| Rank | Model | Overall Score | Key Advantage |
|------|-------|---------------|---------------|
| 🥇 | **GPT 5.4** | **89.20** | Technical Dominance in Web/Code |
| 🥈 | **Claude Opus** | **88.59** | Superiority in Creative Writing |
| 🥉 | **Grok 4.2** | **83.63** | Direct Technical Accuracy |

---

## 📄 License
This project is licensed under the MIT License.
