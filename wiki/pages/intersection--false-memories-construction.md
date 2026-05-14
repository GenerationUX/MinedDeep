# Semantic False Memories × Construction

**Type:** intersection
**Slug:** intersection--false-memories-construction
**Parents:** paper--semantic-representations-in-the-temporal-pole-predict-false-memories, paper--deconstructing-episodic-memory-with-construction
**Last updated:** 2026-05-14
**Epistemic status:** Grounded

---

## The intersection
The false memory paper (2016) shows a similarity-based code in the temporal pole predicts both true and false memory — the same neural representation that helps you remember "apple" also makes you falsely remember "pear." The construction paper (2007) argues the hippocampus builds scenes by recombining stored elements. Combined: **false memories are over-construction — the system constructs scenes that are too semantically coherent, collapsing distinctions that should be maintained.**

Construction is adaptive when it produces plausible scenes from partial information. It becomes maladaptive when semantic priors (from the temporal pole) overwhelm episodic specificity (from the hippocampus). The false memory paper provides the neural mechanism for this balance failure: the temporal pole's similarity code is the learned prior that construction draws upon, and when it's too strong relative to hippocampal input, constructed scenes are plausible but wrong.

## What the corpus implies
Both papers come from the Hassabis neuroscience group (Chadwick, Kumaran, Schacter, Hassabis for false memories; Hassabis, Maguire for construction). They were published nine years apart but share co-authors (Kumaran, Schacter). The false memory paper doesn't reference the construction framework; the construction paper doesn't discuss false memories. Yet they describe the same system from complementary angles — construction describes the generative process, false memories describe a specific failure mode of that process.

The false memory paper's key finding — the *same* code predicts both true and false memory — has a deep implication for construction: **you cannot have good construction without some false memories.** The error isn't a bug; it's the cost of the compression that makes construction efficient.

## What's missing
- No paper frames false memories as a failure mode of the construction system rather than a separate memory phenomenon.
- No paper asks whether amnesia patients (who can't construct) are immune to semantic false memories — a clean prediction of the over-construction account.
- No paper models the temporal pole's similarity code as the *prior* in a Bayesian construction system, with hippocampal input as the *likelihood* — though this is the natural formalisation.
- The construction paper's emphasis on "novel combinations" never considers that some combinations are *too* novel (impossible scenes) while others aren't novel enough (false memories — conflating similar elements).

## Generative potential
**Formal model — Bayesian construction:** Scene construction = sampling from a generative model where the temporal pole provides the prior (semantic similarity structure) and hippocampal input provides the likelihood (episodic specifics). False memories occur when the prior dominates (high semantic similarity, low episodic distinctiveness). Impossible scenes occur when the likelihood dominates (low semantic constraint, high episodic noise). This predicts a U-shaped curve: memory accuracy is highest at intermediate semantic similarity and drops at both extremes.

**Clinical prediction:** Patients with temporal pole damage should have *reduced* false memories (less semantic prior = less over-construction) but also *reduced* true memory for semantically related items (less prior = less useful constraint). This is testable and would distinguish the construction account from standard accounts that treat false memories as independent of true memory.

**Connection to learnable nature:** If the temporal pole's similarity code is *learned* rather than innate, then false memory rates should change with experience — exposure to a domain should reshape the similarity code and thus change which lures are most likely to produce false memories. This predicts individual and cultural variation in false memory patterns that reflects learned semantic structure.

---

**Falsification:** If false memories occur in conditions where construction is intact but semantic association is impaired (dissociating false memories from construction), the over-construction account is false.
