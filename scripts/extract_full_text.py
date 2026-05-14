#!/usr/bin/env python3
"""Extract full text from all corpus PDFs to raw/text/ for absorb pipeline."""

import sys
from pathlib import Path
import pdfplumber

CORPUS_DIR = Path("/Users/dominicreeves/Documents/GitHub/Hassabis__Wiki/raw/corpus")
TEXT_DIR = Path("/Users/dominicreeves/Documents/GitHub/Hassabis__Wiki/raw/text")

def extract_full_text(pdf_path: Path) -> str:
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            page_text = page.extract_text()
            if page_text:
                text += f"\n--- PAGE {i+1} ---\n{page_text}\n"
    return text

def main():
    TEXT_DIR.mkdir(parents=True, exist_ok=True)
    pdfs = sorted(CORPUS_DIR.glob("*.pdf"))
    print(f"Extracting text from {len(pdfs)} PDFs...")
    
    for i, pdf in enumerate(pdfs, 1):
        slug = pdf.stem
        out = TEXT_DIR / f"{slug}.txt"
        if out.exists():
            print(f"[{i:2d}/{len(pdfs)}] SKIP (exists): {slug[:60]}")
            continue
        try:
            text = extract_full_text(pdf)
            out.write_text(text, encoding="utf-8")
            chars = len(text)
            print(f"[{i:2d}/{len(pdfs)}] OK ({chars:>6,} chars): {slug[:60]}")
        except Exception as e:
            print(f"[{i:2d}/{len(pdfs)}] ERROR: {slug[:60]}: {e}", file=sys.stderr)
    
    print("Done.")

if __name__ == "__main__":
    main()