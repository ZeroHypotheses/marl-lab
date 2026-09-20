---
title: A Hands-On Study Loop for marl-lab
type: note
status: solid
sources: ["[[ch02-reinforcement-learning]]", "[[ch03-games]]", "[[ch05-marl-in-games]]", "[[ch06-foundational-algorithms]]", "[[ch07-deep-learning]]", "[[ch08-deep-rl]]", "[[ch09-deep-marl]]", "[[iql-tabular]]"]
updated: 2026-09-20
---

# A hands-on study loop for marl-lab

The best first implementation after Chapters 1–5 is the **tabular Independent
Q-Learning exercise** in `upstream/exercises/tabular_marl/iql.py`. It turns the
Q-learning and ε-greedy machinery from [Ch. 2.6] into the independent learners
described in [Ch. 5.3.2], while the one-step, stateless Prisoner's Dilemma keeps
the mechanics visible → [Tabular IQL](../topics/iql-tabular.md).

## The loop

Use a short cycle for each new concept:

1. **Predict before running.** State what each algorithm should learn, what the
   plot should look like, and what observation would falsify that prediction.
2. **Implement the smallest missing mechanism.** For IQL, write `act()` first,
   then `learn()`; translate [Eq. 2.55] and [Eq. 2.58] into the per-agent data
   structures without adding abstractions.
3. **Run the supplied baseline.** Inspect evaluation returns and both Q-tables.
   Explain the result using the payoff matrix before changing anything.
4. **Change one cause at a time.** Start with the ε schedule, then learning
   rate, then random seed. Keep the baseline fixed while varying one factor.
5. **Write the conclusion in the wiki.** Record what the result taught, what
   remains unclear, and whether the evidence supports the prediction. A
   learning curve alone does not establish convergence to a solution
   [Ch. 5.2] → [convergence types](../topics/convergence-types.md).

## Questions to answer during the IQL exercise

- Why does the terminal flag matter to the Q-learning target even though
  `gamma=0.99` is configured?
- Which action is dominant in the exercise's payoff matrix, and which joint
  action is the unique [Nash equilibrium](../topics/nash-equilibrium.md)?
- Why can the agents' learned values move even though the environment's payoff
  matrix never changes? → [non-stationarity](../topics/non-stationarity.md)
- Do evaluation returns and Q-values tell the same story?
- Does the apparent result survive several seeds and a different ε decay?

The final two questions turn the coding exercise into a small experiment.
Prisoner's Dilemma is particularly useful because idealised IQL is not
guaranteed to converge in this game class and may obtain average rewards above
the unique Nash-equilibrium reward [Ch. 5.3.2].

## Cadence

A productive cadence is: read one section, predict, implement or inspect one
mechanism, run it, explain the result aloud, then file the durable insight. Use
[Tabular IQL](../topics/iql-tabular.md) immediately after Chapters 1–5;
continue into Chapter 6 only
after the Q-learning-to-IQL connection is comfortable enough to explain
without looking at the code.

## Bridge from matrix games to Chapter 6

The Prisoner's Dilemma and Stag Hunt experiments are not discarded: a
stochastic game associates a normal-form game with every state. Their one-step
environments are degenerate cases in which there is no continuation value
[Ch. 3.3; Ch. 6.1]. The missing Chapter 6 mechanism is the dependence of each
state game's payoff matrix on transitions and bootstrapped future values.

Add that mechanism in two steps:

1. Implement Shapley value iteration for a tiny, fully known, two-state
   zero-sum stochastic game. Check that different initial value vectors converge
   to the same values and that their max-norm distance shrinks at no more than
   the discount factor. This isolates Algorithm 6's model-based minimax backup.
2. After reading §6.2.1, replace the known transition expectation with sampled
   transitions to obtain minimax Q-learning. This isolates the move from
   dynamic programming to temporal-difference learning.

