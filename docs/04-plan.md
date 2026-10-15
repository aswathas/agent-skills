# 04 — Plan

**Date.** 2026-10-16

Locked. This records the plan the three existing commits actually followed, plus
the documentation round added on 2026-10-16.

## Phase 1 — Publish `project-chronicle` (`54cf9f3`)

One directory, two files, matching the `deep-teach/` layout exactly. The skill
body and its README moved from a local install directory to a public path.

Delivered: the directory its own README had always named now exists.

## Phase 2 — Make it discoverable (`b613b9f`)

Root README skills table gains a row. Quick Install gains a second command, and the
`# Install all skills globally` comment is removed, because `npx skills add` takes
one selector and there is no "all".

Delivered: a visitor reading the front page of the repository can see both skills.

## Phase 3 — Record the decisions (`be5aa9c` → `9268cd2`)

This chronicle. `01-problem`, `02-options`, `03-decision`, `06-verification`,
plus the cross-reference between the two beats that needed one.

Delivered: the reasoning that was previously only in commit messages.

## Phase 4 — Fix what the round found

Not yet done. Two items are identified and both are recorded in
`06-verification.md` as open:

- **`deep-teach`'s framework count.** Two READMEs say "8 thinking frameworks"; there
  are seven, with a memory technique as an eighth lens. `03-decision.md` records why
  this was not changed unilaterally — the intended unit is the author's call.
- **The install path has never been executed by a second machine.** The directory
  layout says the selector resolves. Nobody has run it.

## What this plan does not include

- **No build, no CI, no dependency.** Two markdown files and a licence. There is
  nothing to test, which is the honest trade rather than an omission.
- **No skill validation.** Nothing checks that frontmatter parses or that `name`
  matches the directory. A malformed skill fails silently at the agent's expense.
- **No `references/` split.** Deliberate while both skills are small. See
  `02-options.md`.