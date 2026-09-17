# Wiki Index

The catalog of everything in this knowledge base. **Agents: read this first**
when answering a question, then drill into the pages it points at.

Status legend: `stub` = placeholder · `drafted` = written, unverified ·
`solid` = checked against a cited source.

**Chapters 1–5 are ingested** (all of Part I plus the introduction). Chapters
6–11 and Appendix A have *skeleton* pages: verified section structure, page
ranges, equation counts and errata pointers, but **no summary of their content**
— they haven't been read. They exist so the wiki is navigable ("where is IGM
defined?" → §9.5.1) without anything being invented. Fill one in with
[`/marl-ingest <n>`](../workflows/ingest.md).

---

## Sources

### The textbook
Albrecht, Christianos & Schäfer, *Multi-Agent Reinforcement Learning:
Foundations and Modern Approaches* (MIT Press, 2024).

Our copy is the **second printing**; all published errata are already applied
— see [[errata]]. Cite by section or equation, not page (pagination shifts
between printings).

Chapter list verified against the PDF's own table of contents. Extracted text
is in `book/text/ch<NN>.md` (gitignored) — ingest reads from there, but
equations must be checked against the PDF, since extraction is lossy.

| Page                             | Ch. | Title                                     | Pages   | Status       |
| -------------------------------- | --- | ----------------------------------------- | ------- | ------------ |
| [[ch01-introduction]]            | 1   | Introduction                              | 1–18    | **ingested** |
| [[ch02-reinforcement-learning]]  | 2   | Reinforcement Learning                    | 19–42   | **ingested** |
| [[ch03-games]]                   | 3   | Games: Models of Multi-Agent Interaction  | 43–60   | **ingested** |
| [[ch04-solution-concepts]]       | 4   | Solution Concepts for Games               | 61–88   | **ingested** |
| [[ch05-marl-in-games]]           | 5   | MARL in Games: First Steps and Challenges | 89–114  | **ingested** |
| [[ch06-foundational-algorithms]] | 6   | MARL: Foundational Algorithms             | 115–160 | skeleton     |
| [[ch07-deep-learning]]           | 7   | Deep Learning                             | 161–182 | skeleton     |
| [[ch08-deep-rl]]                 | 8   | Deep Reinforcement Learning               | 183–218 | skeleton     |
| [[ch09-deep-marl]]               | 9   | Multi-Agent Deep Reinforcement Learning   | 219–304 | skeleton     |
| [[ch10-marl-in-practice]]        | 10  | Multi-Agent Deep RL in Practice           | 305–318 | skeleton     |
| [[ch11-environments]]            | 11  | Multi-Agent Environments                  | 319–336 | skeleton     |
| [[appendix-a-surveys]]           | A   | Surveys on MARL                           | 337–340 | skeleton     |

Part structure — note chapter 1 sits *outside* both parts, as a standalone
introduction:

- **Part I — Foundations of Multi-Agent Reinforcement Learning** (p. 17): ch. 2–6
- **Part II — Multi-Agent Deep Reinforcement Learning: Algorithms and Practice** (p. 159): ch. 7–11

Slide decks in `upstream/slides/` cover chapters 1–9 only; chapters 10 and 11
have no deck.

