# Agent Arena

A prototype evaluation framework for benchmarking autonomous AI agents across structured tasks. Current public release includes simulated agent profiles, rubric-based scoring, and a leaderboard prototype for early framework validation.

**Status**
- **Framework maturity:** Prototype
- **Evaluation mode:** Simulated / Hybrid prototype
- **Public task count:** 100
- **Public agents:** 3 (GPT-4, Claude-3, LangChain)
- **Paper alignment:** v1.0 synced with manuscript dated March 2026

---

> [!CAUTION]
> **Purpose:** Early validation of the Agent Arena benchmark architecture, **not a final production benchmark**. Current results are simulated to demonstrate framework design and statistical convergence properties as described in the accompanying white paper.

---

## 🧪 30/40/30 Hybrid Scoring Model

The Agent Arena framework implements a three-layer validation stack to quantify agentic capability:

1.  **Rule-Based (30%)**: Deterministic checks for structural markers and task constraints.
2.  **Sim-Judge (40%)**: Qualitative reasoning depth simulated via calibrated performance profiles. Models the logical coherence and tool-selection accuracy described in the paper.
3.  **Sim-Human (30%)**: Modeled subjective utility and instructional alignment. Simulates end-user satisfaction and safety constraint adherence based on stochastic utility functions.

---

## 🤖 Benchmark Subjects

| Agent Configuration | Target benchmark score | Implementation Profile |
| :--- | :---: | :--- |
| **GPT-4 Agent Prototype** | **82%** | High-fidelity planning and broad tool-use utility. |
| **Claude-3 Agent Prototype** | **79%** | Superior nuanced reasoning and safety alignment. |
| **LangChain Agent Prototype** | **61%** | Standard deterministic tool-loop architecture. |

---

## 📋 100-Task Evaluation Bank (Simulated)

The study leverages 100 tasks across 5 autonomous domains:
- **Autonomous Coding**: Feature implementation and iterative debugging.
- **Web Research**: Multi-source synthesis and market intelligence.
- **Multi-step Planning**: Deployment strategies and intricate logistics.
- **Logic & Reasoning**: Multi-variable constraint satisfaction puzzles.
- **Data Transformation**: High-entropy schema mapping and ETL logic.

---

## 📊 Prototype Leaderboard (Simulation Evidence)

The following scores reflect the statistical convergence of the prototype engine across multi-round simulations:

| Rank | Model | Overall Score | Convergence Profile |
| :--- | :--- | :---: | :--- |
| 🥇 | **GPT-4 Agent** | **82%** | Aligned with paper prototype findings |
| 🥈 | **Claude-3 Agent** | **79%** | Aligned with paper prototype findings |
| 🥉 | **LangChain Agent** | **61%** | Aligned with paper prototype findings |

---

## 🧬 Reproducibility Section

To replicate the simulation study results:
1.  **Task Bank**: Ensure `src/tasks/task_bank.py` generates 100 tasks (20 per domain).
2.  **Scoring Formula**: `Overall = (Rule * 0.3) + (Judge * 0.4) + (Human * 0.3)`.
3.  **Agent Configs**: Use the `target_score_factor` metadata in `src/agents/` (0.82, 0.79, 0.61).
4.  **Execution**: Run `python simulation_study.py`.

---

## 📁 Repository Structure

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

## 📚 Citation & Paper Alignment

For detailed methodology, see [PAPER_ALIGNMENT.md](PAPER_ALIGNMENT.md).

```text
@article{agentarena_prototype_2026,
  title={Agent Arena: A Framework Prototype for Autonomous Agent Evaluation},
  author={Reddy Nangi, Babureddy},
  year={2026}
}
```
