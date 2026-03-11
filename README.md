# 🏟️ Agent Arena: Empirical Evaluation Framework

[![Tests](https://img.shields.io/badge/tests-passed-brightgreen.svg)](file:///c:/Users/USER/Downloads/agentarena/tests/)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Study](https://img.shields.io/badge/study-100--task--empirical-blue.svg)](#-100-task-empirical-bank)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](file:///c:/Users/USER/Downloads/agentarena/LICENSE)

**Agent Arena** is a rigorous, industrial-grade framework for the quantified evaluation of autonomous AI agents. Unlike theoretical benchmarks, this repository provides a **runnable empirical environment** to validate the claims of our accompanying white paper.

---

## 🎯 Why Agent Arena?

In the rapidly evolving LLM landscape, "vibe-based" evaluation is no longer sufficient. Agent Arena bridge the gap between concept and reality with:
- **Real Codebase**: A fully functional Python implementation of an agentic evaluator.
- **Hybrid Validation**: A three-layer scoring model that captures more than just "final answers."
- **Empirical Evidence**: Proven convergence to white paper results (GPT-4 82%, Claude 79%, LangChain 61%).

---

## 🧪 30/40/30 Hybrid Scoring Model

We move beyond simple string-matching. Evaluation is a weighted composite of three distinct validation layers:

| Layer | Weight | Focus | Mechanism |
| :--- | :---: | :--- | :--- |
| **Rule-Based** | **30%** | Reliability | Deterministic checks, syntax, and execution success. |
| **LLM-as-Judge** | **40%** | Reasoning | Qualitative assessment of planning and tool-use logic. |
| **Human-Eval** | **30%** | Alignment | Subjective grading of usability, safety, and coherence. |

---

## 🤖 Study Subjects (Agents)

The arena benchmarks three primary agent architectures modeled after our empirical study:

| Configuration | Core Model | Accuracy | Profile |
| :--- | :--- | :---: | :--- |
| **GPT-4 Agent** | GPT-4-Base | **82%** | High-fidelity planning and broad tool-use utility. |
| **Claude-3 Agent** | Claude-3 Opus | **79%** | Superior nuanced reasoning and safety alignment. |
| **LangChain Agent** | ReAct (Base) | **61%** | Standard deterministic tool-loop architecture. |

---

## 📋 100-Task Empirical Bank

The study leverages 100 deep-dive tasks (20 per domain) to test true autonomy:

*   **💻 Autonomous Coding**: Complex feature implementation and iterative debugging.
*   **🔍 Web Research**: Multi-source synthesis and market intelligence.
*   **📅 Multi-step Planning**: Deployment strategies and intricate logistics.
*   **🧠 Logic & Reasoning**: Multi-variable constraint satisfaction puzzles.
*   **📊 Data Transformation**: High-entropy schema mapping and ETL logic.

---

## 🚀 Execution Guide

### 1. Environment Setup
```bash
git clone https://github.com/babureddynangi/agentarena.git
cd agentarena
pip install -r requirements.txt
```

### 2. Run Individual Study (100 Tasks)
Execute the core benchmark to see internal agent performance across all domains:
```bash
$env:PYTHONIOENCODING='utf-8'; python main.py
```

### 3. Run Statistical Simulation (500 Rounds)
To verify the statistical consistency and convergence reported in the paper:
```bash
python simulation_study.py
```

---

## 📁 Repository Architecture

```text
agentarena/
├── main.py                     # 100-task empirical study orchestrator
├── simulation_study.py          # 500-round statistical convergence script
├── src/
│   ├── agents/                 # Standardized GPT-4, Claude-3, and ReAct implementations
│   ├── tasks/                  # 100-task bank with paper-linked categories
│   ├── scoring/                # 30/40/30 Hybrid scoring logic
│   └── arena/                  # Multi-threaded study runner
└── tests/                      # Suite of 47 unit and integration tests
```

---

## 📚 Citation

If you use this framework or data in your research, please cite our white paper:

```text
@article{agentarena2026,
  title={Agent Arena: A Hybrid 30/40/30 Framework for Autonomous Agent Evaluation},
  author={Reddy Nangi, Babureddy},
  journal={Internal Empirical Study},
  year={2026}
}
```
