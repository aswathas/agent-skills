---
name: linkedin-growth
description: Write, gate, schedule and publish LinkedIn posts in Aswath's voice, aimed at growing from the current following to 1K, 10K, 100K and 1M. Use for "write a LinkedIn post", "post this on LinkedIn", "draft a LinkedIn post about X", "LinkedIn news post", "log this project for LinkedIn", "set up my LinkedIn schedule", "review my LinkedIn posts", or any request to turn a project, PR, hackathon or AI-news item into a post.
---

# linkedin-growth

One skill for the whole loop: pick a topic, write it in Aswath's voice, pass the
gate, publish with postiee, and keep a log of the work that feeds the next post.

This skill is a synthesis, not a copy. It takes the useful parts of the
highest-star LinkedIn skill repos (see `NOTICE.md`) and adds the things none of
them have: a stage-by-stage follower roadmap, a project log that generates
topics, a hard publish gate, and a real publishing path.

## Read before writing anything

| File | Why |
|---|---|
| `assets/voice.md` | how Aswath actually writes, derived from published posts |
| `references/hooks.md` | 20 hook formulas that fit this account |
| `references/humanizer.md` | banned phrases + the 10-point gate |
| `references/pillars.md` | the five content pillars and their ratios |
| `references/formats.md` | post shapes, including document carousels |
| `references/never-do.md` | the things that quietly kill an account |
| `references/roadmap.md` | 1K → 10K → 100K → 1M and what changes at each stage |

Do not draft before reading `voice.md` and `never-do.md`.

## The pipeline

1. **Topic.** From `assets/projects.md`, a merged PR, a shipped feature, a
   hackathon, or the day's AI news. One topic per post.
2. **Angle.** The angle is a claim, not a summary. "Five bugs, none of them
   threw an error" is an angle. "I contributed to HarnessRouter" is not.
3. **Draft.** Write three hooks first, pick one, then write the post. Never
   write the post first and bolt a hook on.
4. **Gate.** Score the draft with `references/humanizer.md`. Anything below 8/10
   gets rewritten, not published.
5. **Publish.** `postiee post --file ... --visibility PUBLIC`, recording the
   permalink.
6. **Log.** Append one row to `assets/projects.md` so the next post has raw
   material.

## Commands

```
/linkedin-growth draft <topic|PR link|file>
/linkedin-growth news
/linkedin-growth log <what I shipped>
/linkedin-growth publish <draft file>
/linkedin-growth review
/linkedin-growth schedule show
/linkedin-growth schedule set <key> <value>
/linkedin-growth schedule apply
/linkedin-growth schedule off
```

### draft

1. Read `assets/projects.md` and the last 10 rows of `postiee history`.
2. Read the pillar this topic belongs to and the matching format.
3. Produce **three hooks** labelled by formula, then one full post (~150–250
   words for text, ~120 for a carousel caption).
4. Run the gate and print the score with the draft. Save to `drafts/`.

### news

1. Search for the day's AI/agent news.
2. Pick one story where the account can add first-hand experience — a harness
   that shipped, a protocol change, a failure mode that matches the work in
   `projects.md`.
3. Write a take (never a summary). State the news in one line, then the
   practitioner angle.
4. Gate, save, and offer to publish.

### log

Append a row to `assets/projects.md`:

```
| 2026-10-28 | HarnessRouter | five merged PRs: trace context, step budget, grok streaming, failure detail, aider nudge | #473 #474 #501 #504 #513 | POSTED |
```

Status is `IDEA`, `DRAFTED` or `POSTED`. Never write a post from an IDEA row
without the raw detail — go get the numbers first.

### publish

**On Windows, put the command in a `.sh` file and run the file.** Nested quoting
through `wsl -e bash -lc '...'` can swallow the trailing flag into `--alt`; a
swallowed `--dry-run` publishes a real post. The script form is the only form
that has been reliable:

