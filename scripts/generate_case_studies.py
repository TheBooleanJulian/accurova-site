#!/usr/bin/env python3
"""
Accurova case study generator.

Workflow:
  1. Copy case-studies/data/_TEMPLATE.json to a new file, e.g. event-c.json
  2. Fill in the real story + swap picsum.photos URLs for real delivered images
     (drop images in /assets/case-studies/<slug>/ and point to them)
  3. Run: python3 scripts/generate_case_studies.py   (run from the accurova/ root)
  4. git add -A && git commit -m "case study: event-c" && git push
     -> Zeabur auto-deploys, page is live at /case-studies/event-c/

No dependencies beyond the standard library. Regenerates every page + the
index every run, so editing an old JSON and re-running updates that page too.
"""

import json
import re
from pathlib import Path
from html import escape

ROOT = Path(__file__).parent.parent
DATA_DIR = ROOT / "case-studies" / "data"
OUT_DIR = ROOT / "case-studies"
PAGE_TEMPLATE = (OUT_DIR / "template.html").read_text(encoding="utf-8")
INDEX_TEMPLATE = (OUT_DIR / "index-template.html").read_text(encoding="utf-8")

CATEGORY_LABEL = {"event": "Event", "portrait": "Portrait", "product": "Product", "property": "Property"}


def load_entries():
    entries = []
    for path in sorted(DATA_DIR.glob("*.json")):
        if path.stem.startswith("_"):
            continue  # skip templates like _TEMPLATE.json
        entries.append(json.loads(path.read_text(encoding="utf-8")))
    return entries


def results_html(results):
    return "\n".join(
        f'    <div class="result-cell"><div class="num">{escape(r["num"])}</div>'
        f'<div class="label">{escape(r["label"])}</div></div>'
        for r in results
    )


def gallery_html(images, title):
    cells = []
    for i, img in enumerate(images):
        span = ' span-2 row-2' if i == 0 else ''
        cells.append(
            f'<div class="work-item{span}"><a href="{escape(img)}" target="_blank" rel="noopener">'
            f'<img src="{escape(img)}" alt="{escape(title)} — delivered frame {i+1}" loading="lazy"></a></div>'
        )
    return "\n    ".join(cells)


def related_html(entry, all_entries):
    related = [e for e in all_entries if e["category"] == entry["category"] and e["slug"] != entry["slug"]][:3]
    if len(related) < 3:
        extra = [e for e in all_entries if e["slug"] != entry["slug"] and e not in related]
        related += extra[: 3 - len(related)]
    return "\n    ".join(card_html(e, depth=2) for e in related)


def card_html(entry, depth):
    prefix = "../" * (depth - 1) if depth > 1 else ""
    href = f"{prefix}{entry['slug']}/" if depth > 1 else f"{entry['slug']}/"
    return f"""<a class="cs-card" href="{href}" data-category="{escape(entry['category'])}">
      <div class="thumb"><img src="{escape(entry['cover_image'])}" alt="{escape(entry['title'])}" loading="lazy"></div>
      <div class="cs-card-body">
        <div class="cs-card-cat">{escape(CATEGORY_LABEL.get(entry['category'], entry['category']))}</div>
        <div class="cs-card-title">{escape(entry['title_short'])}</div>
      </div>
    </a>"""


def render_page(entry, all_entries):
    html = PAGE_TEMPLATE
    replacements = {
        "{{TITLE}}": entry["title"],
        "{{TITLE_SHORT}}": entry["title_short"],
        "{{SLUG}}": entry["slug"],
        "{{CATEGORY}}": CATEGORY_LABEL.get(entry["category"], entry["category"]),
        "{{CLIENT}}": entry["client"],
        "{{LOCATION}}": entry["location"],
        "{{DATE}}": entry["date"],
        "{{DATE_DISPLAY}}": entry["date_display"],
        "{{SERVICES}}": entry["services"],
        "{{SUMMARY}}": entry["summary"],
        "{{COVER_IMAGE}}": entry["cover_image"],
        "{{CHALLENGE}}": entry["challenge"],
        "{{APPROACH}}": entry["approach"],
        "{{BEHIND_THE_SCENES}}": entry["behind_the_scenes"],
        "{{AI_WORKFLOW}}": entry["ai_workflow"],
        "{{TESTIMONIAL_QUOTE}}": entry["testimonial_quote"],
        "{{TESTIMONIAL_AUTHOR}}": entry["testimonial_author"],
        "{{RESULTS_BLOCK}}": results_html(entry["results"]),
        "{{GALLERY_BLOCK}}": gallery_html(entry["gallery"], entry["title"]),
        "{{RELATED_BLOCK}}": related_html(entry, all_entries),
        "{{SHARE_TEXT_URL}}": re.sub(
            r"\s+", "%20", f"{entry['title']} — https://accurova.com/case-studies/{entry['slug']}/"
        ),
    }
    for token, value in replacements.items():
        html = html.replace(token, value)
    return html


def render_index(entries):
    html = INDEX_TEMPLATE
    html = html.replace("{{COUNT}}", str(len(entries)))
    html = html.replace("{{CARDS_BLOCK}}", "\n    ".join(card_html(e, depth=1) for e in entries))
    return html


def main():
    entries = load_entries()
    if not entries:
        print("No case study JSON files found in case-studies/data/")
        return

    for entry in entries:
        page_dir = OUT_DIR / entry["slug"]
        page_dir.mkdir(parents=True, exist_ok=True)
        (page_dir / "index.html").write_text(render_page(entry, entries), encoding="utf-8")
        print(f"  built /case-studies/{entry['slug']}/")

    (OUT_DIR / "index.html").write_text(render_index(entries), encoding="utf-8")
    print(f"  built /case-studies/index.html  ({len(entries)} stories)")


if __name__ == "__main__":
    main()
