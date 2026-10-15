# 07 — Retro

**Date.** 2026-10-16

## What worked

**The install line was written before the directory existed, and nothing caught it.**
`project-chronicle/README.md` said `npx skills add aswathas/agent-skills@project-chronicle
-g` from the day the skill was written. The repository contained only `deep-teach/`.
The line was aspirational for as long as it was false, and nothing in the workflow
compared a documented path against the tree.

**One commit fixed both gaps at once.** Directory and README row landed together, so
the install path and its discoverability became true in the same change.

## What did not work

**The root README was invisible from inside the repository.** It listed one skill
while holding two. Nobody notices a missing table row from the working directory —
the README is read by someone arriving, and you are not arriving.

**Writing documentation as the last step.** A skill can be finished, published, and
advertised on LinkedIn while the README that explains how to install it points at
nothing. The public surface is not covered by the build, by review, or by any check.

## The proposal that was declined

A redesigned variant of this skill was proposed late in the session: split output
into per-problem files, per-day logs, and file-mutation manifests, and commit them
in micro-batches to raise visible contribution density.

It was declined. The reasoning is recorded here rather than silently dropped,
because the reason is a design property of this skill and future readers should not
have to rediscover it.

**Daily logs destroy the thing a chronicle is for.** The skill's stated purpose is
that a reader can `ls docs/` and know the story order without opening anything. A
`docs/lifecycle/days/day_014.md` tree replaces that with a directory listing
numbered by date, which is not the order of a story. It is the order of a calendar.

**Micro-batched commits make a graph mean less.** The skill already has the rule:
*"It won't pad your commit graph. No daily filler commits, no comment tweaks dressed
up as work. If a day has no real work, the graph has a gap — and that's correct. A
graph that means something is worth more than a full one that doesn't."*

Volume and density are not the same property, and only one of them is legible to
someone reading the repository.

**Forced per-function comment blocks would degrade the code the skill is used on.**
Context/Intent/Edge-Cases on every function contradicts the standard already in force
across this account — `postiee`'s guide says to comment only the why the code cannot
show.

## What would be done differently

**Check the documented path against the tree before publishing.** One `test -d` at
the path named in an install command would have caught this. It is worth more than
any amount of prose about it, and it is Phase 4 of the plan, still open.

**Add a frontmatter validator.** Two skills is enough to justify a script that
confirms each `SKILL.md` parses, that `name` matches its directory, and that
`description` is present. It would run in a second and would need no CI.

## What the next iteration should start with

1. Execute the documented install on a clean machine. Everything else in this file is
   less important than proving the one thing users actually do.
2. Resolve the `deep-teach` lens count. One word, two files, and a decision from the
   author about whether the unit is a lens or a framework.
3. Write the frontmatter validator.

Then: a third skill. The first two established the shape; the third is where the
`references/` split question from `02-options.md` gets a real answer.