# Frontmatter Schema

Generated: 2026-05-14T11:01:31.152Z

## Mapping Rules

### Title
Source: `# Title` from line 1 of each markdown file.
No derivation from filename — the human-readable title is already present.

### Tags
Tags are lowercase-hyphenated. The tag set depends on page type:

**Primary corpus pages** (paper, essay, interview, lecture):
- First tag: format slugified (e.g. `peer-reviewed-paper`, `essay`, `op-ed`, `interview`, `lecture`, `review-article`)
- Then: all theme values slugified
- Then: domain slugified
- Then: era slugified
- Then: project (if not `(none)`)

**Derived pages** (claim, collaborator, gap, period, project, theme):
- Single tag: page type (e.g. `claim`, `collaborator`, `period`, `theme`, `project`, `gap`)
- Intersection subtypes flattened: `intersection` (all subtypes get the same tag)

**Synthetic pages** (intersection, venue):
- Single tag: page type (`intersection` or `venue`)

### Description
Source: First sentence of `## Summary` section, truncated to ≤160 characters.
Omitted if no Summary section exists.

### Date
Source for corpus pages: `year` from extraction data, formatted as `YYYY-01-01`.
Source for non-corpus pages: `**Last updated:**` from bold-metadata header.
Omitted if neither available.

### Fields dropped from frontmatter
These stay in the page body only — not useful for Quartz navigation/filtering:
co_authors, impact, venue, influences, contradicts, open-questions, claim, notable-quote

## Distinct Values

### Formats (6)
- essay (from "essay")
- interview (from "interview")
- lecture (from "lecture")
- op-ed (from "op-ed")
- peer-reviewed-paper (from "peer-reviewed-paper")
- review-article (from "review-article")

### Themes (20)
- agi-definition (from "AGI-definition")
- ai-for-science (from "AI-for-science")
- chess (from "chess")
- clinical-ai (from "clinical-AI")
- complementary-learning-systems (from "complementary-learning-systems")
- deep-rl (from "deep-RL")
- episodic-memory (from "episodic-memory")
- game-playing-ai (from "game-playing-AI")
- go (from "go")
- hippocampal-construction (from "hippocampal-construction")
- learnable-nature-conjecture (from "learnable-nature-conjecture")
- memory-imagination (from "memory-imagination")
- model-based-rl (from "model-based-RL")
- neuroscience-ai-bridge (from "neuroscience-AI-bridge")
- protein-folding (from "protein-folding")
- reinforcement-learning (from "reinforcement-learning")
- safety-governance (from "safety-governance")
- self-play (from "self-play")
- starcraft (from "starcraft")
- structural-biology (from "structural-biology")

### Eras (6)
- alphafold-era (from "alphafold-era")
- deepmind-ascent (from "deepmind-ascent")
- early-deepmind (from "early-deepmind")
- phd-period (from "phd-period")
- post-alphafold (from "post-alphafold")
- postdoc-period (from "postdoc-period")

### Domains (11)
- agi-theory (from "AGI-theory")
- ai-for-science (from "AI-for-science")
- clinical-ai (from "clinical-AI")
- cognitive-neuroscience (from "cognitive-neuroscience")
- game-playing-ai (from "game-playing-AI")
- mathematics-ai (from "mathematics-AI")
- multi-agent-systems (from "multi-agent-systems")
- neuroscience-ai-bridge (from "neuroscience-AI-bridge")
- protein-structure (from "protein-structure")
- reinforcement-learning (from "reinforcement-learning")
- safety-governance (from "safety-governance")

### Projects (13)
- AlphaFold
- AlphaFold-Multimer
- AlphaFold2
- AlphaGo
- AlphaGo-Zero
- AlphaStar
- AlphaZero
- DNC
- DQN
- DeepMind-general
- GQN
- MuZero
- hippocampus-research
