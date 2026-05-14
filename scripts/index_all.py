#!/usr/bin/env python3
"""
/wiki index all — Extract §0 taxonomy from all corpus PDFs.
Reads raw/corpus/*.pdf, classifies into taxonomy, outputs JSON for downstream processing.
"""

import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import pdfplumber

CORPUS_DIR = Path("/Users/dominicreeves/Documents/GitHub/Hassabis__Wiki/raw/corpus")
OUTPUT_DIR = Path("/Users/dominicreeves/Documents/GitHub/Hassabis__Wiki/wiki")
EXTRACT_PAGES = 4  # Read first N pages for metadata


def extract_text(pdf_path: Path, max_pages: int = EXTRACT_PAGES) -> str:
    """Extract text from first N pages of a PDF."""
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages[:max_pages]:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        print(f"  ERROR reading {pdf_path.name}: {e}", file=sys.stderr)
    return text


def extract_year(text: str) -> int | None:
    """Extract publication year from PDF text."""
    # Look for common patterns: "2021", "(2021)", "Nature 2021", etc.
    # Try to find the most likely publication year
    patterns = [
        r'\b((?:19|20)\d{2})\b',  # Any 4-digit year
    ]
    years = []
    for pat in patterns:
        for m in re.finditer(pat, text[:2000]):  # Only look in first 2000 chars
            y = int(m.group(1))
            if 2005 <= y <= 2026:
                years.append(y)
    
    if not years:
        return None
    
    # Deduplicate preserving order, take most common or first reasonable one
    # In academic papers, the year usually appears near the top
    from collections import Counter
    counts = Counter(years)
    # Return the most common year, or the first if tied
    return counts.most_common(1)[0][0]


def extract_venue(text: str, filename: str) -> str:
    """Extract publication venue from PDF text."""
    venue_keywords = [
        (r'\bNature\b(?!\s*(Methods|Communications|Neuroscience|Chemistry|Physics|Genetics|Materials|Energy|Catalysis|Electronics|Sustainability|Computational|Machine|Reviews|Portfolios|Climate))', 'Nature'),
        (r'\bScience\b', 'Science'),
        (r'\bNeuron\b', 'Neuron'),
        (r'\bPNAS\b|Proceedings of the National Academy', 'PNAS'),
        (r'\bCurrent\s+Biology\b', 'Current-Biology'),
        (r'\bNature\s+Medicine\b', 'Nature-Medicine'),
        (r'\bNature\s+Neuroscience\b', 'Nature-Neuroscience'),
        (r'\bTrends\s+in\s+Cognitive\s+Sciences\b', 'Trends-Cognitive-Sciences'),
        (r'\bCerebral\s+Cortex\b', 'Cerebral-Cortex'),
        (r'\bJournal\s+of\s+Neuroscience\b', 'Journal-of-Neuroscience'),
        (r'\bProteins\b', 'Proteins'),
        (r'\bNucleic\s+Acids\s+Research\b', 'Nucleic-Acids-Research'),
        (r'\bbioRxiv\b', 'bioRxiv'),
        (r'\bNobel\s+Prize\b', 'Nobel-Prize'),
        (r'\bTIME\b', 'TIME'),
        (r'\bThe\s+Guardian\b', 'The-Guardian'),
        (r'\bLex\s+Fridman\b', 'Lex-Fridman-Podcast'),
        (r'\bBehavioral\s+and\s+Brain\s+Sciences\b', 'Behavioral-and-Brain-Sciences'),
        (r'\bPhilosophical\s+Transactions', 'Philosophical-Transactions-B'),
        (r'\bNature\s+Methods\b', 'Nature-Methods'),
    ]
    
    for pat, venue in venue_keywords:
        if re.search(pat, text[:3000]):
            return venue
    
    return "(unknown)"


