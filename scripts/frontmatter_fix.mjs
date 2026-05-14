#!/usr/bin/env node
/**
 * Fix: strip existing frontmatter, fix summary regex + dedupe tags, re-inject.
 */
import fs from 'fs';
import path from 'path';

const PAGES_DIR = path.resolve('wiki/pages');
const EXTRACTION_RAW = path.resolve('wiki/_extraction_raw.json');

const extractionData = JSON.parse(fs.readFileSync(EXTRACTION_RAW, 'utf8'));

function slugify(str) {
  return str.toLowerCase().replace(/\s+/g, '-').replace(/[^a-z0-9-]/g, '');
}

function truncate(str, maxLen = 160) {
  if (!str) return '';
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

// FIXED: allow optional blank line after ## Summary
function extractSummary(content) {
  const match = content.match(/## Summary\n(?:\n)?(.+?)(?=\n## |\n---\n|$)/s);
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
  const match = filename.match(/^([a-z-]+)--/);
  return match ? match[1] : '';
}

function buildFrontmatter(filename, content) {
  const meta = parseBoldMetadata(content);
  const title = extractTitle(content);
  const summary = extractSummary(content);
  const description = truncate(summary);
  const fileType = getFileType(filename);
  const firstSource = getFirstSourceSlug(meta);

  // FIXED: use Set to deduplicate
  const tagSet = new Set();
  let date = null;

  const primaryTypes = ['paper', 'essay', 'interview', 'lecture'];
  if (primaryTypes.includes(fileType) && firstSource && extractionData[firstSource]) {
    const tax = extractionData[firstSource].taxonomy;
    const entry = extractionData[firstSource];
    if (tax.format) tagSet.add(slugify(tax.format));
    if (Array.isArray(tax.theme)) tax.theme.forEach(t => tagSet.add(slugify(t)));
    if (tax.domain) tagSet.add(slugify(tax.domain));
    if (tax.era) tagSet.add(slugify(tax.era));
    if (Array.isArray(tax.project)) tax.project.forEach(p => { if (p !== '(none)') tagSet.add(p); });
    if (entry.year) date = entry.year + '-01-01';
  } else {
    const baseType = fileType === 'intersection' ? 'intersection' : fileType;
    if (baseType) tagSet.add(baseType);
    const lastUpdated = meta['last updated'] || '';
    if (lastUpdated && /^\d{4}-\d{2}-\d{2}$/.test(lastUpdated)) {
      date = lastUpdated;
    }
  }

  const tags = [...tagSet];
  let yaml = '---\n';
  yaml += 'title: "' + title.replace(/"/g, '\\"') + '"\n';
  if (tags.length > 0) {
    yaml += 'tags:\n';
    for (const tag of tags) {
      yaml += '  - ' + tag + '\n';
    }
  }
  if (description) {
    yaml += 'description: "' + description.replace(/"/g, '\\"') + '"\n';
  }
  if (date) {
    yaml += 'date: ' + date + '\n';
  }
  yaml += '---\n';
  return yaml;
}

const files = fs.readdirSync(PAGES_DIR)
  .filter(f => f.endsWith('.md') && f !== '.gitkeep')
  .sort();

let fixed = 0;
for (const filename of files) {
  const filepath = path.join(PAGES_DIR, filename);
  let content = fs.readFileSync(filepath, 'utf8');

  // Strip existing frontmatter if present
  if (content.startsWith('---\n')) {
    const endIdx = content.indexOf('\n---\n', 4);
    if (endIdx !== -1) {
      content = content.substring(endIdx + 5); // skip past \n---\n
      // Remove leading blank line if present
      if (content.startsWith('\n')) content = content.substring(1);
    }
  }

  const yaml = buildFrontmatter(filename, content);
  fs.writeFileSync(filepath, yaml + '\n' + content);
  fixed++;
}

console.log('Fixed and re-injected frontmatter for ' + fixed + ' files.');