### Other sources
| Page | What | Status |
|---|---|---|
| [[errata]] | **Author-published corrections** — our PDF is the 2nd printing; all applied | solid |
| [[bcn-summer-school]] | Barcelona MARL Summer School 2024 lectures ([videos](https://iiia.csic.es/en-us/marl-course/)) | stub |

---

## Topics

### Single-agent RL foundations — ch. 2
| Page | What | Status |
|---|---|---|
| [[markov-decision-process]] | The standard single-agent model; Markov property | solid |
| [[returns-and-discounting]] | Discounted return; **γ is part of the problem, not a knob** | solid |
| [[value-functions-and-bellman]] | $V^\pi$, $Q^\pi$, Bellman (optimality) equations | solid |
| [[dynamic-programming]] | Policy/value iteration; contraction mappings | solid |
| [[temporal-difference-learning]] | Sarsa, Q-learning, ε-greedy, convergence conditions | solid |
| [[learning-curves]] | Evaluation protocol — cumulative steps, not episodes | solid |

### Game models — ch. 3
| Page | What | Status |
|---|---|---|
| [[normal-form-games]] | Single interaction; matrix games; the 78 distinct 2×2 games | solid |
| [[repeated-normal-form-games]] | History-conditioned policies; finite ≠ infinite | solid |
| [[stochastic-games]] | Games with state — the core MARL model | solid |
| [[partial-observability]] | POSGs, Dec-POMDPs, belief states and why they're unusable | solid |
| [[knowledge-assumptions]] | MARL assumes agents know almost nothing | solid |
| [[communication-in-games]] | Messages as actions that don't move the state | solid |
| [[rl-game-theory-dictionary]] | RL ↔ game theory vocabulary | solid |

### Solution concepts — ch. 4
| Page | What | Status |
|---|---|---|
| [[solution-concepts]] | **Hub** — what counts as solving a game | solid |
| [[best-response]] | The primitive underlying every equilibrium | solid |
| [[minimax]] | 2-agent zero-sum; polynomial via linear programming | solid |
| [[nash-equilibrium]] | General-sum; and why ε-Nash is not an approximation | solid |
| [[correlated-equilibrium]] | Dropping policy independence; Chicken beats Nash | solid |
| [[pareto-optimality]] | Refinement — the Pareto frontier | solid |
| [[social-welfare-and-fairness]] | Sum vs product of returns | solid |
| [[no-regret]] | Judged across episodes, not on one policy | solid |
| [[complexity-of-equilibria]] | **NASH is PPAD-complete** — MARL is no magic bullet | solid |

### Learning in games — ch. 1 and 5
| Page | What | Status |
|---|---|---|
| [[multi-agent-system]] | Environment + agents + goals; agent vs. object | solid |
| [[reward-structures]] | Common / zero-sum / general-sum — the book's spine | solid |
| [[general-learning-process]] | Data, algorithm, goal; what policies condition on | solid |
| [[convergence-types]] | Five criteria — and why a flat learning curve proves nothing | solid |
| [[central-learning]] | CQL: one policy over joint actions | solid |
| [[independent-learning]] | IQL: ignore the others — and a strong baseline | solid |
| [[training-execution-modes]] | Centralised, decentralised, CTDE | solid |
| [[centralised-training-decentralised-execution]] | CTDE — the dominant deep-MARL paradigm | stub |
| [[non-stationarity]] | The moving target; dynamics become non-Markovian | solid |
| [[equilibrium-selection]] | Stag Hunt; why IQL drifts to the risk-dominant equilibrium | solid |
| [[credit-assignment]] | Whose action? — **not** only a common-reward problem | solid |
| [[scaling-in-number-of-agents]] | Exponential — **except when it isn't** (§5.4.4) | solid |
| [[self-play]] | Algorithm vs policy self-play; mixed-play | solid |
| [[agent-modelling]] | Modelling the others — filled by ch. 6 | stub |
| [[marl-agendas]] | Computational / prescriptive / descriptive | drafted |
| [[value-decomposition]] | Factorising joint value functions; IGM | stub |
| [[parameter-sharing]] | One network, many agents | stub |
| [[level-based-foraging]] | The book's running example | drafted |

---

## Algorithms

Implemented in `upstream/codebase/marlbase/` — confirmed from its Hydra configs.

| Page | Algorithm | Config | Status |
|---|---|---|---|
| [[idqn]] | Independent DQN | `configs/algorithm/idqn.yaml` | stub |
| [[ia2c]] | Independent A2C | `configs/algorithm/ia2c.yaml` | stub |
| [[ippo]] | Independent PPO | `configs/algorithm/ippo.yaml` | stub |
| [[maa2c]] | Multi-Agent A2C (centralised critic) | `configs/algorithm/maa2c.yaml` | stub |
| [[mappo]] | Multi-Agent PPO | `configs/algorithm/mappo.yaml` | stub |
| [[vdn]] | Value Decomposition Networks | `configs/algorithm/vdn.yaml` | stub |
| [[qmix]] | QMIX (monotonic mixing network) | `configs/algorithm/qmix.yaml` | stub |
| [[iql-tabular]] | **Tabular IQL — completed first exercise** | `upstream/exercises/tabular_marl/iql.py` | solid |

---

## Notes

| Page | What | Status |
|---|---|---|
| [Hands-on study loop](notes/hands-on-study-loop.md) | Read → predict → implement → run → explain → record; starts with tabular IQL | solid |
| [[iql-evaluation-vs-solution-concepts]] | Why IQL's mean-return evaluator does not test Nash, Pareto, or no-regret | solid |
| [[solution-concepts-as-specifications]] | What Nash buys when it is not part of the learning update | solid |
| [[first-tabular-iql-exercise]] | Lessons from implementing and testing the first tabular IQL exercise | solid |

---

## Environments

Used by the exercises (`upstream/exercises/deep_marl_data/`):

| Page | Environment | Status |
|---|---|---|
| [[level-based-foraging]] | LBF — the book's running example | stub ✓ ch1 |
| [[robotic-warehouse]] | RWARE — `rware_tiny_4ag` | stub |
| [[smaclite]] | SMAClite — `smaclite_2s3z`, `smaclite_2s_vs_1sc` | stub |
