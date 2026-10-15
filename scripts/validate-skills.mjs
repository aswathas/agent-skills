#!/usr/bin/env node
// Validates every skill directory in this repository.
//
// A skill is a markdown file with YAML frontmatter, copied verbatim into an
// agent's skills directory. A malformed frontmatter block does not fail loudly —
// the agent simply never triggers the skill, and the author finds out weeks later.
// This is the check that turns that into an error at commit time.
//
// Run: node scripts/validate-skills.mjs

import { readdirSync, readFileSync, statSync } from 'node:fs';
import { join } from 'node:path';

const ROOT = new URL('..', import.meta.url).pathname.replace(/^\/([A-Z]:)/, '$1');
const failures = [];
const checked = [];

/** Split `---\n...\n---` frontmatter off the top of a file. */
function splitFrontmatter(text, file) {
  const match = /^---\r?\n([\s\S]*?)\r?\n---\r?\n?/.exec(text);
  if (!match) {
    failures.push(`${file}: no YAML frontmatter block`);
    return null;
  }
  return match[1];
}

/** Flat key: value pairs only — a skill's frontmatter is not a place for nesting. */
function parseScalarFrontmatter(block, file) {
  const fields = new Map();
  for (const [i, raw] of block.split('\n').entries()) {
    // CRLF repos are the norm on Windows; a trailing \r silently breaks every
    // regex anchored at end-of-line, so strip it before matching.
    const line = raw.replace(/\r$/, '');
    if (!line.trim() || line.trimStart().startsWith('#')) continue;
    const kv = /^([A-Za-z0-9_-]+):\s*(.*)$/.exec(line);
    if (!kv) {
      failures.push(`${file}: frontmatter line ${i + 1} is not \`key: value\` — ${line.trim()}`);
      continue;
    }
    fields.set(kv[1], kv[2].replace(/^['"]|['"]$/g, '').trim());
  }
  return fields;
}

for (const entry of readdirSync(ROOT)) {
  const dir = join(ROOT, entry);
  if (entry.startsWith('.') || entry === 'docs' || entry === 'scripts') continue;
  if (!statSync(dir).isDirectory()) continue;

  const skillFile = join(dir, 'SKILL.md');
  let text;
  try {
    text = readFileSync(skillFile, 'utf8');
  } catch {
    failures.push(`${entry}/: no SKILL.md`);
    continue;
  }

  const file = `${entry}/SKILL.md`;
  const block = splitFrontmatter(text, file);
  if (!block) continue;
  const fields = parseScalarFrontmatter(block, file);

  const name = fields.get('name');
  const description = fields.get('description');
  if (!name) failures.push(`${file}: missing \`name\``);
  else if (name !== entry) failures.push(`${file}: \`name: ${name}\` does not match directory \`${entry}\``);

  if (!description) {
    failures.push(`${file}: missing \`description\``);
  } else if (description.length < 40) {
    // The description is what an agent matches against before opening the file.
    // A short one under-matches and the skill silently stops triggering.
    failures.push(`${file}: \`description\` is ${description.length} chars; too short to match reliably`);
  }

  const body = text.slice(text.indexOf('---', 3) + 3);
  if (body.trim().length < 200) failures.push(`${file}: body is under 200 chars`);

  if (!readdirSync(dir).includes('README.md')) {
    failures.push(`${entry}/: no README.md — every skill ships one`);
  }

  checked.push(`${name ?? entry} (${description?.length ?? 0}-char description)`);
}

for (const c of checked) console.log(`  ok  ${c}`);

if (failures.length) {
  console.error(`\n${failures.length} problem(s):`);
  for (const f of failures) console.error(`  FAIL ${f}`);
  process.exit(1);
}
console.log(`\n${checked.length} skill(s) valid.`);