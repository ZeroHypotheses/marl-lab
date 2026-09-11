---
title: Agent Modelling
type: topic
status: stub
sources: ["[[ch03-games]]", "[[ch04-solution-concepts]]", "[[ch05-marl-in-games]]"]
updated: 2026-09-11
---

# Agent Modelling

Building models of the other agents — their policies, or the game components you
cannot observe — and acting on the predictions.

**Why it's needed:** [[knowledge-assumptions]] says MARL agents typically know
neither others' reward functions nor $T$ or $O_i$. An agent "only experiences
the immediate effects of its own actions" and "may use such experiences to
construct models of the unknown components in a game (such as $T$) or the
policies of other agents" [Ch. 3.6].

Also forced by [[partial-observability]]: where $o_i^t = (s^t, a_i^{t-1})$,
agents "may need to infer with some uncertainty the possible actions of other
agents based on changes in the observed environment state" [Ch. 3.4] — the book's
example being inferring a pass in robot soccer from the ball's motion.

## Where it appears

- **[[best-response]] computation** — knowing $R_j$ lets you estimate agent $j$'s
  best response, which informs your own [Ch. 3.6].
- **[[equilibrium-selection]]** — predicting others' actions can steer agents to
  the reward-dominant equilibrium in Stag Hunt, "however, whether such an outcome
  occurs depends on several factors, such as the details of the agents'
  exploration strategies and learning rates and how the agent model is used"
  [Ch. 5.4.2].
- **Mixed-play and ad hoc teamwork** → [[self-play]].

## Where it's defined

**§6.3** ([[ch06-foundational-algorithms]]) is the real treatment: fictitious
play (§6.3.1), joint-action learning with agent modelling (§6.3.2), Bayesian
learning and value of information (§6.3.3). Deep versions in §9.6
([[ch09-deep-marl]]).

Reference: Albrecht & Stone (2018).

> Skeleton — filled in when ch. 6 is ingested.

## Related
[[knowledge-assumptions]] · [[best-response]] · [[equilibrium-selection]] ·
[[ch06-foundational-algorithms]]
