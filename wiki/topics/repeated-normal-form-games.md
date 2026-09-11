---
title: Repeated Normal-Form Games
type: topic
status: solid
sources: ["[[ch03-games]]"]
updated: 2026-09-11
---

# Repeated Normal-Form Games

The same [[normal-form-games|normal-form game]] $\Gamma$ played over
$t = 0,\dots,T-1$ [Ch. 3.2]. Each agent samples $a_i^t \sim \pi_i(\cdot \mid h^t)$
where $h^t = (a^0,\dots,a^{t-1})$ is the **joint-action history**.

**Terminology in this book**: $T = 1$ is a *non-repeated* normal-form game;
$T > 1$ is *repeated*.

## The addition is history-conditioning

Policies can now depend on everything that has happened, "giving rise to a
complex space of policies." In practice a policy conditions on some function
$f(h^t)$ of the history — the last joint action, or summary statistics such as
action counts.

**Tit-for-Tat** (Axelrod & Hamilton 1981) is the canonical example: in repeated
Prisoner's Dilemma, copy the other agent's most recent action.

## Finite ≠ infinite

> "A game with finite repetitions is not in general equivalent to the same game
> with infinite repetitions" [Ch. 3.2].

With a known horizon $T$, **end-game effects** appear — agents behave differently
near the end (§6.3.3 gives a Prisoner's Dilemma example →
[[ch06-foundational-algorithms]]).

For infinitely repeated games, a per-step termination probability can be
specified — and this is **the same $(1-\gamma)$ reading of the discount factor**
from [[returns-and-discounting]]. For $\gamma < 1$ the game still counts as
infinite, since every finite $T > 0$ has non-zero probability.

## Related
[[normal-form-games]] · [[stochastic-games]] · [[returns-and-discounting]] ·
[[iql-tabular]]
