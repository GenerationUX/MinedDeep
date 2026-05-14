#!/usr/bin/env node
/**
 * Tasks 2-4: Schema → Inject → Validate
 * 
 * Task 2: Produce wiki/_frontmatter_schema.md
 * Task 3: Batch-inject YAML frontmatter into all wiki/pages/*.md
 * Task 4: Validate and produce wiki/_frontmatter_validation.md
 */

import fs from 'fs';
import path from 'path';

const PAGES_DIR = path.resolve('wiki/pages');
const EXTRACTION_RAW = path.resolve('wiki/_extraction_raw.json');
const AXIS_INDEX = path.resolve('wiki/_axis_index.json');
const LOG_FILE = path.resolve('wiki/_log.md');
const SCHEMA_FILE = path.resolve('wiki/_frontmatter_schema.md');
const VALIDATION_FILE = path.resolve('wiki/_frontmatter_validation.md');

// ── Load data ────────────────────────────────────────────────────────────────
const extractionData = JSON.parse(fs.readFileSync(EXTRACTION_RAW, 'utf8'));
const axisIndex = JSON.parse(fs.readFileSync(AXIS_INDEX, 'utf8'));

// ── Helpers ──────────────────────────────────────────────────────────────────
function slugify(str) {
  return str.toLowerCase().replace(/\s+/g, '-').replace(/[^a-z0-9-]/g, '');
}

function truncate(str, maxLen = 160) {
  if (!str) return '';
  // Take first sentence
  const firstSentence = str.match(/^[^.!?]+[.!?]/);
  let text = firstSentence ? firstSentence[0] : str;
  text = text.replace(/\s+/g, ' ').trim();
  if (text.length > maxLen) {
    text = text.substring(0, maxLen - 1).replace(/\s+\S*$/, '') + '…';
  }
  return text;
}

function parseBoldMetadata(content) {
  const metadata = {};
  const lines = content.split('\n');
  for (let i = 0; i < Math.min(lines.length, 15); i++) {
    if (lines[i].trim() === '---') break;
    const match = lines[i].match(/\*\*([^*]+):\*\*\s*(.+)/);
    if (match) {
      metadata[match[1].trim().toLowerCase()] = match[2].trim();
    }
  }
  return metadata;
}

