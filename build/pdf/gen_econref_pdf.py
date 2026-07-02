import re, markdown, pathlib
import sys; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); import docmeta as dm

src = pathlib.Path("/home/claude/wetheusers/references/economic-foundations-collaboration.md").read_text()
# strip only the H1 title line (shown in the header); keep the caveat + body
lines = src.split("\n")
body_md = "\n".join(lines[1:]).lstrip("\n")
# body date is registry-driven: the {{LASTTOUCHED}} token is filled from versions.json,
# so the in-text "Last touched ..." date can no longer drift from the registry.
body_md = body_md.replace("{{LASTTOUCHED}}", dm.updated_display("economic-foundations"))

html_body = markdown.markdown(body_md, extensions=['extra','smarty','sane_lists'], output_format='html5')
html_body = html_body.replace('<div class="footnote">',
                              '<div class="footnote"><div class="footnote-title">Sources &amp; notes</div>')

CSS = """
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; }
body { font-family: "Charter","Bitstream Charter","Georgia","DejaVu Serif",serif; font-size: 11.4pt; line-height: 1.6; color: #1c1c1c; margin: 0; }
.docheader { text-align: center; padding-top: 6mm; margin-bottom: 8mm; }
.docheader .kicker { font-family: "DejaVu Sans",sans-serif; text-transform: uppercase; letter-spacing: 0.28em; font-size: 9pt; color: #6b7280; margin-bottom: 8mm; }
.docheader .title { font-size: 40pt; line-height: 1.05; margin: 0 auto; color: #1b2a4a; font-weight: 700; }
.docheader .drule { width: 64px; height: 3px; background: #b08d3a; margin: 8mm auto 6mm auto; }
.docheader .subtitle { font-size: 12.5pt; font-style: italic; color: #333; margin: 0 auto 3.5mm auto; max-width: 150mm; }
.docheader .meta { font-size: 9.5pt; font-style: italic; color: #777; }
main { max-width: 172mm; margin: 0 auto; }
h2 { font-size: 15pt; color: #1b2a4a; font-weight: 700; margin: 1.9em 0 0.5em 0; page-break-after: avoid; line-height: 1.25; }
h3 { font-size: 12.3pt; color: #1b2a4a; font-weight: 700; margin: 1.5em 0 0.4em 0; line-height: 1.3; page-break-after: avoid; }
p { margin: 0 0 0.85em 0; }
strong { font-weight: 700; color: #1b2a4a; }
em { font-style: italic; }
a { color: #1b2a4a; text-decoration: none; }
hr { border: 0; height: 2px; width: 64px; background: #d8c79a; margin: 2.2em auto; }
blockquote { margin: 1.1em auto 1.3em auto; max-width: 150mm; font-style: italic; color: #444; font-size: 11pt; line-height: 1.5; border-left: 3px solid #b08d3a; padding: 0.2em 0 0.2em 1.2em; }
blockquote p { margin: 0 0 0.4em 0; }
blockquote strong { color: #1b2a4a; }
ul, ol { margin: 0.5em 0 1em 0; padding-left: 1.4em; }
li { margin: 0.35em 0; line-height: 1.5; }
li > ul, li > ol { margin: 0.3em 0; }
code { font-family: "DejaVu Sans Mono", monospace; font-size: 9.5pt; background: #f3f1ea; padding: 0 3px; border-radius: 2px; }
sup { font-size: 0.72em; line-height: 0; }
sup a, a.footnote-ref { color: #b08d3a; text-decoration: none; font-weight: 700; }
.footnote { margin-top: 9mm; border-top: 1px solid #ddd; padding-top: 4.5mm; font-size: 8.8pt; line-height: 1.5; color: #555; }
.footnote-title { font-family: "DejaVu Sans",sans-serif; text-transform: uppercase; letter-spacing: 0.2em; font-size: 8.5pt; color: #6b7280; margin-bottom: 3.5mm; }
.footnote hr { display: none; }
.footnote ol { padding-left: 1.15em; margin: 0; }
.footnote li { margin: 0 0 0.5em 0; padding-left: 0.15em; }
.footnote li p { margin: 0; }
.footnote a { color: #1b2a4a; word-break: break-word; }
.footnote-backref { color: #b08d3a; text-decoration: none; }
"""

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><style>__CSS__</style></head>
<body>
<section class="docheader">
  <div class="kicker">We the Users &nbsp;&middot;&nbsp; Research Note</div>
  <div class="title">Economic Foundations</div>
  <div class="drule"></div>
  <div class="subtitle">The case for a collaborative internet &mdash; sources for the economic argument</div>
  <div class="meta">__META__</div>
</section>
<main>
__BODY__
</main>
</body></html>"""

html = TEMPLATE.replace("__CSS__", CSS).replace("__BODY__", html_body).replace("__META__", dm.meta_html("economic-foundations", label="Working note"))
pathlib.Path("/home/claude/econref.html").write_text(html)
print("HTML written:", len(html), "chars")