def extract_authors(text: str) -> list[str]:
    """Extract co-author names from first page of PDF."""
    # Get first ~1500 chars which typically has the author block
    block = text[:1500]
    
    # Remove line numbers that pdfplumber often includes
    lines = block.split('\n')
    clean_lines = []
    for line in lines:
        # Remove trailing line numbers (digits at end of line)
        cleaned = re.sub(r'\s+\d+$', '', line)
        clean_lines.append(cleaned)
    block = ' '.join(clean_lines)
    
    # Find the author block - typically between title and affiliation
    # Look for patterns like "Name1,Name2,Name3" or "Name1 Name2 Name3"
    # Authors usually come after the title (first few words) and before affiliations (numbers like "1Department")
    
    # Split on common delimiters and try to find name-like tokens
    # This is heuristic - PDF author extraction is inherently noisy
    
    authors = []
    
    # Try to find comma-separated or semicolon-separated author lists
    # Split the block into potential author section
    sentences = re.split(r'(?<=[.!?])\s+', block)
    
    # Usually first "sentence" is the title, second area has authors
    if len(sentences) >= 2:
        author_area = sentences[1] if len(sentences) > 1 else block
    else:
        author_area = block
    
    # Remove affiliation markers like "1DeepMind", "2UCL", etc.
    author_area = re.sub(r'\d+[A-Z][\w\s,&;]+(?:University|Institute|Department|Lab|DeepMind|Google|Present)', '', author_area)
    author_area = re.sub(r'\d+\s+', '', author_area)
    
    # Split on commas and asterisks
    parts = re.split(r'[,*]', author_area)
    
    for part in parts:
        part = part.strip()
        # Skip if it looks like an affiliation, a number, too short, or too long
        if not part or len(part) < 4 or len(part) > 60:
            continue
        if re.match(r'^\d+$', part):
            continue
        if re.search(r'(University|Institute|Department|Laboratory|Hospital|Present|address|UK|USA|London|California|MIT)', part, re.IGNORECASE):
            continue
        if re.match(r'^\d', part):
            continue
        # Check if it looks like a name (starts with uppercase, has internal uppercase)
        if re.match(r'^[A-Z]', part) and re.search(r'[A-Z]', part[1:]):
            # Clean up
            name = re.sub(r'\s+\d+$', '', part)
            name = re.sub(r'\s+', ' ', name).strip()
            if name and name != 'DemisHassabis' and name != 'Demis Hassabis':
                authors.append(name)
    
    return authors


