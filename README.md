# MinedDeep

A structured, interlinked knowledge base built on the Karpathy LLM Wiki
pattern, dedicated to the complete published intellectual output of
**Sir Demis Hassabis** (b. 1976) — co-founder and CEO of Google DeepMind,
2024 Nobel Laureate in Chemistry.

---

## What This Is

This wiki is a synthesis layer over a curated corpus of Hassabis's peer-reviewed
papers, authored essays, formal lectures, long-form interviews, and significant
public statements. It is maintained by Claude Code using the Karpathy/Farzaa
wiki-generation pattern and the domain schema defined in `CLAUDE.md`.

The goal is not a biography. It is a navigable intellectual map: what Hassabis
argued, when he argued it, how his positions developed, and where the record
is incomplete.

---

## Corpus Coverage

The corpus spans three phases:

| Phase | Years | Character |
|---|---|---|
| PhD / postdoc | 2007–2010 | Cognitive neuroscience. Hippocampus, memory, imagination. UCL under Eleanor Maguire. |
| Early DeepMind | 2010–2018 | Deep reinforcement learning. AlphaGo. The neuroscience–AI bridge. |
| AlphaFold era and beyond | 2018–present | Protein structure. AI for science. Safety/governance. Nobel Prize. AGI theory. |

**~47 source documents** in the initial corpus, including:
- 30 peer-reviewed papers (Nature, Science, Neuron, PNAS)
- 3 authored essays / reviews
- 9 long-form interviews (with transcript access)
- 4 blog / social posts
- 1 doctoral thesis (UCL, 2009)

---

## Architecture

```
raw/corpus/       Immutable. The source files. Claude reads; never writes here.
wiki/             LLM-maintained. Claude writes; human reads.
  _index.md       Page catalog by type.
  _log.md         Append-only operation log.
  _axis_index.json  Taxonomy axis lookup table.
  _corpus_log.json  Per-file read and absorption tracking.
  pages/          All wiki articles — flat, slug-named.
assets/           Diagrams, timelines, exported reference figures.
```

---

## How to Use

### Reading the wiki

Browse `wiki/pages/` or use `wiki/_index.md` as the entry point.

Page types:
- **paper--** · **lecture--** · **interview--** · **essay--** · **post--** — individual source pages
- **theme--** · **project--** · **period--** — synthesis pages
- **collaborator--** · **venue--** · **claim--** — navigation pages
- **gap--** — documented gaps in corpus coverage

### Extending the corpus

1. Create a new file in `raw/corpus/` named `[slug]--Hassabis.md`
2. Include a `## §0` block with all 8 required taxonomy fields
3. Include full text or best available excerpt of the source
4. Run `/wiki index [slug]` in a Claude Code session
5. Run `/wiki absorb [slug]` to generate the wiki page

### Running Claude Code

Open Claude Code at the root of this directory. It reads `CLAUDE.md`
automatically. Then run:

```
/wiki index all        — index all unprocessed corpus files
/wiki absorb [slug]    — generate a wiki page for one file
/wiki synthesise [axis]=[value]   — generate a synthesis page
/wiki status           — report current coverage
```

---

## Source File Format

Every file in `raw/corpus/` should follow this template:

```markdown
---
# [slug]--Hassabis.md
---

## §0 Taxonomy & Identity

format: [controlled value]
domain: [controlled value]
era: [controlled value]
venue: [controlled value]
theme: [controlled value(s)]
project: [controlled value or none]
co-authors: [names]
impact: [controlled value(s)]

<!-- optional fields -->
claim: [if applicable]
influences: [if applicable]
contradicts: [if applicable]
open-questions: [if applicable]
notable-quote: [≤25 words, verbatim]

---

## §1 Full Text / Excerpt

[Full text, abstract, or best available excerpt of the source.]
```

---

## Key Texts (Acquisition Priority)

For the initial corpus, prioritise these five:

1. **N1/2007** — Hassabis et al., PNAS: *Patients with hippocampal amnesia cannot imagine new experiences.* Intellectual origin.
2. **A9/2017** — Hassabis et al., Neuron: *Neuroscience-Inspired Artificial Intelligence.* Fullest theoretical statement.
3. **A1/2015** — Mnih et al., Nature: *Human-Level Control through Deep Reinforcement Learning.* DQN. Field-defining.
4. **A24/2021** — Jumper et al., Nature: *Highly accurate protein structure prediction with AlphaFold.* Most cited.
5. **E3/2024** — Nobel Lecture: *Accelerating Scientific Discovery with AI.* Most recent primary statement.

---

## Known Gaps

**`gap--learnable-nature-paper`** — The conjecture stated in the 2024 Nobel
Lecture ("any pattern found in nature can be efficiently discovered by a
classical learning algorithm") has no peer-reviewed paper as of May 2026.
This is the most significant current gap in the corpus.

---

*Wiki scaffold version: 1.0*  
*Upstream patterns: Karpathy LLM Wiki, Farzaa wiki-gen skill*  
*Domain: Hassabis intellectual corpus*  
*Scaffold date: 2026-05-13*
