#!/usr/bin/env node
/**
 * Task 1 — Frontmatter Audit
 * Scans all wiki/pages/*.md, parses bold-metadata headers,
 * cross-references against _extraction_raw.json.
 * Outputs wiki/_frontmatter_audit.md
 */

import fs from 'fs';
import path from 'path';

const PAGES_DIR = path.resolve('wiki/pages');
const EXTRACTION_RAW = path.resolve('wiki/_extraction_raw.json');
const OUTPUT = path.resolve('wiki/_frontmatter_audit.md');

// Load extraction data
const extractionData = JSON.parse(fs.readFileSync(EXTRACTION_RAW, 'utf8'));

// Get all .md files (excluding .gitkeep)
const files = fs.readdirSync(PAGES_DIR)
  .filter(f => f.endsWith('.md') && f !== '.gitkeep')
  .sort();

const results = [];

for (const filename of files) {
  const filepath = path.join(PAGES_DIR, filename);
  const content = fs.readFileSync(filepath, 'utf8');
  const lines = content.split('\n');

  // Check for YAML frontmatter at line 1
  const hasFrontmatter = lines[0].trim() === '---';

  // Parse bold-metadata header (lines before the first --- separator)
  const metadata = {};
  let headerEnd = -1;
  for (let i = 0; i < Math.min(lines.length, 15); i++) {
    if (lines[i].trim() === '---') {
      headerEnd = i;
      break;
    }
    const match = lines[i].match(/\*\*([^*]+):\*\*\s*(.+)/);
    if (match) {
      metadata[match[1].trim().toLowerCase()] = match[2].trim();
    }
  }

  const typeFromHeader = metadata['type'] || '';
  const sourcesRaw = metadata['sources'] || '';
  const slugFromHeader = metadata['slug'] || '';
  const lastUpdated = metadata['last updated'] || '';

  // Try to find corpus taxonomy data
  let corpusDataFound = 'no';
  let format = '';
  let themes = '';
  let era = '';
  let domain = '';
  let year = '';

  if (sourcesRaw) {
    // Sources can be comma-separated; try each
    const sourceSlugs = sourcesRaw.split(',').map(s => s.trim());
    for (const slug of sourceSlugs) {
      if (extractionData[slug]) {
        corpusDataFound = 'yes';
        const tax = extractionData[slug].taxonomy;
        format = tax.format || '';
        themes = Array.isArray(tax.theme) ? tax.theme.join(', ') : (tax.theme || '');
        era = tax.era || '';
        domain = tax.domain || '';
        year = String(extractionData[slug].year || '');
        break;
      }
    }
  }

  // Also check if the filename's slug (without type prefix) is in extraction data
  if (corpusDataFound === 'no') {
    // Try matching by the slug from the header
    if (slugFromHeader && extractionData[slugFromHeader]) {
      corpusDataFound = 'yes (slug match)';
      const tax = extractionData[slugFromHeader].taxonomy;
      format = tax.format || '';
      themes = Array.isArray(tax.theme) ? tax.theme.join(', ') : (tax.theme || '');
      era = tax.era || '';
      domain = tax.domain || '';
      year = String(extractionData[slugFromHeader].year || '');
    }
  }

  results.push({
    filename,
    hasFrontmatter: hasFrontmatter ? 'yes' : 'no',
    typeFromHeader,
    corpusDataFound,
    format,
    themes,
    era,
    domain,
    year,
    lastUpdated,
  });
}

// Build output markdown
let output = `# Frontmatter Audit\n\n`;
output += `Generated: ${new Date().toISOString()}\n`;
output += `Total files scanned: ${results.length}\n`;
output += `Files with frontmatter: ${results.filter(r => r.hasFrontmatter === 'yes').length}\n`;
output += `Files with corpus taxonomy: ${results.filter(r => r.corpusDataFound !== 'no').length}\n\n`;

output += `| Slug | Has FM | Type | Corpus Data | Format | Themes | Era | Year |\n`;
output += `|---|---|---|---|---|---|---|---|\n`;

for (const r of results) {
  const slug = r.filename.replace('.md', '');
  output += `| ${slug} | ${r.hasFrontmatter} | ${r.typeFromHeader} | ${r.corpusDataFound} | ${r.format} | ${r.themes} | ${r.era} | ${r.year} |\n`;
}

// Add type breakdown
output += `\n## Type Breakdown\n\n`;
const typeCounts = {};
for (const r of results) {
  const t = r.typeFromHeader || '(none)';
  typeCounts[t] = (typeCounts[t] || 0) + 1;
}
output += `| Type | Count |\n|---|---|\n`;
for (const [t, c] of Object.entries(typeCounts).sort((a, b) => b[1] - a[1])) {
  output += `| ${t} | ${c} |\n`;
}

// Add corpus vs non-corpus breakdown
output += `\n## Corpus vs Non-Corpus\n\n`;
const corpusFiles = results.filter(r => r.corpusDataFound !== 'no');
const nonCorpusFiles = results.filter(r => r.corpusDataFound === 'no');
output += `- **Corpus pages** (have extraction data): ${corpusFiles.length}\n`;
output += `- **Non-corpus pages** (no extraction data): ${nonCorpusFiles.length}\n`;

fs.writeFileSync(OUTPUT, output);
console.log(`Audit written to ${OUTPUT}`);
console.log(`Total: ${results.length}, With frontmatter: ${results.filter(r => r.hasFrontmatter === 'yes').length}, With corpus data: ${corpusFiles.length}`);