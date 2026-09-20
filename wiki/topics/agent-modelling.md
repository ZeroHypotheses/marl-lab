---
title: Agent Modelling
type: topic
status: solid
sources: ["[[ch03-games]]", "[[ch05-marl-in-games]]", "[[ch06-foundational-algorithms]]"]
updated: 2026-09-20
---

# Agent Modelling

Agent modelling estimates other agents' policies or hidden characteristics and
uses those predictions in the learner's own decision rule [Ch. 6.3]. It replaces
the equilibrium assumption “everyone follows this solution concept” with the
empirical question “what is this particular agent likely to do?”

## Generic decision rule

If agent $i$ has models $\hat\pi_{-i}$ of the other policies, it can choose

$$
\pi_i\in BR_i(\hat\pi_{-i}),
$$

where $BR_i$ is the [[best-response]] correspondence [Eq. 6.13]. This is useful
because MARL agents usually do not know the others' reward functions or policies
[Ch. 3.6]. Under partial observability they may first need to infer actions from
state changes before they can even update a model [Ch. 3.4].

## Three levels in Chapter 6

1. **[[fictitious-play]]:** estimate an opponent's policy by its empirical
   action frequencies, then best-respond [Eqs. 6.14–6.15].
2. **[[jal-agent-modelling]]:** condition those frequency estimates on state
   and combine them with a learned joint-action Q-function [Eqs. 6.16–6.17;
   Algorithm 8].
3. **Bayesian modelling and value of information:** maintain a posterior over
   possible opponent models and plan over both physical state and future belief
   updates [Eqs. 6.18–6.20].

The third level changes the meaning of an action's value. An action can be worth
taking because its observation distinguishes opponent types, even when its
immediate reward is worse. The repeated Prisoner's Dilemma example cooperates
to test whether the opponent is a cooperative `Grim` strategy or always defects;
near a finite horizon, that information loses value because there is little
time left to exploit it [Ch. 6.3.3].

## Assumptions and failure modes

- **Observability:** fictitious play and JAL-AM require observed opponent or
  joint actions [Ch. 6.3.1–6.3.2].
- **Stationarity:** empirical-frequency models converge cleanly only if the
  modelled policies settle; simultaneous learning violates this during
  training [Ch. 6.3.2].
- **Independence:** modelling each opponent separately and multiplying the
  policies cannot represent correlated joint behaviour [Eq. 6.17].
- **Model-space support:** Bayesian inference cannot learn a true opponent type
  excluded by its hypothesis class; the chapter states the required coverage in
  terms of absolute continuity [Ch. 6.3.3].
- **Strategic response:** once another learner reacts to being modelled, the
  prediction target and the learner's actions co-determine one another
  [Ch. 6.3].

## Relation to equilibrium selection

In Stag Hunt, predictions can help a learner condition on likely cooperation
instead of treating the other agent as uncontrolled noise. They do not by
themselves guarantee the reward-dominant equilibrium: exploration, learning
rates, initial data, and the way predictions enter the update still determine
the learning path [Ch. 5.4.2; Ch. 6.3].

## Related

[[knowledge-assumptions]] · [[best-response]] · [[equilibrium-selection]] ·
[[partial-observability]] · [[ch06-foundational-algorithms]]
