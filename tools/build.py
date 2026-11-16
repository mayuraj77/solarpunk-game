"""Build the single-file prototype page from its parts.

Run from the repository root:
    python3 tools/build.py

Joins prototype/shell.html (layout and styles) with prototype/game.js (all game
logic) into prototype/solarpunk-valley.html, the file that gets published.
"""
from pathlib import Path

root = Path(__file__).resolve().parent.parent
shell = (root / "prototype" / "shell.html").read_text(encoding="utf-8")
game = (root / "prototype" / "game.js").read_text(encoding="utf-8")
out = root / "prototype" / "solarpunk-valley.html"
out.write_text(f"{shell}<script>\n{game}</script>\n", encoding="utf-8")
print(f"Wrote {out.relative_to(root)} ({out.stat().st_size:,} bytes)")
