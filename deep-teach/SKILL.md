---
name: deep-teach
description: Multi-lens teaching skill. Takes any concept/topic and teaches it through 7 thinking frameworks (First Principles, Feynman, Chunking, Analogy, Inversion, Systems Thinking, MECE), adds a memory technique, then delivers an exam-ready answer. Styled with Botanical Garden theme.
trigger: /deep-teach
---

# /deep-teach

A multi-lens concept decoder built for exam preparation. Given any topic, it walks through 7 structured thinking frameworks to build deep understanding, then produces a ready-to-write exam answer.

## Trigger

`/deep-teach <topic>`

Examples:
- `/deep-teach Pandas DataFrame`
- `/deep-teach Data Wrangling`
- `/deep-teach GroupBy and Aggregation`
- `/deep-teach NumPy array indexing`

## What It Does

For any given topic, produce a structured HTML artifact with the **Botanical Garden** theme, walking through these 8 lenses in order:

---

## The 8 Lenses

### Lens 1 — First Principles
> *"What are the most basic truths this concept is built on? Strip away all assumptions."*

- Ask: Why does this exist? What problem was it solving?
- Reduce to 2-3 irreducible facts
- Then show how the full concept is built back up from those facts
- Label: **WHY IT EXISTS**

---

### Lens 2 — Feynman Simplification
> *"Explain it so a curious 12-year-old understands in 2-3 sentences. No jargon."*

- Use plain language, no technical terms
- If you can't simplify it, you don't understand it yet
- This lens forces genuine understanding over memorization
- Label: **SIMPLE TRUTH**

---

### Lens 3 — Chunking
> *"Group everything into 3-5 named clusters. Give each cluster a memorable label."*

- Identify the natural sub-groups within the topic
- Name each chunk clearly (e.g., "The Create family", "The Select family")
- List 3-5 items per chunk max
- This is what experts do — they don't see 20 facts, they see 4 chunks of 5
- Label: **THE CHUNKS**

---

### Lens 4 — Analogy Bridge
> *"This is like ___ because ___. Map the concept to something already familiar."*

- Pick something from everyday life or a well-known domain
- Explicitly map: new concept element → familiar element
- Best analogies make the unfamiliar feel obvious in hindsight
- Label: **ANALOGY**

---

### Lens 5 — Inversion (Charlie Munger)
> *"What would break if this concept didn't exist? What's the opposite of this?"*

- Invert the question: instead of "how does X work?", ask "what goes wrong without X?"
- This reveals the concept's true value and common failure modes
- Also surfaces exam traps — the "gotchas" examiners love
- Label: **INVERSION / TRAP**

---

### Lens 6 — Systems Thinking
> *"Where does this fit? What feeds into it, what does it feed into?"*

- Map: Input → [This Concept] → Output
- Show what comes before and after in the larger workflow
- Helps answer "why are we learning this?" and connects units together
- Label: **SYSTEMS VIEW**

---

### Lens 7 — MECE Breakdown (McKinsey)
> *"Organize everything into buckets that don't overlap and don't miss anything."*

- MECE = Mutually Exclusive, Collectively Exhaustive
- Create a clean taxonomy with no duplicates and no gaps
- This is the structure that turns into great exam answers
- Label: **MECE MAP**

---

### Lens 8 — Memory Technique
> *"Acronym, story, rhyme, or visual palace to lock this in."*

- Choose the best fit: acronym / narrative story / visual image / rhyme / palace
- Make it specific to the concept — generic tricks don't stick
- Label: **MEMORY LOCK**

---

## Output Format

Produce a **self-contained HTML artifact** using the Botanical Garden theme:

```
Colors:
  Background:  #f5f3ed  (Cream)
  Headers:     #4a7c59  (Fern Green)
  Accents:     #f9a620  (Marigold)
  Highlights:  #b7472a  (Terracotta)
  Text:        #2c2c2c  (near-black for readability)

Typography:
  Headers:     Georgia, serif (DejaVu Serif equivalent)
  Body:        system-ui, sans-serif
  Code:        'Courier New', monospace

Card border-left colors per lens:
  First Principles → #4a7c59 (Fern Green)
  Feynman          → #f9a620 (Marigold)
  Chunking         → #4a7c59 (Fern Green)
  Analogy          → #f9a620 (Marigold)
  Inversion        → #b7472a (Terracotta)
  Systems          → #4a7c59 (Fern Green)
  MECE             → #f9a620 (Marigold)
  Memory           → #b7472a (Terracotta)
  Exam Answer      → #4a7c59 (Fern Green, prominent)
```

### HTML Structure
```html
<!DOCTYPE html>
<html>
<head>
  <title>[Topic] — Deep Teach</title>
  <style>/* Botanical Garden theme CSS */</style>
</head>
<body>
  <header>
    <div class="subject-tag">21CSS303T · Data Science</div>
    <h1>[Topic Name]</h1>
    <p class="tagline">8-lens deep decode</p>
  </header>

  <!-- One card per lens -->
  <div class="lens-card" data-lens="first-principles">
    <div class="lens-label">Lens 1 · First Principles</div>
    <div class="lens-title">WHY IT EXISTS</div>
    <div class="lens-content">...</div>
  </div>

  <!-- ... repeat for all 8 lenses ... -->

  <!-- Final exam answer — prominent, boxed -->
  <div class="exam-answer">
    <div class="exam-label">EXAM-READY ANSWER</div>
    <div class="marks-badge">10 marks · ~8 minutes</div>
    <div class="exam-content">...</div>
  </div>

</body>
</html>
```

---

## Execution Steps

1. **Read the topic** from the trigger argument (e.g., `/deep-teach Pandas DataFrame`)
2. **Identify the unit** it belongs to (from SRM Data Science 21CSS303T syllabus context)
3. **Check PYQ frequency** — note how many papers this appeared in and in which part (A/B/C)
4. **Work through all 8 lenses** with content specific to the topic
5. **Write the exam answer** — structured for the exact marks/format of SRM exams:
   - Part A style (1 mark): one crisp definition sentence
   - Part B style (10 marks): definition + 4-5 sub-points with code snippets (max 3 lines each)
   - Part C style (15 marks): full worked example with narrative explanation
6. **Render as Botanical Garden HTML artifact**

---

## Context (SRM Data Science 21CSS303T)

**Exam format:** Part A (20×1=20) · Part B (4 of 6 × 10=40) · Part C (1×15=15) = 75 marks

**Unit map:**
- Unit 1: Data Science Intro, NumPy, Pandas, Data Acquisition
- Unit 2: Data Wrangling, Cleaning, Transformation
- Unit 3: Matplotlib, Seaborn, Advanced Visualization
- Unit 4: Scikit-learn, ML Models
- Unit 5: Advanced ML, Evaluation

**High-frequency topics (4/4 papers):** Data Wrangling, Pandas DataFrame, Matplotlib/Seaborn, GroupBy+Aggregation, Scikit-learn

---

## Quality Rules

- No full programs in lens cards — code max 3 lines per snippet
- Every analogy must be from everyday life (not from another CS concept)
- Memory technique must be original — not the first obvious acronym
- Exam answer must be prose-first, code-second (written exam style)
- Inversion lens must include at least one actual exam trap from PYQ patterns
- MECE map must be a real taxonomy, not a bullet list dressed up as MECE
