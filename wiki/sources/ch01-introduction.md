---
title: "Ch. 1 — Introduction"
type: source
status: solid
sources: ["MARL book, Ch. 1, pp. 1–18 (2nd printing)"]
updated: 2026-09-11
---

# Chapter 1 — Introduction

Scene-setting. Names the vocabulary, the application shapes, the four
challenges, and the three research agendas. **Defines almost nothing formally**
— every concept it introduces is properly defined in [[ch03-games]],
[[ch04-solution-concepts]], [[ch05-marl-in-games]] or [[ch09-deep-marl]].
Contains **no numbered equations**.

Sections: 1.1 Multi-Agent Systems · 1.2 Multi-Agent Reinforcement Learning ·
1.3 Application Examples · 1.4 Challenges of MARL · 1.5 Agendas of MARL ·
1.6 Book Contents and Structure.

> 📕 errata: one entry falls in this chapter (p12, "fourth" → "quarter").
> Already applied in our 2nd printing — see [[errata]].

## What it establishes

**A multi-agent system = environment + multiple decision-making agents + goals**
[§1.1]. The environment specifies available actions and the observations agents
receive; states and actions may be discrete, continuous, or both. Multi-agent
environments are "often characterized by the fact that agents only have a
limited and imperfect view" — partial observability is framed as the normal
case, not an extension. See [[multi-agent-system]].

**Agents are goal-directed, and goals are encoded as reward functions** [§1.1].
A *policy* maps state (or, under partial observability, current and past
observations) to actions or action probabilities.

**The MARL loop** [§1.2, Fig. 1.3]: n agents choose individual actions forming a
**joint action**; the joint action changes the state; each agent receives an
individual reward and a new observation. A run from initial to terminal state is
an **episode**. This is the single-agent loop of [[ch02-reinforcement-learning]]
extended to n agents.

**Two independent reasons to use multiple agents** [§1.2] — worth keeping apart,
because they justify different things:
1. *Tractability.* A central controller in level-based foraging picks from
   $6^3 = 216$ joint actions per step; three independent agents each pick from 6.
   "Most standard single-agent RL algorithms do not scale easily to action
   spaces this large."
2. *Feasibility.* Many applications cannot centralise at execution time at all —
   urban autonomous driving, search-and-rescue robots without a central
   coordinator. Here decentralised policies are a **requirement**, not an
   optimisation. See [[training-execution-modes]].

**Six dimensions for classifying MARL settings** [Fig. 1.4]: size, knowledge,
observability, rewards, objective, centralisation & communication — each
signposted to the chapter that treats it.

**Reward structures**, introduced through the application examples rather than
defined: common/shared reward, zero-sum, general-sum (mixed-motive).
See [[reward-structures]].

**Four challenges** [§1.4], detailed in [[ch05-marl-in-games]]:
[[non-stationarity]], equilibrium selection (→ [[solution-concepts]]),
[[credit-assignment]], and [[scaling-in-number-of-agents]].

**Three agendas** [§1.5]: computational, prescriptive, descriptive.
See [[marl-agendas]].

## Definitional points that matter later

**"Agent" is not the object it controls.** In level-based foraging, "robot" and
"item" label *objects* represented in the state by x/y-position (and, for items,
a binary existence variable). "Agent" is "an abstract decision-making entity
that observes some information from the environment and chooses values for
certain action variables" [§1.1]. The book then uses them interchangeably where
the correspondence is one-to-one — a convenience, but the distinction is what
permits one agent to control several objects, or several agents one object.

**MARL is used in a literal sense here** [footnote 3, p6]: learning policies for
*multiple* agents. Explicitly **not** learning a policy for a single agent
operating in a multi-agent system "in which we have no control over the other
agents." A meaningful scope restriction — much published work sits outside it.

> ⚠️ Watch for: the running level-based foraging example is introduced as fully
> cooperative (+1 to all agents when any item is collected), but §1.1 notes that
> **the implementation actually used in the book** (§11.3.1) gives a normalised
> positive reward only to the agents *involved* in a collection. So the real
> running example is mixed-motive — agents are motivated to beat others to
> items, while still needing to cooperate on items they cannot collect alone.
> Easy to conflate. See [[level-based-foraging]].

## Scope of the book

Covers the **computational** and **prescriptive** agendas; the **descriptive**
agenda (using MARL to model human/animal learning) is explicitly out of scope
[§1.5].

Structure [§1.6]: Part I (ch. 2–6) foundations — RL, game models, solution
concepts, then learning in games. Part II (ch. 7–11) deep MARL — deep learning,
deep RL, deep MARL, practice, environments. **Chapter 1 sits outside both
parts.** The book ships its own Python codebase (→ `upstream/codebase`), used
for code snippets in [[ch10-marl-in-practice]].

## Cited work

Shoham & Leyton-Brown 2008; Wooldridge 2009 (multi-agent systems); Shoham,
Powers & Grenager 2007 (agendas); Harsanyi & Selten 1988 (equilibrium
selection); Krnjaic et al. 2024 (warehouse); Tesauro 1994, Silver et al. 2018,
Vinyals et al. 2019, Bard et al. 2020, Pérolat et al. 2022 (games).

## Open questions

- §1.4 says credit assignment is "still an open problem … in an efficient and
  scalable way", and points at counterfactual reasoning. Which chapter 9 methods
  actually implement that?
- §1.4 hedges that joint-action growth is not always exponential (→ §5.4.4).
  What is the counter-example?
