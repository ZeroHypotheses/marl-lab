---
title: "Ch. 3 — Games: Models of Multi-Agent Interaction"
type: source
status: solid
sources: ["MARL book, Ch. 3, pp. 43–60 (2nd printing)"]
updated: 2026-09-11
---

# Chapter 3 — Games: Models of Multi-Agent Interaction

Formalises what [[ch01-introduction]] described informally. Defines a
**hierarchy of game models** [Fig. 3.1] and the reward-structure taxonomy — but
deliberately **does not** define what it means to *solve* one. That's
[[ch04-solution-concepts]].

Only 8 numbered equations; this is a definitional chapter.

> 📕 errata: p48 — footnote 6 removed. Our copy shows footnote 5 at that point,
> consistent with the 2nd printing. See [[errata]].

## The hierarchy

```
        POSG  (n agents, m states, partially observed)
          │
    Stochastic Game  (n agents, m states, fully observed)
          │
    ┌─────┴─────┐
Repeated NFG    MDP
(n agents,     (1 agent,
 1 state)       m states)
```
[Fig. 3.1]

Each is a special case of the one above:
- **MDP** = stochastic game with one agent → [[markov-decision-process]]
- **Repeated normal-form game** = stochastic game with $|S| = 1$, $\bar{S} = \emptyset$
- **Stochastic game** = POSG where $o_i^t = (s^t, a^{t-1})$
- **POMDP** = POSG with one agent
- **Dec-POMDP** = POSG with common rewards

Pages: [[normal-form-games]] · [[repeated-normal-form-games]] ·
[[stochastic-games]] · [[partial-observability]]

**Normal-form games are the basic building block.** With rewards written
$R_i(s,a)$, every state of a stochastic game *is* a non-repeated normal-form
game with rewards $R_i(s,\cdot)$ [Fig. 3.3, §3.3]. The analogy the book draws:
normal-form game is to stochastic game as multi-armed bandit is to MDP.

> Out of scope: **extensive-form games**, where agents act in turns rather than
> simultaneously [footnote 1]. The book uses simultaneous-move games because
> most MARL research does and because they extend MDPs more naturally;
> transformations between the two exist (Shoham & Leyton-Brown 2008).

## Reward classification — the formal definitions

Carries over unchanged from normal-form games to stochastic games and POSGs
[§3.1, §3.3, §3.4]:

| | Condition |
|---|---|
| **Zero-sum** | $\sum_{i \in I} R_i(a) = 0$ for all $a \in A$ |
| **Common-reward** | $R_i = R_j$ for all $i, j \in I$ |
| **General-sum** | no restriction |

Two agents and zero-sum ⇒ $R_i = -R_j$. Zero-sum is a special case of
**constant-sum** (rewards sum to a constant) [footnote 2].
→ [[reward-structures]]

## §3.6 — What agents know

The chapter's most consequential section for MARL practice, and the multi-agent
counterpart to the MDP knowledge assumption in [[ch02-reinforcement-learning]].

Game theory's default is a **complete knowledge game**: everyone knows every
action space, reward function, $S$, $T$, and all observation functions.
**MARL sits at the opposite end** — agents typically know neither others' reward
functions *nor their own*, and nothing of $T$ or $O_i$ ("incomplete information
game", Harsanyi 1967). → [[knowledge-assumptions]]

## §3.7 — RL ↔ game theory dictionary

Fig. 3.5 maps the vocabularies, since the book uses RL terms throughout:
environment/game, agent/player, reward/payoff-utility, policy/strategy,
deterministic/pure, probabilistic/mixed, joint X / X profile.
→ [[rl-game-theory-dictionary]]

## Other contents

- **§3.2** repeated games — policies condition on joint-action history;
  finite ≠ infinite repetition (end-game effects) → [[repeated-normal-form-games]]
- **§3.4.1** belief states and filtering [Eq. 3.5] → [[partial-observability]]
- **§3.5** modelling communication [Eqs. 3.6–3.7] → [[communication-in-games]]

## Closing frame

> "Similarly to single-agent RL, a learning problem in MARL is given by the
> combination of a game model and a learning objective for the agents" [§3.8].

Exactly parallel to Fig. 2.1 in [[ch02-reinforcement-learning]]. This chapter
supplies the model; [[ch04-solution-concepts]] supplies the objective. Many of
the six dimensions of Fig. 1.4 are fixed by the game specification.

## Related
[[normal-form-games]] · [[stochastic-games]] · [[partial-observability]] ·
[[reward-structures]] · [[knowledge-assumptions]] · [[ch04-solution-concepts]]