```sh
#!/usr/bin/env bash
set -euo pipefail
/home/aswath/.local/bin/postiee --agent post \
  --file "C:/path/to/draft.md" \
  --image "C:/path/to/card.png" \
  --alt "one factual sentence" \
  --dry-run
```

Then `wsl -e bash /mnt/c/path/to/publish.sh`. Remove the `--dry-run` line to
publish for real.

Rules:
- `--dry-run` first and read the escaped commentary. Escaping is automatic;
  it turns `(` into `\(` on the wire, which is correct.
- `--pdf` and `--image` are mutually exclusive. A carousel is a PDF whose pages
  are the content.
- Never post a link-heavy body. Put one link, at the end, or in the first
  comment.
- Record the returned permalink in `posted/<date>-<slug>.md`.

### Mentions — read this before promising a tag

LinkedIn renders a tag only when `commentary` carries little-text markup:

```
@[Display Name](urn:li:person:ID)
@[Company Name](urn:li:organization:ID)
```

postiee's `--mention "Name=urn:li:..."` inserts that markup and **fails the post
if the handle is not in the body**. `postiee mentions add` stores URNs so they
only have to be found once.

Self-serve access cannot look up another member's URN. If a URN is not known,
name the person in plain text with their profile link — do not type `@Name` and
hope. A tag that does not render looks worse than no tag.

## The gate (must pass before publish)

| Check | Pass condition |
|---|---|
| Hook | two short lines, under ~110 characters total, contains a number, a tension, or a claim |
| One idea | the post argues one thing; a second idea is a second post |
| Voice | matches `assets/voice.md`; read it aloud |
| AI tells | zero phrases from the banned list |
| Numbers | every number traces to a file, a commit, a PR or a measurement |
| Claims | nothing invented, no rounded-up results, no fake customers |
| Format | short paragraphs, bullets or arrows, no wall of text |
| Ending | a real question or a concrete next step, never "thoughts?" |
| Hashtags | 3–5, at the end, relevant |
| Tags | only with a real URN |

Score 0–2 on each of clarity, specificity, voice, honesty, and ending. Publish
at 8+. Report the score with the draft.

## Scheduling

Timing, topics, weights and publish mode live in `schedule.toml`:

```toml
enabled         = true
cron            = "0 9 * * 1-5"
topics          = ["ai-news", "build-log", "oss-contribution", "teardown"]
weights         = [0.4, 0.3, 0.2, 0.1]
auto_publish    = true
visibility      = "PUBLIC"
max_per_day     = 1
```

How the job is created depends on the agent you run:

| Agent | Mechanism |
|---|---|
| Command Code | `cron_create` (durable, recurring). `cron/apply.md` has the exact call. |
| Claude Code | `/loop` for a session, or an OS scheduler (cron, Task Scheduler) invoking `claude -p` with `cron/daily-prompt.md` |
| Anything else | point the scheduler at `cron/daily-prompt.md`; it is self-contained |

Rules that hold in every case:
- The job reads `schedule.toml` at run time, so changing topics or weights needs
  no reschedule. Changing `cron` does.
- Skip if `postiee history --limit 1` already shows a post today.
- Stop on an auth error, never retry a failed publish, and never post twice to
  "fix" a failure.
- Recurring agent cron jobs expire after seven days; `cron/apply.md` includes a
  one-shot re-arm so the schedule renews itself.

## Hard limits of the platform

- 3,000 characters per post.
- One document **or** a set of images, never both.
- Document carousels: PDF, ≤100 MB, ≤300 pages.
- 150 API requests/day; one post is one request.
- No scheduling API — the cron job is client-side, which is what this skill uses.

## When something fails

| Symptom | Cause |
|---|---|
| mention not in body | `--mention` handle does not appear verbatim; add it or drop the flag |
| 403 on mention resolve | self-serve token lacks `r_organization_social`; use a stored URN |
| document upload 403 | owner must be the authenticated member |
| post created but not recorded | capture the permalink from stdout; history is best-effort |
