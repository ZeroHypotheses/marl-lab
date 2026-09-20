# AGENTS.md — marl-lab

Canonical instructions for **any** coding agent working in this repository
(Claude Code, Codex, Cursor, Copilot, Gemini CLI, OpenCode/Pi, …).
`CLAUDE.md`, `GEMINI.md`, and `.github/copilot-instructions.md` are symlinks to
this file. Edit this file; never edit the symlinks.

**This repo is harness-agnostic by construction.** Every instruction lives in
plain markdown that any agent can read — this file and `workflows/`. Nothing
here requires a particular tool, and no harness gets behaviour another cannot
reproduce. Where a harness-specific file exists (`.claude/`, `CLAUDE.md`,
`GEMINI.md`), it is a **symlink or a thin pointer**, never a second copy of the
rules.

---

## 1. What this repo is

A personal **learning laboratory** for multi-agent reinforcement learning, built
around the textbook:

> Stefano V. Albrecht, Filippos Christianos, Lukas Schäfer.
> *Multi-Agent Reinforcement Learning: Foundations and Modern Approaches.*
> MIT Press, 2024. — <https://www.marl-book.com>

The repo is not a software product. Its output is **understanding**, and the
durable artifact of that understanding is `wiki/`. Code here exists to test
ideas, not to ship.

The human curates sources, directs the work, and asks the questions.
The agent reads, explains, scaffolds, cross-references, and maintains the wiki.

---

## 2. Layout

```
marl-lab/
├── AGENTS.md              ← you are here (canonical agent contract)
├── book/                  the textbook PDF + extracted per-chapter text
│                          (gitignored — see book/README.md)
├── upstream/              read-only git submodules from the book authors
│   ├── codebase/          marl-book/codebase — reference algorithm implementations
│   ├── slides/            marl-book/slides — lecture slides per chapter
│   └── exercises/         marl-book/marl-book-exercises — code exercises
├── wiki/                  the LLM-maintained knowledge base (agent-owned)
│   ├── index.md           catalog of every page — read this first
│   ├── log.md             append-only chronological record
│   ├── SCHEMA.md          how the wiki is structured and maintained
│   ├── topics/            concepts: game models, solution concepts, …
│   ├── algorithms/        one page per algorithm (IQL, MADDPG, QMIX, …)
│   ├── sources/           one page per ingested source (chapter, paper, talk)
│   └── notes/             synthesis: comparisons, open questions, answers worth keeping
├── experiments/           the human's own work — one directory per experiment
│   └── _template/         copy this to start a new one
├── workflows/             harness-neutral playbooks (the real instructions)
├── scripts/               small utilities (bootstrap, book text, invariant check)
├── .agents/skills/        thin skill wrappers — canonical, cross-harness
└── .claude/skills/        symlinks into .agents/skills/ (Claude Code discovery)
```

---

## 3. Operating principles

These are the agentic-first principles this lab runs on. They override
default agent habits.

**P1 — The wiki is the memory.** Anything learned that will matter next week
belongs in `wiki/`, not in chat scrollback. A good answer to a good question is
a wiki page, not a message. If a session produced insight and touched no file
in `wiki/`, the session leaked.

**P2 — Write for the next agent.** Every page states its own context. Assume the
reader has no conversation history and cannot ask a follow-up. Link related
pages with `[[wikilinks]]` liberally.

**P3 — Teach, don't solve.** For anything in `upstream/exercises/`, the default
is hints, Socratic questions, and pointers to the relevant book section — not
a finished answer. Give the full solution only when explicitly asked for it,
and when you do, explain *why* it works. Learning is the product; working code
is a side effect.

**P4 — Ground every claim.** Cite the source: `[Ch. 9.3]`, `[MADDPG paper §4]`,
`upstream/codebase/…:42`. A claim in the wiki with no citation is a bug. When
the book and a paper disagree, record both and flag the contradiction — do not
silently pick one.

**P5 — Upstream is read-only.** Never modify, reformat, or commit inside
`upstream/`. To adapt an algorithm, copy it into `experiments/` and note its
provenance. Submodule pointers move only via an explicit update.

**P6 — Say what you don't know.** MARL is full of results that hold only under
stated assumptions. Mark uncertainty inline (`> ❓ unverified:`) rather than
rounding it off into confidence. Never invent a citation, a theorem number, or
an equation.

**P7 — Prefer the smallest runnable thing.** An experiment that finishes in
30 seconds and answers one question beats a framework. Every experiment states
its hypothesis before it states its code.

