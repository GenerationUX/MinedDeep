---
title: "Construction×Self-Play + Replay×Hippocampal-Replay"
tags:
  - intersection
date: 2026-05-14
---

# Construction×Self-Play + Replay×Hippocampal-Replay

**Type:** intersection (second-order)
**Slug:** intersection--construction-self-play-replay-consolidation
**Parents:** intersection--hippocampal-construction-self-play, intersection--experience-replay-hippocampal-replay
**Last updated:** 2026-05-14
**Epistemic status:** Extrapolative

---

## The combination
If hippocampal construction is analogous to self-play (generating novel outputs by recombination), and experience replay is analogous to hippocampal SWR replay (consolidating by re-sampling), then the brain's full imagination cycle is: **construct during wake (self-play) → replay during sleep (consolidation) → improved construction next day**. No AI system implements both phases of this cycle.

## What emerges
The two first-order intersections each identify a parallel in isolation. Combined, they reveal a *two-phase architecture* that neither alone implies:
- **Phase 1 (wake):** The hippocampus runs internal self-play — generating candidate scene constructions, evaluating them against internal models, discarding bad ones.
- **Phase 2 (sleep):** The successful constructions are replayed to the neocortex, where they gradually become permanent semantic representations.

This maps directly onto the complementary learning systems theory (CLS): fast hippocampal learning + slow neocortical consolidation. But CLS frames this as "memory transfer," not "self-play with consolidation." The self-play framing adds something CLS lacks: *the hippocampus doesn't just store experiences — it generates novel ones and selects the best.*

## Gap
No AI system combines generative self-play with selective replay-based consolidation. Current self-play systems (AlphaGo, AlphaZero) train continuously without a sleep phase. Current replay systems (DQN) replay past experiences without generating novel ones. The brain does both.

## Generative potential
**Architecture:** A self-play system that generates candidate solutions during "wake" phases, evaluates them, stores the best in a replay buffer, and then trains the main network from the replay buffer during "sleep" phases. This decouples generation from learning — the generator can be more exploratory because bad candidates are filtered during consolidation.

**Neuroscience prediction:** Hippocampal activity during REM sleep (when construction-like imagery is most vivid) should preferentially replay *novel constructions* rather than veridical experiences. This would distinguish the self-play-with-consolidation model from standard CLS (which predicts replay of actual experiences).

---

**Falsification:** If a single system can both construct novel scenarios and consolidate them without separate wake/sleep phases, the phase-separation requirement is false.
