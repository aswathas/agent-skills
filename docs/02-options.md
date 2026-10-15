# 02 — Options considered

**Date.** 2026-10-16

## Where should `project-chronicle` live

### Option A — a new repository, one per skill

Each skill gets its own repo, its own README, its own release cadence.

**Viable because:** independent versioning, and a small skill does not need company.

**Rejected.** The skill's own README had already written the install command naming
this repository:

```bash
npx skills add aswathas/agent-skills@project-chronicle -g
```

That line predated the directory existing. A separate repository would have meant
rewriting the skill's own documented install path to point away from a directory
already named in it — the failure documented in `01-problem.md`.

It would also have split the MIT `LICENSE` across two repositories for two markdown
files.

### Option B — this repository, one directory per skill

**Chosen.** `deep-teach/` and `project-chronicle/`, each holding exactly `SKILL.md`
and `README.md`.

### Option C — no repository; publish each skill some other way

Not seriously considered. The install mechanism is `npx skills add <repo>`, which
requires a repository.

## What should a skill contain

### Option A — `SKILL.md` alone

The minimum that works. `npx skills add` needs frontmatter and a body.

**Kept as the core**, because it is what the agent loads. A skill you cannot read in
one sitting is a skill nobody audits.

### Option B — `SKILL.md` plus a README

**Chosen.** The README is the part a human reads before installing: what it does,
when it triggers, what it refuses to do, and an example.

This is not duplication. `SKILL.md` is instructions addressed to an agent and written
in imperative mood; `README.md` is a pitch and a manual addressed to a person. They
drift apart, and that drift is a known cost — `03-decision.md` records one instance
where they already have.

### Option C — split `SKILL.md` into multiple files with progressive disclosure

The pattern used by `postiee`, where `references/installation.md` holds the long tail
and the skill points at it.

**Rejected here, for now.** Both skills are small enough to read whole. Progressive
disclosure pays off when a skill exceeds what fits in context; neither of these is
there yet, and splitting a 200-line file adds indirection for nothing.

It is the right answer the first time `project-chronicle` grows a reference it does
not need on every trigger.

## How should the two skills relate

### Option A — one skill that does both

**Rejected.** They are unrelated. `deep-teach` explains a topic; `project-chronicle`
records a project's history. Their triggers never overlap, and merging them would
mean loading both sets of instructions for every request.

### Option B — two independent skills in one collection

**Chosen.** They share a repository and a licence and nothing else.

### What was considered and never built

**A shared template or generator for skills.** Two skills do not justify a build step.
The duplication between them is one frontmatter block and a directory shape.

**A skill index, manifest, or registry file.** The root README table is the index.
It was wrong for four months only in the sense that it was written before the second
skill existed, and one commit fixed it.