# PDF build

Renders `docs/founding-brief.md` into a styled, paginated PDF
(`docs/founding-brief.pdf`).

## Pipeline

1. `gen_pdf.py` — strips the markdown title block, converts the body to HTML
   (Python `markdown`, `extra`+`smarty`), and wraps it in a styled template
   (Charter serif, navy + gold, a title page). Writes `founding-brief.html`.
2. `wkhtmltopdf` renders the HTML to a base PDF.
3. `stamp.py` overlays centered page numbers (skipping the title page) and sets
   document metadata, writing the final PDF.

`footer.html` is a page-number footer kept for reference; the bundled
`wkhtmltopdf` is an unpatched-qt build that ignores footer flags, so numbering is
applied by `stamp.py` instead.

## Reproduce

    pip install --break-system-packages markdown pypdf reportlab
    python build/pdf/gen_pdf.py
    xvfb-run -a wkhtmltopdf --enable-local-file-access --page-size Letter \
      --margin-top 20mm --margin-bottom 18mm --margin-left 24mm --margin-right 24mm \
      founding-brief.html base.pdf
    python build/pdf/stamp.py
