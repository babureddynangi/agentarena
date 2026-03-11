# 🏟️ Agent Arena: Framework Prototype & Simulation

[![Tests](https://img.shields.io/badge/tests-passed-brightgreen.svg)](file:///c:/Users/USER/Downloads/agentarena/tests/)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/status-prototype--simulation-orange.svg)](#-simulation-reproducibility)

**Agent Arena** is a specialized framework prototype for the rigorous evaluation of autonomous AI agents. This repository implements the **Agent Arena Evaluation Strategy**, featuring a structural hybrid scorer and a 100-task simulation study across 5 domains.

> [!IMPORTANT]
> **Prototype Disclaimer**: This repository contains a **simulation environment** used to validate the evaluation methodology and scoring strategies. The results presented are derived from **prototype agents** with calibrated performance profiles, not live production logs.

---

## 🧪 30/40/30 Hybrid Scoring Model (Structural Prototype)

Evaluation is conducted using a weighted composite of three independent validation layers implemented in the `AgentArenaScorer`:

| Layer | Weight | Mechanism | Purpose |
| :--- | :---: | :--- | :--- |
| **Rule-Based** | **30%** | **Pattern Matching** | Hard structural checks for markers like `Methodology:`, `Execution:`, and `Confidence:`. |
| **Sim-Judge** | **40%** | **Calibration Profile** | Qualitative reasoning depth simulated based on the agent's target accuracy factor. |
| **Sim-Human** | **30%** | **Stochastic Utility** | Simulated subjective alignment and usability scores with modeled variance. |

---

## 🤖 Subject Configurations (Model Profiles)

The prototype benchmarks three core agent configurations with calibrated performance factors:

1.  **GPT-4 Agent Prototype** (Target: **82%**): Calibrated for high-fidelity structural planning.
2.  **Claude-3 Agent Prototype** (Target: **79%**): Calibrated for nuanced reasoning and safety markers.
3.  **LangChain Agent Prototype** (Target: **61%**): Calibrated for deterministic ReAct loop patterns.

---

## 🧬 Simulation Reproducibility

To ensure the framework's behavior is deterministic and verifiable, the following parameters are used:

- **Task Count**: 100 tasks (20 per domain: Coding, Research, Planning, Logic, Data).
- **Weighting Formula**: `overall = (rule * 0.3) + (judge * 0.4) + (human * 0.3)`.
- **Structural Markers**: Agents must emit `Methodology:`, `Execution:`, and `Confidence:` blocks to satisfy Rule-Based scoring.
- **Convergence**: Leaderboard scores are generated across 100 simulation rounds in `simulation_study.py` to demonstrate statistical stability.

---

## 🚀 Execution Guide

### 1. Environment Setup
```bash
git clone https://github.com/babureddynangi/agentarena.git
cd agentarena
pip install -r requirements.txt
```

### 2. Run Single Simulation (100 Tasks)
```bash
$env:PYTHONIOENCODING='utf-8'; python main.py
```

### 3. Run Statistical Convergence Study (100 Rounds)
```bash
python simulation_study.py
```

---

## 📁 Repository Architecture

```text
agentarena/
├── main.py                     # Single-run framework orchestrator
├── simulation_study.py          # Multi-round statistical convergence tool
├── src/
│   ├── agents/                 # Calibrated Gpt4, Claude3, and LangChain prototypes
│   ├── tasks/                  # 100-task simulation bank
│   ├── scoring/                # AgentArenaScorer (Structural Hybrid Logic)
│   └── arena/                  # Study runner and leaderboard formatter
└── tests/                      # Suite of unit and integration tests
```

---

## 📚 Citation

```text
@article{agentarena_prototype_2026,
  title={Agent Arena: A Framework Prototype for Autonomous Agent Evaluation},
  author={Reddy Nangi, Babureddy},
  year={2026}
}
```
