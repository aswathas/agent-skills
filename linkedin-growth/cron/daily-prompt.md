You are running the scheduled LinkedIn post for Aswath.

Read these first, in this order:
1. `C:/Users/aswat/.commandcode/skills/linkedin-growth/schedule.toml`
2. `C:/Users/aswat/.commandcode/skills/linkedin-growth/SKILL.md`
3. `C:/Users/aswat/.commandcode/skills/linkedin-growth/assets/voice.md`
4. `C:/Users/aswat/.commandcode/skills/linkedin-growth/references/humanizer.md`

Then do exactly this:

1. If `enabled = false` in schedule.toml, stop and say so.
2. Check whether a post already exists today:
   `wsl -e bash -lc '/home/aswath/.local/bin/postiee history --limit 1'`
   If today already has a post, stop. Never post twice in one day.
3. Pick one topic using the weights in schedule.toml:
   - `ai-news`: search the day's AI/agent news and pick one story where the
     account has a first-hand angle from `assets/projects.md`. Never a summary.
   - `build-log`, `oss-contribution`, `teardown`: read `assets/projects.md` and
     pick a row whose status is `IDEA` that fits the pillar.
   If nothing fits, skip the run and say why.
4. Draft using `references/hooks.md` (three hooks, pick one),
   `references/pillars.md` and `references/formats.md`. Append the `angle` from
   schedule.toml to the brief.
5. Score the draft with the 10-point gate in `references/humanizer.md`.
   Below 8/10: rewrite once. If still below 8, stop and report the score —
   do not publish a weak post.
6. Save the draft to
   `C:/Users/aswat/.commandcode/skills/linkedin-growth/drafts/<YYYY-MM-DD>-<slug>.md`
   with the gate score in an HTML comment at the top.
7. If `auto_publish = true`, publish it:
   `wsl -e bash -lc '/home/aswath/.local/bin/postiee --agent post --file <windows path> --visibility PUBLIC'`
   - Use `--pdf` only when the format is a carousel.
   - Never use `--mention` unless you have a real `urn:li:person:` or
     `urn:li:organization:` URN. A name in plain text is acceptable; a fake tag
     is not.
   - Run once. Never retry a failed publish, and never post a second time to
     "fix" a failure.
8. Archive the exact commentary and the returned URN to
   `C:/Users/aswat/.commandcode/skills/linkedin-growth/posted/<YYYY-MM-DD>-<slug>.md`,
   and change the matching row in `assets/projects.md` to `POSTED`.
9. Report: the topic, the pillar, the gate score, and the permalink.

On a 401 or auth error, stop and report that `postiee auth login` is needed.
Do not invent a post, do not reuse an old draft, and do not exceed one post.
