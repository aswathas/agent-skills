# 🌿 deep-teach

> **8-lens concept decoder for exam prep and deep learning.**
> Give it any topic. It teaches you from first principles, locks it in memory, and writes the exam answer for you.

[![Install](https://img.shields.io/badge/install-npx%20skills-4a7c59?style=flat-square&logo=npm)](https://skills.sh/aswathas/agent-skills/deep-teach)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-CLI%20Skill-f9a620?style=flat-square&logo=anthropic)](https://claude.ai/code)
[![License: MIT](https://img.shields.io/badge/License-MIT-b7472a?style=flat-square)](LICENSE)
[![Works on Any Topic](https://img.shields.io/badge/works%20on-any%20topic-4a7c59?style=flat-square)](#-works-on-any-topic)

---

## What is it?

`/deep-teach` is a [Claude Code](https://claude.ai/code) CLI skill that **decodes any concept through 8 structured thinking frameworks** — the same mental models used by physicists, teachers, consultants, and memory champions.

You type one command. You get:

- 🔬 **First Principles** — why this concept exists at all
- 🧒 **Feynman Simplification** — the 2-sentence version a 12-year-old understands
- 📦 **Chunking** — the natural groups experts actually see
- 🌉 **Analogy Bridge** — mapped to something you already know
- 🔄 **Inversion** — what breaks without it + exam traps
- 🔗 **Systems View** — where it fits in the larger picture
- 🗂️ **MECE Map** — clean, non-overlapping taxonomy
- 🔒 **Memory Lock** — acronym/story/palace that makes it stick
- 📝 **Exam-Ready Answer** — structured for 1-mark, 10-mark, or 15-mark formats

All rendered as a **self-contained HTML artifact** with the Botanical Garden theme — cream background, fern green headers, marigold accents, terracotta highlights.

---

## Install

```bash
npx skills add aswathas/agent-skills@deep-teach -g
```

> Requires [Claude Code CLI](https://claude.ai/code). The `-g` flag installs globally so it works in any project.

---

## Usage

```
/deep-teach <topic>
```

### Examples

```
/deep-teach Pandas DataFrame
/deep-teach Data Wrangling
/deep-teach K-means Clustering
/deep-teach OSI Model
/deep-teach Newton's Second Law
/deep-teach Photosynthesis
/deep-teach Opportunity Cost
/deep-teach Recursion
```

---

## The 8 Lenses

Each lens is a different cognitive angle on the same concept. Together they build the kind of understanding that transfers to any question format — not just the one you practiced.

```
╔══════════════════════════════════════════════════════════╗
║              /deep-teach  ·  8-Lens Decoder              ║
╠══════════════════════════════════════════════════════════╣
║  Lens 1 │ 🔬 First Principles    │ WHY IT EXISTS         ║
║         │ Strip to bare truths   │ Build back up         ║
╠══════════════════════════════════════════════════════════╣
║  Lens 2 │ 🧒 Feynman             │ SIMPLE TRUTH          ║
║         │ Explain to a child     │ No jargon allowed     ║
╠══════════════════════════════════════════════════════════╣
║  Lens 3 │ 📦 Chunking            │ THE CHUNKS            ║
║         │ 3-5 named clusters     │ How experts see it    ║
╠══════════════════════════════════════════════════════════╣
║  Lens 4 │ 🌉 Analogy Bridge      │ ANALOGY               ║
║         │ Map to familiar thing  │ Make it obvious       ║
╠══════════════════════════════════════════════════════════╣
║  Lens 5 │ 🔄 Inversion           │ INVERSION / TRAP      ║
║         │ What breaks without it │ Exam gotchas          ║
╠══════════════════════════════════════════════════════════╣
║  Lens 6 │ 🔗 Systems Thinking    │ SYSTEMS VIEW          ║
║         │ Input → [This] → Output│ Where it fits         ║
╠══════════════════════════════════════════════════════════╣
║  Lens 7 │ 🗂️ MECE Breakdown      │ MECE MAP              ║
║         │ McKinsey taxonomy      │ No gaps, no overlaps  ║
╠══════════════════════════════════════════════════════════╣
║  Lens 8 │ 🔒 Memory Technique    │ MEMORY LOCK           ║
║         │ Acronym / Story / Palace│ Makes it stick       ║
╠══════════════════════════════════════════════════════════╣
║  Final  │ 📝 Exam-Ready Answer   │ WRITE THIS IN EXAM    ║
║         │ 1 / 10 / 15 marks      │ Time badge included   ║
╚══════════════════════════════════════════════════════════╝
```

### Lens Details

| # | Lens | Prompt It Answers | Output Label |
|---|------|-------------------|-------------|
| 1 | **First Principles** | *Why does this exist? What problem does it solve?* | WHY IT EXISTS |
| 2 | **Feynman** | *How would you explain this to a curious 12-year-old?* | SIMPLE TRUTH |
| 3 | **Chunking** | *What are the 3–5 natural groups inside this concept?* | THE CHUNKS |
| 4 | **Analogy Bridge** | *This is like ___ because ___* | ANALOGY |
| 5 | **Inversion** | *What goes wrong if this doesn't exist? What are the exam traps?* | INVERSION / TRAP |
| 6 | **Systems Thinking** | *What feeds into this? What does it feed into?* | SYSTEMS VIEW |
| 7 | **MECE Breakdown** | *How do you organize everything with no overlaps, no gaps?* | MECE MAP |
| 8 | **Memory Technique** | *What acronym, story, or visual makes this unforgettable?* | MEMORY LOCK |

---

## Output: Botanical Garden HTML Artifact

Every `/deep-teach` run produces a **self-contained HTML page** rendered directly in your Claude Code session.

**Color scheme:**

```
Background  ·  #f5f3ed  Cream        — easy on the eyes
Headers     ·  #4a7c59  Fern Green   — calm, natural authority
Accents     ·  #f9a620  Marigold     — highlights key terms
Highlights  ·  #b7472a  Terracotta   — warnings, traps, memory
Text        ·  #2c2c2c  Near-black   — readable in all light
```

**Card border colors per lens:**
- 🟢 Fern Green → First Principles, Chunking, Systems Thinking
- 🟡 Marigold → Feynman, Analogy, MECE
- 🔴 Terracotta → Inversion, Memory Technique
- 🟢 Fern Green (prominent) → Exam Answer

**Exam Answer block** includes:
- `10 marks · ~8 minutes` time badge
- Prose-first, code-second format (written exam style)
- Part A (1 mark) / Part B (10 marks) / Part C (15 marks) variants

---

## Why 8 Lenses?

Most study methods teach **what** a concept is. Eight lenses teach you **why** it matters, **how** it works, **where** it fits, and **how to remember** it — permanently.

The cognitive science behind each lens:

| Lens | Cognitive Principle |
|------|---------------------|
| First Principles | Elon Musk / Aristotle — breaks availability bias, forces real understanding |
| Feynman | Richard Feynman's learning technique — if you can't simplify it, you don't know it |
| Chunking | Miller's Law (7±2) — experts store knowledge in chunks, not individual facts |
| Analogy | Schema theory — new knowledge sticks when anchored to existing mental models |
| Inversion | Charlie Munger — thinking backward reveals failure modes and exam traps |
| Systems Thinking | Donella Meadows — understanding context prevents knowledge silos |
| MECE | McKinsey framework — exhaustive taxonomy prevents forgotten edge cases |
| Memory Technique | Spaced repetition + encoding specificity — memory hooks beat re-reading |

> **The result:** After one `/deep-teach` session, you can reconstruct the concept from memory, answer any question format, and spot the traps examiners love to set.

---

## Works on Any Topic

Originally built for **SRM University Data Science (21CSS303T)**, but the 8 lenses work universally:

| Domain | Example Topics |
|--------|---------------|
| 📊 Data Science | `Pandas DataFrame`, `K-means Clustering`, `Overfitting`, `IQR` |
| 💻 Computer Science | `Recursion`, `Binary Search`, `OSI Model`, `TCP/IP` |
| ⚙️ Engineering | `Newton's Second Law`, `Thermodynamic Cycles`, `Signal Processing` |
| 🧬 Biology | `Photosynthesis`, `DNA Replication`, `Natural Selection` |
| 📈 Economics | `Opportunity Cost`, `Supply and Demand`, `Nash Equilibrium` |
| 🏛️ History | `Industrial Revolution`, `Cold War`, `Colonialism` |
| 🔢 Mathematics | `Integration by Parts`, `Eigenvalues`, `Bayes' Theorem` |
| ⚖️ Law | `Consideration in Contract`, `Negligence`, `Habeas Corpus` |

---

## How It Works Internally

```
/deep-teach <topic>
      │
      ▼
 Read topic from trigger argument
      │
      ▼
 Identify subject unit + PYQ frequency
      │
      ▼
 Apply all 8 lenses in sequence
 (Each lens builds on the previous)
      │
      ▼
 Write exam answer
 (1-mark / 10-mark / 15-mark format)
      │
      ▼
 Render Botanical Garden HTML artifact
 (Self-contained, no external dependencies)
```

**Quality rules enforced by the skill:**
- No full programs in lens cards — max 3 lines of code per snippet
- Every analogy must be from everyday life, not another CS concept
- Memory technique must be original — not the first obvious acronym
- Exam answer is prose-first, code-second (written exam style)
- Inversion must include at least one actual exam trap from PYQ patterns
- MECE map must be a real taxonomy, not a bullet list in disguise

---

## Requirements

- [Claude Code CLI](https://claude.ai/code) — `claude` command available in terminal
- Node.js ≥ 18 (for `npx skills`)
- No API keys required beyond Claude Code authentication

---

## Installation

### Global install (recommended)
```bash
npx skills add aswathas/agent-skills@deep-teach -g
```

### Project-level install
```bash
npx skills add aswathas/agent-skills@deep-teach
```

### Verify installation
```bash
npx skills list | grep deep-teach
```

### Use it
```bash
claude
/deep-teach Pandas DataFrame
```

---

## Updating

```bash
npx skills update
```

Or reinstall:
```bash
npx skills add aswathas/agent-skills@deep-teach -g -y
```

---

## Contributing

Found a topic where the lenses could be sharper? Want to add a 9th lens? PRs welcome.

1. Fork this repo
2. Edit `deep-teach/SKILL.md`
3. Test with `/deep-teach <your test topic>`
4. Open a PR with before/after output examples

**Ideas for contributions:**
- Add subject-specific context sections (Physics, Economics, Law)
- Improve the Memory Technique lens with more techniques (method of loci, peg system)
- Add an adaptive difficulty mode (beginner / expert)
- Add a "compare two concepts" mode

---

## Other Skills in This Collection

| Skill | What It Does |
|-------|-------------|
| `deep-teach` | 8-lens concept decoder for exam prep ← **you are here** |
| *(more coming)* | — |

---

## License

MIT — free to use, modify, and distribute.

---

<p align="center">
  Built with 🌿 for anyone who wants to actually understand, not just memorize.
  <br/>
  <a href="https://github.com/aswathas/agent-skills/issues">Report an issue</a> ·
  <a href="https://github.com/aswathas/agent-skills/pulls">Contribute</a>
</p>
