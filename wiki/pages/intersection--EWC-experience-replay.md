# EWC × Experience Replay

**Type:** intersection
**Slug:** intersection--EWC-experience-replay
**Parents:** paper--overcoming-catastrophic-forgetting-in-neural-networks, project--DQN
**Last updated:** 2026-05-14
**Epistemic status:** Grounded

---

## The intersection
EWC (2017) prevents catastrophic forgetting by constraining important weights via Fisher information — inspired by synaptic consolidation in the brain. DQN's experience replay (2015) prevents catastrophic forgetting by re-sampling past transitions — inspired by hippocampal replay. Both solve the same problem from the same lab in the same year, using different biological inspirations, and neither paper acknowledges the other.

This is a **second glaring silence** parallel to the replay×hippocampal intersection. The replay intersection identifies the silence between DQN's replay buffer and hippocampal SWR replay. This intersection identifies the silence between EWC's weight consolidation and synaptic consolidation — and between two DeepMind papers that literally share authors (Kirkpatrick, Rabinowitz, Rusu, Hadsell are on both EWC and DQN-adjacent work).

## What the corpus implies
EWC's biological inspiration is explicit: "When mice learn new skills, only a subset of dendritic spines are modified; previously strengthened spines are protected" (EWC §Introduction). DQN's biological inspiration is implicit but obvious to anyone with Hassabis's background. Both papers appeared in 2015–2017 from overlapping author teams. Yet no source connects them.

The critical question: **do EWC and replay solve complementary or redundant aspects of the forgetting problem?** Replay solves the *data distribution* problem (new data displaces old in the training distribution). EWC solves the *parameter interference* problem (gradient updates for new tasks overwrite old task's solution). The brain uses both hippocampal replay and synaptic consolidation — suggesting they are complementary. But the corpus never analyses this.

## What's missing
- No paper in the corpus compares EWC and replay as solutions to catastrophic forgetting, despite shared authorship and shared biological inspiration.
- No paper asks whether combining EWC + replay outperforms either alone (this was shown by later work outside the corpus — Nguyen et al., 2018; but the original papers never motivate this combination).
- No paper maps EWC's Fisher information matrix onto any known neural quantity, despite claiming biological inspiration.
- The 2017 Neuron neuroscience-AI review discusses both continual learning and replay but never connects EWC to synaptic consolidation or replay.

## Generative potential
**The biological question:** The brain clearly uses both replay (SWR) and consolidation (spine protection). Are these redundant safety mechanisms, or do they solve genuinely different problems? Replay operates over *representations* (reactivating patterns); consolidation operates over *parameters* (protecting synapses). If representations change faster than parameters (which they do — neural activity is milliseconds, synaptic change is minutes), then replay solves short-timescale stability while consolidation solves long-timescale stability. This predicts a two-timescale forgetting prevention architecture: fast replay buffer for within-session stability, slow weight consolidation for cross-session stability.

**Design principle:** Current continual learning systems typically use replay OR regularisation, not both. The brain uses both. This suggests the optimal continual learning architecture combines them — and the reason neither alone fully solves continual learning is that each addresses only half the problem.

**Connection to CLS:** Complementary learning systems theory describes fast hippocampal learning + slow neocortical learning. EWC + replay provides a computational implementation: replay is the hippocampal component (fast re-sampling), EWC is the neocortical component (slow weight protection). The CLS paper in the corpus never makes this connection to the two DeepMind continual learning mechanisms.

## Absorbed speculation

*Speculative: EWC protection could prevent strategic forgetting in self-play — protecting discovered strategies with weight constraints while generating new ones, enabling continual improvement without catastrophic loss of old strategies.*


---

**Falsification:** If EWC and experience replay are discussed together in a DeepMind paper citing both Kirkpatrick et al. 2017 and Mnih et al. 2015, the "glaring silence" claim is false.
