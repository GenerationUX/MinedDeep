# Hybrid Computing Using a Neural Network with Dynamic External Memory

**Type:** paper
**Slug:** hybrid-computing-using-a-neural-network-with-dynamic-external-memory--hassabis
**Sources:** hybrid-computing-using-a-neural-network-with-dynamic-external-memory--hassabis
**Last updated:** 2026-05-13

---

## Summary
Graves, Wayne, Reynolds, Harley, Danihelka, Grabska-Barwińska, Gómez Colmenarejo, Grefenstette, Ramalho, Agapiou, Badia, Hermann, Zwols, Ostrovski, Cain, King, Summerfield, Blunsom, Kavukcuoglu, and Hassabis (2016) introduced the Differentiable Neural Computer (DNC), a neural network architecture with an external memory matrix that can be read from and written to via differentiable attention mechanisms. DNCs learned to perform algorithmic tasks (shortest path, graph inference, language reasoning) and RL tasks (blocksworld) by learning to allocate memory, write and read data structures, and navigate them without explicit programming.

## Core content

**Problem:** Neural networks lack the ability to represent variables, store data over long timescales, and manipulate complex data structures — capabilities that are fundamental to algorithmic reasoning (paper--hybrid-computing-using-a-neural-network-with-dynamic-external-memory §Introduction).

**Architecture:** A controller neural network (LSTM) interfaces with an external N×W memory matrix via read/write heads. Key improvements over the predecessor Neural Turing Machine (paper--hybrid-computing-using-a-neural-network-with-dynamic-external-memory §Related Work):
- **Dynamic memory allocation:** A "link matrix" tracks free vs. used memory locations, enabling the network to allocate and deallocate memory as needed (paper--hybrid-computing-using-a-neural-network-with-dynamic-external-memory §Model).
- **Temporal linking:** Each written memory location is linked to the previous write, creating chains that allow sequential recall in order (paper--hybrid-computing-using-a-neural-network-with-dynamic-external-memory §Model).
- **Content-based + location-based addressing:** Combines similarity-based lookup with backward/forward traversal of memory chains (paper--hybrid-computing-using-a-neural-network-with-dynamic-external-memory §Model).

**Tasks and results:**
- **Graph tasks:** DNC learned to find shortest paths in random graphs and infer missing edges, then generalized to specific graphs (London Underground, family trees) (paper--hybrid-computing-using-a-neural-network-with-dynamic-external-memory §Results).
- **Language reasoning:** Answered bAbI tasks (inductive logic, deduction) with >95% accuracy (paper--hybrid-computing-using-a-neural-network-with-dynamic-external-memory §Results).
- **Blocksworld (RL):** Solved a planning puzzle requiring sequential goal achievement, outperforming standard DQN and LSTM baselines (paper--hybrid-computing-using-a-neural-network-with-dynamic-external-memory §Results).
- Memory visualization confirmed the network learned meaningful representations — e.g., for graph tasks, each node was stored at a distinct memory location with edges encoded in the link matrix (paper--hybrid-computing-using-a-neural-network-with-dynamic-external-memory §Results).

## Connections
- **Theme:** neural-architecture, reasoning
- **Project:** DNC
- **Collaborators:** Alexander Graves (co-first), Greg Wayne (co-first), Malcolm Reynolds, Tim Harley, Ivo Danihelka, Agnieszka Grabska-Barwińska, Sergio Gómez Colmenarejo, Edward Grefenstette, Tiago Ramalho, John Agapiou, Adrià Puigdomènech Badia, Karl Moritz Hermann, Yori Zwols, Georg Ostrovski, Adam Cain, Helen King, Christopher Summerfield, Phil Blunsom, Koray Kavukcuoglu
- **Era:** deepmind-ascent
- **Venue:** venue--Nature
- **Extends:** Neural Turing Machine (Graves et al., 2014) — DNC is the successor with dynamic memory allocation
- **Precedes:** Relational Networks, Transformer-based reasoning architectures

## Honest Gaps
- Metadata lists only 3 co-authors; the actual paper has 19 authors.
- Metadata theme is "reinforcement-learning" — only one task (blocksworld) uses RL; the paper's core contribution is neural architecture for reasoning.
- Scalability concerns: memory access is O(N) per head per timestep, limiting practical memory sizes.
- Tasks are synthetic and relatively small (graphs of ~10–20 nodes, bAbI sentences of ~5 words) — unclear how DNC scales to real-world reasoning.
- The blocksworld RL results used a simplified version of the problem compared to classical AI formulations.
- DNC was largely superseded by Transformers (2017+) for most reasoning tasks, though its memory allocation ideas remain influential.