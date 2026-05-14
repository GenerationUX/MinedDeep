# CLAUDE.md — MinedDeep

Read this file before every session.

---

## What This Project Is

A structured, interlinked wiki built on the Karpathy LLM Wiki pattern with
Farzaa's writer-oriented synthesis layer. The corpus is the complete published
intellectual output of Sir Demis Hassabis (b. 1976) — co-founder and CEO of
Google DeepMind, 2024 Nobel Laureate in Chemistry — spanning peer-reviewed
papers, authored essays, formal lectures, long-form interviews, and notable
public statements.

The wiki is the navigation and synthesis layer built on top of that corpus.
It reads the §0 metadata classifications and full text of source files to
produce indexed, interlinked, synthesised knowledge about Hassabis's thinking,
recurring arguments, intellectual development, and open questions.

Raw sources live in `raw/`. The wiki lives in `wiki/`. You write the wiki.
You never modify `raw/`.

---

## Mission Discipline

This wiki is evidence-first and source-driven.

- Every claim traces to a specific document, page, or timestamp in `raw/`.
- Noun-first: papers, dates, arguments, co-authors, institutions, projects.
- Things over moods. What he *said*, not merely how he *seemed*.
- Track change over time: when did a position appear? When did it shift?
- Distinguish authored text (first-person intellectual ownership) from
  attributed paraphrase (journalist summaries, third-party reporting).
- Bias toward: peer-reviewed papers, formal lectures, authored essays.
  Interviews as secondary; social posts as tertiary.

These principles govern every wiki page. Synthesis must be specific enough
that the reader can identify the paper, the year, the co-author, the argument
— not just the general theme.

---

## Architecture

```
raw/corpus/           Immutable. Source files in [slug]--Hassabis.md format.
                      You read these. You never write here.

wiki/                 Your domain. Everything here is LLM-generated.
  _index.md           Content catalog — every page with a one-line summary.
  _log.md             Append-only operation log. Never delete entries.
  _axis_index.json    Taxonomy axis lookup table — maps §0 values to slugs.
  _corpus_log.json    Per-file read and absorption tracking.
  pages/              All wiki articles — flat directory, slug-named.

assets/               Diagrams, timelines, exported reference figures.
```

---

## §0 Taxonomy Fields

Every source file in `raw/corpus/` must contain a `## §0` block. Fields:

### Required fields (8)

| Field | Description |
|---|---|
| `format` | The type of document — see controlled vocabulary below |
| `domain` | Primary intellectual domain of the text |
| `era` | Career phase during which the text was produced |
| `venue` | Publication, platform, or event where text appeared |
| `theme` | Primary recurring intellectual theme(s) — multi-value |
| `project` | Named DeepMind/research project referenced, if any |
| `co-authors` | Named collaborators (for papers); interviewers (for interviews) |
| `impact` | Significance markers — see controlled vocabulary |

### Optional fields (5)

| Field | Description |
|---|---|
| `claim` | A specific named argument or conjecture stated in the text |
| `influences` | Named intellectual influences cited or invoked |
| `contradicts` | Positions this text revises or contradicts vs. earlier texts |
| `open-questions` | Problems the text explicitly leaves unsolved |
| `notable-quote` | A single sentence of particular analytical value (verbatim, ≤25 words) |

---

## Domain Taxonomy (Controlled Vocabulary)

### `format`
```
peer-reviewed-paper · review-article · thesis · lecture · interview
essay · op-ed · blog-post · social-post · book-review · conference-talk
```

### `domain`
```
cognitive-neuroscience · reinforcement-learning · protein-structure
game-playing-AI · neuroscience-AI-bridge · AI-for-science
safety-governance · AGI-theory · consciousness · multi-agent-systems
clinical-AI · mathematics-AI
```

### `era`
```
phd-period (2007–2009) · postdoc-period (2009–2010)
early-deepmind (2010–2015) · deepmind-ascent (2015–2018)
alphafold-era (2018–2022) · post-alphafold (2022–present)
```

### `venue`
```
Nature · Science · Neuron · PNAS · Current-Biology · Nature-Medicine
Nature-Neuroscience · Trends-Cognitive-Sciences · Cerebral-Cortex
Journal-of-Neuroscience · Proteins · Nucleic-Acids-Research · bioRxiv
Nobel-Prize · TIME · The-Guardian · Wired · NYT · Lex-Fridman-Podcast
CBMM-MIT · DeepMind-Blog · Google-Blog · LinkedIn · Twitter-X
```

### `theme` *(multi-value)*
```
memory-imagination · hippocampal-construction · episodic-memory
reinforcement-learning · deep-RL · self-play · model-based-RL
protein-folding · structural-biology · drug-discovery
game-playing-AI · go · chess · starcraft
neuroscience-AI-bridge · complementary-learning-systems
AI-for-science · learnable-nature-conjecture
safety-governance · AGI-risk · international-coordination
AGI-definition · AGI-timelines · consciousness
```

### `project`
```
AlphaGo · AlphaGo-Zero · AlphaZero · MuZero · AlphaStar
AlphaFold · AlphaFold2 · AlphaFold3 · AlphaFold-Multimer
AlphaGeometry · AlphaProof · DQN · DNC · GQN
DeepMind-general · Isomorphic-Labs · Gemini
hippocampus-research · (none)
```