def classify_paper(slug: str, text: str, year: int | None, venue: str) -> dict:
    """Classify a corpus file into the §0 taxonomy."""
    s = slug.lower()
    
    # === FORMAT ===
    if 'lex-fridman' in s:
        fmt = 'interview'
    elif 'nobel-prize-lecture' in s:
        fmt = 'lecture'
    elif 'deepmind-ceo-demis-hassabis-urges-caution' in s:
        fmt = 'op-ed'
    elif 'demis-hassabis-time100' in s:
        fmt = 'essay'
    elif 'artificial-intelligence-chess-match-of-the-century' in s:
        fmt = 'essay'
    elif 'the-future-of-memory' in s:
        fmt = 'review-article'
    elif 'the-construction-system-of-the-brain' in s:
        fmt = 'review-article'
    else:
        fmt = 'peer-reviewed-paper'
    
    # === DOMAIN ===
    neuro_keywords = ['hippocamp', 'episodic-memory', 'memory', 'imagin', 'construction',
                      'semantic-representations', 'fear', 'prefrontal', 'neural-mechanisms',
                      'tracking-the-emergence', 'personality-models', 'big-loop',
                      'social-hierarchy', 'decoding', 'amnesia', 'using-imagination',
                      'the-future-of-memory', 'the-construction-system']
    rl_keywords = ['reinforcement-learning', 'DQN', 'atari', 'deep-reinforcement',
                   'catastrophic-forgetting', 'meta-reinforcement', 'overcoming-catastrophic',
                   'population-based-rl']
    protein_keywords = ['alphafold', 'protein-structure', 'protein-complex', 'improved-protein']
    game_keywords = ['alphaGo'.lower(), 'chess', 'shogi', 'starcraft', 'go-without-human',
                     'game-of-go']
    bridge_keywords = ['neuroscience-inspired', 'neuroscience-AI', 'vector-based-navigation',
                       'complementary-learning', 'reinforcement-learning-fast-and-slow',
                       'what-learning-systems']
    clinical_keywords = ['clinical', 'kidney-injury', 'retinal-disease']
    math_keywords = ['mathematics', 'density-functionals', 'advancing-mathematics']
    safety_keywords = ['caution-on-ai', 'safety']
    science_keywords = ['nobel-prize-lecture', 'learnable-nature']
    
    domains = []
    for kw in neuro_keywords:
        if kw.lower() in s:
            domains.append('cognitive-neuroscience')
            break
    for kw in rl_keywords:
        if kw.lower() in s:
            if 'reinforcement-learning' not in domains:
                domains.append('reinforcement-learning')
            break
    for kw in protein_keywords:
        if kw.lower() in s:
            domains.append('protein-structure')
            break
    for kw in game_keywords:
        if kw.lower() in s:
            if 'game-playing-AI' not in domains:
                domains.append('game-playing-AI')
            break
    for kw in bridge_keywords:
        if kw.lower() in s:
            domains.append('neuroscience-AI-bridge')
            break
    for kw in clinical_keywords:
        if kw.lower() in s:
            domains.append('clinical-AI')
            break
    for kw in math_keywords:
        if kw.lower() in s:
            domains.append('mathematics-AI')
            break
    for kw in safety_keywords:
        if kw.lower() in s:
            domains.append('safety-governance')
            break
    for kw in science_keywords:
        if kw.lower() in s:
            domains.append('AI-for-science')
            break
    
    # Special cases
    if 'neural-scene-representation' in s:
        if not domains:
            domains.append('game-playing-AI')  # GQN was DeepMind research
    
    if 'hybrid-computing' in s or 'dynamic-external-memory' in s:
        if not domains:
            domains.append('reinforcement-learning')
    
    if 'distributional-code' in s:
        # This bridges neuroscience and RL
        if 'cognitive-neuroscience' not in domains:
            domains.insert(0, 'cognitive-neuroscience')
        if 'reinforcement-learning' not in domains:
            domains.append('reinforcement-learning')
    
    if not domains:
        domains.append('(unknown)')
    
    # Take primary domain (first)
    domain = domains[0]
    
    # === ERA ===
    if year:
        if year <= 2009:
            era = 'phd-period'
        elif year <= 2010:
            era = 'postdoc-period'
        elif year <= 2015:
            era = 'early-deepmind'
        elif year <= 2018:
            era = 'deepmind-ascent'
        elif year <= 2022:
            era = 'alphafold-era'
        else:
            era = 'post-alphafold'
    else:
        # Guess from filename/domain
        if any(kw in s for kw in ['hippocamp', 'episodic', 'amnesia', 'deconstructing', 'decoding-individual', 'decoding-neuronal']):
            era = 'phd-period'
        elif 'construction-system' in s or 'using-imagination' in s or 'fear-is-near' in s:
            era = 'postdoc-period'
        elif any(kw in s for kw in ['neural-mechanisms', 'computations-underlying']):
            era = 'early-deepmind'
        else:
            era = '(unknown)'
    
    # === THEME (multi-value) ===
    themes = []
    theme_map = {
        'memory-imagination': ['memory', 'imagination', 'imagin', 'amnesia', 'construction-system', 'future-of-memory', 'using-imagination'],
        'hippocampal-construction': ['hippocamp', 'big-loop', 'decoding-neuronal', 'decoding-individual'],
        'episodic-memory': ['episodic', 'semantic-representations'],
        'reinforcement-learning': ['reinforcement-learning', 'DQN', 'deep-reinforcement'],
        'deep-RL': ['deep-reinforcement', 'DQN', 'atari'],
        'self-play': ['self-play', 'without-human-knowledge'],
        'model-based-RL': ['planning-with-a-learned-model', 'muzero', 'mastering-atari'],
        'protein-folding': ['alphafold', 'protein-structure', 'protein-complex', 'improved-protein'],
        'structural-biology': ['alphafold', 'protein-structure', 'protein-complex'],
        'drug-discovery': [],  # None directly
        'game-playing-AI': ['game-of-go', 'chess', 'shogi', 'starcraft', 'chess-match'],
        'go': ['game-of-go', 'alphaGo'.lower()],
        'chess': ['chess'],
        'starcraft': ['starcraft'],
        'neuroscience-AI-bridge': ['neuroscience-inspired', 'vector-based-navigation', 'complementary-learning', 'reinforcement-learning-fast-and-slow', 'what-learning-systems', 'distributional-code'],
        'complementary-learning-systems': ['complementary-learning', 'what-learning-systems'],
        'AI-for-science': ['nobel-prize-lecture', 'density-functionals', 'advancing-mathematics'],
        'learnable-nature-conjecture': ['nobel-prize-lecture'],
        'safety-governance': ['caution-on-ai'],
        'AGI-risk': [],
        'AGI-definition': ['time100'],
        'consciousness': [],
    }
    
    for theme, keywords in theme_map.items():
        for kw in keywords:
            if kw.lower() in s:
                themes.append(theme)
                break
    
    if not themes:
        themes.append('(unknown)')
    
    # === PROJECT ===
    project_map = {
        'AlphaGo': ['game-of-go-with-deep-neural', 'artificial-intelligence-chess-match'],
        'AlphaGo-Zero': ['without-human-knowledge'],
        'AlphaZero': ['chess-shogi-and-go'],
        'MuZero': ['planning-with-a-learned-model', 'mastering-atari'],
        'AlphaStar': ['starcraft'],
        'AlphaFold': ['improved-protein'],
        'AlphaFold2': ['highly-accurate-protein-structure-prediction-with'],
        'AlphaFold3': ['protein-structure-predictions-to-atomic'],
        'AlphaFold-Multimer': ['protein-complex-prediction-with-alphafold-multimer'],
        'DQN': ['human-level-control-through-deep-reinforcement', 'atari'],
        'DNC': ['hybrid-computing', 'dynamic-external-memory'],
        'GQN': ['neural-scene-representation'],
        'DeepMind-general': ['kidney-injury', 'retinal-disease', 'catastrophic-forgetting',
                             'population-based-rl', 'density-functionals', 'advancing-mathematics',
                             'highly-accurate-protein-structure-prediction-for-the-human-proteome',
                             'applying-and-improving-alphafold'],
        'hippocampus-research': ['hippocamp', 'episodic', 'amnesia', 'decoding', 'construction',
                                  'semantic-representations', 'fear', 'prefrontal', 'neural-mechanisms',
                                  'tracking-the-emergence', 'personality-models', 'big-loop',
                                  'social-hierarchy', 'future-of-memory', 'using-imagination',
                                  'distributional-code'],
        '(none)': ['caution-on-ai', 'time100', 'lex-fridman', 'nobel-prize-lecture',
                    'reinforcement-learning-fast-and-slow', 'what-learning-systems',
                    'neuroscience-inspired', 'vector-based-navigation',
                    'prefrontal-cortex-as-a-meta'],
    }
    
    projects = []
    for proj, keywords in project_map.items():
        for kw in keywords:
            if kw.lower() in s:
                projects.append(proj)
                break
    
    if not projects:
        projects.append('(none)')
    
    # === IMPACT ===
    impact = []
    impact_map = {
        'Nobel-cited': ['nobel-prize-lecture', 'highly-accurate-protein-structure-prediction-with',
                        'protein-structure-predictions-to-atomic', 'highly-accurate-protein-structure-prediction-for-the-human-proteome'],
        'Science-breakthrough': ['highly-accurate-protein-structure-prediction-with',
                                  'protein-structure-predictions-to-atomic',
                                  'advancing-mathematics', 'density-functionals'],
        'Nature-frontpage': ['mastering-the-game-of-go-with-deep', 'highly-accurate-protein-structure-prediction-with'],
        'field-defining': ['mastering-the-game-of-go-with-deep', 'highly-accurate-protein-structure-prediction-with',
                           'human-level-control-through-deep', 'neuroscience-inspired',
                           'protein-structure-predictions-to-atomic'],
        'top-cited': ['mastering-the-game-of-go-with-deep', 'human-level-control-through-deep',
                      'highly-accurate-protein-structure-prediction-with', 'patients-with-hippocampal-amnesia'],
        'career-origin': ['patients-with-hippocampal-amnesia', 'deconstructing-episodic-memory',
                          'decoding-individual-episodic-memory'],
        'public-statement': ['caution-on-ai', 'time100', 'lex-fridman', 'nobel-prize-lecture',
                              'artificial-intelligence-chess-match'],
        'conjecture': ['nobel-prize-lecture'],
    }
    
    for imp, keywords in impact_map.items():
        for kw in keywords:
            if kw.lower() in s:
                impact.append(imp)
                break
    
    if not impact:
        impact.append('(none)')
    
    return {
        'format': fmt,
        'domain': domain,
        'era': era,
        'venue': venue,
        'theme': themes,
        'project': projects,
        'impact': impact,
    }


