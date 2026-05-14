# Meta-RL×Self-Play + Fast/Slow×AlphaGo Zero

**Type:** intersection (second-order)
**Slug:** intersection--meta-self-play-discovers-fast-slow
**Parents:** intersection--meta-RL-self-play, intersection--fast-slow-RL-alphago-zero-dynamics
**Last updated:** 2026-05-14
**Epistemic status:** Extrapolative

---

## The combination
If meta-RL discovers learning algorithms through self-play (first intersection), and the fast/slow split emerges naturally from self-play systems (second intersection), then: **meta-self-play should spontaneously discover a fast/slow architecture.** This would explain *why* the brain has fast/slow systems — not by design but as the optimal solution that meta-self-play converges to.

## What emerges
A concrete, testable prediction that neither parent intersection makes alone:
1. Run meta-self-play (a system that discovers learning algorithms via self-competition).
2. Check whether the discovered learning algorithm has a fast/slow structure.
3. If yes: the brain's dual-system architecture is not a biological constraint but a computational optimum.

This connects developmental neuroscience (how do fast/slow systems arise?) with AI systems design (should we build fast/slow in, or let it emerge?).

## Gap
Nobody has run meta-RL in a self-play setting, so we don't know whether the fast/slow split is a discovered solution. The 2021 fast/slow paper assumes it should be built in. The AlphaGo Zero paper shows it emerges but doesn't analyse it. The meta-RL paper discovers algorithms but doesn't test in self-play domains.

## Generative potential
**Critical experiment:** Implement meta-self-play on a simple game domain. If the discovered learning algorithm reliably has two components (one fast/local, one slow/global), this is strong evidence that the brain's architecture is a discovered optimum rather than a biological accident.

**Clinical implication:** Psychiatric disorders characterised by fast/slow imbalance (addiction = fast system dominance; anxiety = slow system overactivation) could be reframed as meta-learning failures — the meta-learner discovered a bad fast/slow split.

---

**Falsification:** If meta-self-play never discovers a fast/slow split in 10M+ games across multiple architectures, the discovery claim is false.
