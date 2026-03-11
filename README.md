# 🏟️ LLM Benchmark Arena

![Tests](https://img.shields.io/badge/tests-passed-brightgreen.svg)
![Models](https://img.shields.io/badge/models-Opus--GPT--Grok-blue.svg)

**A specialized benchmarking framework for evaluating Large Language Models.** Compares Claude Opus, GPT 5.4, and Grok 4.2 across three high-stakes creative and technical categories.

---

## 🤖 Models Benchmarked

| Model | Profile | Primary Strength |
|-------|---------|------------------|
| **Claude Opus** | Creative & Nuanced | Book Writing & Literature |
| **GPT 5.4** | Technical & Structured | Website Building & Coding |
| **Grok 4.2** | Direct & Highly Technical | Bug Bounty & Security |

---

## 📋 30 Benchmark Tasks

### ✍️ Book Writing (10)
Opening paragraphs, character descriptions, plot twists, cliffhangers, and theme essays. Focused on prose quality and narrative depth.

### 🌐 Website Builder (10)
Landing pages, hero sections, responsive grids, dark mode toggles, and form validation. Focused on UI/UX and code functionality.

### 🛡️ Bug Bounty (10)
SQLi/XSS detection, IDOR vulnerability analysis, JWT security, and security report drafting. Focused on technical accuracy and remediation.

---

## 🧪 Scoring Rubric (0–10 each)

1. **Completeness**: Meets all prompt requirements.
2. **Quality**: Standard of writing or code implementation.
3. **Relevance**: Directly addresses the specific task.
4. **Creativity**: Originality and nuance in the solution.
5. **Practicality**: Real-world usability or safety.

---

## 🚀 Execution

```bash
# Set encoding for Windows emoji support
$env:PYTHONIOENCODING='utf-8'; python main.py
```

---

## 🏆 Sample Leaderboard

| Rank | Model | Overall Score |
|------|-------|---------------|
| 🥇 | **GPT 5.4** | **89.20** |
| 🥈 | **Claude Opus** | **88.59** |
| 🥉 | **Grok 4.2** | **83.63** |

---

## 📁 Project Structure

- `src/agents/`: Model-specific simulation agents.
- `src/tasks/`: 30 tasks for the 3 core categories.
- `src/scoring/`: Rubric-based evaluation engine.
- `src/arena/`: Orchestrator and leaderboard formatter.
