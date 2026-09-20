---
title: Fictitious Play
type: algorithm
status: solid
sources: ["[[ch06-foundational-algorithms]]"]
updated: 2026-09-20
---

# Fictitious Play

## One-line

Fictitious play models each opponent by its empirical action frequencies and
plays a best response to those models [Ch. 6.3.1].

## Setting

Repeated finite normal-form games. Each agent knows its own reward function and
observes the other agents' actions; it need not know their rewards or current
policies [Ch. 6.3.1].

## Update rule

For opponent $j$, after $z$ rounds estimate

$$
\hat\pi_j^z(a_j)=\frac{1}{z}\sum_{e=1}^{z}
\mathbf{1}\{a_j^e=a_j\},
$$

where $a_j^e$ is $j$'s action in round $e$ [Eq. 6.14]. Agent $i$ then chooses a
deterministic best response to the product of the estimated opponent policies
[Eq. 6.15].

## Why it works / when it breaks

The empirical models smooth a changing sequence of actions into a prediction.
For finite-action two-player zero-sum games, and several other game classes,
the empirical distributions converge to Nash equilibrium [Ch. 6.3.1]. The
actual best-response actions may keep cycling—as in Rock-Paper-Scissors—so this
is not necessarily pointwise policy convergence [Ch. 5.2; Ch. 6.3.1]. The
product model also assumes opponents act independently, and a uniform average
can adapt slowly when their behaviour changes.

## Relation to

[[agent-modelling]] · [[best-response]] · [[jal-agent-modelling]] ·
[[convergence-types]]

## In the codebase

No implementation is indexed in `upstream/codebase/`; the update is given by
Eqs. 6.14–6.15.

## Open questions

- How should recent evidence be weighted when opponents are genuinely
  non-stationary rather than converging?
