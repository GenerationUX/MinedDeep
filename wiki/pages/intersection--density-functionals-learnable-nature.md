# Density Functionals × Learnable Nature

**Type:** intersection
**Slug:** intersection--density-functionals-learnable-nature
**Parents:** paper--pushing-the-frontiers-of-density-functionals-by-solving-the-fractional-electron-problem, claim--learnable-nature-conjecture
**Last updated:** 2026-05-14
**Epistemic status:** Grounded

---

## The intersection
The density functional paper (2022) shows a neural network learning a correctness property — piecewise linearity of energy with respect to fractional electron number — that *all human-crafted approximations violated for decades*. The learnable nature conjecture (2024 Nobel Lecture) holds that natural laws can be discovered by ML from data alone. The density functional paper is the **strongest evidence for learnable nature in the entire corpus**, yet it is never connected to the conjecture.

AlphaFold learned a mapping (sequence → structure) from data. The density functional learned a *constraint on the solution space* — not just what the answer is, but what mathematical form the answer must take. This is strictly harder: it requires the network to discover not just the function but a property of the function that human theorists identified but couldn't achieve. The Nobel Lecture frames learnable nature around AlphaFold; the density functional is a more demanding test case that it overlooks.

## What the corpus implies
Both papers share DeepMind authorship (Kirkpatrick et al. for density functionals; Hassabis for Nobel Lecture). Kirkpatrick was also first author on EWC — he spans the neuroscience-inspired AI and AI-for-science strands of the corpus. The density functional paper appears in the corpus but is indexed under "AI-for-science" without connection to the learnable nature conjecture. The Nobel Lecture doesn't reference the density functional work.

The density functional paper's key insight — training can enforce *correctness properties* rather than just minimising prediction error — generalises beyond quantum chemistry. If a neural network can discover piecewise linearity, what other correctness properties might it discover in other domains? This question is never asked in the corpus.

## What's missing
- The Nobel Lecture's learnable nature conjecture doesn't cite the density functional paper, despite it being a stronger case than AlphaFold for the conjecture's most ambitious claim (discovering *properties of laws*, not just laws themselves).
- No paper generalises the "learned correctness property" idea from density functionals to other domains.
- No paper asks whether the density functional's success is evidence that the brain might discover correctness properties in its own domains (perception, action, social cognition) — not just patterns but *constraints on valid patterns*.
- The transferability limitation of the learned functional (trained on specific molecular systems) is never framed as a challenge to the learnable nature conjecture — if the learned law doesn't generalise, is it really a "law"?

## Generative potential
**Generalised correctness discovery:** The density functional's training procedure — enforce a known correctness property during training — can be flipped: *discover unknown correctness properties* by training multiple networks with different inductive biases and looking for properties they all converge on. If networks with different architectures all learn piecewise-linear functionals, this is evidence that piecewise linearity is a discovered property rather than an artefact of a specific architecture.

**Challenge to learnable nature:** The density functional's limited transferability is a problem for the conjecture. If "laws" are learned but don't generalise beyond training distribution, are they laws or local approximations? The brain faces the same problem: its learned "laws of physics" work in everyday experience but fail at quantum scales. This suggests learnable nature produces *domain-bounded* laws — powerful within their training distribution, fragile outside it.

**Connection to construction:** If the brain discovers correctness properties in its domain (e.g., "scenes have coherent spatial layout"), these would function as the constraints that make construction produce plausible rather than random outputs. The temporal pole's semantic similarity code might be a learned correctness property — not innate, but discovered from experience, like the density functional's piecewise linearity.

---

**Falsification:** If the density functional result is the only case where AI discovers a correctness property human theories violated, the connection to learnable nature is coincidental.
