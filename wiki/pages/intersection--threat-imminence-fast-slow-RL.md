# Threat Imminence × Fast/Slow RL

**Type:** intersection
**Slug:** intersection--threat-imminence-fast-slow-RL
**Parents:** paper--when-fear-is-near-threat-imminence-elicits-prefrontal, paper--reinforcement-learning-fast-and-slow
**Last updated:** 2026-05-14
**Epistemic status:** Grounded

---

## The intersection
The threat imminence paper (2007) shows a literal fast/slow neural shift: vmPFC (slow, cognitive threat evaluation) → PAG (fast, hardwired defensive action) as a virtual predator approaches. The fast/slow RL paper (2021) proposes that the brain's dual-system architecture maps onto two RL subsystems — a fast habit system and a slow planning system. The threat paper is a **domain-specific instantiation of the general fast/slow theory** that neither paper recognises.

Crucially, threat imminence provides a *parametric manipulation* of the fast/slow balance — by varying predator distance, you can map the full transition from slow to fast control. The fast/slow RL paper describes the systems statically; the threat paper shows them dynamically switching. Combined: threat imminence is the richest possible behavioural paradigm for testing dual-system RL models, because it produces graded transitions rather than binary switches.

## What the corpus implies
The threat paper (Mobbs et al., Science 2007, Hassabis as co-author) predates the fast/slow RL paper by 14 years. The fast/slow RL paper (2021) never references defensive systems or the vmPFC-PAG shift, despite it being the clearest empirical demonstration of the theory's core claim. The threat paper frames the shift in defensive-systems terms (from predatory imminence theory); the fast/slow RL paper frames it in RL terms (model-free vs. model-based). Neither translation is offered.

The threat paper's parametric design (continuous distance manipulation) is exactly what the fast/slow RL paper needs but doesn't have: a way to trace the *trajectory* of the fast/slow transition rather than just comparing the two systems in isolation.

## What's missing
- No paper analyses the vmPFC→PAG shift through the lens of model-free vs. model-based RL.
- No paper asks whether the vmPFC represents a model-based evaluation of threat (considering escape routes, probabilities) while the PAG implements a model-free defensive reflex (fixed action pattern).
- No paper uses the threat imminence paradigm to test the fast/slow RL framework — despite it being the most natural behavioural testbed.
- The fast/slow RL paper's clinical implications (addiction, anxiety) never reference the threat paper's finding that anxiety involves abnormal PAG-vmPFC balance — a direct neural validation.

## Generative potential
**Experimental programme:** Reanalyse the threat imminence data with computational RL models. Fit model-based (planning: considering escape routes, probabilities) and model-free (habit: fixed defensive responses) models to behaviour at each threat distance. Predict: model-based control should dominate at far distances, model-free at close distances, with a sharp transition — exactly matching the vmPFC→PAG neural shift.

**Clinical refinement:** The threat paper notes that anxiety patients show decreased vmPFC but increased PAG grey matter. The fast/slow RL paper frames anxiety as fast/slow imbalance. Combined: anxiety is not just "too much fast system" but specifically *premature fast-system takeover* — the vmPFC→PAG transition occurs at longer distances than in healthy controls. This predicts a measurable shift in the transition point, not just a change in the magnitude of either system.

**Connection to distributional RL:** At far threat distances, the vmPFC should maintain a distributional value code (many possible outcomes). At close distances, the PAG should collapse to a point estimate (single defensive action). The transition from distributional to scalar coding might *drive* the behavioural transition from flexible to rigid responding.

## Absorbed speculation

*Speculative: anxiety may involve failure of distributional narrowing rather than a simple fast/slow balance shift — the fast system maintains too-wide a distribution over threat outcomes. Additionally, phobias may involve premature conceptual consolidation of threat: too-rigid categorical fear formed from insufficient episodes, suggesting exposure therapy works by pushing past a second phase transition.*


---

**Falsification:** If the vmPFC→PAG transition is not parametrically graded by threat distance but is a binary switch, the fast/slow model fit is false.
