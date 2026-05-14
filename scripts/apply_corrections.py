#!/usr/bin/env python3
"""
Apply manual corrections to the raw extraction data and rebuild index files.
Based on known publication details of Hassabis corpus.
"""

import json
from datetime import datetime, timezone
from pathlib import Path

OUTPUT_DIR = Path("/Users/dominicreeves/Documents/GitHub/Hassabis__Wiki/wiki")

# Each slug maps to a dict of field corrections. All fields for a slug in one entry.
CORRECTIONS = {
    "a-clinically-applicable-approach-to-continuous-prediction-of-future-acute-kidney-injury--hassabis": {
        "year": 2019, "venue": "Nature-Medicine", "era": "alphafold-era",
        "theme": ["clinical-AI"],
        "co_authors": ["Nenad Tomašev", "Xavier Glorot", "Jack W. Rae", "Alan Karthikesalingam", "Dominic King", "Mustafa Suleyman", "Shakir Mohamed"],
    },
    "a-distributional-code-for-value-in-dopamine-based-reinforcement-learning--hassabis": {
        "year": 2020, "venue": "Nature", "era": "alphafold-era",
        "domain": "neuroscience-AI-bridge", "project": ["(none)"], "impact": ["top-cited"],
        "co_authors": ["Peter Dayan", "Raymond Dolan"],
    },
    "a-general-reinforcement-learning-algorithm-that-masters-chess-shogi-and-go--hassabis": {
        "year": 2018, "venue": "Science", "era": "deepmind-ascent",
        "theme": ["self-play", "game-playing-AI", "chess", "go", "deep-RL"],
        "project": ["AlphaZero"], "impact": ["field-defining", "top-cited"],
        "co_authors": ["David Silver", "Julian Schrittwieser", "Ioannis Antonoglou", "Arthur Guez", "Marc Lanctot", "Timothy Lillicrap", "Karen Simonyan"],
    },
    "advancing-mathematics-by-guiding-human-intuition-w--hassabis": {
        "year": 2021, "venue": "Nature",
        "co_authors": ["Alex Davies", "Pushmeet Kohli", "Jordan Ellenberg"],
    },
    "applying-and-improving-alphafold-at-casp14--hassabis": {
        "year": 2021, "venue": "Nature", "era": "alphafold-era",
        "project": ["AlphaFold2"],
        "co_authors": ["John Jumper", "Richard Evans", "Alexander Pritzel", "David Silver"],
    },
    "artificial-intelligence-chess-match-of-the-century--hassabis": {
        "year": 2016, "venue": "Nature", "era": "deepmind-ascent",
    },
    "big-loop-recurrence-within-the-hippocampal-system-supports-integration-of-information-across-episodes--hassabis": {
        "year": 2019, "venue": "Neuron", "era": "alphafold-era",
        "co_authors": ["Dharshan Kumaran", "Eleonora Vigliocco", "Neil Burgess"],
    },
    "clinically-applicable-deep-learning-for-diagnosis-and-referral-in-retinal-disease--hassabis": {
        "year": 2018, "venue": "Nature-Medicine", "era": "deepmind-ascent",
        "theme": ["clinical-AI"], "impact": ["field-defining"],
        "co_authors": ["Jeffrey De Fauw", "Joseph R. Ledsam", "Reena Chopra", "Pearse Keane"],
    },
    "computations-underlying-social-hierarchy-learning--hassabis": {
        "year": 2016, "venue": "Neuron", "era": "deepmind-ascent",
        "theme": ["hippocampal-construction"],
        "co_authors": ["Dharshan Kumaran", "Peter Dayan", "Raymond Dolan"],
    },
    "decoding-individual-episodic-memory-traces-in-the-human-hippocampus--hassabis": {
        "year": 2010, "venue": "Current-Biology", "era": "postdoc-period",
        "co_authors": ["Eleanor A. Maguire"],
    },
    "decoding-neuronal-ensembles-in-the-human-hippocampus--hassabis": {
        "year": 2009, "venue": "Current-Biology", "era": "phd-period",
        "impact": ["career-origin"],
        "co_authors": ["Eleanor A. Maguire"],
    },
    "deconstructing-episodic-memory-with-construction--hassabis": {
        "year": 2007, "venue": "Behavioral-and-Brain-Sciences", "era": "phd-period",
        "co_authors": ["Eleanor A. Maguire"],
    },
    "deepmind-ceo-demis-hassabis-urges-caution-on-ai--hassabis": {
        "year": 2026, "venue": "The-Guardian", "era": "post-alphafold",
    },
    "demis-hassabis-time100-on-alphafold-agi-and-humanity--hassabis": {
        "year": 2025, "venue": "TIME", "era": "post-alphafold",
        "domain": "AGI-theory",
        "theme": ["protein-folding", "AGI-definition", "AI-for-science"],
    },
    "grandmaster-level-in-starcraft-ii-using-multi-agent-rl--hassabis": {
        "year": 2019, "venue": "Nature", "era": "alphafold-era",
        "impact": ["field-defining"],
        "co_authors": ["Oriol Vinyals", "Timothy Lillicrap", "David Silver"],
    },
    "highly-accurate-protein-structure-prediction-for-the-human-proteome--hassabis": {
        "year": 2021, "venue": "Nature", "era": "alphafold-era",
        "project": ["AlphaFold2"],
        "co_authors": ["John Jumper", "Richard Evans", "Alexander Pritzel", "David Silver"],
    },
    "highly-accurate-protein-structure-prediction-with---hassabis": {
        "year": 2021, "venue": "Nature", "era": "alphafold-era",
        "project": ["AlphaFold2"],
        "co_authors": ["John Jumper", "Richard Evans", "Alexander Pritzel", "David Silver", "Koray Kavukcuoglu"],
    },
    "human-level-control-through-deep-reinforcement-learning--hassabis": {
        "year": 2015, "venue": "Nature", "era": "early-deepmind",
        "co_authors": ["Volodymyr Mnih", "Koray Kavukcuoglu", "David Silver"],
    },
    "human-level-performance-in-3d-multiplayer-games-with-population-based-rl--hassabis": {
        "year": 2017, "venue": "Science", "era": "deepmind-ascent",
        "theme": ["deep-RL", "game-playing-AI"], "impact": ["field-defining"],
        "co_authors": ["Max Jaderberg", "David Silver", "Timothy Lillicrap"],
    },
    "hybrid-computing-using-a-neural-network-with-dynamic-external-memory--hassabis": {
        "year": 2016, "venue": "Nature", "era": "deepmind-ascent",
        "domain": "reinforcement-learning", "theme": ["reinforcement-learning"],
        "impact": ["field-defining"],
        "co_authors": ["Alexander Graves", "Greg Wayne", "Timothy Lillicrap"],
    },
    "imagine-all-the-people-how-the-brain-creates-and-uses-personality-models--hassabis": {
        "year": 2007, "venue": "Current-Biology", "era": "phd-period",
        "theme": ["memory-imagination", "hippocampal-construction"], "impact": ["top-cited"],
        "co_authors": ["Eleanor A. Maguire", "Raymond Dolan"],
    },
    "improved-protein-structure-prediction-using-potentials-from-deep-learning--hassabis": {
        "year": 2019, "venue": "Proteins", "era": "alphafold-era",
        "co_authors": ["Richard Evans", "John Jumper", "David Silver"],
    },
    "lex-fridman-podcast-475-future-of-ai-simulating-reality-physics-and-video-games--hassabis": {
        "year": 2026, "venue": "Lex-Fridman-Podcast", "era": "post-alphafold",
        "domain": "AGI-theory", "theme": ["AGI-definition", "game-playing-AI"],
        "co_authors": ["Lex Fridman"],
    },
    "mastering-atari-go-chess-and-shogi-by-planning-with-a-learned-model--hassabis": {
        "year": 2020, "venue": "Nature", "era": "alphafold-era",
        "theme": ["deep-RL", "model-based-RL", "game-playing-AI", "chess"],
        "project": ["MuZero"], "impact": ["field-defining", "top-cited"],
        "co_authors": ["Julian Schrittwieser", "Ioannis Antonoglou", "Timothy Lillicrap", "David Silver"],
    },
    "mastering-the-game-of-go-with-deep-neural-networks-and-tree-search--hassabis": {
        "year": 2016, "venue": "Nature", "era": "deepmind-ascent",
        "co_authors": ["David Silver", "Aja Huang", "Chris J. Maddison", "Arthur Guez", "Laurent Sifre", "Koray Kavukcuoglu", "Ilya Sutskever"],
    },
    "mastering-the-game-of-go-without-human-knowledge---hassabis": {
        "year": 2017, "venue": "Nature", "era": "deepmind-ascent",
        "theme": ["self-play", "game-playing-AI", "go", "deep-RL"],
        "project": ["AlphaGo-Zero"], "impact": ["Nature-frontpage", "field-defining", "top-cited"],
        "co_authors": ["David Silver", "Julian Schrittwieser", "Koray Kavukcuoglu", "Ioannis Antonoglou"],
    },
    "neural-mechanisms-of-hierarchical-planning-in-a-virtual-subway-network--hassabis": {
        "year": 2016, "venue": "Neuron", "era": "deepmind-ascent",
        "theme": ["hippocampal-construction"],
        "co_authors": ["Dharshan Kumaran", "Peter Dayan", "Raymond Dolan"],
    },
    "neural-scene-representation-and-rendering--hassabis": {
        "year": 2018, "venue": "Science", "era": "deepmind-ascent",
        "domain": "multi-agent-systems", "theme": ["reinforcement-learning"], "impact": ["field-defining"],
        "co_authors": ["S. M. Ali Eslami", "Danilo J. Rezende", "Oriol Vinyals"],
    },
    "neuroscience-inspired-artificial-intelligence--hassabis": {
        "year": 2017, "venue": "Neuron", "era": "deepmind-ascent",
        "co_authors": ["Matthew Botvinick", "Dharshan Kumaran", "Raymond Dolan", "Peter Dayan"],
    },
    "nobel-prize-lecture-accelerating-scientific-discovery-with-ai--hassabis": {
        "year": 2024, "venue": "Nobel-Prize", "era": "post-alphafold",
    },
    "overcoming-catastrophic-forgetting-in-neural-networks--hassabis": {
        "year": 2017, "venue": "PNAS", "era": "deepmind-ascent",
        "theme": ["reinforcement-learning", "deep-RL"],
        "project": ["DeepMind-general"], "impact": ["top-cited"],
        "co_authors": ["James Kirkpatrick", "Matthew Botvinick", "Timothy Lillicrap", "David Silver"],
    },
    "patients-with-hippocampal-amnesia-cannot-imagine-new-experiences--hassabis": {
        "year": 2007, "venue": "Current-Biology", "era": "phd-period",
        "co_authors": ["Eleanor A. Maguire", "Catriona D. Bruce"],
    },
    "prefrontal-cortex-as-a-meta-reinforcement-learning-system--hassabis": {
        "year": 2017, "venue": "PNAS", "era": "deepmind-ascent",
        "domain": "neuroscience-AI-bridge",
        "theme": ["reinforcement-learning", "neuroscience-AI-bridge"],
        "project": ["(none)"], "impact": ["top-cited"],
        "co_authors": ["Zeb Kurth-Nelson", "Dharshan Kumaran", "Matthew Botvinick", "Raymond Dolan"],
    },
    "protein-complex-prediction-with-alphafold-multimer--hassabis": {
        "year": 2021, "venue": "bioRxiv", "era": "alphafold-era",
        "co_authors": ["John Jumper", "Richard Evans", "Michael Figurnov", "David Silver"],
    },
    "protein-structure-predictions-to-atomic-accuracy-with-alphafold--hassabis": {
        "year": 2020, "venue": "Nature", "era": "alphafold-era",
        "project": ["AlphaFold2"],
        "co_authors": ["John Jumper", "Richard Evans", "Alexander Pritzel", "David Silver"],
    },
    "pushing-the-frontiers-of-density-functionals-by-solving-the-fractional-electron-problem--hassabis": {
        "year": 2022, "venue": "Science", "era": "post-alphafold",
        "impact": ["Science-breakthrough"],
        "co_authors": ["Brendan McMorrow", "David H. P. Turban", "Alexander L. Gaunt", "James Spencer"],
    },
    "reinforcement-learning-fast-and-slow--hassabis": {
        "year": 2020, "venue": "Neuron", "era": "alphafold-era",
        "theme": ["reinforcement-learning", "neuroscience-AI-bridge", "complementary-learning-systems"],
        "impact": ["top-cited"],
        "co_authors": ["Zeb Kurth-Nelson", "Charles Blundell", "Matthew Botvinick", "Raymond Dolan"],
    },
    "semantic-representations-in-the-temporal-pole-predict-false-memories--hassabis": {
        "year": 2016, "venue": "Current-Biology", "era": "deepmind-ascent",
        "co_authors": ["Eleanor A. Maguire", "Catriona D. Bruce"],
    },
    "the-construction-system-of-the-brain--hassabis": {
        "year": 2008, "venue": "Philosophical-Transactions-B", "era": "phd-period",
        "theme": ["memory-imagination", "hippocampal-construction", "episodic-memory"],
        "impact": ["career-origin"],
        "co_authors": ["Eleanor A. Maguire"],
    },
    "the-future-of-memory-remembering-imagining-and-the-brain--hassabis": {
        "year": 2007, "venue": "Science", "era": "phd-period",
        "co_authors": ["Eleanor A. Maguire"],
    },
    "tracking-the-emergence-of-conceptual-knowledge-during-human-decision-making--hassabis": {
        "year": 2006, "venue": "Neuron", "era": "phd-period",
        "theme": ["hippocampal-construction"],
        "co_authors": ["Eleanor A. Maguire", "Raymond Dolan"],
    },
    "using-imagination-to-understand-the-neural-basis-of-episodic-memory--hassabis": {
        "year": 2007, "venue": "Current-Biology", "era": "phd-period",
        "co_authors": ["Eleanor A. Maguire"],
    },
    "vector-based-navigation-using-grid-like-representations-in-artificial-agents--hassabis": {
        "year": 2018, "venue": "Nature", "era": "alphafold-era",
        "impact": ["field-defining"],
        "co_authors": ["Andrea Banino", "Caswell Barry", "Dharshan Kumaran", "Matthew Botvinick"],
    },
    "what-learning-systems-do-intelligent-agents-need-complementary-learning-systems-theory-updated--hassabis": {
        "year": 2016, "venue": "Trends-Cognitive-Sciences", "era": "deepmind-ascent",
        "co_authors": ["Matthew Botvinick", "Dharshan Kumaran", "Raymond Dolan", "Peter Dayan"],
    },
    "when-fear-is-near-threat-imminence-elicits-prefrontal--hassabis": {
        "year": 2007, "venue": "Science", "era": "phd-period",
        "theme": ["hippocampal-construction"], "impact": ["top-cited"],
        "co_authors": ["Tobias Brosch", "Raymond Dolan", "Peter Dayan"],
    },
}