**P8 — Accelerate adaptively, and make the trade-off explicit.** The current
deep-MARL route uses the minimum viable Chapter 6 pass in
`wiki/notes/hands-on-study-loop.md`, treats detailed foundational algorithms
and Chapters 7–8 as references when their prerequisites are already secure,
and then proceeds to Chapter 9. At every reading or experiment transition,
state what this route skips or defers and why. Treat the route as a reversible
hypothesis, not a fixed syllabus: if the human has trouble connecting concepts,
repeatedly encounters unexplained assumptions or notation, or cannot relate an
implementation to its strategic mechanism, recommend the smallest relevant
backfill and update the route in the wiki.

---

## 4. Workflows

**The playbooks in `workflows/` are the instructions.** They are plain markdown
with no harness-specific syntax. Read the relevant one in full before acting —
whatever agent you are.

| Task | Playbook | Ask for it by saying |
|---|---|---|
| File a chapter, paper, or talk into the wiki | [workflows/ingest.md](workflows/ingest.md) | "ingest chapter 6", "file this paper" |
| Answer a question against the wiki | [workflows/query.md](workflows/query.md) | "ask the wiki…", "what do we know about X" |
| Health-check the wiki (incl. errata drift) | [workflows/lint.md](workflows/lint.md) | "lint the wiki", "check the wiki" |
| Work through a book exercise | [workflows/exercise.md](workflows/exercise.md) | "help me with the IQL exercise" |
| Start a new experiment | [workflows/experiment.md](workflows/experiment.md) | "start an experiment to test…" |

### Skills

`.agents/skills/<name>/SKILL.md` holds a thin wrapper per workflow, in the
cross-harness skills layout. Each is ~19 lines and its whole body says "read
`workflows/<x>.md`" — **the substance lives in one place only, so nothing can
drift.**

`.claude/skills/` contains symlinks into `.agents/skills/`, so Claude Code
offers them as `/marl-ingest`, `/marl-ask`, `/marl-lint`, `/marl-exercise`,
`/marl-experiment`. Other harnesses that read `.agents/skills/` pick them up
directly.

**If your harness has no skill mechanism at all, nothing is lost** — the table
above is the routing, and the playbook files are the same ones the skills point
to. A slash command is a shortcut, never a prerequisite.

**Editing rule.** To change *behaviour*, edit `workflows/*.md`. To change when a
skill triggers, edit `.agents/skills/*/SKILL.md` — the real files. Never replace
a `.claude/skills/` symlink with a copy, and never paste a playbook's content
into a skill; the moment the same instruction exists twice, the two harnesses
stop agreeing.

---

## 5. Conventions

**Python.** `uv` manages the environment. `uv sync` to install, `uv run python …`
to execute. Experiments live in `experiments/<nn>-<slug>/` and may import the
book's reference code from `upstream/codebase/`.

**Submodules.** After cloning: `git submodule update --init --recursive`
(or `scripts/bootstrap.sh`). Update upstream deliberately:
`git submodule update --remote upstream/codebase` — then commit the pointer
change with a message saying what moved and why.

**The book PDF is not committed.** It is free to download for personal use but
is not redistributable, and this repo has a public remote. `book/` is
gitignored apart from its README. See `book/README.md`.

**Citations: section, not page.** The book's pagination shifts between
printings (the errata itself says "p203 (previously p202)"). `[Ch. 9.3]` and
`[Eq. 2.54]` are stable; `[p. 203]` is not. Where only a page will do, write
`[p. 203, 2nd printing]`. Our PDF is the **second printing** — see
[`wiki/sources/errata.md`](wiki/sources/errata.md), and re-check with
`./scripts/fetch-errata.sh`.

**Wikilinks.** `[[page-name]]` by slug, matching the filename without `.md`.
A link to a page that doesn't exist yet is fine — it marks a gap worth filling.

**Harness-agnosticism is checked.** `./scripts/check-harness-agnostic.sh`
verifies the invariants: contract files are symlinks not copies, skills are
canonical in `.agents/skills/` with `.claude/skills/` symlinked to them, skills
stay thin, every workflow is reachable from this file, and `workflows/` names no
particular tool. Run it after touching any agent-facing file.

**Commits.** Present tense, scoped by area: `wiki: add page on CTDE`,
`exp/03: sweep QMIX mixing-network width`, `upstream: bump codebase to <sha>`.

---

## 6. Hard rules

- Never write to `upstream/`.
- Never commit `book/*.pdf` or extracted book text.
- Never fabricate a citation, equation, theorem number, or experimental result.
- Never transcribe an equation from a page covered by the errata without
  checking [`wiki/sources/errata.md`](wiki/sources/errata.md) first.
- Never hand over an exercise solution unless explicitly asked (P3).
- Never delete a wiki page without recording the removal in `wiki/log.md`.
