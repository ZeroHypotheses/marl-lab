---
title: Generalized Infinitesimal Gradient Ascent (GIGA)
type: algorithm
status: solid
sources: ["[[ch06-foundational-algorithms]]"]
updated: 2026-09-20
---

# Generalized Infinitesimal Gradient Ascent (GIGA)

## One-line

GIGA performs projected gradient ascent directly in each agent's policy simplex
and guarantees sublinear external regret [Ch. 6.4.5].

## Setting

Repeated finite normal-form games with any finite number of agents and actions.
An agent observes the others' realised actions, but not their policies, and uses
its own reward function to compute a reward gradient [Ch. 6.4.5].

## Update rule

For episode $z$, agent $i$ takes a gradient step and projects it back onto the
probability simplex:

$$
\pi_i^{z+1}=P_{\Delta(A_i)}
\left(\pi_i^z+\eta_z\nabla_{\pi_i}U_i
(\pi_i^z, a_{-i}^z)\right),
$$

where $P_{\Delta(A_i)}$ is Euclidean projection, $\eta_z$ is the step size, and
$a_{-i}^z$ is the observed opponent action profile [Eqs. 6.50–6.51].

## Why it works / when it breaks

With a step size proportional to $1/\sqrt z$, regret grows only as
$O(\sqrt z)$, so average regret vanishes regardless of the other agents'
behaviour [Ch. 6.4.5]. If all agents do this, their empirical joint-action
distribution approaches the set of coarse correlated equilibria. This does not
imply that the current policies converge, nor that their realised returns are
optimal [Ch. 6.4.5; [[no-regret]]].

## Relation to

[[no-regret]] · [[regret-matching]] · [[correlated-equilibrium]] ·
[[wolf-policy-hill-climbing]]

## In the codebase

No implementation is indexed in `upstream/codebase/`; the book presents GIGA
in §6.4.5.

## Open questions

- How does simplex projection compare empirically with regret matching in the
  same small game?
