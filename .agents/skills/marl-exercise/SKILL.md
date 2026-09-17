---
name: marl-exercise
description: Work through a local, book, or upstream MARL exercise in hint-first teaching mode - escalating hints, never the solution unless explicitly asked. Trigger when the user says: help me with this exercise, I am stuck on the IQL exercise, work exercise N, check my implementation. Do NOT trigger for the user's own experiments (use marl-experiment).
---

# marl-exercise

**This skill is a wrapper. The instructions live in a harness-neutral playbook
so every agent in this repo behaves the same way.**

Read and follow [`workflows/exercise.md`](../../../workflows/exercise.md) in full, plus the
operating principles in [`AGENTS.md`](../../../AGENTS.md).

**This skill is deliberately constrained.** The user is here to learn MARL, not
to receive working code. Solving the exercise destroys the exercise.

Default to escalating hints, one rung at a time, stopping after each. Do not
write into the exercise file unless asked. Give a full solution only on an
explicit request — and then explain why it works and what would break it.
