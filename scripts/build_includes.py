#!/usr/bin/env python3
"""
Injects partials/header.html and partials/footer.html into every hand-authored
page between its <!--INCLUDE:HEADER-->/<!--/INCLUDE:HEADER--> and
<!--INCLUDE:FOOTER-->/<!--/INCLUDE:FOOTER--> markers, so nav/footer only need
editing in one place. Safe to re-run any time.

Does not touch case-studies/ (that section has its own generator,
generate_case_studies.py) or partials/ itself.
"""
import pathlib
import re

ROOT_DIR = pathlib.Path(__file__).parent.parent
PARTIALS_DIR = ROOT_DIR / "partials"
SKIP_DIRS = {"case-studies", "partials", ".git", "scripts"}

# errors/ holds the site-wide Caddy error page, served for any missing URL at
# any depth — it needs root-absolute links, not depth-relative ones like the
# rest of the site, since the browser's URL never actually becomes /errors/...
ABSOLUTE_ROOT_DIRS = {"errors"}

MARKER_RE = {
    "HEADER": re.compile(
        r"<!--INCLUDE:HEADER-->.*?<!--/INCLUDE:HEADER-->", re.S
    ),
    "FOOTER": re.compile(
        r"<!--INCLUDE:FOOTER-->.*?<!--/INCLUDE:FOOTER-->", re.S
    ),
}


def render_partial(name: str, root_prefix: str) -> str:
    text = (PARTIALS_DIR / f"{name.lower()}.html").read_text(encoding="utf-8")
    return text.replace("{{ROOT}}", root_prefix)


def root_prefix_for(path: pathlib.Path) -> str:
    rel_parts = path.relative_to(ROOT_DIR).parts
    if rel_parts[0] in ABSOLUTE_ROOT_DIRS:
        return "/"
    depth = len(rel_parts) - 1
    return "../" * depth


def find_pages():
    for path in ROOT_DIR.rglob("*.html"):
        rel_parts = path.relative_to(ROOT_DIR).parts
        if any(part in SKIP_DIRS for part in rel_parts):
            continue
        yield path


def main():
    updated = 0
    for path in find_pages():
        text = path.read_text(encoding="utf-8")
        original = text
        root_prefix = root_prefix_for(path)
        for name, pattern in MARKER_RE.items():
            if not pattern.search(text):
                continue
            rendered = render_partial(name, root_prefix)
            replacement = f"<!--INCLUDE:{name}-->\n{rendered}<!--/INCLUDE:{name}-->"
            text = pattern.sub(lambda m: replacement.replace("\\", "\\\\"), text)
        if text != original:
            path.write_text(text, encoding="utf-8")
            updated += 1
            print(f"updated {path.relative_to(ROOT_DIR)}")
    print(f"done — {updated} file(s) updated")


if __name__ == "__main__":
    main()
