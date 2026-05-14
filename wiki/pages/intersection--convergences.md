---
title: "Convergences (Third-Order Intersections)"
tags:
  - intersection
date: 2026-05-14
---

# Convergences (Third-Order Intersections)

**Type:** intersection (third-order)
**Slug:** intersection--convergences
**Last updated:** 2026-05-14
**Epistemic status:** Conjectural

---

Four points where multiple first-order intersections converge into unified theories. These are the most speculative but also the most generative combinations in the wiki.

## 19. AlphaFold for Imagination (Construction + Self-Play + Learnable Nature)

**Converging lines:**
- Construction×Self-Play: imagination generates novel outputs by recombination without supervision
- Learnable×Construction: construction is structure prediction from compressed representations
- Self-Play Sufficiency: self-play produces superhuman outputs from pure self-competition

**Unified theory:** An AlphaFold for imagination — a system that discovers the "laws of experiential coherence" from data (learnable nature), uses them to construct novel scenes by self-play (construction × self-play), and does all this without explicit rules. Just as AlphaFold discovered protein folding laws from sequence data, an imagination system would discover scene coherence laws from experiential data.

**What makes this non-trivial:** AlphaFold works because protein structure is highly constrained by physics. Experiential scenes are constrained by... what? If the constraints are learnable (as the conjecture claims), then the architecture transfers. If not, it fails — which would *disprove* the learnable nature conjecture in the domain of experience. This is a high-value falsification target.

**Test:** Train a construction model on egocentric video. If it learns to construct plausible novel scenes *without being told the laws of physics or narrative coherence*, the conjecture holds in this domain. If it can't, the conjecture has a domain boundary.

**Falsification:** A construction model trained on egocentric video that produces plausible novel scenes without explicit physics/narrative rules falsifies the domain-boundary worry. Conversely, failure to do so after reasonable compute establishes a domain boundary for learnable nature.

---

## 20. The Developmental Stack (Replay + Meta-RL + Big-Loop)

**Converging lines:**
- Replay×Hippocampal: replay consolidates experiences by re-sampling
- Meta-RL×Self-Play: the brain discovers its learning algorithm
- Big-Loop×Attention: iterative integration produces coherent global representations

**Unified theory:** A computational model of cognitive development with three stacked mechanisms:
1. **Bottom layer — Big-loop integration:** Integrates information across episodes into coherent representations (perceptual/cognitive development)
2. **Middle layer — Replay consolidation:** Selectively consolidates important representations into permanent stores (memory development)
3. **Top layer — Meta-self-play:** Discovers the learning algorithms that govern both lower layers (executive development)

Each layer operates on a different timescale (hours, days, years) and the top layer optimises the lower layers. This maps onto the developmental trajectory: infants first integrate percepts (big-loop), then consolidate memories (replay), then develop flexible learning strategies (meta-RL) — with each layer bootstrapping the next.

**What makes this non-trivial:** Standard developmental theories describe these stages descriptively. This convergence provides a *computational mechanism* for why the stages occur in this order: you can't do meta-learning until you have stable representations to meta-learn over, and you can't have stable representations until you've integrated across episodes.

**Speculative extension:** Each developmental layer may show its own phase transition — perceptual integration suddenly produces coherent objects, memory consolidation suddenly reorganises knowledge, meta-learning suddenly improves strategy. Development may be a cascade of phase transitions rather than gradual change.

**Falsification:** If meta-learning emerges in an artificial system *before* stable representations are available to meta-learn over (i.e., the ordering constraint is violated), the sequential bootstrapping mechanism is false.

---

## 21. The Social Construction Engine (Construction×Self-Play + Social Hierarchy×Self-Play + Personality×Meta-RL)

**Converging lines:**
- Construction×Self-Play (2): generate novel scenarios by recombination
- Social Hierarchy×Self-Play (G): discover rank representations in competitive settings
- Personality×Meta-RL (L): meta-learn different strategies for different agent types

**Unified theory:** Theory of mind as a construction system. You literally "construct" what another person might think, using the same recombination machinery as spatial scene construction, but parameterised by personality models and conditioned by perceived social rank. The construction system doesn't need a separate "social module" — social cognition is scene construction where the "elements" are people instead of objects, and the "plausibility constraints" include personality consistency and social rank.

**What makes this non-trivial:** This predicts hippocampal damage should produce parallel deficits in spatial construction and social construction — not just amnesia and imagination deficits, but also theory-of-mind deficits. This is actually observed in some hippocampal lesion patients but is rarely interpreted through the construction lens. The prediction is specific: the *pattern* of social cognition deficits should mirror the pattern of spatial construction deficits (e.g., difficulty with novel social scenarios but preserved knowledge of familiar social routines = difficulty with novel imagined scenes but preserved knowledge of familiar places).

**Falsification:** If hippocampal lesion patients show theory-of-mind deficits that do *not* parallel their spatial construction deficits (e.g., impaired novel social reasoning but preserved novel spatial imagination), the shared-mechanism claim is false.

---

## 22. The Self-Diagnostic Discovery Machine (Learnable Nature + Density Functionals + Math Guidance)

**Converging lines:**
- Learnable Nature conjecture: natural laws are discoverable from data
- Density Functionals×Learnable Nature (H): AI discovers correctness properties human theories violated
- Mathematics×Construction (10): AI generates conjectures for human verification

**Unified theory:** A scientific discovery system that doesn't just learn to predict but *identifies when its learned model satisfies correctness properties that existing theories violate*. The density functional paper is the proof of concept: the learned functional was piecewise-linear (correct) while all human functionals were curved (incorrect) — and the system could be *checked* for this property. The next step: a discovery system that automatically searches for correctness properties in its learned models, identifies discrepancies with existing theories, and generates conjectures about what the correct property should be.

**What makes this non-trivial:** Current AI for science learns to predict. This system would learn to predict *and* to self-diagnose — to identify structural properties of its own learned representations that correspond to physical/mathematical truths. This turns the learnable nature conjecture from "AI can learn laws" into "AI can know that it has learned laws, and know which laws human theories got wrong." The density functional paper demonstrates the first case; extending it requires a meta-learning layer that searches for properties across domains rather than being told which property to check.

**Falsification:** If the density functional result is unique — no other domain shows AI discovering a correctness property that human theories systematically violate — then the self-diagnostic pattern is coincidental rather than generalisable.