def process_all():
    """Main processing loop."""
    pdf_files = sorted(CORPUS_DIR.glob("*.pdf"))
    print(f"Found {len(pdf_files)} PDF files in corpus.")
    
    results = {}
    
    for i, pdf_path in enumerate(pdf_files, 1):
        slug = pdf_path.stem  # filename without .pdf
        print(f"[{i:2d}/{len(pdf_files)}] Processing: {slug[:70]}...")
        
        text = extract_text(pdf_path)
        if not text:
            print(f"  WARNING: No text extracted from {slug}")
            results[slug] = {
                'filename': pdf_path.name,
                'slug': slug,
                'error': 'no-text-extracted',
                'year': None,
                'venue': '(unknown)',
                'co_authors': [],
                'taxonomy': {
                    'format': '(unknown)',
                    'domain': '(unknown)',
                    'era': '(unknown)',
                    'venue': '(unknown)',
                    'theme': ['(unknown)'],
                    'project': ['(none)'],
                    'impact': ['(none)'],
                }
            }
            continue
        
        year = extract_year(text)
        venue = extract_venue(text, slug)
        co_authors = extract_authors(text)
        taxonomy = classify_paper(slug, text, year, venue)
        
        # Override venue with extracted if taxonomy had unknown
        if taxonomy['venue'] == '(unknown)' and venue != '(unknown)':
            taxonomy['venue'] = venue
        
        results[slug] = {
            'filename': pdf_path.name,
            'slug': slug,
            'year': year,
            'venue': taxonomy['venue'],
            'co_authors': co_authors,
            'taxonomy': taxonomy,
        }
        
        print(f"  year={year} venue={taxonomy['venue']} era={taxonomy['era']} "
              f"format={taxonomy['format']} domain={taxonomy['domain']} "
              f"themes={taxonomy['theme']}")
    
    return results


