---
title: Regret Matching
type: algorithm
status: solid
sources: ["[[ch06-foundational-algorithms]]"]
updated: 2026-09-20
---

# Regret Matching

## One-line

Regret matching chooses future actions in proportion to positive average gains
from counterfactually replacing past actions [Ch. 6.5.1].

## Setting

Repeated finite normal-form games. Each agent needs its own reward function and
the realised joint actions, so it can evaluate counterfactual rewards for its
alternative actions [Ch. 6.5.1]. No assumption is made about how the other
agents choose their actions [Ch. 6.5.2].

## Update rule

Unconditional regret for replacing all past choices by $a_i$ is the average
counterfactual payoff gain

$$
\bar r_i^z(a_i)=\frac1z\sum_{e=1}^{z}
\left[R_i(\langle a_i,a_{-i}^e\rangle)-R_i(a^e)\right].
$$

The next policy assigns probability proportional to
$[\bar r_i^z(a_i)]_+=\max(0,\bar r_i^z(a_i))$; if all positive parts are zero,
any policy may be used [Eqs. 6.53–6.55]. Conditional regret instead measures
the gain from replacing only occurrences of one previous action with another,
and conditions the next policy on the most recent action [Eqs. 6.56–6.58].

## Why it works / when it breaks

Average regret falls at rate $O(1/\sqrt z)$ [Ch. 6.5.2]. If every agent uses
unconditional regret matching, the empirical joint-action distribution
approaches the set of coarse correlated equilibria; conditional regret matching
approaches the set of correlated equilibria [Ch. 6.5.2]. The actual policies
can continue changing, so the guarantee is not pointwise policy convergence.
Counterfactual rewards must also be computable from the observed outcome and
known reward function.

## Relation to

[[no-regret]] · [[correlated-equilibrium]] ·
[[generalized-infinitesimal-gradient-ascent]] · [[convergence-types]]

## In the codebase

No implementation is indexed in `upstream/codebase/`; the book gives the update
in Eqs. 6.53–6.58.

## Open questions

- How do tie handling and the arbitrary zero-positive-regret policy affect
  finite-time behaviour without changing the asymptotic guarantee?
