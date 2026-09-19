---
title: Pareto Optimality
type: topic
status: solid
sources: ["[[ch04-solution-concepts]]"]
updated: 2026-09-19
---

# Pareto Optimality

A **refinement**, used to narrow the space of equilibria [Ch. 4.8, Def. 9].

$\pi$ is **Pareto-dominated** by $\pi'$ if
$$\forall i : U_i(\pi') \ge U_i(\pi) \quad\text{and}\quad \exists i : U_i(\pi') > U_i(\pi)$$
[Eq. 4.25]

$\pi$ is **Pareto-optimal** if nothing Pareto-dominates it — no agent can be made
better off without making another worse off. (Some game theory literature says
"Pareto-efficient/inefficient".)

## Why this is not Nash equilibrium

The two definitions quantify over different changes:

- Nash holds the other agents' policies fixed and asks whether **one agent**
  can profitably deviate: $(\pi_i',\pi_{-i})$ [Ch. 4.4, Eq. 4.16].
- Pareto optimality permits an entirely different **joint policy** $\pi'$ and
  asks whether all agents weakly improve and at least one strictly improves
  [Ch. 4.8, Eq. 4.25].

Therefore neither property implies the other. In Stag Hunt, hare/hare is Nash
but is Pareto-dominated by stag/stag: reaching the improvement requires both
agents to change together. In Prisoner's Dilemma, cooperate/cooperate is
Pareto-optimal but not Nash: either agent can profit by deviating alone while
the other continues to cooperate [Ch. 4.7; Ch. 5.4.2]. Nash measures
**unilateral stability**; Pareto optimality measures **joint efficiency**.

**Every game has at least one Pareto-optimal joint policy.** In common-reward
games, all Pareto-optimal joint policies achieve the same expected return, which
is the maximum achievable → [[reward-structures]].

## Why a refinement is needed

Equilibria alone are too permissive: different equilibria pay agents very
differently, and the **folk theorems** say essentially any feasible, enforceable
return profile is realisable by *some* equilibrium — making the space "very large
or infinite" [Ch. 4.8]. Pareto optimality carves out a frontier.

Fig. 4.4 plots the convex hull of feasible joint returns in Chicken (900 joint
policies from discretising each agent's policy in steps of $\tfrac{1}{30}$). The
hull's corners are the four deterministic joint actions; the **Pareto frontier**
is the red edge. Both the deterministic and probabilistic Nash equilibria are
plotted against it. In Chicken the minmax value is 2 for both, so any hull point
with $U_1, U_2 \ge 2$ is equilibrium-realisable — the frontier is what picks out
the desirable ones.

## Its own limits

- **Pareto optimality does not imply equilibrium**, nor the reverse.
- "All joint policies in zero-sum games are Pareto-optimal by definition" — so
  it says nothing there.
- In general-sum games many Pareto-optimal policies are still undesirable,
  notably those with "large differences between the agents' expected returns"
  — which is why [[social-welfare-and-fairness]] follows.

**Welfare optimality ⇒ Pareto optimality** (proved in §4.9), but not conversely.

## Related
[[social-welfare-and-fairness]] · [[nash-equilibrium]] · [[solution-concepts]] ·
[[reward-structures]]
