# 03 — Decision

**Date.** 2026-10-16

## Publish `project-chronicle` into this repository rather than a new one

**Chosen.** `54cf9f3`. The skill landed at `project-chronicle/`, matching the
`deep-teach/` layout — a directory containing `SKILL.md` and `README.md`, nothing
else.

### What ruled out the alternative

A separate repository per skill.

Its own README had already written the install command naming this repository and
the `@project-chronicle` selector:

```bash
npx skills add aswathas/agent-skills@project-chronicle -g
```

That line was written before there was anything here to install. A new repository
would have meant rewriting the skill's own documented install path to point away
from a directory that already existed in the name.

One repository also keeps the MIT `LICENSE` in one place, which is why neither skill
carries its own.

### What would change this decision

If the skills ever needed different release cadences, or if one grew dependencies the
others did not, splitting would be reasonable. Neither has a build step, so there is
nothing to version independently yet.

## List the skill in the repository README

**Chosen.** `b613b9f`, adding a row to the skills table and a second line to Quick
Install.

### What ruled out the alternative

Leaving the README listing only `deep-teach`.

This is a small fix and it is worth recording because the omission was invisible.
The skill existed, was documented, was installable, and was completely absent from
the front page of the repository that contains it. A visitor reading the README would
conclude the repository had one skill.

The commit also replaced a comment that was simply wrong:

```bash
# Install all skills globally
npx skills add aswathas/agent-skills@deep-teach -g
```

There is no "all". `npx skills add` takes one selector. The comment claimed a
convenience that does not exist, and now that there are two skills it would have been
actively misleading. Two explicit lines are the accurate version.

### What would change this decision

Nothing.

## Do not document `deep-teach`'s lens count by counting headings

**Decision, recorded 2026-10-16 while writing this chronicle:** leave the count as it
is and record the ambiguity, rather than changing the wording without knowing which
number was intended.

**What the evidence actually says.** `deep-teach/SKILL.md` has eight numbered
sections:

```
### Lens 1 — First Principles
### Lens 2 — Feynman Simplification
### Lens 3 — Chunking
### Lens 4 — Analogy Bridge
### Lens 5 — Inversion (Charlie Munger)
### Lens 6 — Systems Thinking
### Lens 7 — MECE Breakdown (McKinsey)
### Lens 8 — Memory Technique
```

But Lens 8 is not a thinking framework. The skill's own `description` frontmatter
says:

> "teaches it through 7 thinking frameworks (First Principles, Feynman, Chunking,
> Analogy, Inversion, Systems Thinking, MECE), **adds a memory technique**"

So the description is correct: seven frameworks, plus one technique. Three other
places say something different:

| Location | Wording | Accurate? |
|---|---|---|
| `deep-teach/SKILL.md` frontmatter | "7 thinking frameworks ... adds a memory technique" | Yes |
| `deep-teach/SKILL.md:150` tagline | "8-lens deep decode" | Defensible — eight lenses exist |
| Root `README.md` | "8 thinking frameworks" | **No** — there are seven |
| `project-chronicle/README.md` | "8-lens concept decoder" | Defensible |
| Commit `247dd46` | "8-lens concept decoder" | Defensible |

**"8-lens" is true. "8 thinking frameworks" is not.** The distinction is that a lens
is a numbered step and a framework is a way of thinking, and only seven of the eight
are the latter.

This is recorded rather than fixed because changing published wording about someone
else's skill is the author's call. It is a one-word fix in two files when that call
is made.

### What would change this decision

A decision from the author on whether "lens" or "framework" is the intended unit.
Everything else follows from that one answer.