---
name: marl-experiment
description: Scaffold and run a new MARL experiment in experiments/, hypothesis first. Trigger when the user says: start an experiment, I want to test whether X, set up a run comparing X and Y, new experiment. Do NOT trigger for book exercises (use marl-exercise).
---

# marl-experiment

**This skill is a wrapper. The instructions live in a harness-neutral playbook
so every agent in this repo behaves the same way.**

Read and follow [`workflows/experiment.md`](../../../workflows/experiment.md) in full, plus the
operating principles in [`AGENTS.md`](../../../AGENTS.md).

Push the user toward a falsifiable question before any code gets written —
`HYPOTHESIS.md` comes first, and it must name what would falsify the prediction.

Reuse `upstream/codebase`'s `marlbase` rather than reimplementing, but never
edit it in place. Report over several seeds; never report a number you did not
actually produce.
