---
title: "Hippocampal Construction × Self-Play"
tags:
  - intersection
date: 2026-05-14
---

# Hippocampal Construction × Self-Play

**Type:** intersection
**Slug:** intersection--hippocampal-construction-self-play
**Parents:** claim--hippocampus-as-construction-system, claim--self-play-sufficiency
**Last updated:** 2026-05-14
**Epistemic status:** Extrapolative

---

## The intersection
The hippocampus constructs novel episodic scenes by recombining stored elements (people, places, objects) from distributed cortical stores. Self-play generates novel game strategies by recombining board states through iterative play against itself. Both systems produce outputs that transcend their training distribution — generating things that have never been experienced before. Neither system relies on external supervision for the quality of its outputs: the hippocampus evaluates constructed scenes against internal constraints (plausibility, coherence), and self-play evaluates strategies against the opponent (which is itself).

## What the corpus implies
The two ideas are never connected in any of the 45 sources. The hippocampal construction hypothesis (2007) is framed purely as a neuroscience claim about memory and imagination. Self-play sufficiency (2017) is framed purely as an AI training paradigm. Yet Hassabis was the lead author on both — the intellectual continuity is personal, not textual.

The closest the corpus comes is the 2017 Neuron review (paper--neuroscience-inspired-artificial-intelligence), which argues for bidirectional inspiration between neuroscience and AI but does not make this specific connection.

## What's missing
- No paper asks whether the hippocampus might implement something analogous to self-play during imagination — generating candidate scenes, evaluating them against an internal model, and refining.
- No paper asks whether self-play systems develop internal representations that resemble hippocampal scene construction.
- The "construction without supervision" aspect is discussed in the imagination papers but never formalised as a learning algorithm that could be compared to self-play.

## Generative potential
**Testable prediction:** If hippocampal construction is computationally analogous to self-play, then hippocampal activity during imagination should show signatures of iterative refinement — early "draft" constructions followed by evaluation-driven revision. This could be tested with high-temporal-resolution fMRI during imagination tasks.

**AI direction:** A self-play system equipped with a construction module (recombining stored elements rather than sampling from a policy) might exhibit more sample-efficient learning, because construction constrains the search space to plausible recombinations rather than arbitrary states.

**Unifying theory:** Both systems may be instances of a general principle: **generative systems that improve by critiquing their own outputs eventually exceed the quality of their training data.** This would connect construction, self-play, and the learnable nature conjecture into a single framework.

---

**Falsification:** If construction requires hippocampal replay but self-play does not (or vice versa), the shared recombination mechanism claim is false.
