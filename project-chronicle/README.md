# 📖 project-chronicle

> **The project history you wish you'd written.**
> Every decision, every dead end, every scope change — recorded where the next person can actually find it.

[![Install](https://img.shields.io/badge/install-npx%20skills-4a7c59?style=flat-square&logo=npm)](https://skills.sh/aswathas/agent-skills/project-chronicle)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-CLI%20Skill-f9a620?style=flat-square&logo=anthropic)](https://claude.ai/code)
[![License: MIT](https://img.shields.io/badge/License-MIT-b7472a?style=flat-square)](../../LICENSE)
[![Auto-Triggers](https://img.shields.io/badge/triggers-automatically-4a7c59?style=flat-square)](#-it-triggers-itself)

---

## What is it?

`project-chronicle` is a [Claude Code](https://claude.ai/code) CLI skill that **documents a project's entire history while you build it** — not after, and not only the parts that worked.

Most project docs are written once at the end, from memory, describing only what shipped. That's the version where the reader has no idea why the obvious solution didn't work, what got cut from the MVP, or which promise was quietly abandoned.

This skill writes the story *as it happens*, beat by beat:

- 📝 **The problem** — what breaks, for whom, and what it costs today
- ⚖️ **The options** — every approach considered, including the ones dismissed in five minutes
- 🎯 **The decision** — what we picked, and what specifically ruled out the rest
- 🗺️ **The plan** — phases, locked
- 🎯 **MVP scope** — what's in, what's out, and why each exclusion
- 💀 **Failed attempts** — the dead ends, kept forever
- 🧪 **Verification** — what was tested, what passed, what broke
- 🔁 **Retro** — what we'd do differently

You keep building. It keeps the record.

---

## Install

```bash
npx skills add aswathas/agent-skills@project-chronicle -g
```

> Requires [Claude Code CLI](https://claude.ai/code). The `-g` flag installs globally so it works in any project.

---

## It Triggers Itself

There's no slash command to memorize. The skill reads what you're already doing and engages on its own:

| You say | It writes |
|---|---|
| *"Let's start a new project, I want to fix X"* | `01-problem.md` |
| *"We could use Postgres, or SQLite, or just JSON"* | `02-options.md` |
| *"Let's go with SQLite"* | `03-decision.md` |
| *"OK here's the plan"* | `04-plan.md` |
| *"For the MVP let's skip auth"* | `05-mvp.md` |
| *"Let me try a relational schema first"* | `attempts/001-relational-schema.md` |
| *"That didn't work, p95 was 900ms"* | Closes the attempt, records why |
| *"Drop live search from this phase"* | `decisions/001-drop-live-search.md` |
| *"Tests are passing now"* | `06-verification.md` |

It stays out of the way for typo fixes, dependency bumps, and routine bugs. A record with no signal in it is worse than no record.

---

## The Seven Beats

```
docs/
├── 01-problem.md          ← what's broken and what it costs
├── 02-options.md          ← every approach, not just the winner
├── 03-decision.md         ← what we chose and what ruled out the rest
├── 04-plan.md             ← phases, locked
├── 05-mvp.md              ← in scope / out of scope, with reasons
├── 06-verification.md     ← tested, passing, still untested
├── 07-retro.md            ← what we'd do differently
│
├── attempts/              ← 💀 THE VALUABLE PART
│   ├── 001-postgres-schema.md      outcome: abandoned
│   └── 002-sqlite-first.md         outcome: shipped
│
└── decisions/             ← scope and plan changes
    ├── 001-drop-live-search.md
    └── 002-move-audit-to-v2.md
```

Numbering is fixed. `ls docs/` and you know the story order without opening anything.

---

## Failed Attempts Are the Point

This is what separates this from a normal project README.

When you start trying an approach, the skill opens `docs/attempts/NNN-slug.md`. When it dies, it records exactly what happened and closes the file. Two commits: **one when it opens, one when it's written up as abandoned.**

```markdown
# Attempt 001 — Postgres schema

**Hypothesis.** Normalized relational schema avoids the fan-out we hit on reads.

**How we tested it.** Built the schema, seeded 10k rows, measured p95 read.

**What actually happened.** p95 was 40ms on the 4-column join and 900ms on the
audit join. The audit path is the hot one, and relational made it worse.

**Outcome.** Abandoned.

**Why we moved on.** We need wide reads far more than write integrity, and every
fix for the join problem added a cache layer we'd now have to invalidate anyway.
```

Six months later, you — or someone else — open that file instead of spending two days rediscovering that relational was the wrong call. **The failures are worth more than the wins, and most projects throw them away.**

---

## Locked Beats Are Never Edited

Once `04-plan.md` and `05-mvp.md` are written, they're frozen. When the scope changes, the skill writes a new file in `decisions/` and links it from the original.

```markdown
# 001 — Drop live search from v1

**Date.** 2026-10-15
**Supersedes.** Beat 4, phase 3.
**Change.** Live search moved out of v1 into v2.
**Why.** Index rebuild is 4 minutes on current dataset size. Untenable on every
deploy. Deferred, not rejected.
```

Your plan gets edited every week. The record of *how your thinking changed* is the thing nobody else has. Editing beats 4 in place destroys it.

---

## Commit Discipline

Every file is its own commit, written the moment it's created. No batching at project end.

| What | Message |
|---|---|
| New beat | `docs: state problem` · `docs: decide on <X>` |
| Plan locked | `docs: lock plan, <N> phases` |
| MVP frozen | `docs: define MVP scope` |
| Verification | `docs: record verification, <N>/<M> passing` |
| Attempt opened | `docs: open attempt NNN, <hypothesis>` |
| **Attempt abandoned** | `docs: abandon attempt NNN, <why>` |
| Scope change | `docs: change NNN, <what>` |

Three hard rules:

1. **Never squash, never amend.** Squashed commits vanish from the contribution graph and collapse the reasoning this skill exists to preserve. If a commit was wrong, add a correcting one.
2. **Only `docs/` is ever committed.** The skill never stages source code, config, or lockfiles. Worst case is a stray doc file you delete.
3. **Never invent a beat.** If you haven't stated a problem, the file stays unwritten. An honest gap beats a plausible fiction in a document whose entire job is to be trusted.

---

## What It Won't Do

This matters as much as what it does.

- **It won't pad your commit graph.** No daily filler commits, no comment tweaks dressed up as work. If a day has no real work, the graph has a gap — and that's correct. A graph that means something is worth more than a full one that doesn't.
- **It won't write a beat you didn't earn.** Sections stay empty until the moment actually happens.
- **It won't force you through beats 1–3 in order.** Starting mid-project with a problem and a decision already made? It writes beats 2 and 3 and moves on.
- **It won't touch your code.** Documentation only.

---

## Example: One Project, End to End

```
docs: state problem                        ← 01-problem.md
docs: record options considered            ← 02-options.md
docs: decide on SQLite over Postgres       ← 03-decision.md
docs: lock plan, 4 phases                  ← 04-plan.md
docs: define MVP scope                     ← 05-mvp.md
docs: open attempt 001, relational schema  ← attempts/001
docs: add schema, seed script              ← you, in the code
docs: add audit join benchmark             ← you, in the code
docs: abandon attempt 001, p95 900ms       ← attempts/001 closed
docs: open attempt 002, SQLite-first       ← attempts/002
docs: add SQLite repository layer          ← you, in the code
docs: attempt 002 shipped                  ← attempts/002 closed
docs: record verification, 47/47 passing   ← 06-verification.md
docs: retro                               ← 07-retro.md
```

Roughly **15–30 documentation commits per project**, plus whatever the code itself honestly decomposes into. The number is a byproduct of work worth writing down — never the other way around.

---

## How It Works Internally

```
User states something consequential
      │
      ▼
 Match against beat triggers
      │
      ▼
 Does the beat already exist? → read it, don't overwrite
      │
      ▼
 Write docs/NN-slug.md
      │
      ▼
 git commit docs/NN-slug.md   ← path-scoped, silent
      │
      ▼
 Return to building. Skill goes quiet.
```

**Writing rules the skill enforces:**
- Prose, not bullet soup. A sentence that says *why* beats a list of nouns.
- The reader has seen none of this before.
- Every claim traces to something you actually said.
- Your own words for the problem statement — a complaint is not polished into a spec and presented back as your requirement.

---

## Requirements

- [Claude Code CLI](https://claude.ai/code)
- Node.js ≥ 18 (for `npx skills`)
- A git repository — the skill writes to `docs/`, so it needs somewhere to commit to
- No API keys beyond your existing Claude Code authentication

---

## Installation

### Global install (recommended)
```bash
npx skills add aswathas/agent-skills@project-chronicle -g
```

### Project-level install
```bash
npx skills add aswathas/agent-skills@project-chronicle
```

### Verify
```bash
npx skills list | grep project-chronicle
```

### Use it
```bash
claude
# no command needed — just start working
```

---

## Updating

```bash
npx skills update
```

Or reinstall:
```bash
npx skills add aswathas/agent-skills@project-chronicle -g -y
```

---

## Contributing

PRs welcome.

1. Fork this repo
2. Edit `project-chronicle/SKILL.md`
3. Test on a real project before opening the PR
4. Include a before/after of the `docs/` tree

**Ideas:**
- A `08-handoff.md` beat for team transitions
- Templates for specific domains (CLI tools, web apps, ML models)
- A mode that reads an *existing* repo and backfills beats 1–2 from git history

---

## Other Skills in This Collection

| Skill | What It Does |
|-------|-------------|
| [deep-teach](../deep-teach) | 7-frame concept decoder for exam prep and deep learning |
| `project-chronicle` | Project history, decisions, and dead ends ← **you are here** |

---

## License

MIT — free to use, modify, and distribute.

---

<p align="center">
  Built with 📖 for anyone who'll have to work on this in six months.
  <br/>
  <a href="https://github.com/aswathas/agent-skills/issues">Report an issue</a> ·
  <a href="https://github.com/aswathas/agent-skills/pulls">Contribute</a>
</p>