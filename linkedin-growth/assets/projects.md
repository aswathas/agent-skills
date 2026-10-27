# Project log

The raw material for build logs, teardowns and open-source posts. Append a row
whenever something ships, merges, wins, or breaks in an interesting way. The
next post comes from this table, not from memory.

**Status:** `IDEA` (exists, not written) · `DRAFTED` · `POSTED`

| Date | Project | What shipped | Evidence | Status |
|---|---|---|---|---|
| 2026-10-21 | HarnessRouter | W3C trace context propagated end to end (PR 537) | +847/−12 · runner 1109 tests · gateway 1229 | POSTED |
| 2026-10-21 | HarnessRouter | Conformance T-12 measures the step budget (PR 536) | suite 2026.10.19.post3 | POSTED |
| 2026-10-21 | HarnessRouter | Grok partial streaming through `_want_partial()` (PR 533) | +164/−6 | POSTED |
| 2026-10-22 | HarnessRouter | Failed turns keep exception, stack, base and tool (PR 545) | 11 new tests | POSTED |
| 2026-10-22 | HarnessRouter | Aider writes the block instead of answering "DONE" (PR 544) | 5 of 6 → fixed | POSTED |
| 2026-10-26 | Captain Code | Local control room over a Claude Code install | 181 skills, 33 parked, 29 plugins, 31 memory files | POSTED |
| 2026-10-24 | VIHANSA-2K26 | First prize, Web3 stolen-fund tracing | 24h hackathon, SRIT Coimbatore | POSTED |
| 2026-10-22 | Stock MCP | Free MCP server for the Indian stock market | repo + demo | POSTED |
| 2026-10-28 | postiee | Little-text mentions, PDF document posts, escape fix | 5 new tests, 8 new files | IDEA |

## How to add a row

```
| 2026-11-02 | <project> | <one line, concrete> | <commit / PR / metric> | IDEA |
```

Rules:
- One line. If it needs two, it is two projects.
- The Evidence column must be checkable. A PR number, a commit, a measured
  number, a link. "Improved performance" is not evidence.
- Never write a post from an IDEA row without going back for the number.

## Angles waiting to be written

- Why a silent failure is more expensive than a crash (teardown, from the
  HarnessRouter PRs).
- The conformance suite that measured nothing (teardown).
- What de-duplicating transcripts taught me about trusting dashboards (build
  log, Captain Code).
- A mention that does not render is worse than no mention (postiee, open
  source).
