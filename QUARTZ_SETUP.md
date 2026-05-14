# Quartz Setup for MinedDeep

End-to-end guide — roughly 20 minutes from scratch to live site.

---

## Prerequisites

- Node 18+ installed locally
- Git configured
- GitHub repo already exists at `GenerationUX/MinedDeep`

---

## Step 1 — Add Quartz as a submodule

From the root of your local `MinedDeep` clone:

```bash
git submodule add https://github.com/jackyzha0/quartz.git quartz-src
cd quartz-src
git checkout v4           # pin to stable v4 branch
cd ..
git add .gitmodules quartz-src
git commit -m "chore: add Quartz v4 as submodule"
```

> **Why submodule?** It lets you control which Quartz version you're on and
> keeps the Quartz source separate from your wiki content.

---

## Step 2 — Install Quartz dependencies

```bash
cd quartz-src
npm ci
cd ..
```

---

## Step 3 — Drop in the config files

Copy the two files from this scaffold into your repo root:

```
MinedDeep/
├── quartz.config.ts       ← copy here
├── quartz.layout.ts       ← Quartz default; copy from quartz-src/quartz.layout.ts
├── quartz-src/            ← submodule
├── wiki/
│   ├── _index.md
│   └── pages/
└── .github/
    └── workflows/
        └── deploy.yml     ← copy here
```

Then symlink the config into the submodule so it can find it:

```bash
ln -sf ../quartz.config.ts quartz-src/quartz.config.ts
ln -sf ../quartz.layout.ts quartz-src/quartz.layout.ts
```

---

## Step 4 — Frontmatter tagging (recommended)

Quartz surfaces taxonomy via frontmatter `tags`. Your pages use the §0 block
format, but Quartz reads YAML frontmatter at the top of each file.

Add a `---` YAML block to your wiki pages so the type prefix becomes a tag:

```markdown
---
tags:
  - paper
  - neuroscience
  - 2007-2010
---

## §0 Taxonomy & Identity
...
```

Claude Code can batch-add these. In your `CLAUDE.md` or a one-off command:

```
/wiki frontmatter all     (if you add this command)
```

Or run this bash script to auto-generate frontmatter from the §0 block:

```bash
# scripts/add-frontmatter.sh
# Reads `format:` and `theme:` from §0 and writes YAML frontmatter.
# Run once; idempotent (skips files that already have ---).

for f in wiki/pages/*.md; do
  if head -1 "$f" | grep -q "^---"; then
    continue   # already has frontmatter
  fi
  format=$(grep "^format:" "$f" | head -1 | sed 's/format: //')
  theme=$(grep "^theme:" "$f" | head -1 | sed 's/theme: //')
  era=$(grep "^era:" "$f" | head -1 | sed 's/era: //')
  tmpfile=$(mktemp)
  {
    echo "---"
    [ -n "$format" ] && echo "tags: [$format]"
    [ -n "$theme"  ] && echo "  - $theme"
    [ -n "$era"    ] && echo "era: \"$era\""
    echo "---"
    echo ""
    cat "$f"
  } > "$tmpfile" && mv "$tmpfile" "$f"
done
```

---

## Step 5 — Test locally

```bash
cd quartz-src
npx quartz build --directory ../wiki --serve
```

Open `http://localhost:8080`. You should see:

- Home page (from `wiki/index.md` — rename `_index.md` → `index.md` once)
- Left sidebar with page explorer
- Right sidebar with graph preview
- Global search (cmd/ctrl+K)
- Backlinks at the bottom of each page

---

## Step 6 — Enable GitHub Pages

1. Go to **Settings → Pages** in your GitHub repo
2. Set **Source** to **GitHub Actions** (not a branch)
3. Save

---

## Step 7 — Push and deploy

```bash
git add .
git commit -m "feat: add Quartz frontend"
git push origin main
```

The Actions workflow triggers automatically. After ~2 minutes:

```
https://generationux.github.io/MinedDeep/
```

---

## What you get

| Feature | Where |
|---|---|
| Full-text search | Cmd+K from anywhere |
| Interactive knowledge graph | Every page, bottom-right |
| Backlinks panel | Every page, right sidebar |
| Tag pages | `/tags/paper`, `/tags/neuroscience`, etc. |
| Table of contents | Right sidebar on long pages |
| RSS feed | `/index.xml` |
| Dark mode | Automatic (respects OS) |
| Mobile responsive | Yes |

---

## Optional: custom domain

1. Add a `CNAME` file to `wiki/` containing your domain, e.g. `hassabis.wiki`
2. Update `baseUrl` in `quartz.config.ts` to match
3. Configure DNS per GitHub's docs

---

## Updating Quartz later

```bash
cd quartz-src
git pull origin v4
cd ..
git add quartz-src
git commit -m "chore: update Quartz"
```
