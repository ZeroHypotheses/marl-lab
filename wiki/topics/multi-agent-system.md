---
title: Multi-Agent System
type: topic
status: stub
sources: ["[[ch01-introduction]]"]
updated: 2026-09-11
---

# Multi-Agent System

An environment plus multiple decision-making agents interacting in it to achieve
goals [Ch. 1.1, Fig. 1.1].

- **Environment** — a physical or virtual world whose state evolves over time
  and is influenced by agents' actions. Specifies the available actions and the
  observations each agent receives. States and actions may be discrete,
  continuous, or mixed.
- **Agent** — an entity that receives information about the state and chooses
  actions to influence it. Goal-directed; goals are encoded as reward functions.
- **Policy** — maps state to an action or a distribution over actions. Under
  partial observability it may condition on current *and past* observations.

"Multi-agent environments are often characterized by the fact that agents only
have a limited and imperfect view of the environment" [Ch. 1.1] — partial
observability is presented as the normal case. → [[partial-observability]]

## Agent ≠ the object it controls

A **robot** or **item** in [[level-based-foraging]] is an *object*, represented
in the state by x/y-position variables (and a binary existence variable for
items). An **agent** is "an abstract decision-making entity that observes some
information from the environment and chooses values for certain action
variables" [Ch. 1.1].

The book uses the terms interchangeably where the correspondence is one-to-one.
The distinction still matters: it is what allows one agent to control several
objects, or several agents to control one.

## Defining characteristic

Agents must coordinate their actions *with* or *against* each other. Where on
that spectrum a system sits is set by its [[reward-structures]].

> Formal game models are in [[ch03-games]]. This page holds only what ch. 1
> establishes.

## Related
[[reward-structures]] · [[training-execution-modes]] · [[ch01-introduction]]
