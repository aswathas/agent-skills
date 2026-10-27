# Applying the schedule

Read `../schedule.toml`. If `enabled = false`, delete the daily job (if one
exists) and stop.

Otherwise create two cron jobs with `cron_create`, **one call per turn** — two
creates in the same turn race and one write can be lost.

**1. The daily AI-news post**

- `cron`: the `cron` value from `schedule.toml` (default `0 9 * * *`)
- `recurring`: `true`
- `durable`: `true`
- `prompt`: the full contents of `ai-news-daily.md`, verbatim

**2. The re-arm**

Recurring cron jobs expire after seven days. Create a one-shot six days out
that re-runs this file, so the schedule renews itself:

- `cron`: `30 8 <day six days from today> <month> *`
- `recurring`: `false`
- `durable`: `true`
- `prompt`: `Read C:/Users/aswat/.commandcode/skills/linkedin-growth/cron/apply.md and run it exactly as written. This is the weekly re-arm: recreate the daily AI-news job and schedule the next re-arm. Then report the job ids and the next fire time.`

Before creating, call `cron_list` and delete any job whose prompt starts with
either:

- `You are publishing the scheduled AI-news post`
- `You are running the scheduled LinkedIn post`

so a re-apply cannot create duplicates or leave an older rotation job running.

After creating, report both job ids and the next fire time.

## Changing the schedule later

- Topics, weights, auto_publish, visibility: edit `schedule.toml`. No re-apply
  needed — the daily job reads the file at run time.
- `cron`: edit `schedule.toml`, then run this file again so the timing and the
  re-arm move together.
- Off: set `enabled = false` and delete the jobs.
