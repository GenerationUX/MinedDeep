---
title: "Big-Loop Recurrence × Attention"
tags:
  - intersection
date: 2026-05-14
---

# Big-Loop Recurrence × Attention

**Type:** intersection
**Slug:** intersection--big-loop-recurrence-attention
**Parents:** paper--big-loop-recurrence-within-the-hippocampal-system-supports-integration-of-information-across-episodes, project--AlphaFold2
**Last updated:** 2026-05-14
**Epistemic status:** Grounded

---

## The intersection
Big-loop recurrence in the hippocampal system (CA3→neocortex→entorhinal cortex→CA3) integrates information across temporally distant episodes by passing representations through the cortex and back. AlphaFold's Evoformer uses iterative attention to integrate information across sequence positions by passing representations through attention layers and recycling them. Both solve the problem of **integrating distributed information into a coherent global representation through iterative refinement loops**.

The hippocampal loop integrates across *episodes* (separated by hours or days). AlphaFold's attention integrates across *positions* (separated by sequence distance). The computational question is the same: how do you build a global representation from local information when the relevant elements are far apart?

## What the corpus implies
The big-loop recurrence paper (2019, from the Kumaran lab) and AlphaFold (2021) share DeepMind authorship but no conceptual connection is drawn. The big-loop paper frames hippocampal recurrence as a mechanism for "integrating information across episodes" — a temporal integration problem. AlphaFold frames iterative attention as a mechanism for "integrating information across positions" — a spatial integration problem. Neither paper abstracts beyond its domain to ask whether these are instances of the same computational principle.

The neural scene representation paper (paper--neural-scene-representation-and-rendering, 2018) is a third instance: it uses iterative processing to integrate information across spatial locations into a coherent scene representation. Three papers, three domains (temporal, spatial, sequential), one computational skeleton.

## What's missing
- No paper abstracts "iterative information integration" as a general computational principle spanning neuroscience and AI.
- No paper asks whether attention is a computational generalisation of hippocampal recurrence, or whether they are fundamentally different mechanisms that happen to look similar at a high level.
- The key difference (episodic vs. positional integration) is never analysed: hippocampal loops operate across experiences separated by time, while attention operates across positions separated by sequence distance. Is this difference superficial or fundamental?

## Generative potential
**"Big-loop attention":** Design an attention system that integrates across *episodes* rather than positions. Standard attention attends over tokens within a sequence. Big-loop attention would attend over representations from *previous sequences*, recycling them through the network to build a cross-episode global representation. This would be directly inspired by CA3→cortex→ENT→CA3 loops and could be applied to problems requiring integration across long time scales (continual learning, multi-session reasoning).

**Unifying formalisation:** Both hippocampal recurrence and iterative attention can be described as fixed-point iteration: x_{t+1} = f(x_t), where f is a neural network (the cortex in the hippocampal case, the attention layer in AlphaFold's case). The system converges when x_{t+1} ≈ x_t. This suggests that the key question is not "what architecture?" but "what makes the fixed point useful?" — i.e., what inductive biases in f ensure that the fixed point is a good global representation rather than a trivial attractor?

**Testable prediction:** If big-loop recurrence and iterative attention are computationally equivalent, then disrupting the hippocampal loop (e.g., entorhinal cortex lesions) should produce deficits that mirror removing attention iterations from AlphaFold — specifically, loss of long-range dependencies while preserving local structure. This is testable in the spatial navigation paradigms used in the big-loop paper.

## Absorbed speculation

*Speculative: big-loop cycles may compress distributional representations into point estimates — each cycle applies a cortical prior that constrains possible outcomes, analogous to AlphaFold's recycling steps compressing local structure into global structure.*


---

**Falsification:** If big-loop recurrence does not show fixed-point convergence behaviour (representations continue changing indefinitely with more iterations), the fixed-point interpretation is false.
