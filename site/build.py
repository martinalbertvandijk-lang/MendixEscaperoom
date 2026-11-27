#!/usr/bin/env python3
"""Genereert de statische site (HTML) uit de Markdown in docs/.

Gebruik:  python3 site/build.py
Uitvoer:  site/*.html (gecommit, GitHub Pages deployt `site/` direct)

De facilitatordocumenten (00-facilitator-handleiding.md en
03-antwoorden-en-oplossingen.md) worden bewust NIET naar de site gerenderd.
"""

from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
SITE = ROOT / "site"

PAGES = [
    ("index.html", "01-verhaal-en-spelregels.md", "Start", "Operation VEILIG"),
    ("kamer-1.html", "02-puzzels-deelnemers.md", "Kamer 1 — De Manifestkaart", "Kamer 1 — De Manifestkaart"),
    ("kamer-2.html", "02-puzzels-deelnemers.md", "Kamer 2 — De Domeinmodel-kluis", "Kamer 2 — De Domeinmodel-kluis"),
    ("kamer-3.html", "02-puzzels-deelnemers.md", "Kamer 3 — De Anonieme Deur", "Kamer 3 — De Anonieme Deur"),
    ("kamer-4.html", "02-puzzels-deelnemers.md", "Kamer 4 — De Nanoflow-val", "Kamer 4 — De Nanoflow-val"),
    ("kamer-5.html", "02-puzzels-deelnemers.md", "Kamer 5 — De Serverkamer", "Kamer 5 — De Serverkamer"),
    ("antwoordformulier.html", "05-antwoordformulier.md", "Antwoordformulier", "Antwoordformulier"),
]

NAV = [
    ("index.html", "Start"),
    ("kamer-1.html", "Kamer 1"),
    ("kamer-2.html", "Kamer 2"),
    ("kamer-3.html", "Kamer 3"),
    ("kamer-4.html", "Kamer 4"),
    ("kamer-5.html", "Kamer 5"),
    ("antwoordformulier.html", "Formulier"),
    ("console.html", "🖥️ Console"),
]

START_BUTTON = """
<div class="startbox">
  <p class="start-hint">De klok loopt 75 minuten en blijft doorlopen op elke pagina.</p>
  <button id="start-clock" type="button">▶ Start de klok van De Kraai</button>
  <button id="reset-clock" type="button" hidden>⟲ Opnieuw beginnen</button>
</div>
"""

TEMPLATE = """<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — Operation VEILIG</title>
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<header class="topbar">
  <a class="brand" href="index.html">OP<span>ERATION</span> VEILIG</a>
  <div id="timer" class="timer">75:00</div>
</header>
<nav class="crumbs">
  {nav}
</nav>
<main>
{content}
</main>
<footer>
  <p>Operation VEILIG — escaperoom voor Mendix-developers ·
     Facilitator? Lees <code>docs/00-facilitator-handleiding.md</code> en houd
     <code>docs/03-antwoorden-en-oplossingen.md</code> uit handen van de teams.</p>
</footer>
<script src="assets/game.js"></script>
</body>
</html>
"""

md = markdown.Markdown(extensions=["tables", "fenced_code", "nl2br"])


def render_nav(active: str) -> str:
    parts = []
    for href, label in NAV:
        cls = ' class="active"' if href == active else ""
        parts.append(f'<a href="{href}"{cls}>{label}</a>')
    return "\n".join(parts)


def page_source(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def slice_puzzles(text: str) -> tuple[str, dict[str, str]]:
    """Splitst het puzzelbestand op '# KAMER n' koppen.

    Geeft terug: (prelude met de gedeelde context, chunks per kamer).
    """
    chunks: dict[str, str] = {}
    current: str | None = None
    prelude_lines: list[str] = []
    buffer: list[str] = []
    for line in text.splitlines():
        if line.startswith("# KAMER ") or line.startswith("# DE FINALE"):
            if current:
                chunks[current] = "\n".join(buffer)
            current = line.split("—")[0].strip("# ").strip()
            buffer = [line]
        elif current:
            buffer.append(line)
        else:
            prelude_lines.append(line)
    if current:
        chunks[current] = "\n".join(buffer)
    return "\n".join(prelude_lines).strip(), chunks


def main() -> None:
    SITE.mkdir(exist_ok=True)
    puzzle_text = page_source(DOCS / "02-puzzels-deelnemers.md")
    prelude, chunks = slice_puzzles(puzzle_text)
    intro = page_source(DOCS / "01-verhaal-en-spelregels.md")
    intro = intro.replace("## De spelregels", START_BUTTON + "\n## De spelregels", 1)

    for out_name, src_name, title, header in PAGES:
        if src_name == "02-puzzels-deelnemers.md":
            key = f"KAMER {out_name.split('-')[1].split('.')[0]}"
            body = prelude + "\n\n" + chunks[key]
        elif src_name == "01-verhaal-en-spelregels.md":
            body = intro
        else:
            body = page_source(DOCS / src_name)

        md.reset()
        html = md.convert(body)
        page = TEMPLATE.format(
            title=header,
            nav=render_nav(out_name),
            content=html,
        )
        (SITE / out_name).write_text(page, encoding="utf-8")
        print(f"✓ {out_name}")


if __name__ == "__main__":
    main()
