# Grid Cells × Self-Play

**Type:** intersection
**Slug:** intersection--grid-cells-self-play
**Parents:** paper--vector-based-navigation-using-grid-like-representations-in-artificial-agents, paper--mastering-the-game-of-go-without-human-knowledge
**Last updated:** 2026-05-14
**Epistemic status:** Grounded

---

## The intersection
Grid cells spontaneously emerge in deep RL agents trained on vector-based navigation tasks (2018), demonstrating that hexagonal periodic firing patterns are a general-purpose computation that biological evolution and artificial training converge upon. Self-play generates superhuman strategies by playing against an improving opponent (2017). Both involve agents developing internal representations through interaction with an environment — but self-play creates a fundamentally *non-stationary* environment because the opponent improves continuously.

The intersection asks: **do grid-like representations emerge differently under self-play than under single-agent training?** If grid cells are a general solution to vector-based problems, they should still emerge in self-play — but their dynamics might differ. A non-stationary opponent forces rapid spatial re-evaluation, potentially accelerating the emergence of multiple spatial scales (different grid spacings for strategic vs. tactical analysis).

## What the corpus implies
The grid cell paper (Banino, Barry, Kumaran, Hassabis et al., Nature 2018) and AlphaGo Zero (Silver et al., Nature 2017) were published a year apart, both in Nature, both from DeepMind, both with Hassabis as co-author. Neither cites the other. The grid cell paper analyses representations from a single-agent navigation task; the self-play papers never examine the internal representations of game-playing agents for spatial structure. The question of what representations emerge from self-play was simply not asked.

The grid cell paper's key finding — emergence depends on *task demands* (vector navigation required, simple control insufficient) — suggests self-play might impose different representational demands. In Go, the board is a 19×19 spatial grid, and self-play agents must develop spatial representations to play well. But nobody checked whether those representations have hexagonal periodicity.

## What's missing
- No paper analyses AlphaGo/AlphaZero's internal representations for grid-cell-like hexagonal periodicity.
- No paper trains a navigation agent under self-play (two agents navigating competitively) to see whether grid cells still emerge, or whether competitive pressure produces different spatial codes.
- No paper asks whether the *multi-scale* property of grid cells (different grid spacings) maps onto different levels of strategic abstraction in game-playing (local tactics vs. global strategy).
- The grid cell paper notes emergence depends on architecture and training conditions — self-play is a training condition never tested.

## Generative potential
**Empirical test:** Analyse AlphaZero's network activations at board positions. If hexagonal periodicity appears in the spatial dimensions of the representation, this would show grid-like codes emerge even in non-navigation domains under self-play. If not, it would suggest grid cells are navigation-specific rather than general-purpose spatial codes.

**Competitive navigation experiment:** Train two agents to navigate the same maze competitively (e.g., racing to a goal, or predator-prey). Compare the spatial representations that emerge under competition vs. solitary navigation. This tests whether the social/non-stationary dimension of self-play modifies the basic grid cell computation.

**Developmental prediction:** If grid cells emerge from computational demands rather than being hardwired, they should appear in human infants at the age when spatial navigation becomes competently self-supervised — not at birth. This is consistent with some evidence but hasn't been framed through the computational lens.

**Connection to fast/slow:** If grid cells emerge at multiple scales in self-play agents, the different scales might map onto the fast/slow systems — fine-grained grids for immediate move selection (fast), coarse grids for strategic evaluation (slow). This would connect the grid cell intersection to the fast/slow×AlphaGo intersection.

---

**Falsification:** If grid-like representations in RL agents are identical in static and self-play environments (no difference in scale, stability, or non-stationarity response), the self-play-specific prediction is false.
