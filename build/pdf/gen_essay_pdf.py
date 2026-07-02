import re, markdown, pathlib
import sys; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); import docmeta as dm

src = pathlib.Path("/home/claude/wetheusers/docs/essay/it-is-not-the-weather.md").read_text()
parts = re.split(r'\n-{3,}\n', src, maxsplit=1)
body_md = parts[1] if len(parts) > 1 else src

html_body = markdown.markdown(body_md, extensions=['extra', 'smarty', 'sane_lists'], output_format='html5')
html_body = html_body.replace('<div class="footnote">',
                              '<div class="footnote"><div class="footnote-title">Sources &amp; notes</div>')

CSS = """
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; }
body {
  font-family: "Charter", "Bitstream Charter", "Georgia", "DejaVu Serif", serif;
  font-size: 11.7pt; line-height: 1.62; color: #1c1c1c; margin: 0;
}
.docheader { text-align: center; padding-top: 6mm; margin-bottom: 9mm; }
.docheader .kicker {
  font-family: "DejaVu Sans", sans-serif; text-transform: uppercase;
  letter-spacing: 0.34em; font-size: 9.5pt; color: #6b7280; margin-bottom: 9mm;
}
.docheader .title {
  font-size: 46pt; line-height: 1.04; margin: 0 auto; color: #1b2a4a;
  font-weight: 700; letter-spacing: 0.005em; max-width: 150mm;
}
.docheader .drule { width: 64px; height: 3px; background: #b08d3a; margin: 8mm auto 6.5mm auto; }
.docheader .subtitle { font-size: 13.5pt; font-style: italic; color: #333; margin: 0 auto 4mm auto; max-width: 150mm; }
.docheader .meta { font-size: 9.5pt; font-style: italic; color: #777; }
main { max-width: 165mm; margin: 0 auto; }
h2 {
  font-size: 15pt; color: #1b2a4a; font-weight: 700; letter-spacing: 0.005em;
  margin: 1.95em 0 0.5em 0; page-break-after: avoid; line-height: 1.25;
}
p { margin: 0 0 0.9em 0; }
strong { font-weight: 700; color: #1b2a4a; }
em { font-style: italic; }
a { color: #1b2a4a; text-decoration: none; }
hr { border: 0; height: 2px; width: 64px; background: #d8c79a; margin: 2.4em auto; }
sup { font-size: 0.72em; line-height: 0; }
sup a, a.footnote-ref { color: #b08d3a; text-decoration: none; font-weight: 700; }
.footnote { margin-top: 9mm; border-top: 1px solid #ddd; padding-top: 4.5mm; font-size: 8.9pt; line-height: 1.5; color: #555; }
.footnote-title { font-family: "DejaVu Sans",sans-serif; text-transform: uppercase; letter-spacing: 0.2em; font-size: 8.5pt; color: #6b7280; margin-bottom: 3.5mm; }
.footnote hr { display: none; }
.footnote ol { padding-left: 1.15em; margin: 0; }
.footnote li { margin: 0 0 0.55em 0; padding-left: 0.15em; }
.footnote li p { margin: 0; }
.footnote a { color: #1b2a4a; word-break: break-word; }
.footnote-backref { color: #b08d3a; text-decoration: none; }
"""

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><style>__CSS__</style></head>
<body>
<section class="docheader">
  <div class="kicker">We the Users</div>
  <div class="title">We Never Agreed</div>
  <div class="drule"></div>
  <div class="subtitle">The case for an internet that belongs to the people who use it</div>
  <div class="meta">__META__</div>
</section>
<main>
__BODY__
</main>
</body></html>"""

html = TEMPLATE.replace("__CSS__", CSS).replace("__BODY__", html_body).replace("__META__", dm.meta_html("it-is-not-the-weather"))
pathlib.Path("/home/claude/essay.html").write_text(html)
print("Essay HTML written:", len(html), "chars")
