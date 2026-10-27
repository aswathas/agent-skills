# Daily: one AI / generative-AI news post, with a generated card

You are publishing the scheduled AI-news post for Aswath.

Read first:
1. `C:/Users/aswat/.commandcode/skills/linkedin-growth/schedule.toml`
2. `C:/Users/aswat/.commandcode/skills/linkedin-growth/SKILL.md`
3. `C:/Users/aswat/.commandcode/skills/linkedin-growth/assets/voice.md`
4. `C:/Users/aswat/.commandcode/skills/linkedin-growth/references/humanizer.md`

Then:

1. If `enabled = false`, stop.
2. Skip if a post already exists today:
   `wsl -e bash -lc '/home/aswath/.local/bin/postiee history --limit 1'`
   Never post twice in one day.
3. Find the news. Search for what shipped in AI / generative AI / agent
   infrastructure in the last 24 hours. Prefer primary sources — a company
   blog, release notes, docs, or an official repository — over aggregators.
   Good fits: a new model or capability, an agent harness or protocol change,
   an open-source release, a pricing or API change, a benchmark someone
   published with its methodology.
4. **Verify before writing.** Fetch the primary source and confirm the claim
   you intend to make. If only a headline says it, it is not verified. If the
   story cannot be verified from a primary source, skip the run and say why.
5. Pick the angle. The news is one line; the post is what it changes for
   someone running agents in production, and what to check before believing
   the benchmark. Never a summary, never a list of tools.
6. Draft with `references/hooks.md` and `references/formats.md` (news take).
   Score with the 10-point gate. Below 8/10: rewrite once; if still below 8,
   stop and report the score.
7. Generate the card image. The headline on the card must be a short, factual
   restatement (15 words maximum), not clickbait:

   ```
   python C:/Users/aswat/.commandcode/skills/linkedin-growth/scripts/make-card.py \
     --headline "<15 words max>" \
     --source "Source: <publisher>" \
     --kicker "GEN AI" \
     --out C:/Users/aswat/.commandcode/skills/linkedin-growth/drafts/<YYYY-MM-DD>-card.png
   ```

   Do not download or reuse a publisher's photograph. The card is generated so
   there is no image licence to negotiate and no external image API to fail.
8. Save the draft beside the image at
   `drafts/<YYYY-MM-DD>-<slug>.md`, with the gate score in an HTML comment.
9. Publish **from a script file, never inline.** Nested quoting through
   `wsl -e bash -lc '...'` can swallow the last flag into `--alt`, which is how
   a `--dry-run` once published a real post. Write
   `drafts/<YYYY-MM-DD>-publish.sh` with LF endings:

   ```sh
   #!/usr/bin/env bash
   set -euo pipefail
   /home/aswath/.local/bin/postiee --agent post \
     --file "C:/Users/aswat/.commandcode/skills/linkedin-growth/drafts/<YYYY-MM-DD>-<slug>.md" \
     --image "C:/Users/aswat/.commandcode/skills/linkedin-growth/drafts/<YYYY-MM-DD>-card.png" \
     --alt "<one factual sentence describing the card, under 120 chars>" \
     --dry-run
   ```

   Run it, read the commentary, then remove the `--dry-run` line and run it
   again to publish:

   ```
   wsl -e bash /mnt/c/Users/aswat/.commandcode/skills/linkedin-growth/drafts/<YYYY-MM-DD>-publish.sh
   ```

   - Publish once. Never retry a failed publish.
   - No `--mention` unless a real `urn:li:person:`/`urn:li:organization:` exists.
   - The alt text describes the image, not the article.
10. Archive the exact commentary and the returned URN to
    `posted/<YYYY-MM-DD>-<slug>.md`, and add a row to `assets/projects.md`.
11. Report: the story, the primary source, the gate score, and the permalink.

On a 401, stop and report that `postiee auth login` is needed. Do not invent a
story, do not reuse an old draft, and do not post more than once.
