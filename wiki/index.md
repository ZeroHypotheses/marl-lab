# Wiki Index

The catalog of everything in this knowledge base. **Agents: read this first**
when answering a question, then drill into the pages it points at.

Status legend: `stub` = placeholder · `drafted` = written, unverified ·
`solid` = checked against a cited source.

Everything below is a `stub` — this wiki is new. Pages get created and promoted
as sources are ingested via [`/marl-ingest`](../workflows/ingest.md).

---

## Sources

### The textbook
Albrecht, Christianos & Schäfer, *Multi-Agent Reinforcement Learning:
Foundations and Modern Approaches* (MIT Press, 2024).

Chapter list verified against the PDF's own table of contents. Extracted text
is in `book/text/ch<NN>.md` (gitignored) — ingest reads from there, but
equations must be checked against the PDF, since extraction is lossy.

| Page | Ch. | Title | Pages | Status |
|---|---|---|---|---|
| `[[ch01-introduction]]` | 1 | Introduction | 1–18 | stub |
| `[[ch02-reinforcement-learning]]` | 2 | Reinforcement Learning | 19–42 | stub |
| `[[ch03-games]]` | 3 | Games: Models of Multi-Agent Interaction | 43–60 | stub |
| `[[ch04-solution-concepts]]` | 4 | Solution Concepts for Games | 61–88 | stub |
| `[[ch05-marl-in-games]]` | 5 | MARL in Games: First Steps and Challenges | 89–114 | stub |
| `[[ch06-foundational-algorithms]]` | 6 | MARL: Foundational Algorithms | 115–160 | stub |
| `[[ch07-deep-learning]]` | 7 | Deep Learning | 161–182 | stub |
| `[[ch08-deep-rl]]` | 8 | Deep Reinforcement Learning | 183–218 | stub |
| `[[ch09-deep-marl]]` | 9 | Multi-Agent Deep Reinforcement Learning | 219–304 | stub |
| `[[ch10-marl-in-practice]]` | 10 | Multi-Agent Deep RL in Practice | 305–318 | stub |
| `[[ch11-environments]]` | 11 | Multi-Agent Environments | 319–336 | stub |
| `[[appendix-a-surveys]]` | A | Surveys on MARL | 337–340 | stub |

Part structure — note chapter 1 sits *outside* both parts, as a standalone
introduction:

- **Part I — Foundations of Multi-Agent Reinforcement Learning** (p. 17): ch. 2–6
- **Part II — Multi-Agent Deep Reinforcement Learning: Algorithms and Practice** (p. 159): ch. 7–11

Slide decks in `upstream/slides/` cover chapters 1–9 only; chapters 10 and 11
have no deck.

### Other sources
| Page | What | Status |
|---|---|---|
| `[[bcn-summer-school]]` | Barcelona MARL Summer School 2024 lectures ([videos](https://iiia.csic.es/en-us/marl-course/)) | stub |

---

## Topics

| Page | What | Status |
|---|---|---|
| `[[normal-form-games]]` | Stateless multi-agent interaction | stub |
| `[[stochastic-games]]` | Games with state; the core MARL model | stub |
| `[[partial-observability]]` | POSGs, Dec-POMDPs, what agents can't see | stub |
| `[[solution-concepts]]` | Nash, correlated, Pareto, social welfare | stub |
| `[[non-stationarity]]` | Why single-agent RL guarantees break | stub |
| `[[centralised-training-decentralised-execution]]` | CTDE — the dominant deep-MARL paradigm | stub |
| `[[credit-assignment]]` | Which agent caused the team reward? | stub |
| `[[value-decomposition]]` | Factorising joint value functions; IGM | stub |
| `[[parameter-sharing]]` | One network, many agents | stub |
| `[[self-play]]` | Training against copies of yourself | stub |

---

## Algorithms

Implemented in `upstream/codebase/marlbase/` — confirmed from its Hydra configs.

| Page | Algorithm | Config | Status |
|---|---|---|---|
| `[[idqn]]` | Independent DQN | `configs/algorithm/idqn.yaml` | stub |
| `[[ia2c]]` | Independent A2C | `configs/algorithm/ia2c.yaml` | stub |
| `[[ippo]]` | Independent PPO | `configs/algorithm/ippo.yaml` | stub |
| `[[maa2c]]` | Multi-Agent A2C (centralised critic) | `configs/algorithm/maa2c.yaml` | stub |
| `[[mappo]]` | Multi-Agent PPO | `configs/algorithm/mappo.yaml` | stub |
| `[[vdn]]` | Value Decomposition Networks | `configs/algorithm/vdn.yaml` | stub |
| `[[qmix]]` | QMIX (monotonic mixing network) | `configs/algorithm/qmix.yaml` | stub |
| `[[iql-tabular]]` | Tabular Independent Q-Learning | `upstream/exercises/tabular_marl/iql.py` | stub |

---

## Notes

*(Synthesis, comparisons, answered questions. Empty — nothing synthesised yet.)*

---

## Environments

Used by the exercises (`upstream/exercises/deep_marl_data/`):

| Page | Environment | Status |
|---|---|---|
| `[[level-based-foraging]]` | LBF — cooperative foraging, `lbf_8x8-2p-3f_coop` | stub |
| `[[robotic-warehouse]]` | RWARE — `rware_tiny_4ag` | stub |
| `[[smaclite]]` | SMAClite — `smaclite_2s3z`, `smaclite_2s_vs_1sc` | stub |
