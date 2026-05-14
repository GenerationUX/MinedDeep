# Fast/Slow RL × AlphaGo Zero's Training Dynamics

**Type:** intersection
**Slug:** intersection--fast-slow-RL-alphago-zero-dynamics
**Parents:** paper--reinforcement-learning-fast-and-slow, project--AlphaGo
**Last updated:** 2026-05-14
**Epistemic status:** Grounded

---

## The intersection
"Reinforcement learning, fast and slow" (2021) argues that the brain's dual-system architecture — a fast habit system (dorsolateral striatum) and a slow planning system (prefrontal/hippocampal) — maps onto two RL subsystems. AlphaGo Zero's training naturally exhibits a fast/slow split: the policy network adapts rapidly within self-play games (making move-by-move decisions), while the value network updates slowly across games (evaluating whole-board positions). The system *discovers* the fast/slow distinction rather than having it designed in.

## What the corpus implies
The fast/slow RL paper (2021) was published four years after AlphaGo Zero (2017) and three years after AlphaZero (2018). It cites neither. It frames the fast/slow split as an architectural requirement derived from neuroscience — something you should *build into* an AI system. But AlphaGo Zero already had this split emerge *without* being designed for it. This suggests the paper's framing is backwards: the fast/slow split may not be an architectural constraint but an emergent property of any system that must both act (fast) and evaluate (slow).

The AlphaGo Zero paper describes the policy-value network as a single shared trunk with two heads. The policy head updates more frequently (every move) than the value head (every game outcome). Over training, the two heads specialise — the policy head becomes a fast, local decision-maker while the value head becomes a slow, global evaluator. This is precisely the habit/planning split, but it was never described in those terms.

## What's missing
- No paper analyses AlphaGo Zero's training dynamics through the lens of dual-system theory.
- No paper asks whether the emergent fast/slow split in game-playing systems is computationally equivalent to the brain's fast/slow split.
- The fast/slow RL paper proposes specific architectural modifications (separate networks, different learning rates) but never checks whether AlphaGo Zero already implements something equivalent.

## Generative potential
**Empirical test:** Analyse AlphaGo Zero's policy and value heads during training. If the policy head shows characteristics of model-free control (local, fast, habit-like) and the value head shows characteristics of model-based control (global, slow, planning-like), this would suggest the fast/slow split is emergent rather than designed.

**Design principle:** If the fast/slow split is emergent, then explicitly building it in (as the 2021 paper suggests) might actually be counterproductive — it might constrain the system to discover a worse split than it would find naturally. The design implication is: give the system a single network with two output heads and let it discover its own fast/slow division of labour.

**Neuroscience prediction:** If the fast/slow split is emergent, then it should appear in domains where the brain hasn't evolutionarily specialised it. For example, social cognition might show a fast/slow split (rapid social judgments vs. slow social reasoning) that emerges from a single neural system rather than being implemented in separate circuits.

## Absorbed speculation

*Speculative: the emergent fast system may encode distributional value (rich uncertainty) while the slow system encodes point value (precise estimates), predicting different uncertainty signatures in habitual vs. deliberate choices.*


---

**Falsification:** If AlphaGo Zero's value and policy networks show no qualitative difference in temporal abstraction (e.g., both produce only immediate move evaluations), the emergent fast/slow claim is false.