function extractSummary(content) {
  const match = content.match(/## Summary\n\n(.+?)(?=\n## |\n---\n|$)/s);
  return match ? match[1].trim() : '';
}

function extractTitle(content) {
  const match = content.match(/^# (.+)/);
  return match ? match[1].trim() : '';
}

function getFirstSourceSlug(metadata) {
  const sources = metadata['sources'] || '';
  if (!sources) return null;
  return sources.split(',')[0].trim();
}

function getFileType(filename) {
  // Extract type prefix: paper, essay, intersection, claim, etc.
  const match = filename.match(/^([a-z-]+)--/);
  return match ? match[1] : '';
}

// ── Collect all distinct values for schema ───────────────────────────────────
const allFormats = new Set();
const allThemes = new Set();
const allEras = new Set();
const allDomains = new Set();
const allProjects = new Set();

for (const entry of Object.values(extractionData)) {
  const tax = entry.taxonomy;
  if (tax.format) allFormats.add(tax.format);
  if (tax.era) allEras.add(tax.era);
  if (tax.domain) allDomains.add(tax.domain);
  if (Array.isArray(tax.theme)) tax.theme.forEach(t => allThemes.add(t));
  if (Array.isArray(tax.project)) tax.project.forEach(p => { if (p !== '(none)') allProjects.add(p); });
}

// ── Task 2: Generate Schema ─────────────────────────────────────────────────
function generateSchema() {
  let s = `# Frontmatter Schema\n\n`;
  s += `Generated: ${new Date().toISOString()}\n\n`;
  s += `## Mapping Rules\n\n`;
  s += `### Title\n`;
  s += `Source: \`# Title\` from line 1 of each markdown file.\n`;
  s += `No derivation from filename — the human-readable title is already present.\n\n`;
  s += '### Tags\n';
  s += 'Tags are lowercase-hyphenated. The tag set depends on page type:\n\n';
  s += '**Primary corpus pages** (paper, essay, interview, lecture):\n';
  s += '- First tag: format slugified (e.g. `peer-reviewed-paper`, `essay`, `op-ed`, `interview`, `lecture`, `review-article`)\n';
  s += '- Then: all theme values slugified\n';
  s += '- Then: domain slugified\n';
  s += '- Then: era slugified\n';
  s += '- Then: project (if not `(none)`)\n\n';
  s += '**Derived pages** (claim, collaborator, gap, period, project, theme):\n';
  s += '- Single tag: page type (e.g. `claim`, `collaborator`, `period`, `theme`, `project`, `gap`)\n';
  s += '- Intersection subtypes flattened: `intersection` (all subtypes get the same tag)\n\n';
  s += '**Synthetic pages** (intersection, venue):\n';
  s += '- Single tag: page type (`intersection` or `venue`)\n\n';
  s += `### Description\n`;
  s += `Source: First sentence of \`## Summary\` section, truncated to ≤160 characters.\n`;
  s += `Omitted if no Summary section exists.\n\n`;
  s += `### Date\n`;
  s += `Source for corpus pages: \`year\` from extraction data, formatted as \`YYYY-01-01\`.\n`;
  s += `Source for non-corpus pages: \`**Last updated:**\` from bold-metadata header.\n`;
  s += `Omitted if neither available.\n\n`;
  s += `### Fields dropped from frontmatter\n`;
  s += `These stay in the page body only — not useful for Quartz navigation/filtering:\n`;
  s += 'co_authors, impact, venue, influences, contradicts, open-questions, claim, notable-quote\n\n';

  s += '## Distinct Values\n\n';
  s += '### Formats (' + allFormats.size + ')\n';
  s += [...allFormats].sort().map(f => '- ' + slugify(f) + ' (from "' + f + '")').join('\n') + '\n\n';
  s += '### Themes (' + allThemes.size + ')\n';
  s += [...allThemes].sort().map(t => '- ' + slugify(t) + ' (from "' + t + '")').join('\n') + '\n\n';
  s += '### Eras (' + allEras.size + ')\n';
  s += [...allEras].sort().map(e => '- ' + slugify(e) + ' (from "' + e + '")').join('\n') + '\n\n';
  s += '### Domains (' + allDomains.size + ')\n';
  s += [...allDomains].sort().map(d => '- ' + slugify(d) + ' (from "' + d + '")').join('\n') + '\n\n';
  s += '### Projects (' + allProjects.size + ')\n';
  s += [...allProjects].sort().map(p => '- ' + p).join('\n') + '\n';

  fs.writeFileSync(SCHEMA_FILE, s);
  console.log(`Schema written to ${SCHEMA_FILE}`);
}

// ── Task 3: Build frontmatter for a file ─────────────────────────────────────
function buildFrontmatter(filename, content) {
  const meta = parseBoldMetadata(content);
  const title = extractTitle(content);
  const summary = extractSummary(content);
  const description = truncate(summary);
  const fileType = getFileType(filename);
  const firstSource = getFirstSourceSlug(meta);

  const tags = [];
  let date = null;

  // Primary corpus types: use their own extraction data
  const primaryTypes = ['paper', 'essay', 'interview', 'lecture'];
  if (primaryTypes.includes(fileType) && firstSource && extractionData[firstSource]) {
    const tax = extractionData[firstSource].taxonomy;
    const entry = extractionData[firstSource];

    // Format tag
    if (tax.format) tags.push(slugify(tax.format));
    // Theme tags
    if (Array.isArray(tax.theme)) tax.theme.forEach(t => tags.push(slugify(t)));
    // Domain tag
    if (tax.domain) tags.push(slugify(tax.domain));
    // Era tag
    if (tax.era) tags.push(slugify(tax.era));
    // Project tag (skip "(none)")
    if (Array.isArray(tax.project)) tax.project.forEach(p => { if (p !== '(none)') tags.push(p); });
    // Date from year
    if (entry.year) date = `${entry.year}-01-01`;
  } else {
    // Non-corpus pages: type tag only
    // Flatten intersection subtypes
    const baseType = fileType === 'intersection' ? 'intersection' : fileType;
    if (baseType) tags.push(baseType);

    // Try to get date from Last updated
    const lastUpdated = meta['last updated'] || '';
    if (lastUpdated && /^\d{4}-\d{2}-\d{2}$/.test(lastUpdated)) {
      date = lastUpdated;
    }
  }

  // Build YAML block
  let yaml = '---\n';
  yaml += `title: "${title.replace(/"/g, '\\"')}"\n`;
  if (tags.length > 0) {
    yaml += 'tags:\n';
    for (const tag of tags) {
      yaml += `  - ${tag}\n`;
    }
  }
  if (description) {
    yaml += `description: "${description.replace(/"/g, '\\"')}"\n`;
  }
  if (date) {
    yaml += `date: ${date}\n`;
  }
  yaml += '---\n';

  return yaml;
}

// ── Task 3: Inject frontmatter ───────────────────────────────────────────────
function injectFrontmatter() {
  const files = fs.readdirSync(PAGES_DIR)
    .filter(f => f.endsWith('.md') && f !== '.gitkeep')
    .sort();

  let updated = 0;
  let skipped = 0;
  const logEntries = [];
  const timestamp = new Date().toISOString();

  for (const filename of files) {
    const filepath = path.join(PAGES_DIR, filename);
    let content = fs.readFileSync(filepath, 'utf8');
    const lines = content.split('\n');

    // Skip if already has frontmatter
    if (lines[0].trim() === '---') {
      skipped++;
      continue;
    }

    const yaml = buildFrontmatter(filename, content);
    const newContent = yaml + '\n' + content;

    fs.writeFileSync(filepath, newContent);
    updated++;
    logEntries.push(`[frontmatter-injected] ${filename.replace('.md', '')} ${timestamp}`);
  }

  // Append to log
  const logHeader = `\n## Frontmatter Injection — ${timestamp}\n\n`;
  const logBody = logEntries.map(e => `- ${e}`).join('\n') + '\n';
  fs.appendFileSync(LOG_FILE, logHeader + logBody);

  console.log(`Injection complete: ${updated} updated, ${skipped} skipped`);
}

// ── Task 4: Validate ─────────────────────────────────────────────────────────
function validateFrontmatter() {
  const files = fs.readdirSync(PAGES_DIR)
    .filter(f => f.endsWith('.md') && f !== '.gitkeep')
    .sort();

  let pass = 0;
  let fail = 0;
  const results = [];

  for (const filename of files) {
    const filepath = path.join(PAGES_DIR, filename);
    const content = fs.readFileSync(filepath, 'utf8');
    const slug = filename.replace('.md', '');
    const failures = [];

    // Check YAML frontmatter exists
    if (!content.startsWith('---\n')) {
      failures.push('Missing YAML frontmatter block');
      results.push({ slug, status: 'FAIL', failures });
      fail++;
      continue;
    }

    // Extract YAML block (between first --- and second ---)
    const endMatch = content.indexOf('\n---\n', 4);
    if (endMatch === -1) {
      failures.push('Malformed YAML: no closing ---');
      results.push({ slug, status: 'FAIL', failures });
      fail++;
      continue;
    }
    const yamlBlock = content.substring(4, endMatch);

    // Check title
    const titleMatch = yamlBlock.match(/^title:\s*"(.+)"/m);
    if (!titleMatch || !titleMatch[1].trim()) {
      failures.push('Title is empty or missing');
    }

    // Check tags
    const tagLines = yamlBlock.match(/^  - (.+)$/gm);
    if (!tagLines || tagLines.length === 0) {
      failures.push('No tags found');
    } else {
      // Check that a type-matching tag exists
      const fileType = getFileType(filename);
      const baseType = fileType === 'intersection' ? 'intersection' : fileType;
      const tags = tagLines.map(l => l.replace(/^  - /, ''));
      if (baseType && !tags.some(t => t === baseType || t === slugify(baseType))) {
        // For primary types, check format tag instead
        const primaryTypes = ['paper', 'essay', 'interview', 'lecture'];
        if (primaryTypes.includes(fileType)) {
          if (!tags.some(t => ['peer-reviewed-paper', 'essay', 'op-ed', 'interview', 'lecture', 'review-article'].includes(t))) {
            failures.push(`No format/type tag matching page type "${fileType}"`);
          }
        } else {
          failures.push(`No tag matching page type "${baseType}"`);
        }
      }
    }

    // Check description length
    const descMatch = yamlBlock.match(/^description:\s*"(.+)"/m);
    if (descMatch) {
      const descLen = descMatch[1].length;
      if (descLen > 160) {
        failures.push(`Description too long: ${descLen} chars (max 160)`);
      }
    }

    // Check date
    const dateMatch = yamlBlock.match(/^date:\s*(\d{4}-\d{2}-\d{2})$/m);
    if (!dateMatch) {
      failures.push('Missing or invalid date (expected YYYY-MM-DD)');
    }

    if (failures.length === 0) {
      pass++;
      results.push({ slug, status: 'PASS', failures: [] });
    } else {
      fail++;
      results.push({ slug, status: 'FAIL', failures });
    }
  }

  // Build validation report
  let report = `# Frontmatter Validation\n\n`;
  report += `Generated: ${new Date().toISOString()}\n`;
  report += `Total: ${pass + fail} | PASS: ${pass} | FAIL: ${fail}\n\n`;

  if (fail > 0) {
    report += `## Failures\n\n`;
    for (const r of results.filter(r => r.status === 'FAIL')) {
      report += `### ${r.slug} — FAIL\n`;
      for (const f of r.failures) {
        report += `- ${f}\n`;
      }
      report += '\n';
    }
  }

  report += `## All Files\n\n`;
  report += `| Slug | Status |\n|---|---|\n`;
  for (const r of results) {
    report += `| ${r.slug} | ${r.status} |\n`;
  }

  fs.writeFileSync(VALIDATION_FILE, report);
  console.log(`Validation written to ${VALIDATION_FILE}: ${pass} PASS, ${fail} FAIL`);
}

// ── Run ──────────────────────────────────────────────────────────────────────
console.log('=== Task 2: Schema ===');
generateSchema();
console.log('\n=== Task 3: Inject ===');
injectFrontmatter();
console.log('\n=== Task 4: Validate ===');
validateFrontmatter();
console.log('\nDone.');