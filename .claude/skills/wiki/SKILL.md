# SKILL.md — MinedDeep Synthesis

This is the writer synthesis skill for MinedDeep. It governs how
Claude Code produces wiki pages from corpus sources. Read it alongside
`CLAUDE.md`. If they conflict, `CLAUDE.md` takes precedence.

---

## Core Discipline

**Evidence before atmosphere. Argument before impression.**

Every sentence in a wiki page must trace to a source in `raw/corpus/`. If it
cannot, it does not belong in the page body — it belongs in `## Honest Gaps`.

Noun discipline: name the paper, the year, the co-author, the journal, the
specific claim. Do not write "Hassabis has long been interested in memory."
Write "In his 2007 PNAS paper (N1), Hassabis demonstrated for the first time
that hippocampal patients unable to recall the past were equally unable to
*imagine* the future — a finding Science named a Top 10 Breakthrough of the Year."

The difference is: the second sentence could only have been written by someone
who read the source. That is the standard.

---

## `/wiki index all` — Batched §0 Extraction

**Purpose:** Build the axis index from §0 blocks without generating wiki pages.

**Procedure:**

1. List all files in `raw/corpus/` that are not yet in `_corpus_log.json`.
2. Process in batches of 50.
3. For each file:
   - Read the `## §0` block.
   - Extract all 8 required fields. If any are missing, log the file as
     `status: malformed` in `_corpus_log.json` and continue — do not halt.
   - Extract any present optional fields.
   - Add each field value → slug mapping to `_axis_index.json`.
   - Mark the file as `status: indexed` in `_corpus_log.json`.
4. Write `_axis_index.json` and `_corpus_log.json` after each batch of 50.
5. Append a single log entry to `_log.md` summarising the batch.

**Quality gate:** A file is considered successfully indexed only if all 8
required §0 fields are present and their values match the controlled vocabulary
in `CLAUDE.md`. Files failing this gate are marked `status: malformed`.

---

## `/wiki absorb [slug]` — Single-File Page Generation

**Purpose:** Produce a wiki page for one corpus file.

**Procedure:**

1. Confirm the file is in `_corpus_log.json` with `status: indexed`.
   If not, run `/wiki index [slug]` first.
2. Read the full content of the corpus file — §0 through end.
3. Determine page type from the `format` §0 field using this mapping:

   | `format` value | Page type |
   |---|---|
   | `peer-reviewed-paper`, `review-article`, `thesis` | `paper` |
   | `lecture`, `conference-talk` | `lecture` |
   | `interview` | `interview` |
   | `essay`, `op-ed`, `book-review` | `essay` |
   | `blog-post`, `social-post` | `post` |

4. Apply the per-type synthesis guidance below.
5. Write the page to `wiki/pages/[type]--[slug].md`.
6. Update `_corpus_log.json`: `status: absorbed`, `page: [path]`.
7. Add the page to `_index.md` under its type section.
8. Append a log entry to `_log.md`.

---

## Per-Type Synthesis Guidance

### `paper` pages

The reader wants to understand: what did this paper claim, why did it matter,
and where does it sit in Hassabis's intellectual arc?

Structure:
- **Summary** (2–3 sentences): the central finding stated as a claim, not
  a description. "This paper showed X" not "This paper is about X."
- **Argument**: the core hypothesis, the methodology in one sentence, the
  result, and the stated implication. No jargon not earned by the source.
- **Significance**: why this paper specifically — not why the field matters.
  Use citation counts, award citations, or Science/Nature Breakthrough
  designations where present in the corpus file.
- **Connections**: always link to the project page (if applicable), the
  co-author pages, the era page, and any theme pages this paper contributes to.
- **Honest Gaps**: note if full text was not available, if only abstract was
  read, or if key claims could not be verified from available source material.

Do NOT reproduce abstract text verbatim. Restate in your own analytical voice.

### `lecture` pages

The reader wants to know: what was the thesis, what was new here vs. prior
positions, and what specific claims or conjectures did he advance?

- Name the occasion, venue, and date in the first sentence.
- Identify the one or two central arguments that make this lecture distinct
  from his prior record.
