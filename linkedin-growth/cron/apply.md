# Applying the schedule

Read `../schedule.toml`. If `enabled = false`, delete the daily job (if one
exists) and stop.

Otherwise create two cron jobs with `cron_create`:

**1. The daily post**

- `cron`: the `cron` value from `schedule.toml` (default `7 9 * * 1-5`)
- `recurring`: `true`
- `durable`: `true`
- `prompt`: the full contents of `daily-prompt.md`, verbatim

**2. The re-arm**

Recurring cron jobs expire after seven days. Create a one-shot six days out
that re-runs this file, so the schedule renews itself:

- `cron`: `30 8 <day six days from today> <month> *`
- `recurring`: `false`
- `durable`: `true`
- `prompt`: `Read C:/Users/aswat/.commandcode/skills/linkedin-growth/cron/apply.md and run it exactly as written. Then report the job ids.`

Before creating, call `cron_list` and delete any existing job whose prompt starts
with "You are running the scheduled LinkedIn post" so a re-apply cannot create
duplicates.

After creating, report both job ids and the next fire time.

## Changing the schedule later

- Topics, weights, auto_publish, visibility: edit `schedule.toml`. No re-apply
  needed — the daily job reads the file at run time.
- `cron`: edit `schedule.toml`, then run this file again (`schedule apply`) so
  the timing and the re-arm move together.
- Off: set `enabled = false` and delete the jobs.
