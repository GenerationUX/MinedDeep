# Decoding Individual Episodic Memory Traces in the Human Hippocampus

**Type:** paper
**Slug:** decoding-individual-episodic-memory-traces-in-the-human-hippocampus--hassabis
**Sources:** decoding-individual-episodic-memory-traces-in-the-human-hippocampus--hassabis
**Last updated:** 2026-05-13

---

## Summary
Chadwick, Hassabis, Weiskopf, and Maguire (2010) used high-spatial-resolution fMRI with multivariate pattern analysis (MVPA) to demonstrate that individual rich episodic memories can be decoded from voxel-level BOLD patterns in the human hippocampus. The study revealed a functional topography within the hippocampus, with preferential episodic processing in bilateral anterior and right posterior regions, and showed that hippocampal decoding significantly outperformed adjacent entorhinal cortex and parahippocampal gyrus.

## Core content

**Research question:** Can traces of individual complex everyday episodic memories be detected and distinguished from hippocampal fMRI activity patterns, and if so, is this information distributed uniformly across the hippocampus?

**Method:** Ten participants viewed three 7-second film clips of everyday events (e.g., a woman drinking from a cup) 15 times each during a prescan training session. During fMRI scanning at 3T with 1.5mm isotropic voxels, participants performed both cued recall and free recall of the three memories. A linear SVM with multivariate feature selection (searchlight-based) was trained to classify which of the three memories was being recalled (paper--decoding-individual-episodic-memory-traces-in-the-human-hippocampus §Results).

**Key findings:**
- Episodic memory decoding was successful in the hippocampus for all ten participants, significantly above chance (33.3%) (paper--decoding-individual-episodic-memory-traces-in-the-human-hippocampus §Results).
- Entorhinal cortex and parahippocampal gyrus also contained above-chance episodic information, but significantly less than the hippocampus (one-way ANOVA, p=0.027; HC>EC p=0.035; HC>PHG p=0.048) (paper--decoding-individual-episodic-memory-traces-in-the-human-hippocampus §Results).
- Hippocampal "information maps" showed consistent peak regions across participants in bilateral anterior hippocampus and right posterior hippocampus (p<0.001, binomial test), revealing a functional topography (paper--decoding-individual-episodic-memory-traces-in-the-human-hippocampus §Results).
- The stability of memory traces across re-activations was implied by the classifier's ability to decode across multiple recall trials (paper--decoding-individual-episodic-memory-traces-in-the-human-hippocampus §Results).
- Right posterior hippocampus involvement was speculated to relate to spatial coding of memory locations; bilateral anterior loci were linked to autobiographical memory literature (paper--decoding-individual-episodic-memory-traces-in-the-human-hippocampus §Results).

**Significance:** First demonstration that traces of individual rich episodic memories are detectable noninvasively in the human hippocampus. The functional topography finding opened new lines of investigation into hippocampal subfield specialization for episodic memory.

## Connections- **Precedes:** paper--decoding-neuronal-ensembles-in-the-human-hippocampus (2009) — the prior spatial decoding study by the same group using the same MVPA methodology
- **Theme:** [theme--hippocampal-construction](pages/theme--hippocampal-construction.md), episodic-memory, [theme--memory-imagination](pages/theme--memory-imagination.md)
- **Collaborators:** Martin J. Chadwick (co-first author), Nikolaus Weiskopf, Eleanor A. Maguire
- **Era:** postdoc-period — Hassabis's final neuroscience paper before full transition to DeepMind
- **Venue:** venue--Current-Biology
- **Cited:** Marr's (1971) memory index theory as theoretical framework for hippocampal multimodal binding

## Honest Gaps
- The metadata lists only Eleanor A. Maguire as co-author; the actual paper includes Martin J. Chadwick (co-first author) and Nikolaus Weiskopf.
- The three film clip memories were emotionally neutral and highly constrained (7-second everyday actions) — generalizability to more complex, emotional, or self-relevant episodic memories is unclear.
- The functional topography claims are based on a frequency heatmap across only 10 participants with relatively low statistical thresholds (uncorrected p<0.001).
- The paper does not resolve whether the decoded patterns reflect the episodic content per se or associated spatial/contextual features.