# 🏟️ Agent Arena — Empirical Evaluation Framework

![Tests](https://img.shields.io/badge/tests-passed-brightgreen.svg)
![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Study](https://img.shields.io/badge/study-100--task--empirical-blue.svg)

**Agent Arena is a specialized framework for the rigorous evaluation of autonomous AI agents.** This repository implements the testing strategy described in our white paper, featuring a hybrid scoring model and a 100-task empirical study across 5 autonomous domains.

---

## 🧪 30/40/30 Hybrid Scoring Model

Evaluation is conducted using a weighted composite of three independent validation layers:

1.  **Rule-Based (30%)**: Deterministic checks for syntax, execution success, and final answer accuracy.
2.  **LLM-as-Judge (40%)**: Qualitative assessment of reasoning coherence, planning efficiency, and tool-use logic.
3.  **Human Feedback (30%)**: Subjective evaluation of output usability, safety, and instructional alignment.

---

## 🤖 Study Subjects (Agents)

The arena benchmarks three core agent configurations as analyzed in the manuscript:

| Configuration | Study Model | Paper Accuracy | Implementation Profile |
|---------------|-------------|----------------|------------------------|
| **GPT-4 Agent** | GPT-4-Base | **82%** | High-fidelity planning and tool use |
| **Claude-3 Agent** | Claude-3 Opus | **79%** | Nuanced reasoning and safety |
| **LangChain Agent** | ReAct (Base) | **61%** | Standard tool-loop architecture |

---

## 📋 100-Task Empirical Bank

The study spans 100 tasks (20 per domain) designed to test agentic autonomy:

- **Autonomous Coding**: End-to-end feature implementation and debugging.
- **Web Research**: Multi-source synthesis and market analysis.
- **Multi-step Planning**: Deployment strategies and complex logistics.
- **Logic & Reasoning**: Multi-variable constraint satisfaction.
- **Data Transformation**: Complex schema mapping and ETL logic.

---

## 🚀 Execution

### Installation
```bash
git clone https://github.com/babureddynangi/agentarena.git
cd agentarena
pip install -r requirements.txt
```

### Run Empirical Study (100 Tasks)
```bash
$env:PYTHONIOENCODING='utf-8'; python main.py
```

### Run Statistical Simulation (500 Rounds)
```bash
python simulation_study.py
```

---

## 📁 Project Structure

```text
agentarena/
├── main.py                     # 100-task empirical study runner
├── simulation_study.py          # 500-round statistical analysis script
├── src/
│   ├── agents/                 # GPT-4, Claude-3, and ReAct agent logic
│   ├── tasks/                  # 100-task bank + paper-aligned categories
│   ├── scoring/                # 30/40/30 Hybrid Scoring Engine
│   └── arena/                  # Study orchestrator
└── tests/                      # Validation suite (47 tests)
```
