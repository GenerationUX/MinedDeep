# Advancing Mathematics by Guiding Human Intuition with AI

**Type:** paper
**Slug:** advancing-mathematics-by-guiding-human-intuition-w--hassabis
**Sources:** advancing-mathematics-by-guiding-human-intuition-w--hassabis
**Last updated:** 2026-05-13

---

## Summary
Davies, Veličković, Buesing, Blackwell, Zheng, Tomašev, Tanburn, Battaglia, Blundell, Juhász, Lackenby, Williamson, Hassabis, and Kohli (2021) demonstrated that deep learning can guide mathematicians toward discovering new theorems. The system was used to find a new conjecture in knot theory (verified by rigorous proof) and to discover a new relationship in representation theory. Rather than replacing mathematicians, the AI served as an "intuition aid" — highlighting patterns that human experts could then formalize.

## Core content

**Approach:** Supervised learning to identify interesting patterns in mathematical objects. The AI was trained to predict whether a mathematical object had a particular property, and the attention patterns of the trained model were inspected to identify which features drove the predictions — these features suggested new conjectures (paper--advancing-mathematics-by-guiding-human-intuition-w §Methods).

**Knot theory application:**
- Trained a graph neural network on knot invariants to predict algebraic invariants (paper--advancing-mathematics-by-guiding-human-intuition-w §Results).
- Model attention patterns revealed a new quantity ("natural slope") that led to a conjecture relating geometric and algebraic knot invariants (paper--advancing-mathematics-by-guiding-human-intuition-w §Results).
- The conjecture was subsequently proven rigorously by co-author Marc Lackenby (paper--advancing-mathematics-by-guiding-human-intuition-w §Results).

**Representation theory application:**
- Similar approach applied to combinatorial objects in representation theory, discovering a new relationship verified by co-author Geordie Williamson (paper--advancing-mathematics-by-guiding-human-intuition-w §Results).

**Key insight:** The value was not in the AI's predictions per se, but in using learned representations to guide human mathematical intuition toward fruitful conjectures.

## Connections- **Theme:** [theme--AI-for-science](pages/theme--AI-for-science.md)
- **Project:** DeepMind-general
- **Collaborators:** Alex Davies (first), Petar Veličković, Lars Buesing, Sam Blackwell, Daniel Zheng, Nenad Tomašev, Richard Tanburn, Peter Battaglia, Charles Blundell, András Juhász, Marc Lackenby (Oxford), Geordie Williamson (Sydney Institute for Mathematics), Pushmeet Kohli
- **Era:** alphafold-era
- **Venue:** venue--Nature
- **Notable quote:** "We believe that this work serves as a proof of principle that ML can be used to guide the intuition of mathematicians." (paper--advancing-mathematics-by-guiding-human-intuition-w §Discussion)

## Honest Gaps
- Metadata lists only 3 co-authors; the actual paper has 14 authors.
- The AI did not produce proofs — it suggested conjectures that humans then proved. The gap between conjecture and proof remains vast.
- The approach is relatively domain-specific; it's unclear how broadly applicable this "intuition-guiding" paradigm is across mathematics.
- The representation theory conjecture was not fully proven — only partially verified.
- Sceptics noted that the knot theory result could potentially have been reached without AI, just more slowly.