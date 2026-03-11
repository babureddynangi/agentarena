# Agent Arena

A prototype evaluation framework for benchmarking autonomous AI agents across structured tasks. Current public release includes simulated agent profiles, rubric-based scoring, and a leaderboard prototype for early framework validation.

**Status**
- **Framework maturity:** Prototype
- **Evaluation mode:** Simulated / Hybrid prototype
- **Public task count:** 100
- **Public agents:** 3 (GPT-4o, Claude 3.5 Sonnet, Llama 3.1 70B)
- **Paper alignment:** v1.0 synced with manuscript dated March 2026

---

> [!CAUTION]
> **Purpose:** Early validation of the Agent Arena benchmark architecture, **not a final production benchmark**. Current results validate framework mechanics via calibrated simulation; live deployment study planned for Q3 2026.

---

## 🧪 30/40/30 Hybrid Scoring Model

The Agent Arena framework implements a three-layer validation stack to quantify agentic capability:

1.  **Rule-Based (30%)**: Deterministic checks for structural markers and task constraints.
2.  **Sim-Judge (40%)**: Qualitative reasoning depth simulated via calibrated performance profiles. Models the logical coherence and tool-selection accuracy described in the paper.
3.  **Sim-Human (30%)**: Modeled subjective utility and instructional alignment. Simulates end-user satisfaction and safety constraint adherence based on stochastic utility functions.

---

## 🤖 Benchmark Subjects

**Table 1: Simulated Benchmark Subjects and Target Scores**
| Agent Configuration | Target benchmark score | Implementation Profile |
| :--- | :---: | :--- |
| **GPT-4o Agent** | **82%** | High-fidelity planning and broad tool-use utility. |
| **Claude 3.5 Sonnet Agent** | **79%** | Superior nuanced reasoning and safety alignment. |
| **Llama 3.1 70B Agent** | **61%** | Standard deterministic tool-loop architecture. |

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

**Table 2: Statistical Convergence Leaderboard (Simulation Evidence)**
| Rank | Model | Overall Score | Convergence Profile |
| :--- | :--- | :---: | :--- |
| 🥇 | **GPT-4o Agent** | **82%** | Aligned with paper prototype findings |
| 🥈 | **Claude 3.5 Sonnet Agent** | **79%** | Aligned with paper prototype findings |
| 🥉 | **Llama 3.1 70B Agent** | **61%** | Aligned with paper prototype findings |

---

## ⚙️ Technical Implementation Details (Simulation Environment)

To support the evaluation architecture described in the paper, this simulation enforces three key technical constraints:

1.  **Injection-Stripping Filter (Section 11.5)**: A regex-based sanitation layer (`(?i)(ignore previous|system prompt|bypass)`) is applied to agent outputs before structural evaluation to prevent common prompt-injection vectors from artificially inflating Rule Scores.
2.  **Embedding Similarity (Section 11.2)**: Task duplication and domain overlap are controlled by clustering prompt templates using cosine similarity metrics computed via `text-embedding-3-small`. Prompts with >0.85 similarity are flagged for manual review or automated deprecation.
3.  **Compute Budgets**: The simulated execution environment enforces a compute ceiling per agent configuration to ensure fair comparisons. This is modeled as a maximum limit of **4,000 output tokens per turn** and a hard cap of **3 maximum tool-call loops** before the agent's turn is truncated.

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
│   ├── agents/                 # Calibrated Gpt4o, Claude3.5 Sonnet, and Llama3.1 prototypes
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
