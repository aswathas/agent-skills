# Humanizer and the publish gate

Two jobs: strip the phrases that make a post read as generated, then score the
draft so a weak post does not go out.

## Banned phrases (delete on sight)

**Openers**
- "In today's fast-paced world", "In the ever-evolving landscape of"
- "I'm excited to announce", "Thrilled to share", "Humbled to"
- "Let that sink in", "Read that again"
- "Hot take:", "Unpopular opinion:"

**Fillers**
- "game-changer", "revolutionize", "seamless", "robust", "cutting-edge"
- "leverage", "synergy", "unlock", "empower", "elevate"
- "delve into", "navigate the complexities", "at the end of the day"
- "It's not just X, it's Y" (unless it is the actual argument)
- "This changes everything", "This is huge"

**Closers**
- "Thoughts?", "Agree?", "What do you think? 👇"
- "Drop a comment", "Comment 'YES'", "Follow for more"
- "The future is here", "We're just getting started"

**Structural tells**
- Three-item lists everywhere. Two is fine. Four is fine. Three is suspicious.
- Every paragraph starting with "But", "And", "So".
- A one-line paragraph after every sentence for no reason.
- Bolded first three words of each bullet.
- Emoji at the start of every line.
- A hook, a line break, then a single word on its own line for drama.

## Replace, do not decorate

| Generated | Human |
|---|---|
| "leverage a robust caching layer" | "cache it on (mtime, size)" |
| "significantly faster" | "15s cold, under 1s warm" |
| "seamless integration" | "one command, no account" |
| "revolutionize your workflow" | "moves the skill folder instead of deleting it" |

Specificity is the humanizer. If a sentence could appear in someone else's post
unchanged, it is not doing work.

## The 10-point gate

Score each 0–2. **Publish at 8+.** Below 6, rewrite from the angle, not the
sentences.

| Axis | 0 | 1 | 2 |
|---|---|---|---|
| **Clarity** | needs a second read | mostly clear | one pass, no ambiguity |
| **Specificity** | adjectives only | one concrete detail | numbers, paths, names |
| **Voice** | generic LinkedIn | resembles the account | indistinguishable from `voice.md` |
| **Honesty** | overclaims | accurate, vague | accurate, states the limit |
| **Ending** | "Thoughts?" | a weak CTA | a real question or a concrete next step |

Also required regardless of score:
- Hook under ~110 characters across two lines.
- 3–5 hashtags, at the end.
- No banned phrase from the list above.
- Every claim traceable to a commit, PR, file or measurement.

## Before publishing, read it aloud once

If a sentence is hard to say, it is hard to read. Cut it. If two consecutive
sentences start the same way, change one. If the post has no number in it, ask
whether it has any information at all.

## Post-publish

Reply to every comment for the first 30 minutes. A post with no author reply
teaches the feed that the author does not engage.