Do not begin this bridge with stochastic Stag Hunt: combining state dynamics,
multiple general-sum Nash equilibria, and equilibrium selection would introduce
three new mechanisms at once. Revisit general-sum stochastic games after the
zero-sum backup is understood.

## Fast path from Chapter 6 to Chapter 9

Readers already comfortable with deep learning and deep RL can skip a linear
reading of Chapters 7 and 8 after completing Chapter 6. Chapter 7 is background
on function approximation, neural networks, optimization, CNNs, and RNNs.
Chapter 8 supplies the single-agent algorithms and notation that Chapter 9
extends [Ch. 7; Ch. 8; Ch. 9 introduction].

Use Chapters 7 and 8 as references if the following are already comfortable:

- DQN, including replay buffers, online and target networks, and the TD target;
- policy gradients, REINFORCE, actor–critic, advantage estimates, A2C, and PPO;
- on-policy versus off-policy learning and bootstrapping;
- the distinction between environment state, agent observation, and observation
  history under partial observability;
- recurrent policies or value functions for sequence-dependent decisions.

Before starting Chapter 9, skim §8.3 and §9.2 to align with the book's
state/observation conventions and its $\phi_i$ policy-parameter versus $\theta_i$
value-parameter notation. Return to §§8.1 or 8.2 only when Chapter 9's
value-based or policy-gradient derivations expose a gap.

### Accelerated route when deep MARL is the priority

A reader who already knows deep RL does not need to finish every Chapter 6
derivation or implement every foundational algorithm before starting Chapter 9.
The safe shortcut is to skip the **catalogue**, not the conceptual bridge
[Ch. 6; Ch. 9].

Minimum viable Chapter 6 pass:

1. Read §6.1 closely: understand that each stochastic-game state induces a
   normal-form continuation game, and that a solution-concept operator replaces
   the single-agent maximum in the Bellman backup [Eqs. 6.3–6.8].
2. Read the beginning of §6.2 through Eq. 6.11, then §6.2.4. Know how a
   minimax/Nash/correlated value enters a TD target and why joint-action values
   can still be insufficient.
3. Read the §6.3 introduction and the JAL-AM idea in §6.3.2. Chapter 9.6 later
   replaces these tabular agent models with neural representations.
4. Read §6.6. Treat the detailed Nash-Q, correlated-Q, IGA, WoLF, GIGA, and
   regret-matching derivations as references until a later topic needs them.

Then start Chapter 9 at §§9.1–9.5: training/execution modes, independent deep
learning, centralised critics, and value decomposition. Backfill §6.3 before
Chapter 9.6 if neural agent modelling is important, and §§6.4–6.5 when studying
learning dynamics, regret, or equilibrium convergence in depth.

This route is appropriate for becoming productive with modern deep-MARL
algorithms quickly. It is not equivalent to mastering MARL foundations: a full
skip makes it easier to mistake function approximation for the main conceptual
advance and obscures why different strategic operators have different
information and convergence requirements [Ch. 6.1–6.5].

### Keep the shortcut adaptive

This route is provisional. At each reading or experiment transition, explicitly
name the sections being deferred and the concepts assumed from them. Continue
on the fast path only while the reader can connect the current mechanism to the
strategic problem it addresses—for example, why a centralised critic, mixing
network, or agent model changes the information available during learning
[Ch. 5; Ch. 6; Ch. 9].

Pause and backfill when a skipped dependency causes repeated confusion, the
book starts using unexplained assumptions or notation, or an implementation can
be followed mechanically but not explained conceptually. Backfill the smallest
relevant section first, then revise this route if the same kind of gap recurs.
The decision to accelerate is a working hypothesis and may be changed as the
reader's experience supplies better evidence.

## Related

[Tabular IQL](../topics/iql-tabular.md) ·
[independent learning](../topics/independent-learning.md) ·
[temporal-difference learning](../topics/temporal-difference-learning.md) ·
[learning curves](../topics/learning-curves.md) ·
[[bcn-summer-school]]
