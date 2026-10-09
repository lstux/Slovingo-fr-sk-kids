#!/usr/bin/env python3
"""build_md_fr.py

Publie md-fr/ (traduction française de relecture des fiches) en pages HTML
statiques, pour être lues dans le navigateur sous /fr/.

Ce n'est pas un cours jouable : le moteur Slovingo n'est pas utilisé. Les
fiches SMD sont converties en texte simple :
  - "! phrase"  -> phrase en gras (carte audio)
  - "> ligne" dans une carte -> ligne de traduction (→)
  - "+ note"    -> note (💡)
  - "@ image"   -> supprimée (les images sont en TODO)
  - {{...}}     -> le texte seul

Usage :
  python3 tools/build_md_fr.py md-fr/ _site/fr/
"""

import pathlib
import re
import sys

import markdown

PAGE = """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>{title} — relecture</title>
<style>
  :root {{ --bg: #fbfaf7; --fg: #1d1d1b; --muted: #6b6b66; --accent: #2f6f4e; --line: #e2e0d8; }}
  @media (prefers-color-scheme: dark) {{
    :root {{ --bg: #161715; --fg: #ece9e1; --muted: #9a978d; --accent: #7fc09a; --line: #32332f; }}
  }}
  body {{ margin: 0; background: var(--bg); color: var(--fg);
         font: 17px/1.6 system-ui, -apple-system, "Segoe UI", sans-serif; }}
  main {{ max-width: 44rem; margin: 0 auto; padding: 1rem 16px 3rem; }}
  nav {{ border-bottom: 1px solid var(--line); padding: .6rem 16px; font-size: .95rem; }}
  nav a {{ color: var(--accent); }}
  h1 {{ font-size: 1.5rem; line-height: 1.25; }}
  h2 {{ font-size: 1.2rem; margin-top: 2rem; border-top: 1px solid var(--line); padding-top: 1rem; }}
  h3 {{ font-size: 1.05rem; }}
  table {{ border-collapse: collapse; width: 100%; font-size: .95rem; }}
  th, td {{ text-align: left; padding: .35rem .5rem; border-bottom: 1px solid var(--line); vertical-align: top; }}
  blockquote {{ margin: 1rem 0; padding: .2rem 1rem; border-left: 3px solid var(--accent); color: var(--muted); }}
  .card {{ margin: .9rem 0; padding: .6rem .9rem; border: 1px solid var(--line); border-radius: 8px; }}
  .card .tr {{ color: var(--muted); }}
  hr {{ border: 0; border-top: 1px solid var(--line); margin: 1.6rem 0; }}
  a {{ color: var(--accent); }}
</style>
</head>
<body>
<nav><a href="../">← Retour au cours</a> · <a href="./">Index de la relecture</a></nav>
<main>
{body}
</main>
</body>
</html>
"""


def smd_to_markdown(text: str) -> str:
    """Convertit le SMD des fiches en Markdown lisible."""
    out = []
    in_card = False
    for raw in text.splitlines():
        line = raw.rstrip()
        if line.startswith("@ "):
            continue
        if not line.strip():
            in_card = False
            out.append("")
            continue
        if line.startswith("! "):
            in_card = True
            out.append("")
            out.append("**" + line[2:] + "**")
            continue
        if line.startswith("+ "):
            out.append("")
            out.append("💡 " + line[2:])
            continue
        if in_card and line.startswith("> "):
            out.append("→ " + line[2:])
            continue
        out.append(line)
    text = "\n".join(out)
    return text.replace("{{", "").replace("}}", "")


def render(md_text: str) -> tuple[str, str]:
    """Retourne (titre, html) pour un fichier de md-fr."""
    title = "Relecture"
    for line in md_text.splitlines():
        if line.startswith("# "):
            title = line[2:].strip()
            break
    html = markdown.markdown(
        smd_to_markdown(md_text),
        extensions=["tables", "nl2br"],
    )
    return title, html


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 2
    src = pathlib.Path(sys.argv[1])
    dst = pathlib.Path(sys.argv[2])
    if not src.is_dir():
        print(f"Dossier introuvable : {src}", file=sys.stderr)
        return 1
    dst.mkdir(parents=True, exist_ok=True)

    files = sorted(src.glob("*.md"))
    index_items = []
    index_body = ""
    for path in files:
        text = path.read_text(encoding="utf-8")
        title, body = render(text)
        if path.name == "README.md":
            index_body = body
            continue
        out_name = path.stem + ".html"
        (dst / out_name).write_text(
            PAGE.format(title=title, body=body), encoding="utf-8"
        )
        index_items.append((out_name, title))
        print(f"{path.name} -> {out_name}")

    listing = "\n".join(
        f'<li><a href="{name}">{title}</a></li>' for name, title in index_items
    )
    index_body = index_body + "\n<h2>Les fiches</h2>\n<ul>\n" + listing + "\n</ul>"
    (dst / "index.html").write_text(
        PAGE.format(title="Index", body=index_body), encoding="utf-8"
    )
    print(f"index.html ({len(index_items)} fiches)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