def build_axis_index(results: dict) -> dict:
    """Build the axis index from results."""
    axes = ['format', 'domain', 'era', 'venue', 'theme', 'project', 'impact',
            'claim', 'influences', 'contradicts', 'open-questions', 'notable-quote']
    
    axis_index = {}
    for axis in axes:
        axis_index[axis] = {}
    
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
            
            # Special: co-authors
            if axis == 'co-authors':
                for author in data.get('co_authors', []):
                    if author not in axis_index[axis]:
                        axis_index[axis][author] = []
                    axis_index[axis][author].append(slug)
    
    return axis_index


def build_corpus_log(results: dict) -> dict:
    """Build the corpus log from results."""
    now = datetime.now(timezone.utc).isoformat()
    files = {}
    
    for slug, data in results.items():
        entry = {
            'indexed': 'error' not in data,
            'indexed_at': now,
            'absorbed': False,
        }
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
    results = process_all()
    
    # Save raw extraction results for review
    extraction_path = OUTPUT_DIR / "_extraction_raw.json"
    with open(extraction_path, 'w') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\nRaw extraction saved to {extraction_path}")
    
    # Build and save axis index
    axis_index = build_axis_index(results)
    axis_index_obj = {
        "_note": "Taxonomy axis lookup table. Maps each §0 field value to the slugs of all corpus files carrying that value. Written by /wiki index only. Do not edit manually.",
        "_generated": datetime.now(timezone.utc).isoformat(),
        "_corpus_count": len(results),
        **axis_index,
    }
    axis_path = OUTPUT_DIR / "_axis_index.json"
    with open(axis_path, 'w') as f:
        json.dump(axis_index_obj, f, indent=2, ensure_ascii=False)
    print(f"Axis index saved to {axis_path}")
    
    # Build and save corpus log
    corpus_log = {
        "_note": "Per-file tracking log. Written by /wiki index and /wiki absorb only. Do not edit manually.",
        "files": build_corpus_log(results),
    }
    corpus_path = OUTPUT_DIR / "_corpus_log.json"
    with open(corpus_path, 'w') as f:
        json.dump(corpus_log, f, indent=2, ensure_ascii=False)
    print(f"Corpus log saved to {corpus_path}")
    
    # Print summary
    print(f"\n{'='*60}")
    print(f"INDEX COMPLETE: {len(results)} files processed")
    errors = sum(1 for d in results.values() if 'error' in d)
    print(f"Errors: {errors}")
    
    # Print axis summary
    for axis in ['format', 'domain', 'era', 'venue']:
        vals = axis_index.get(axis, {})
        print(f"\n{axis}: {len(vals)} values")
        for val, slugs in sorted(vals.items()):
            print(f"  {val}: {len(slugs)} files")


if __name__ == '__main__':
    main()