### `impact`
```
Nobel-cited · Science-breakthrough · Nature-frontpage
field-defining · top-cited · policy-relevant · first-authored
career-origin · public-statement · conjecture
```

---

## Page Types

| Type | Slug prefix | Description |
|---|---|---|
| `paper` | `paper--` | A single peer-reviewed publication |
| `lecture` | `lecture--` | A formal delivered lecture with transcript or recording |
| `interview` | `interview--` | A long-form public interview |
| `essay` | `essay--` | An authored non-peer-reviewed written piece |
| `post` | `post--` | Blog post, social post, or short statement |
| `theme` | `theme--` | Synthesis: a recurring intellectual theme across sources |
| `project` | `project--` | Synthesis: a named research project (AlphaFold, AlphaGo, etc.) |
| `period` | `period--` | Synthesis: a career phase |
| `collaborator` | `collaborator--` | A named co-author or intellectual influence |
| `venue` | `venue--` | A journal, podcast, or publication platform |
| `claim` | `claim--` | A specific named argument or conjecture |
| `gap` | `gap--` | An honest gap: topic present in corpus but insufficiently sourced |

**Above the line** (content pages, synthesised from corpus):
`paper`, `lecture`, `interview`, `essay`, `post`, `theme`, `project`, `period`

**Below the line** (navigation / meta pages):
`collaborator`, `venue`, `claim`, `gap`

---

## Page Structure

Every wiki page uses this template:

```markdown
# [Page title]

**Type:** [page type]
**Slug:** [slug]
**Sources:** [comma-separated corpus slugs]
**Last updated:** [date]

---

## Summary
[2–3 sentence synthesis. Noun-first. Specific enough to stand alone.]

## Core content
[Substance: argument, findings, positions. Evidence cited as (corpus-slug §section).]

## Connections
[Links to related pages: themes, projects, collaborators, claims.]

## Honest Gaps
[What is missing, unclear, or unverifiable from available sources.]
```

---

## Commands

| Command | Action |
|---|---|
| `/wiki index all` | Read all unprocessed files in `raw/corpus/`, extract §0 fields, update `_axis_index.json` and `_corpus_log.json`. Batch 50 files at a time; write after each batch. |
| `/wiki index [slug]` | Index a single named corpus file. |
| `/wiki absorb [slug]` | Read the full content of a corpus file and produce a wiki page for it. Use page type from §0 `format` field. |
| `/wiki synthesise [axis]=[value]` | Generate a synthesis page for all corpus files sharing a given §0 field value. E.g. `/wiki synthesise theme=protein-folding`. |
| `/wiki link` | Scan all existing wiki pages; add missing `## Connections` cross-links. |
| `/wiki status` | Report: files indexed, files absorbed, pages created, gaps logged. |

---

## Domain Priors

These are the known structural features of this corpus. Apply them when
synthesising across sources:

1. **Two-phase career**: The corpus splits at 2010 (DeepMind founding). Pre-2010
   texts are neuroscience. Post-2010 are AI-systems. But the intellectual thread
   is continuous — the neuroscience period generates the ideas the AI period
   implements.

2. **The construction system hypothesis** originates in N1/2007 and recurs
   silently in every subsequent paper on memory replay, imagination-based
   planning, and generative world models.

3. **The neuroscience-AI bridge** is Hassabis's distinctive contribution as
   an intellectual, not merely as a builder. A9/2017 (Neuron review) is the
   canonical statement. Weight it heavily.

4. **AlphaFold2 (A24/2021) is the pivot point** of public recognition. Papers
   before it are specialist; papers after have a different kind of cultural
   weight. The Nobel Lecture (E3/2024) is the capstone public statement.

5. **Safety and governance statements are mostly interview-sourced**, not
   paper-sourced. Treat them as first-person positions with lower academic
   rigour than peer-reviewed work, but high primary-source value for tracking
   his public intellectual positions.

6. **The "learnable nature conjecture"** (Nobel Lecture 2024) is the most
   recent and least-examined claim. It has no corresponding peer-reviewed paper
   yet. Flag as `gap--learnable-nature-paper`.

7. **Co-authorship patterns matter**: papers with Maguire = neuroscience;
   with Silver/Kavukcuoglu/Mnih = RL systems; with Jumper/Evans = protein
   structure; with Botvinick/Kumaran = theory bridge. Co-author networks
   are proxy evidence for intellectual phase.

---

## Never Violate

- Never write to `raw/corpus/`. It is immutable.
- Never invent citations. If a claim cannot be traced to a source slug, mark
  it as an Honest Gap.
- Never collapse a position change into a single static claim. If Hassabis's
  view on AGI timelines shifts across sources, document both states with dates.
- Never use vague temporal language ("recently", "in recent years"). Use
  specific years or era labels from the controlled vocabulary.
- Never exceed one synthesis page per `/wiki synthesise` call. Finish and
  write before starting the next.
- `_log.md` is append-only. Never edit or delete existing entries.
- All axis values must come from the controlled vocabulary. Do not invent
  new taxonomy terms.