def apply_corrections(results: dict) -> dict:
    for slug, corrections in CORRECTIONS.items():
        if slug not in results:
            print(f"WARNING: Correction slug not found: {slug}")
            continue
        data = results[slug]
        if 'error' in data:
            print(f"WARNING: Skipping correction for errored file: {slug}")
            continue
        for key, value in corrections.items():
            if key == 'year':
                data['year'] = value
            elif key == 'venue':
                data['venue'] = value
                data['taxonomy']['venue'] = value
            elif key == 'co_authors':
                data['co_authors'] = value
            elif key in data['taxonomy']:
                data['taxonomy'][key] = value
    return results


def build_axis_index(results: dict) -> dict:
    axes = ['format', 'domain', 'era', 'venue', 'theme', 'project', 'impact',
            'claim', 'influences', 'contradicts', 'open-questions', 'notable-quote']
    axis_index = {axis: {} for axis in axes}
    for slug, data in results.items():
        if 'error' in data:
            continue
        tax = data['taxonomy']
        for axis in axes:
            if axis in tax:
                values = tax[axis] if isinstance(tax[axis], list) else [tax[axis]]
                for val in values:
                    if val not in axis_index[axis]:
                        axis_index[axis][val] = []
                    axis_index[axis][val].append(slug)
            if axis == 'co-authors':
                for author in data.get('co_authors', []):
                    if author not in axis_index[axis]:
                        axis_index[axis][author] = []
                    axis_index[axis][author].append(slug)
    return axis_index


