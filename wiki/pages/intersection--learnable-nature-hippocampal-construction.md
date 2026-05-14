# Learnable Nature × Hippocampal Construction

**Type:** intersection
**Slug:** intersection--learnable-nature-hippocampal-construction
**Parents:** claim--learnable-nature-conjecture, claim--hippocampus-as-construction-system
**Last updated:** 2026-05-14
**Epistemic status:** Extrapolative

---

## The intersection
The learnable nature conjecture holds that many natural laws can be discovered by machine learning systems from data alone — AlphaFold learned the laws of protein folding without being told them. The hippocampal construction hypothesis holds that the brain builds novel experiences by recombining stored elements without being told how to combine them. Both claim that a structured, rule-governed output can emerge from a system that possesses only elements and a learning objective — no explicit rules required.

AlphaFold maps from sequence (compressed representation) to 3D structure (rich, constrained output). The hippocampus maps from episodic elements (people, places, objects) to constructed scenes (rich, constrained output). Both are structure-prediction problems where the "structure" is implicit in the training data rather than specified by hand.

## What the corpus implies
These two ideas come from opposite ends of Hassabis's career — 2007 neuroscience and 2024 Nobel Lecture — and are never connected. The Nobel Lecture doesn't reference the hippocampal construction work at all. The construction papers don't speculate about the learnability of natural laws. Yet both are expressions of the same underlying conviction: **complex structured outputs can be learned from data without explicit rules, provided the system has the right inductive biases.**

The bridging concept is "inductive bias." The hippocampus's inductive bias is recombination of stored elements. AlphaFold's inductive bias is the Evoformer's attention structure. Both are domain-specific biases that enable the system to discover domain-general structure.

## What's missing
- No paper frames hippocampal construction as "the brain's structure prediction problem."
- No paper asks whether the construction system's recombination bias is a special case of the more general principle that AlphaFold exemplifies.
- The learnable nature conjecture lacks a peer-reviewed paper — the construction hypothesis has 12 papers but no formalisation as a computational algorithm. Their intersection would naturally motivate such a formalisation.

## Generative potential
**Unifying framework:** If both systems are instances of "constrained structure prediction from compressed representations," then we can ask: what are the minimal inductive biases needed for structure prediction in a given domain? For proteins, it's attention over residue pairs. For experience, it might be attention over element pairs (person–place, object–action). This would suggest a general architecture: **pairwise attention over stored elements, iterated to convergence, producing a structured output.**

**Philosophical implication:** The learnable nature conjecture threatens to make the hippocampus redundant — if AI can learn structure from data, why does the brain need a specialised construction system? The intersection reverses this: the hippocampus *is* evidence for the learnable nature conjecture. If biology evolved a structure-prediction system millions of years before AlphaFold, this suggests that learnable structure prediction is a general solution that evolution discovered independently.

**Research direction:** Train a construction model on egocentric video data using an AlphaFold-like architecture (pairwise attention over detected elements, iterated refinement) and test whether it can construct plausible novel scenes. If it works, it would be strong evidence that construction and protein folding share a computational skeleton.

---

**Falsification:** If construction is demonstrably not learnable from data (e.g., requires innate scene grammar), the connection to learnable nature is false.
