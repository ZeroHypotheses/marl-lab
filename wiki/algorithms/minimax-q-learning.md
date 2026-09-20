---
title: Minimax Q-Learning
type: algorithm
status: solid
sources: ["[[ch06-foundational-algorithms]]"]
updated: 2026-09-20
---

# Minimax Q-Learning

## One-line

Minimax Q-learning replaces Q-learning's greedy next-state value with the value
of the learned two-player zero-sum matrix game [Ch. 6.2.1].

## Setting

Finite, discounted, two-agent zero-sum stochastic games. The learner observes
states, both actions, and rewards and maintains joint-action values
$Q_i(s,a_i,a_j)$ [Algorithm 7; Ch. 6.2.1].

## Update rule

Use the [[joint-action-learning]] update with

$$
\operatorname{Value}_i(\Gamma_s)=
\max_{\pi_i}\min_{\pi_j}
\sum_{a_i,a_j}\pi_i(a_i)\pi_j(a_j)Q_i(s,a_i,a_j),
$$

where $\pi_i$ and $\pi_j$ are mixed policies in state $s$ [Ch. 6.2.1; see
[[minimax]]]. The corresponding minimax policy selects actions.

## Why it works / when it breaks

The zero-sum minimax-value operator is non-expansive, so discounting makes the
Bellman-style operator a contraction. With every state/joint-action pair sampled
infinitely often and standard stochastic-approximation learning rates, the
Q-values converge [Ch. 6.2.1]. The learned policy is robust against a worst-case
opponent, but may underexploit an opponent that is systematically weaker than
that worst case [Ch. 6.2.1]. The guarantee does not transfer to general-sum
games.

## Relation to

[[minimax]] · [[joint-action-learning]] · [[nash-q-learning]] ·
[[dynamic-programming]]

## In the codebase

No implementation is indexed in `upstream/codebase/`; the book instantiates
Algorithm 7 conceptually.

## Open questions

- How large is the robustness–exploitation trade-off against non-adversarial
  opponents in a small stochastic game?
