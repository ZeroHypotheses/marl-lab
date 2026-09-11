---
title: Partial Observability (POSGs)
type: topic
status: solid
sources: ["[[ch03-games]]"]
updated: 2026-09-11
---

# Partial Observability (POSGs)

The **partially observable stochastic game** sits at the top of the hierarchy
and "includes all of the other game models covered in this book as special
cases" [Ch. 3.4, Def. 4] (Hansen, Bernstein & Zilberstein 2004).

A POSG is a [[stochastic-games|stochastic game]] plus, for each agent $i$:
- finite observation set $O_i$
- observation function $O_i : A \times S \times O_i \to [0,1]$ with
  $\sum_{o_i} O_i(a,s,o_i) = 1$ [Eq. 3.4]

At $t$ each agent receives $o_i^t \sim O_i(\cdot \mid a^{t-1}, s^t)$ and acts on
$\pi_i(a_i^t \mid h_i^t)$, where $h_i^t = (o_i^0,\dots,o_i^t)$ is its **own**
observation history. Agents no longer share a history.

The fully general form is $\Pr(s^t, o^t \mid s^{t-1}, a^{t-1})$; the per-agent
$O_i$ above is the common simplification where observations depend only on the
new state and the joint action that led to it.

## Special cases

- $o_i^t = (s^t, a^{t-1})$ ⇒ [[stochastic-games]]
- $|I| = 1$ ⇒ POMDP (Kaelbling, Littman & Cassandra 1998)
- **common rewards ⇒ Dec-POMDP**, widely studied in multi-agent planning
  (Oliehoek & Amato 2016) → [[reward-structures]]

## Observability conditions it can express

- **Unobserved actions of others** — $o_i^t = (s^t, a_i^{t-1})$: see the state and
  your own action, not others'. E.g. robot soccer; markets where prices are
  public but buy/sell actions private. Agents must *infer* others' actions →
  [[agent-modelling]].
- **Limited view region** — $o_i^t = (\bar{s}^t, \bar{a}^t)$ with
  $\bar{s}^t \subset s^t$. E.g. vision fields in
  [[level-based-foraging]] [Fig. 3.4]; fog of war in RTS games.
- **Noise** — spread probability over several observations (imperfect sensors).
- **Communication**, including range limits and message loss →
  [[communication-in-games]].

## §3.4.1 Belief states and filtering

With partial observation, the current observation is generally **not enough** to
act optimally — the book's example: the level-1 agent should move toward an item
now outside its vision field, which it can only know from memory.

A **belief state** $b_i^t$ is a distribution over possible current states. For a
single agent (POMDP), $b_i^0 = \mu$ and the Bayesian update is
$$b_i^{t+1}(s') \propto \sum_{s \in S} b_i^t(s)\, T(s'\mid s,a_i^t)\, O_i(o_i^{t+1} \mid a_i^t, s')$$
[Eq. 3.5]. This is a **sufficient statistic** — it retains all relevant
information from the history. The update process is **filtering**.

**Two reasons this is not usable directly in MARL:**

1. **Intractable.** Space to store and time to update exact belief states are
   each *exponential in the number of state variables* [Ch. 3.4.1]. Approximate
   filtering is its own research area (Albrecht & Ramamoorthy 2016).
2. **Requires knowledge MARL assumes away.** Eq. 3.5 needs $T$ and $O_i$ — and
   §3.6 says agents typically have neither → [[knowledge-assumptions]]. With
   more than one agent it's worse: you must also infer others' observations and
   actions, needing *their* observation functions and policies (Gmytrasiewicz &
   Doshi 2005).

**What is done instead:** recurrent neural networks process observations
sequentially, and the recurrent state learns to encode what matters [§3.4.1,
pointing to §7.5.2 and §8.3]. That is the practical answer carried into
[[ch08-deep-rl]] and [[ch09-deep-marl]].

## Related
[[stochastic-games]] · [[knowledge-assumptions]] · [[communication-in-games]] ·
[[level-based-foraging]] · [[ch08-deep-rl]]
