#!/usr/bin/env python3
"""Render every founding document to PDF, from its markdown source.

This is the single entry point for rebuilding all PDFs. Each document's
version/date stamp is read from build/pdf/versions.json (via docmeta), so the
stamps cannot drift from the registry. After running this, run check_meta.py to
verify every PDF prints the date the registry says it should.

    python build/pdf/build_all.py      # render everything
    python build/pdf/check_meta.py     # verify + regenerate VERSIONS.md

Requires wkhtmltopdf + xvfb and:  pip install -r build/pdf/requirements.txt
"""
import pathlib
import shutil
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent          # .../wetheusers/build/pdf
ROOT = HERE.parent.parent                                 # .../wetheusers
OUT = pathlib.Path("/mnt/user-data/outputs")
HOME = pathlib.Path("/home/claude")
sys.path.insert(0, str(HERE))
import docmeta as dm

WK = ["xvfb-run", "-a", "wkhtmltopdf", "--enable-local-file-access", "--page-size", "Letter"]


def margins(top, bot, side):
    return ["--margin-top", f"{top}mm", "--margin-bottom", f"{bot}mm",
            "--margin-left", f"{side}mm", "--margin-right", f"{side}mm"]


def run(cmd):
    """Run quietly; on failure, surface captured output and stop."""
    r = subprocess.run([str(c) for c in cmd], capture_output=True, text=True)
    if r.returncode != 0:
        sys.stderr.write((r.stdout or "") + "\n" + (r.stderr or "") + "\n")
        raise SystemExit(f"FAILED: {' '.join(str(c) for c in cmd)}")


def set_title(pdf, key):
    from pypdf import PdfReader, PdfWriter
    r = PdfReader(str(pdf))
    w = PdfWriter()
    for p in r.pages:
        w.add_page(p)
    w.add_metadata({"/Title": f"{dm.title(key)} — We the Users", "/Author": "We the Users"})
    with open(pdf, "wb") as f:
        w.write(f)


# (generator, html it writes, output pdf, repo destination, registry key)
STANDARD = [
    ("gen_declaration_pdf.py", "declaration.html", "We-the-Users-Declaration.pdf",
     "docs/declaration/declaration.pdf", "declaration"),
    ("gen_essay_pdf.py", "essay.html", "We-the-Users-We-Never-Agreed.pdf",
     "docs/essay/it-is-not-the-weather.pdf", "it-is-not-the-weather"),
    ("gen_shadow_pdf.py", "shadow.html", "We-the-Users-Your-Digital-Shadow.pdf",
     "docs/essay/shape-of-your-digital-shadow.pdf", "shape-of-digital-shadow"),
    ("gen_federalism_pdf.py", "ambition.html", "We-the-Users-Ambition-Against-Ambition.pdf",
     "docs/essay/ambition-against-ambition.pdf", "ambition-against-ambition"),
    ("gen_collab_pdf.py", "coop.html", "We-the-Users-The-Longer-Race.pdf",
     "docs/essay/the-longer-race.pdf", "the-longer-race"),
    ("gen_ledger_pdf.py", "ledger.html", "We-the-Users-The-Ledger-and-the-Spoils.pdf",
     "docs/essay/the-ledger-and-the-spoils.pdf", "the-ledger-and-the-spoils"),
    ("gen_secondzero_pdf.py", "secondzero.html", "We-the-Users-The-Second-Zero.pdf",
     "docs/essay/the-second-zero.pdf", "the-second-zero"),
    ("gen_econref_pdf.py", "econref.html", "We-the-Users-Economic-Foundations.pdf",
     "references/economic-foundations-collaboration.pdf", "economic-foundations"),
    ("gen_invitation_pdf.py", "invitation.html", "We-the-Users-Framer-Invitation.pdf",
     "docs/outreach/framer-invitation.pdf", "framer-invitation"),
]


def render_standard(gen, html, out_pdf, repo_dest, key):
    run(["python", HERE / gen])
    pdf = OUT / out_pdf
    run(WK + margins(20, 18, 22) + [HOME / html, pdf])
    set_title(pdf, key)
    shutil.copy(pdf, ROOT / repo_dest)
    print(f"  {out_pdf}")


def render_brief():
    # The brief has a title page + page numbers, applied by stamp.py.
    run(["python", HERE / "gen_pdf.py"])  # writes founding-brief.html
    run(WK + margins(20, 18, 24) + [HOME / "founding-brief.html", HOME / "base.pdf"])
    run(["python", HERE / "stamp.py"])    # writes We-the-Users-Founding-Brief.pdf
    shutil.copy(OUT / "We-the-Users-Founding-Brief.pdf", ROOT / "docs/founding-brief.pdf")
    print("  We-the-Users-Founding-Brief.pdf (title page + page numbers)")


def render_outreach():
    run(["python", HERE / "gen_outreach_pdf.py"])  # writes starthere.html + covernote.html
    for html, out_pdf, repo_dest, key in [
        ("starthere.html", "We-the-Users-Start-Here.pdf", "docs/outreach/packet-start-here.pdf", "packet-start-here"),
        ("covernote.html", "We-the-Users-Cover-Note.pdf", "docs/outreach/cover-note.pdf", "cover-note"),
    ]:
        pdf = OUT / out_pdf
        run(WK + margins(20, 18, 22) + [HOME / html, pdf])
        set_title(pdf, key)
        shutil.copy(pdf, ROOT / repo_dest)
        print(f"  {out_pdf}")


if __name__ == "__main__":
    print(f"Rendering all documents (stamps as of {dm.as_of_display()}):")
    render_brief()
    for spec in STANDARD:
        render_standard(*spec)
    render_outreach()
    print("\nDone. Next: python build/pdf/check_meta.py")