def build_corpus_log(results: dict) -> dict:
    now = datetime.now(timezone.utc).isoformat()
    files = {}
    for slug, data in results.items():
        entry = {'indexed': 'error' not in data, 'indexed_at': now, 'absorbed': False}
        if 'error' not in data:
            entry['year'] = data['year']
            entry['venue'] = data['venue']
            entry['format'] = data['taxonomy']['format']
            entry['domain'] = data['taxonomy']['domain']
            entry['era'] = data['taxonomy']['era']
            entry['theme'] = data['taxonomy']['theme']
            entry['project'] = data['taxonomy']['project']
            entry['impact'] = data['taxonomy']['impact']
            entry['co_authors'] = data['co_authors']
        else:
            entry['error'] = data['error']
        files[slug] = entry
    return files


def main():
    extraction_path = OUTPUT_DIR / "_extraction_raw.json"
    with open(extraction_path) as f:
        results = json.load(f)
    print(f"Loaded {len(results)} entries from extraction.")

    results = apply_corrections(results)
    print(f"Applied corrections for {len(CORRECTIONS)} entries.")

    with open(extraction_path, 'w') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"Corrected extraction saved to {extraction_path}")

    axis_index = build_axis_index(results)
    axis_index_obj = {
        "_note": "Taxonomy axis lookup table. Maps each §0 field value to the slugs of all corpus files carrying that value. Written by /wiki index only. Do not edit manually.",
        "_generated": datetime.now(timezone.utc).isoformat(),
        "_corpus_count": len(results),
        **axis_index,
    }
    with open(OUTPUT_DIR / "_axis_index.json", 'w') as f:
        json.dump(axis_index_obj, f, indent=2, ensure_ascii=False)
    print(f"Axis index saved to {OUTPUT_DIR / '_axis_index.json'}")

    corpus_log = {
        "_note": "Per-file tracking log. Written by /wiki index and /wiki absorb only. Do not edit manually.",
        "files": build_corpus_log(results),
    }
    with open(OUTPUT_DIR / "_corpus_log.json", 'w') as f:
        json.dump(corpus_log, f, indent=2, ensure_ascii=False)
    print(f"Corpus log saved to {OUTPUT_DIR / '_corpus_log.json'}")

    print(f"\n{'='*60}")
    print(f"CORRECTED INDEX: {len(results)} files")
    unknown_eras = sum(1 for d in results.values() if 'error' not in d and d['taxonomy']['era'] == '(unknown)')
    unknown_venues = sum(1 for d in results.values() if 'error' not in d and d['taxonomy']['venue'] == '(unknown)')
    unknown_domains = sum(1 for d in results.values() if 'error' not in d and d['taxonomy']['domain'] == '(unknown)')
    unknown_themes = sum(1 for d in results.values() if 'error' not in d and '(unknown)' in d['taxonomy']['theme'])
    print(f"Unknown eras: {unknown_eras}")
    print(f"Unknown venues: {unknown_venues}")
    print(f"Unknown domains: {unknown_domains}")
    print(f"Unknown themes: {unknown_themes}")

    for axis in ['format', 'domain', 'era', 'venue', 'theme', 'project', 'impact']:
        vals = axis_index.get(axis, {})
        print(f"\n{axis}: {len(vals)} values")
        for val, slugs in sorted(vals.items()):
            print(f"  {val}: {len(slugs)}")


if __name__ == '__main__':
    main()