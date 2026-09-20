---
title: "IIIA-CSIC MARL Course 2024 — Session-to-Chapter Map"
type: source
status: solid
sources: ["https://iiia.csic.es/en-us/marl-course/", "https://www.youtube.com/playlist?list=PLkoCa1tf0XjCU6GkAfRCkChOOSH6-JC_2"]
updated: 2026-09-20
---

# IIIA-CSIC MARL Course 2024 — Session-to-Chapter Map

Stefano V. Albrecht taught this four-session course at IIIA-CSIC on 16–19
September 2024. The [official course page](https://iiia.csic.es/en-us/marl-course/)
says that it follows *Multi-Agent Reinforcement Learning: Foundations and Modern
Approaches* and links all four recordings.

This page maps the recordings to the book. The organisers do not publish a
session syllabus, so the mapping below was verified from the lectures'
auto-generated transcripts, especially the points where Albrecht names the book
chapter or introduces the next lecture block. Timestamps are navigation aids and
may be a few seconds off.

## Quick map

| Recording | Book coverage | Important qualification |
|---|---|---|
| [Session 1](https://youtu.be/QfYx5q0Q75M) · 3:06:23 | Chapters 1–3 | Introduction and motivation, single-agent RL, then game models. |
| [Session 2](https://youtu.be/uYKYb2iqcYY) · 2:35:47 | Chapters 4–5 | Solution concepts, then first MARL methods and challenges. Chapter 6 is explicitly skipped. |
| [Session 3](https://youtu.be/P1M1wCOxxEk) · 2:42:05 | Chapters 7–8; Chapter 9 §§9.1–9.5 begins | Chapters 7–8 are presented as a compressed deep-learning/deep-RL on-ramp; the second half starts deep MARL. |
| [Session 4](https://youtu.be/wdJeN8-Upwg) · 2:33:52 | Chapter 9 §§9.5–9.9 | Finishes value decomposition, then agent modelling, parameter sharing, self-play, and population-based training. |

The practical consequence is that the videos do **not** form a recording of
every chapter: Chapter 6 is omitted, and Chapters 10–11 are not systematically
covered.

## Session 1 — Chapters 1–3

Video: [Session 1](https://youtu.be/QfYx5q0Q75M)

- **Chapter 1:** the opening motivation, applications, multi-agent systems, and
  preview of MARL's main challenges.
- **Chapter 2:** [reinforcement-learning basics begin around 0:42:11](https://youtu.be/QfYx5q0Q75M?t=2531),
  covering MDPs, dynamic programming, TD learning, Q-learning, and evaluation.
- **Chapter 3:** after the break, Albrecht explicitly moves from single-agent RL
  to [game models at 1:56:36](https://youtu.be/QfYx5q0Q75M?t=6996): normal-form,
  repeated, stochastic, and partially observable stochastic games, followed by
  communication and knowledge assumptions.

This is the best companion recording for [[ch01-introduction]],
[[ch02-reinforcement-learning]], and [[ch03-games]].

## Session 2 — Chapters 4–5; Chapter 6 skipped

Video: [Session 2](https://youtu.be/uYKYb2iqcYY)

- **Chapter 4:** from the beginning through roughly 1:18, covering expected
  returns, best response, minimax, Nash and correlated equilibria, Pareto and
  welfare refinements, regret, and computational complexity. The lecturer
  [summarises this block at 1:16:45](https://youtu.be/uYKYb2iqcYY?t=4605).
- **Chapter 5:** [starts around 1:22:16](https://youtu.be/uYKYb2iqcYY?t=4936),
  with the general learning process, independent and central learning, and the
  characteristic MARL challenges.
- **Chapter 6:** [at 1:23:09–1:23:35](https://youtu.be/uYKYb2iqcYY?t=4989),
  Albrecht says that Chapters 5 and 6 form the foundational learning block, but
  that the Chapter 6 algorithms will not be covered because of time. The session
  contains occasional references to Chapter 6 ideas, not a Chapter 6 lecture.

Thus Session 2 accompanies [[ch04-solution-concepts]] and
[[ch05-marl-in-games]], but **not** [[ch06-foundational-algorithms]].

### Why Chapter 6 was skipped

Albrecht gives the direct reason at
[1:23:22](https://youtu.be/uYKYb2iqcYY?t=5002): Chapter 6 contains many
algorithms and ideas, becomes complicated, and cannot fit into the available
course time; he recommends reading it independently before the course jumps to
the deep-RL part of the book [Session 2, 1:23:09–1:23:40].

This is best understood as **course compression, not a claim that Chapter 6 is
unimportant**. The official course description promises both foundations and
contemporary deep-MARL methods, but only four three-hour sessions were scheduled.
The lecture therefore keeps Chapter 5's simplest tabular baselines, compresses
Chapters 7–8, and devotes roughly half the course to Chapter 9. That allocation
matches the course's emphasis on contemporary methods such as CTDE, value
decomposition, parameter sharing, and self-play
([official description](https://iiia.csic.es/en-us/marl-course/)).

For learning the field from first principles, Chapter 6 remains unusually
important. It is where the book shows how solution concepts become actual
learning operators: minimax/Nash/correlated values inside TD targets, explicit
agent models, policy-learning dynamics, and regret matching. It also makes the
restricted assumptions behind convergence results visible [Ch. 6.1–6.5]. The
course itself later relies on this foundation: Session 4 explicitly returns to
the skipped chapter while introducing neural agent modelling
([0:43:18](https://youtu.be/wdJeN8-Upwg?t=2598)).

For this lab, the right conclusion is therefore **do not copy the course's
omission**. Read Chapter 6 and implement one small model-based or minimax-Q
example before entering Chapter 9; use the recordings to supplement that path,
not to define it.

## Session 3 — Chapters 7–8 and the first half of Chapter 9

Video: [Session 3](https://youtu.be/P1M1wCOxxEk)

- **Chapters 7–8:** a compressed neural-network and single-agent deep-RL
  prerequisite block: DQN, policy gradients, actor–critic methods, PPO,
  parallel data collection, and recurrent networks. Albrecht explicitly locates
  the material in [Chapters 7 and 8 at 1:23:57](https://youtu.be/P1M1wCOxxEk?t=5037).
- **Chapter 9 begins:** after the break, the deep-MARL lecture
  [starts around 1:34:40](https://youtu.be/P1M1wCOxxEk?t=5680). It covers
  training/execution modes and CTDE (§9.1), notation (§9.2), independent deep
  learning (§9.3), and multi-agent policy gradients and centralised critics
  (§9.4). Value decomposition (§9.5) is introduced near the end
  [around 2:32:13](https://youtu.be/P1M1wCOxxEk?t=9133).

For a reader who already knows deep learning and deep RL, the high-value entry
point is the Chapter 9 transition at about 1:34:40; the earlier block is a useful
alignment with the book's notation and chosen baseline algorithms.

## Session 4 — the remainder of Chapter 9

Video: [Session 4](https://youtu.be/wdJeN8-Upwg)

Session 4 resumes exactly where Session 3 stopped:

| Timestamp | Chapter 9 section | Topics |
|---|---|---|
| [Start](https://youtu.be/wdJeN8-Upwg) | §9.5 | IGM, VDN, QMIX, and value decomposition in practice. |
| [0:40:49](https://youtu.be/wdJeN8-Upwg?t=2449) | §9.6 | Agent modelling with neural networks, including the bridge back to Chapter 6. |
| [1:24:02](https://youtu.be/wdJeN8-Upwg?t=5042) | §9.7 | Homogeneous agents, parameter sharing, and experience sharing. |
| [1:41:31](https://youtu.be/wdJeN8-Upwg?t=6091) | §9.8 | Policy self-play, Monte Carlo tree search, and AlphaZero. |
| [2:00:28](https://youtu.be/wdJeN8-Upwg?t=7228) | §9.9 | Population-based training, PSRO, and AlphaStar. |

The taught material ends with Chapter 9's population-based methods around
[2:20:14](https://youtu.be/wdJeN8-Upwg?t=8414); the remainder is questions and
course wrap-up.

## Coverage by book chapter

| Chapter | Recording | Coverage |
|---|---|---|
| 1 — Introduction | Session 1 | Overview rather than a line-by-line rendering. |
| 2 — Reinforcement Learning | Session 1 | Substantial. |
| 3 — Games | Session 1 | Substantial. |
| 4 — Solution Concepts | Session 2 | Substantial. |
| 5 — MARL: First Steps and Challenges | Session 2 | Substantial. |
| 6 — Foundational Algorithms | — | **Explicitly skipped**; referenced briefly in Sessions 2 and 4. |
| 7 — Deep Learning | Session 3 | Compressed prerequisite treatment. |
| 8 — Deep Reinforcement Learning | Session 3 | Substantial but compressed into the first half. |
| 9 — Multi-Agent Deep RL | Sessions 3–4 | Main focus of the second half of the course. |
| 10 — Multi-Agent Deep RL in Practice | — | No systematic chapter coverage identified. |
| 11 — Multi-Agent Environments | — | No systematic chapter coverage identified. |
| Appendix A — Surveys | — | Not covered. |

## How this fits our reading path

After finishing Chapter 6, a deep-RL-experienced reader can use Session 3's
first half as an optional refresher, start the new material at
[Session 3, 1:34:40](https://youtu.be/P1M1wCOxxEk?t=5680), and then watch Session
4. The recordings are a companion to the book rather than a replacement:
notably, they leave out the foundational Chapter 6 algorithms and the practical
and environment chapters.

## Related

[[ch01-introduction]] · [[ch02-reinforcement-learning]] · [[ch03-games]] ·
[[ch04-solution-concepts]] · [[ch05-marl-in-games]] ·
[[ch06-foundational-algorithms]] · [[ch07-deep-learning]] · [[ch08-deep-rl]] ·
[[ch09-deep-marl]] · [[ch10-marl-in-practice]] · [[ch11-environments]]
