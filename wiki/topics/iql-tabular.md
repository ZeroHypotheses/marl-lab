---
title: Tabular IQL (the exercise)
type: algorithm
status: solid
sources: ["[[ch05-marl-in-games]]", "upstream/exercises/tabular_marl/"]
updated: 2026-09-17
---

# Tabular IQL — the Barcelona exercise

`upstream/exercises/tabular_marl/` — implement
[[independent-learning|independent Q-learning]] for the non-repeated
Prisoner's Dilemma.

> 🎓 **This is an exercise. Hints only unless you ask outright** — see
> `workflows/exercise.md` and AGENTS.md P3.

## What you implement

Two methods in `iql.py`; everything else (environment, training loop,
plotting) is written.

| Method | What it is | Book reference |
|---|---|---|
| `act(obss)` | ε-greedy action selection, per agent | [Eq. 2.55] → [[temporal-difference-learning]] |
| `learn(obss, actions, rewards, n_obss, done)` | Q-learning update, per agent | [Eq. 2.58], applied as [Algorithm 5] |

`schedule_hyperparameters` is already written (linear ε decay to 0.01 over 80%
of training) and you're invited to change it.

The whole thing is **~15 lines**. The value is not the typing — it is that
Algorithm 5 in the book and `learn()` here are the same object, and writing it
makes that concrete.

## Setup

Runs in the project venv as-is — `gymnasium`, `numpy`, `matplotlib` are already
installed by `uv sync`:

```bash
cd upstream/exercises/tabular_marl
../../../.venv/bin/python train_iql.py
```

Before implementing, it raises `NotImplementedError` from `act()` — that is the
"wired up correctly" signal.

> ⚠️ `upstream/` is read-only for **agents** (P5). You are the exception — this
> is your exercise. Just don't commit into the submodule; if you want to keep
> your solution, copy it to `experiments/`.

## The environment

`matrix_game.py` — stateless (observation is always `0`), `ep_length=1`, so
this is the **non-repeated** normal-form game → [[normal-form-games]],
[[repeated-normal-form-games]].

Action **0 = cooperate**, **1 = defect**.

> ⚠️ **The payoff matrix differs from the book's.** `create_pd_game` uses
> positive rewards:
>
> | | C | D |
> |---|---|---|
> | **C** | 3, 3 | 0, 5 |
> | **D** | 5, 0 | 1, 1 |
>
> The book's Fig. 3.2(c) uses negative rewards: (C,C)=(−1,−1), (C,D)=(−5,0),
> (D,C)=(0,−5), (D,D)=(−3,−3).
>
> **Both are genuine Prisoner's Dilemmas** — what defines the game is the
> ordinal structure $T > R > P > S$, satisfied by $5 > 3 > 1 > 0$ and by
> $0 > -1 > -3 > -5$ alike. But the numbers on your plots will not match the
> numbers in the book, and D is still dominant in both. Don't spend twenty
> minutes hunting a bug that isn't there.

### Prison sentences are costs, not rewards

The familiar story may instead label outcomes by **years in prison**: mutual
cooperation costs one year each, mutual defection costs two, and the exploited
cooperator serves three while the defector goes free
([Wikipedia, “Prisoner's dilemma”](https://en.wikipedia.org/wiki/Prisoner%27s_dilemma)).
Those numbers must be **minimised**, whereas the book and this exercise use
rewards that agents maximise. Converting sentence cost $c$ to reward $-c$
gives $(C,C)=(-1,-1)$ and $(D,D)=(-2,-2)$; cooperation is still collectively
better because $-1>-2$. The numerical magnitudes are presentation choices—the
defining preference order remains $T>R>P>S$.

## What to expect, and why it's interesting

The unique [[nash-equilibrium]] is (D,D) — here paying **1 each**, while (C,C)
pays **3 each**. So converging to the equilibrium means converging to the worse
outcome for everyone. That is §4.7's *sub-optimality* limitation, live on your
own plot → [[solution-concepts]].

And Prisoner's Dilemma is **class 3b** in Fig. 5.2 ([[independent-learning]]):
one deterministic Nash equilibrium, no probabilistic one, a dominant action, and
a joint action that beats the equilibrium for both. IQL's convergence there is
listed as **"Y/N"** — converges only under some conditions. Wunder, Littman &
Babes (2010) found idealised IQL can be **chaotically non-convergent while
averaging above the Nash equilibrium reward**.

> So the honest question to hold while watching your Q-values: *does it settle
> on (D,D), and does that depend on the learning rate and ε schedule?* That is a
> real open experiment, not a checkbox → `workflows/experiment.md`.

## Visualisations provided

`utils.py` gives `visualise_q_tables`, `visualise_q_convergence` and
`visualise_evaluation_returns` — Q-values per agent, convergence over training,
and evaluation returns. Note these are **evaluation** returns under
$\epsilon = 0.05$, in the sense of [[learning-curves]]. They estimate achieved
returns but do not test a game-theoretic solution concept; see
[[iql-evaluation-vs-solution-concepts]].

## Related
[[independent-learning]] · [[temporal-difference-learning]] ·
[[normal-form-games]] · [[nash-equilibrium]] · [[non-stationarity]] ·
[hands-on study loop](../notes/hands-on-study-loop.md) ·
[[first-tabular-iql-exercise]] · [[exp-02-iql-stag-hunt-selection]]
