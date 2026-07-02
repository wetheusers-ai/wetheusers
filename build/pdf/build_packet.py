#!/usr/bin/env python3
"""Assemble the framer outreach packet from the rendered repo PDFs.

Run after build_all.py. Produces a single zip of PDFs, numbered in reading order:
orientation, the invitation, the Declaration, the four essays, then the full brief.

    python build/pdf/build_packet.py
"""
import pathlib
import zipfile

ROOT = pathlib.Path("/home/claude/wetheusers")
OUT = pathlib.Path("/mnt/user-data/outputs/We-the-Users-Framer-Packet.zip")

# (name inside the packet, source PDF in the repo) — order is the reading order.
ITEMS = [
    ("00-START-HERE.pdf", "docs/outreach/packet-start-here.pdf"),
    ("01-cover-note.pdf", "docs/outreach/cover-note.pdf"),
    ("02-framer-invitation.pdf", "docs/outreach/framer-invitation.pdf"),
    ("03-declaration.pdf", "docs/declaration/declaration.pdf"),
    ("04-it-is-not-the-weather.pdf", "docs/essay/it-is-not-the-weather.pdf"),
    ("05-the-shape-of-your-digital-shadow.pdf", "docs/essay/shape-of-your-digital-shadow.pdf"),
    ("06-ambition-against-ambition.pdf", "docs/essay/ambition-against-ambition.pdf"),
    ("07-the-longer-race.pdf", "docs/essay/the-longer-race.pdf"),
    ("08-founding-brief.pdf", "docs/founding-brief.pdf"),
]

if OUT.exists():
    OUT.unlink()
missing = [src for _, src in ITEMS if not (ROOT / src).exists()]
if missing:
    raise SystemExit("Missing source PDFs (run build_all.py first):\n  " + "\n  ".join(missing))

with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
    for name, src in ITEMS:
        z.write(ROOT / src, name)

print(f"packet -> {OUT}  ({len(ITEMS)} files)")
for name, _ in ITEMS:
    print(f"  {name}")
