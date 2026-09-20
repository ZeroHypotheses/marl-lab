---
title: Joint-Action Learning with Game-Theoretic Operators
type: algorithm
status: solid
sources: ["[[ch06-foundational-algorithms]]"]
updated: 2026-09-20
---

# Joint-Action Learning with Game-Theoretic Operators

## One-line

JAL-GT learns a payoff table over joint actions at each state and solves that
learned state game inside its temporal-difference target [Ch. 6.2].

## Setting

A finite stochastic game with observable states, joint actions, and every
agent's reward. Each learner stores one $Q_j(s,a)$ for **every** agent
$j\in I$, state $s$, and joint action $a$ [Algorithm 7]. This is decentralised
learning with unusually strong observations: the update is performed
independently, but each learner sees enough to reconstruct every agent's state
game [Ch. 6.2].

## Update rule

At state $s$, define a normal-form game $\Gamma_s$ with payoff
$R_{\Gamma_s,i}(a)=Q_i(s,a)$ [Eq. 6.10]. Given transition
$(s,a,r,s')$, update

$$
Q_i(s,a)\leftarrow Q_i(s,a)+\alpha
\left[r_i+\gamma\operatorname{Value}_i(\Gamma_{s'})-Q_i(s,a)\right],
$$

where $\alpha$ is the learning rate, $\gamma$ the discount factor, and
`Value` is defined by a chosen solution concept [Eq. 6.11; Algorithm 7]. The
same concept supplies the action policy for the current state game.

## Where the Q-functions are learned

Algorithm 7 uses two agent indices with different roles. Its heading fixes
$i$ as the agent controlled by this copy of the algorithm. The loop variable
$j\in I$ on lines 8–9 ranges over the **entire** agent set, including $j=i$.
Consequently, one learner maintains and updates local estimates of
$Q_1,\ldots,Q_n$, not only its controlled agent's $Q_i$.

The policy-selection step does not update a Q-function. First, the current
tables $Q_1(s,\cdot),\ldots,Q_n(s,\cdot)$ are treated as the payoff functions of
$\Gamma_s$ and solved to obtain $(\pi_1,\ldots,\pi_n)$; the controlled agent then
samples its own action from $\pi_i$ [Eq. 6.10; Algorithm 7, lines 5–6]. After the
environment reveals the complete joint action, every reward, and the next
state, Algorithm 7 applies the temporal-difference update above to the observed
entry $Q_j(s,a)$ for every agent $j$ [Algorithm 7, lines 7–9].

Thus $Q_i$ is agent $i$'s value function, but it is indexed by the **joint**
action and is not generally sufficient by itself to choose $a_i$. In a
general-sum game, the solution for $\pi_i$ depends on the full learned game,
including the other agents' payoff tables $Q_j$. This differs from IQL, where
agent $i$ greedily or ε-greedily selects directly from $Q_i(s,a_i)$ while
ignoring the other agents [Ch. 5.3.2; Ch. 6.2]. In a two-agent zero-sum game,
one payoff table determines the other, so minimax can be computed from a single
agent's table.

## Why it works / when it breaks

The construction is the model-free analogue of Shapley value iteration: the
solution operator replaces Q-learning's single-agent $\max$ [Ch. 6.1–6.2]. Its
properties depend entirely on that operator. Minimax gives a contraction in
the zero-sum case; Nash and correlated-equilibrium variants face discontinuous
or ambiguous equilibrium selection [Ch. 6.2.1–6.2.3]. Moreover, joint-action
Q-values may be insufficient to identify the stationary probabilistic policy
needed by a game [Ch. 6.2.4].

## Relation to

[[minimax-q-learning]] · [[nash-q-learning]] · [[correlated-q-learning]] ·
[[jal-agent-modelling]] · [[temporal-difference-learning]] ·
[[independent-learning]]

## In the codebase

No Chapter 6 JAL-GT implementation is indexed in `upstream/codebase/`; the
book presents Algorithm 7 as pseudocode.

## Open questions

- What minimal additional state or coordination signal resolves the
  insufficiency example in §6.2.4?
