# 06 — Verification

**Date.** 2026-10-16

## What passed

**Both skills are readable in full before you install them.** `SKILL.md` and
`README.md` are the entire payload of each directory. There is no build step to
verify, because there is no build step — a fact worth stating plainly rather than
discovering later.

**The install command now resolves.** `project-chronicle/` exists at the path its own
README has always named, and the root README lists it in both the skills table and
Quick Install. The command

```bash
npx skills add aswathas/agent-skills@project-chronicle -g
```

now points at a directory that is actually there. It had not been, until `54cf9f3`.

**The Quick Install comment is gone.** `# Install all skills globally` described a
capability `npx skills add` does not have. It is now two explicit commands, one per
skill, which is what actually works.

**Frontmatter is well-formed on both.** `name` and `description` are present on
`project-chronicle`; `deep-teach` also carries `trigger: /deep-teach`. The
`description` fields are the part that matters operationally, because they are what
an agent matches against before the file is ever opened — and both are written as
trigger conditions rather than as summaries.

**The MIT `LICENSE` covers both.** One licence at the root, which is part of why
shipping both skills in one repository was the cheaper option.

**`deep-teach`'s eight numbered sections exist and are in order.** Verified by
reading them.

## What failed

**`project-chronicle`'s documented install command had never worked.** Its README
named `aswathas/agent-skills@project-chronicle` while the repository contained only
`deep-teach/`. Anyone who had tried it would have got a failure and no explanation.

This was not a typo that survived a review. The install line was written first, the
directory came later, and nothing between the two checked whether the line was
still true. Fixed by `54cf9f3`.

**The root README listed one skill and the repository had two.** Invisible from
inside the repository. Fixed by `b613b9f`.

**Two READMEs describe `deep-teach`'s framework count differently from the skill
itself.** The frontmatter says seven thinking frameworks and adds a memory technique.
The root README says "8 thinking frameworks" and `project-chronicle/README.md` says
"8-lens". Only the second of those is defensible, and it is arguably still
imprecise. See `03-decision.md` — not fixed, because the intended unit is the
author's call.

## Still untested

**Neither skill has ever been installed from this repository by a second machine.**
The path is now correct, but nobody has run `npx skills add` against the published
URL and confirmed the selector resolves. The one-line install is asserted from the
directory layout, not observed working.

**The skills have not been run against a fresh project.** Both were written against
projects already in progress. `project-chronicle`'s own rules include a case this
repository has never exercised — *"Before the first commit in a directory, check
`docs/01-problem.md` does not already exist"* — which only fires on a project with
no chronicle yet, in a repository with no `docs/`. Both this repository and
`aswathas.github.io` started with no `docs/`, so the path exists but the rule has
never been tested on a first-run project.

**No linting, no frontmatter schema check.** Nothing validates that a `SKILL.md`
frontmatter block parses, that `name` matches the directory name, or that the
`description` is present. A skill with malformed frontmatter fails silently, at the
agent's expense, rather than at the author's.

**No CI at all.** This repository has no workflow. It also has nothing to test, which
is the honest trade: two markdown files and a licence.

**`deep-teach`'s seven frameworks were not evaluated.** They were written once in May
and nothing records whether they work better than a single well-chosen framework, or
than no skill at all. There is no feedback loop and no way to answer that question
from inside the repository.