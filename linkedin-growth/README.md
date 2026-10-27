# 📈 linkedin-growth

> **A LinkedIn growth system, not a post generator.**
> Voice, hooks, a publish gate, a follower roadmap, a project log, and a scheduler — all pointed at one account.

[![Install](https://img.shields.io/badge/install-npx%20skills-4a7c59?style=flat-square&logo=npm)](https://skills.sh/aswathas/agent-skills/linkedin-growth)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-CLI%20Skill-f9a620?style=flat-square&logo=anthropic)](https://claude.ai/code)
[![License: MIT](https://img.shields.io/badge/License-MIT-b7472a?style=flat-square)](../../LICENSE)
[![Publishes](https://img.shields.io/badge/publishes-via%20postiee-0A66C2?style=flat-square&logo=linkedin)](#publishing)

---

## What is it?

Most "write my LinkedIn post" prompts produce the same post everyone else is
posting: a hook, three bullets, a question, hashtags. It reads fine and it grows
nothing, because it has no point of view and no memory of what you have actually
built.

`linkedin-growth` is the whole loop instead:

- 🎙️ **A voice profile** derived from your published posts, not a generic style guide
- 🪝 **20 hook formulas** chosen for technical accounts, plus the rules that make a hook land above "…see more"
- 🚦 **A 10-point publish gate** — a draft below 8/10 gets rewritten, not posted
- 🧱 **Five content pillars** with a ratio, so the account does not drift into all-news or all-promo
- 🗺️ **A roadmap** from 0 → 1K → 10K → 100K → 1M, with the leading metric that gates each stage
- 📓 **A project log** that turns the work you already did into the next post
- ⏰ **A scheduler** whose timing, topics and frequency live in one config file

---

## The Loop

```
        projects.md  ──┐
        merged PRs     ├──►  pick one topic by weight
        daily AI news ─┘              │
                                      ▼
                          three hooks → one draft
                                      │
                                      ▼
                         ┌─── the 10-point gate ───┐
                         │  < 8/10 → rewrite once  │
                         └──────────┬──────────────┘
                                    ▼
                         postiee post (dry-run first)
                                    │
                                    ▼
                    posted/<date>-<slug>.md + URN
```

The URN matters: LinkedIn's read-your-own-posts permission is closed, so the
local record is the only copy of that post's identity that will ever exist.

---

## Install

```bash
npx skills add aswathas/agent-skills@linkedin-growth -g
```

Then, once per machine:

```bash
# the CLI this skill publishes through
curl -fsSL https://raw.githubusercontent.com/aswathas/postiee/main/install.sh | sh   # macOS/Linux
# Windows:
irm https://raw.githubusercontent.com/aswathas/postiee/main/install.ps1 | iex

postiee auth login
```

> `postiee auth login` is user-only — it opens a browser and needs your approval.
> An agent cannot and should not do it for you.

---

## Commands

| Command | What it does |
|---|---|
| `/linkedin-growth draft <topic\|PR link>` | three hooks, then one gated draft |
| `/linkedin-growth news` | today's AI news, turned into a practitioner take |
| `/linkedin-growth log <what I shipped>` | appends a row to the project log |
| `/linkedin-growth publish <draft>` | dry-run, then publish via postiee |
| `/linkedin-growth review` | what worked, what to repeat |
| `/linkedin-growth schedule show\|set\|apply\|off` | the scheduler |

---

## The Gate

Every draft is scored before it can go out. Below 8/10, it is rewritten.

| Axis | 0 | 1 | 2 |
|---|---|---|---|
| Clarity | needs a second read | mostly clear | one pass |
| Specificity | adjectives | one detail | numbers, paths, names |
| Voice | generic LinkedIn | resembles the account | matches `voice.md` |
| Honesty | overclaims | accurate but vague | accurate, states the limit |
| Ending | "Thoughts?" | weak CTA | real question or next step |

Also required: hook under ~110 characters, 3–5 hashtags, no phrase from the
banned list, and every claim traceable to a commit or a measurement.

---

## The Roadmap

| Stage | Followers | Leading metric that gates it |
|---|---|---|
| 1 | 0–1K | 3 consecutive posts over 2,000 impressions; 50 profile views/week |
| 2 | 1K–10K | one format clears 10K twice; >8% monthly follower growth |
| 3 | 10K–100K | inbound DMs; 3 posts over 100K impressions |
| 4 | 100K–1M | the work gets cited without you posting it |

Each stage also records what stops working when you carry it forward — the
comments that built stage 1 do nothing at stage 3.

Full detail in [`references/roadmap.md`](./references/roadmap.md).

---

## What's Inside

```
linkedin-growth/
├── SKILL.md                    ← the loop, commands, gate, limits
├── schedule.toml               ← cron, topics, weights, auto_publish
├── references/
│   ├── hooks.md                ← 20 formulas + re-hook rules
│   ├── humanizer.md            ← banned phrases + the 10-point gate
│   ├── pillars.md              ← five pillars and their ratios
│   ├── formats.md              ← text, carousel, teardown, news, build log, personal
│   ├── never-do.md             ← the 18 habits that cap an account
│   └── roadmap.md              ← 1K → 10K → 100K → 1M
├── assets/
│   ├── voice.md                ← derived from real published posts
│   └── projects.md             ← the log that feeds the next post
├── cron/
│   ├── ai-news-daily.md        ← the self-contained daily task
│   └── apply.md                ← create / renew the job
├── scripts/
│   └── make-card.py            ← generates the 1200×1200 news card
├── drafts/                     ← unpublished, with gate scores
└── posted/                     ← archive + URN + day-one numbers
```

---

## Publishing

The skill publishes through [`postiee`](https://github.com/aswathas/postiee),
which uses LinkedIn's official API and captures the post URN at creation.

```bash
postiee post --file draft.md                        # text post
postiee post --file caption.md --pdf deck.pdf --title "Deck"   # carousel
postiee post "text" --mention "Name=urn:li:person:ID"          # real tag
```

Two things the skill enforces:

- **`--dry-run` before every publish, from a script file.** Nested quoting
  through `wsl -e bash -lc '...'` can swallow the trailing flag into `--alt`; a
  swallowed `--dry-run` publishes a real post. Write a `.sh` file and run it.
- **No fake tags.** A mention only renders from little-text markup, and a
  member's URN cannot be looked up at self-serve access. Name the person and link
  their profile unless you have a real URN.

---

## Scheduling

`schedule.toml` holds the whole policy:

```toml
enabled      = true
cron         = "0 9 * * *"
topics       = ["ai-news"]
weights      = [1.0]
auto_publish = true
max_per_day  = 1
```

The daily run: verify a story against its primary source, draft the take, gate
it, generate a card, publish, archive. The image is not downloaded from the
publisher — `scripts/make-card.py` renders a 1200×1200 card from the headline,
so there is no licence to negotiate and no image API to fail at 09:00:

```bash
python scripts/make-card.py \
  --headline "Anthropic open-sources a harness that runs agents for days" \
  --source "Source: Anthropic" --kicker "GEN AI" --out card.png
```

The job reads the file at run time, so changing **topics or weights** needs no
reschedule. Changing **cron** does. `cron/apply.md` creates the job for Command
Code (`cron_create`), Claude Code (`/loop` or an OS scheduler), or anything else
that can run `cron/ai-news-daily.md`.

Guardrails baked into the prompt: one post per day, skip if today already has
one, verify before writing, stop on an auth error, never retry a failed publish.

---

## Requirements

- [`postiee`](https://github.com/aswathas/postiee) + a LinkedIn developer app
  with **Share on LinkedIn** and **Sign In with LinkedIn**
- `postiee auth login` completed once (user-only)
- Optional: an agent with a scheduler for the daily job

---

## What It Won't Do

- **It won't invent numbers.** Every metric must trace to a commit, a PR, or a
  measurement. A rounded-up figure that someone can disprove costs more than it
  buys.
- **It won't fake a tag.** See above.
- **It won't publish below the gate.** The gate is the product.
- **It won't post engagement bait.** No "comment YES", no pods, no fake
  vulnerability arcs.
- **It won't write for you forever.** `voice.md` is derived from your posts; as
  your writing changes, regenerate it.

---

## Attribution

This skill is original. Its rules were informed by reading the highest-star
public LinkedIn skill repositories — `sergebulaev/linkedin-skills` (5,264★),
`Jakeschincariol/linkedin-agent-skill` (2,790★), and six others. Their hook
taxonomies and humanizer categories shaped the references; the roadmap, project
log, gate scoring and publishing path are added here. See
[`NOTICE.md`](./NOTICE.md) for the full list and licences.

---

## Other Skills in This Collection

| Skill | What It Does |
|-------|-------------|
| [deep-teach](../deep-teach) | 7-frame concept decoder for exam prep and deep learning |
| [project-chronicle](../project-chronicle) | Project history, decisions, and dead ends |
| `linkedin-growth` | LinkedIn growth system ← **you are here** |

---

## License

MIT — free to use, modify, and distribute.

---

<p align="center">
  Built for accounts that grow on proof of work, not posting volume.
  <br/>
  <a href="https://github.com/aswathas/agent-skills/issues">Report an issue</a> ·
  <a href="https://github.com/aswathas/agent-skills/pulls">Contribute</a>
</p>