- If a specific conjecture was stated (e.g. "any pattern found in nature can
  be learned by a classical algorithm"), give it a `claim--` page and link it.
- Note audience: a Nobel lecture is different from a podcast is different from
  an MIT seminar. The framing shapes what Hassabis was willing to say.

### `interview` pages

Interviews are primary-source texts but not authored texts. Apply extra care:

- Distinguish between: (a) claims Hassabis makes spontaneously vs. (b) claims
  made in response to a leading question.
- Always record the interviewer and platform. The context shapes interpretation.
- For AGI timeline estimates: record the specific estimate AND the caveat
  language he uses. He rarely states timelines without hedging. Capture both.
- Never strip the hedges. "I think there's a 50% chance of AGI by 2030" is
  a different claim from "AGI by 2030."

### `essay` pages

Essays and review articles are the corpus's highest-value authored texts.

- For peer-reviewed reviews (e.g. Neuron 2017): treat with full paper rigour.
- For book reviews, op-eds: note what motivated the piece (book under review,
  occasion, event). These reveal intellectual positioning.
- Identify any arguments that first appear here and later recur in papers or
  lectures — these are intellectual origin points.

### `post` pages

Blog posts and social posts are corpus evidence for positions at a moment in
time. They are not developed arguments.

- Record the platform, approximate date, and the precise text (or as much as
  is available in the corpus file).
- Useful primarily for tracking: first announcement of a project, first public
  statement of a position, real-time reactions.
- Do not over-synthesise. A page for a tweet should be short.

---

## `/wiki synthesise [axis]=[value]` — Cross-Corpus Synthesis

**Purpose:** Produce a synthesis page (theme, project, period, collaborator,
or claim) from all corpus files sharing a given §0 field value.

**Procedure:**

1. Query `_axis_index.json` for all slugs matching `[axis]=[value]`.
2. Confirm all matched slugs have `status: absorbed` in `_corpus_log.json`.
   If any are only indexed (not absorbed), note them as gaps in the synthesis.
3. Read all matched absorbed pages from `wiki/pages/`.
4. Apply the synthesis discipline below.
5. Write the page to `wiki/pages/[type]--[value].md`.

**Synthesis discipline:**

- Open with the thesis: what is the pattern across these sources?
- Build from specific to general — start with the earliest source, track
  development forward in time.
- For **theme** pages: show how the idea evolved. Early statement →
  refinement → mature form. Use source slugs as inline evidence markers:
  `(N1/2007)`, `(A9/2017)`, `(E3/2024)`.
- For **project** pages: track from conception (earliest mention) through
  key milestones to current state. Include team composition where knowable.
- For **period** pages: characterise the intellectual work of that era,
  the key outputs, and the transitions in and out.
- For **claim** pages: state the claim precisely, identify its first
  appearance, note any later refinements or retractions, assess current
  evidential support.
- For **collaborator** pages: identify shared intellectual work, not just
  co-authorship. What problems did they work on together? What was each
  person's contribution?

**Intersection signal format:**

When two axes intersect in a way that reveals something neither reveals alone,
note it explicitly:

```
[Intersection: theme=memory-imagination × era=early-deepmind]
The construction-system hypothesis from the neuroscience phase did not
appear explicitly in early DeepMind papers — but its logic underlies the
replay buffer architecture in DQN (A1/2015). The connection was only made
explicit in A9/2017 (Neuron review) and retrospectively acknowledged
in E3/2024 (Nobel Lecture).
```

---

## Batching Strategy for `/wiki index`

- Process in batches of 50 files.
- Within each batch, process in chronological order by `era` field value.
- After each batch: write axis index, write corpus log, append log entry.
- If a batch encounters 3 or more `malformed` files in sequence, pause and
  report before continuing.
- Never process more than 5 batches in a single session without a status
  report.

---

## Evidence Format

Inline corpus references use the following notation:

```
([slug]/[year])        e.g. (N1/2007) or (A24/2021)
([slug] §[section])    e.g. (A9/2017 §Discussion)
```

Do not use footnote-style references. Evidence marks belong inline.

When a claim cannot be sourced to a specific corpus slug, write:

```
[UNSOURCED — candidate for gap--[topic]]
```

---

## Honest Gaps as First-Class Outputs

A gap page (`gap--[topic].md`) is not a failure. It is a finding.

Create a gap page when:
- A topic is clearly present in Hassabis's work but the relevant source
  has not been acquired for the corpus.
- A claim has been attributed to Hassabis across multiple secondary sources
  but cannot be verified in a primary corpus document.
- A position shift appears to have occurred (earlier and later texts conflict)
  but the transitional text is missing.
- A paper has been cited as Hassabis-authored but is not in the corpus.

Gap page format:
```markdown
# Gap: [topic]

**Type:** gap
**Slug:** gap--[topic]
**Identified:** [date]

## What is missing
[Specific description of the absent source or unverifiable claim.]

## Why it matters
[What this gap prevents the wiki from concluding.]

## Acquisition note
[Where the missing source might be found, if known.]
```

Priority gap at project launch: `gap--learnable-nature-paper`
(Nobel Lecture conjecture; no peer-reviewed paper yet published as of May 2026.)

---

## Quality Standards

Before writing any wiki page, ask:

1. Can every factual claim be traced to a corpus slug?
2. Have I named the paper/year/co-author rather than speaking in generalities?
3. Have I preserved nuance in quoted positions (hedges, caveats)?
4. Does the `## Honest Gaps` section exist, even if brief?
5. Are all cross-links to related pages present in `## Connections`?

If the answer to any of these is no, revise before writing.
