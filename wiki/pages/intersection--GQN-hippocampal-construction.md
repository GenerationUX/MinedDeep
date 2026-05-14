# GQN × Hippocampal Construction

**Type:** intersection
**Slug:** intersection--GQN-hippocampal-construction
**Parents:** paper--neural-scene-representation-and-rendering, paper--the-construction-system-of-the-brain
**Last updated:** 2026-05-14
**Epistemic status:** Grounded

---

## The intersection
GQN (Generative Query Network, 2018) builds scene representations from partial 2D observations via iterative attention and renders novel viewpoints from those representations. The hippocampal construction system (2007) builds scene representations from stored elements (people, places, objects) and generates novel imagined scenes. Both systems take partial inputs and produce rich scene representations that support *novel outputs* — GQN renders from viewpoints never seen during training; construction generates scenes never experienced. Neither receives explicit rules about scene structure.

The deeper parallel is **viewpoint generalisation**. GQN's signature capability is that a single scene representation can be queried from arbitrary camera poses. The construction papers never ask whether hippocampal scene representations support analogous "mental viewpoint shifts" — yet first-person vs. third-person autobiographical memories are a well-documented phenomenon that has no computational account.

## What the corpus implies
Both papers share DeepMind authorship (Eslami, Rezende, Botvinick, Hassabis for GQN; Hassabis, Maguire for construction). Botvinick is a co-author on GQN and on the 2017 Neuron neuroscience-AI review, yet no source connects GQN's scene representation to hippocampal construction. The construction papers describe scene construction purely in verbal/cognitive terms; GQN provides the first computational formalisation of scene representation from partial views — but this formalisation was never applied to the neuroscience question.

GQN's representation network uses iterative attention over context views to build a scene vector. The big-loop recurrence paper (2019, from the same Kumaran lab as construction work) shows hippocampal circuits iteratively integrate across episodes. Three papers, one computational skeleton — but GQN is never connected to either the construction hypothesis or big-loop recurrence.

## What's missing
- No paper asks whether hippocampal scene representations support viewpoint generalisation analogous to GQN's query mechanism.
- No paper applies GQN-style analysis to fMRI data during scene construction/imagination to test whether neural scene representations show the same linear interpolation properties GQN representations exhibit.
- The first-person/third-person memory shift is unexplained by standard memory models; GQN provides a natural account (same representation, different query viewpoint) that has never been proposed.
- No paper asks whether the hippocampus implements something like GQN's generation network — a "rendering" process that takes a scene representation and produces a conscious mental image.

## Generative potential
**Testable prediction:** If hippocampal construction ≈ GQN, then shifting perspective during imagination (first-person → third-person) should be computationally cheap — it shouldn't require full re-construction, just re-querying the same scene representation from a different viewpoint. This predicts: (a) neural scene representations should be viewpoint-invariant (same pattern regardless of imagined perspective), and (b) perspective shifts should be faster than constructing a new scene from scratch.

**Architecture — "Cognitive GQN":** Train a GQN-like system on egocentric video where "context views" are stored episodic elements and "query viewpoints" are imagined perspectives. If it learns to render plausible third-person perspectives from first-person training data, this would be a computational model of viewpoint-independent autobiographical memory.

**Connection to false memories:** GQN sometimes renders implausible scenes (e.g., objects in impossible configurations) when the scene representation is ambiguous. This parallels false memories in construction — over-generalised scene representations produce constructions that feel vivid but are implausible. GQN's failure modes may model construction's failure modes.

---

**Falsification:** If hippocampal damage eliminates viewpoint manipulation in imagination but spares scene element retrieval (or vice versa), the unified scene-representation claim is false.
