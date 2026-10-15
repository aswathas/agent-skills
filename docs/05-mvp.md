# 05 — MVP scope

**Date.** 2026-10-16

## What the MVP does

- **Two skills, each a directory holding exactly `SKILL.md` and `README.md`.**
  That is the entire payload. A skill is an instructions file you can read before
  you run it, and nothing here changes that.
- **Both skills are installable in one line**, with the selector naming this
  repository and the skill.
- **Both are listed in the root README**, in the skills table and in Quick Install.
- **`project-chronicle` writes to `docs/` and commits path-scoped.** It never stages
  source, config or lockfiles.
- **Neither skill is coupled to the other.** They share a licence and a repository
  and nothing else.
- **MIT licence at the root**, covering both.

## What the MVP deliberately does not do

Each exclusion is a decision. None are oversights.

- **No build step, no package manager, no dependencies.** The entire value
  proposition is that `npx skills add` copies a markdown file. A build would add a
  failure mode to the one operation that must not fail.

- **No tests.** There is nothing to execute. A test suite here would be testing
  markdown parsing, which is the user's editor's job and GitHub's job.

- **No CI.** Same reason, stated in `04-plan.md`. The absence is consistent rather
  than lazy — a workflow that runs `ls` would be theatre.

- **No skill validator.** Nothing checks that frontmatter parses, that `name`
  matches the directory, or that `description` is present. This one is a real gap
  with a real consequence, recorded in `06-verification.md` rather than hidden here.

- **No `references/` progressive disclosure.** `postiee` splits its skill because
  it is long. These are not. See `02-options.md`.

- **No cross-skill invocation.** `deep-teach` does not call `project-chronicle` and
  vice versa. Their triggers never overlap.

- **No versioning or releases for the skills.** Installing a skill means fetching
  `main`. There is no changelog and no tag. For an instructions file that changes
  when its author changes their mind, that is acceptable — and it is also the
  reason a user cannot pin a known-good version.

## What is excluded because it was tried and rejected

- **Forced inline-comment standards across the skill's output.** Considered as a way
  to make the rules more forceful. Rejected: the skill's own guidance already says
  to comment only the why, and a rule that contradicts the codebase's standard makes
  every instruction slightly less credible.

- **Daily or per-file logging inside a chronicle.** A `docs/lifecycle/days/` tree was
  proposed to increase commit volume. Rejected, and recorded in `07-retro.md`, on
  the grounds that a chronicle's value is that a reader can skip to the beat they
  need — which daily logs destroy.