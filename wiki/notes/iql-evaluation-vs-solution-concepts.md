---
title: IQL Evaluation vs. Solution Concepts
type: note
status: solid
sources: ["[[ch04-solution-concepts]]", "[[ch05-marl-in-games]]", "[[iql-tabular]]"]
updated: 2026-09-12
---

# IQL evaluation vs. solution concepts

The tabular exercise's `iql_eval` is a **performance evaluator**, not a
**solution-concept evaluator**. It executes the current independent
$\epsilon$-greedy policies for 500 episodes and reports each agent's sample mean
and standard deviation of return
[`train_iql.py:28`](../../upstream/exercises/tabular_marl/train_iql.py#L28),
[`train_iql.py:48`](../../upstream/exercises/tabular_marl/train_iql.py#L48),
[`train_iql.py:61`](../../upstream/exercises/tabular_marl/train_iql.py#L61).
That estimates $U_i(\pi)$, the quantity from which solution concepts are
defined, but it does not test any of their defining relations.

This distinction matters because a MARL problem is a game model **plus a
solution concept** [Ch. 4, Fig. 4.1]. A vector of high, low, or stable returns
does not by itself establish that a policy is a [[nash-equilibrium]], is
[[pareto-optimality|Pareto-optimal]], or satisfies any of the convergence
criteria in [[convergence-types]] [Ch. 5.2].

## What the exercise actually evaluates

`iql_eval` loads the learned per-agent Q-tables into fresh IQL agents, acts with
`eval_epsilon = 0.05`, and aggregates rewards
[`train_iql.py:16`](../../upstream/exercises/tabular_marl/train_iql.py#L16),
[`train_iql.py:39`](../../upstream/exercises/tabular_marl/train_iql.py#L39).
It therefore answers:

> What returns does this exploratory joint behaviour produce empirically?

It does **not** answer:

> Is each agent's policy a best response to the other agent's policy?

The second question is the [[nash-equilibrium|Nash]] test [Ch. 4.4, Eq. 4.16].
For each agent $i$, a solution-aware evaluator would compute its unilateral
deviation gain

$$
\delta_i = \max_{\pi_i'} U_i(\pi_i', \pi_{-i}) - U_i(\pi).
$$

The joint policy is Nash when every $\delta_i=0$, and $\epsilon$-Nash when
every $\delta_i\le\epsilon$ [Ch. 4.4--4.5]. In this one-step finite matrix game,
testing deterministic deviations is enough to find the maximum because
expected return is linear in an agent's mixed policy.

## What the Prisoner's Dilemma lets us infer

The exercise uses $(C,C)=(3,3)$, $(C,D)=(0,5)$, $(D,C)=(5,0)$, and
$(D,D)=(1,1)$
[`matrix_game.py:45`](../../upstream/exercises/tabular_marl/matrix_game.py#L45).
Defection strictly dominates cooperation for both agents, so:

- $(D,D)$ is the unique Nash equilibrium, paying $(1,1)$;
- $(C,C)$ pays $(3,3)$ and is welfare-optimal, fairness-optimal, and
  Pareto-optimal, but it is not Nash because either agent can gain by defecting;
- [[minimax]] is not the relevant chapter-4 equilibrium concept because this is
  a general-sum game, not a two-agent zero-sum game [Ch. 4.3--4.4].

Thus, if the greedy actions implied by both learned Q-tables are $D$, we can
identify the underlying greedy joint policy with the unique Nash equilibrium.
But `iql_eval` itself neither makes nor verifies that claim. Its nonzero
evaluation exploration also means the reported mean returns describe a noisy
behaviour policy rather than the exact greedy joint policy.

## Other concepts need different measurements

- **Pareto/welfare/fairness:** compare the learned return vector with the
  feasible return set or enumerate this small payoff matrix [Ch. 4.8--4.9].
- **No-regret:** retain the episode-by-episode action history and compare actual
  rewards with counterfactual fixed actions; a final mean return is insufficient
  [Ch. 4.10, Eqs. 4.28--4.29].
- **Learning convergence:** inspect the policy or empirical joint-action
  distribution over training, not just a flat evaluation-return curve
  [Ch. 5.2, Eqs. 5.3--5.8].

The larger lesson is that [[independent-learning|IQL]] is a learning rule, not a
solution concept. It can sometimes arrive at a Nash equilibrium, fail to
converge, or even average above an equilibrium's reward while oscillating
[Ch. 5.3.2]. The evaluator must state separately which of those outcomes it is
trying to recognise.

## Related

[[iql-tabular]] · [[solution-concepts]] · [[best-response]] ·
[[learning-curves]] · [[no-regret]]
