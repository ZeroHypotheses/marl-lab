---
title: Central Learning
type: topic
status: solid
sources: ["[[ch05-marl-in-games]]"]
updated: 2026-09-11
---

# Central Learning

Train **one** central policy $\pi_c$ that receives all agents' observations and
picks a **joint** action from $A = A_1 \times \dots \times A_n$ [Ch. 5.3.1]. This
reduces MARL to single-agent RL, so any single-agent algorithm applies.

**Central Q-learning (CQL)** [Algorithm 4] is Q-learning over joint actions:
maintain $Q(s,a)$ for $a \in A$, act ε-greedily over joint actions, scalarise the
joint reward, and apply the standard update.

**What it buys:** it "circumvents the multi-agent aspects of the non-stationarity
and credit assignment problems" — there is only one learner, and joint-action
values *can* distinguish who contributed → [[credit-assignment]].

## Three limitations

**1. Reward scalarisation.** Single-agent RL needs one scalar $r$ from
$(r_1,\dots,r_n)$.
- **Common-reward games** — take $r = r_i$ for any $i$. Then an optimal
  single-agent algorithm yields a $\pi_c$ that is **a Pareto-optimal correlated
  equilibrium**. (Optimality ⇒ max expected return in every state ⇒
  [[pareto-optimality|Pareto-optimal]], since all agents share the reward ⇒ no
  agent gains by deviating ⇒ [[correlated-equilibrium|correlated equilibrium]].)
- **Zero-sum and general-sum** — "it is less clear how the reward scalarization
  should be done." Social welfare suggests $r = \sum_i r_i$, but **"if the desired
  solution is an equilibrium type solution, then no scalar transformation may
  exist that leads to equilibrium policies."**

**2. Exponential joint-action space.** $6^3 = 216$ in three-agent LBF; "most
standard single-agent RL algorithms do not scale easily to action spaces this
large" → [[scaling-in-number-of-agents]].

**3. Centralisation may be impossible.** Agents are "often localized entities
that are physically or virtually distributed", so communicating with a central
$\pi_c$ "may not be possible or desirable" → [[training-execution-modes]].

## When $\pi_c$ *can* be decomposed

In a **stochastic game** (full observability), yes. Central learning there
amounts to solving an MDP, and **MDPs always admit deterministic optimal
policies** [Eq. 2.26, [[value-functions-and-bellman]]], so
$$\pi_c(s) = (\pi_1(s) = a_1, \dots, \pi_n(s) = a_n)$$
[Eq. 5.9] — every agent just carries a copy of $\pi_c$, computes the joint
action, and executes its own component.

**In a POSG, no.** Each $\pi_i$ only has $o_i$, so the decomposition may not
exist. Partial observability is what breaks it →
[[partial-observability]].

## Related
[[independent-learning]] · [[credit-assignment]] · [[correlated-equilibrium]] ·
[[scaling-in-number-of-agents]] · [[training-execution-modes]]
