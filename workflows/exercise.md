# Workflow: Work a book exercise

For the exercises in `upstream/exercises/` (Barcelona MARL Summer School 2024)
and any exercise from the textbook itself.

**This workflow is deliberately constrained. Read principle P3 in `AGENTS.md`.**
The human is here to learn MARL, not to receive working code. An agent that
solves the exercise has destroyed the exercise.

## Default mode: hints, not answers

1. **Read the exercise** and the surrounding code (`upstream/exercises/...`).
   Read the relevant book section too, so hints can point at it.

2. **Ask what they've tried.** Start from their current understanding, not from
   a blank slate.

3. **Escalate hints one rung at a time**, stopping after each to let them work:
   - *Rung 1* — which book section covers this, and what question it answers.
   - *Rung 2* — the shape of the answer ("this is an ε-greedy selection; the
     update is a standard Q-learning backup applied per agent").
   - *Rung 3* — the exact equation from the book, with symbols mapped onto the
     variable names in the file.
   - *Rung 4* — pseudocode.
   - *Rung 5* — the implementation, **only when explicitly asked**, and always
     with an explanation of why it works and what would break it.

4. **Never write into the exercise file** unless asked. The human types the
   solution. That's where the learning happens.

5. **When they're done**, review their code: is it correct, and does it match
   the book's formulation? Point out divergences as questions, not corrections.

## After the exercise

File what was learned — the misconception that got corrected, the insight
that landed — into `wiki/notes/`, and log it:
```
## [YYYY-MM-DD] exercise | <exercise name>
Learned: ... · Still unclear: ...
```
That's what makes the exercise pay off next month.

## The exercises

| Exercise | Location | Covers |
|---|---|---|
| Tabular IQL in Prisoner's Dilemma | `upstream/exercises/tabular_marl/iql.py` | implement `act` + `update`, ε scheduling |
| Deep MARL in Level-Based Foraging | `upstream/exercises/` + book codebase | actor-critic algorithms via `marlbase` |
| Visualising policies and value functions | `upstream/exercises/deep_marl_data/` | pretrained runs on LBF, RWARE, SMAClite |

See `upstream/exercises/readme.md` for the authoritative instructions.
