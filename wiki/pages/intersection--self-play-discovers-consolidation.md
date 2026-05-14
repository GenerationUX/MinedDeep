# Self-Play Discovers Its Own Consolidation

**Type:** intersection (feedback loop)
**Slug:** intersection--self-play-discovers-consolidation
**Parents:** intersection--consolidated-self-play, intersection--meta-self-play-discovers-fast-slow
**Last updated:** 2026-05-14
**Epistemic status:** Conjectural

---

## The feedback loop
Consolidated Self-Play (O) adds EWC-like weight protection to self-play to solve strategic forgetting — protecting old strategies while generating new ones. Meta-Self-Play Discovers Fast/Slow (2) shows that a meta-learner in self-play spontaneously discovers the fast/slow dual-system split. Combined: **a meta-self-play system should discover the need for consolidation *without any biological priors*.** The meta-learner should learn to protect old strategies when it discovers that forgetting them hurts performance — effectively discovering complementary learning systems through pure competition.

## Why this is the highest-stakes prediction in the wiki
If a self-play system with sufficient meta-learning capability spontaneously develops (a) a fast temporary store for new strategies, (b) an iterative transfer mechanism to integrate strategies, and (c) a protection mechanism to prevent forgetting of transferred strategies — this would be the strongest possible evidence for the learnable nature conjecture in cognitive architecture. It wouldn't just learn laws of nature from data; it would *discover that it needs a hippocampus*.

Conversely, if meta-self-play never discovers consolidation — if it always finds it more efficient to simply retrain from scratch or use a fixed-capacity memory — this would suggest that complementary learning systems are a *biological peculiarity*, not a universal computational necessity. Either way, the result is decisive.

## Specific experimental design
Train a population-based self-play system (like AlphaZero) with a meta-learning layer that can modify the base learning algorithm. The meta-learner has access to primitives including: learning rate modulation, weight regularisation strength, replay buffer size, and number of gradient updates per batch. No primitive is labelled "consolidation" or "hippocampus." After sufficient training, inspect whether the meta-learner has:
1. Developed a two-phase learning process (fast acquisition + slow integration)
2. Introduced weight protection for older strategies
3. Created an implicit replay mechanism for previously successful strategies

If all three emerge, self-play has discovered CLS. If none emerge, CLS may be biologically specific rather than computationally universal.

## What makes this non-trivial
Existing meta-RL work shows discovery of learning algorithms in simple tasks. Self-play work shows emergent capabilities in complex games. But nobody has combined them to ask whether *memory architecture itself* is discoverable through competition. The standard assumption is that memory architecture is engineered (DNC, replay buffers, EWC) — this asks whether it can be *discovered*.

## Connection back to learnable nature
The Learnable Nature conjecture says natural laws are discoverable from data. This intersection extends it: *computational architectures are discoverable from task demands*. If self-play discovers CLS, then the brain's memory system isn't just "like" an AI memory system — it's the *optimal* memory system for the task of learning from non-stationary experience, discoverable from first principles.

---

**Falsification:** If a meta-self-play system with access to learning-rate, regularisation, and replay-buffer primitives never develops two-phase learning after 10M self-play games, the conjecture is false.
