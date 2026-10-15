# 01 — The problem

**Date.** 2026-10-16

## What this repository is for

Two Claude Code skills that had no home and no common record.

`deep-teach` landed first, on 2026-05-11, as a single commit. It teaches a concept
through seven thinking frameworks, adds a memory technique, and produces an
exam-ready answer.

`project-chronicle` arrived later and did not land in this repository at first. It
existed only at `~/.claude/skills/project-chronicle/`, installed locally, with no
remote, no README link from the repo root, and an install command in its own README
that pointed at a directory which did not exist here.

That last part is the concrete failure. `project-chronicle/README.md` had said since
before it was published:

```bash
npx skills add aswathas/agent-skills@project-chronicle -g
```

`aswathas/agent-skills` contained only `deep-teach/`. Following the documented
install command would have failed. A skill whose install instructions are known to
be wrong is worse than an unpublished skill, because it looks finished.

## What it cost

Nothing was visibly broken. That is what made it worth fixing quietly rather than
urgently: a skill that exists, is described as installable, and cannot be installed.

The second cost is quieter. Neither skill had a record of why it was built. The
README for `project-chronicle` explains what it does very well. It does not explain
what was tried first, or why the rules are the rules. `docs/` did not exist in
either skill.

## What is not the problem

This is not a framework, a plugin collection, or a marketplace. It is two
instructions files with frontmatter, installed into an agent's skills directory.
The whole value proposition is that a skill is a markdown file you can read before
you run it.

Anything that adds a build step, a runtime, or a dependency to this repository would
be solving a problem nobody has.