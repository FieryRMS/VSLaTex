#!/usr/bin/env python3
import pathlib
import sys
import pymupdf

if len(sys.argv) != 2:
    print(f"usage: {sys.argv[0]} <dir>", file=sys.stderr)
    sys.exit(1)

src_dir = pathlib.Path(sys.argv[1])

for pdf_path in sorted(src_dir.glob("*.pdf")):
    out_path = pdf_path.with_suffix(".md")
    doc = pymupdf.open(pdf_path)
    with out_path.open("w", encoding="utf-8") as f:
        for page in doc:
            text = page.get_text()
            if text.strip():
                f.write(f"<!-- page {page.number + 1} -->\n")
                f.write(text)
                f.write("\n\n---\n\n")
    doc.close()
    print(f"extracted: {pdf_path.name} -> {out_path.name}")
