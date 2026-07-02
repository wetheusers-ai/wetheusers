import re, markdown, pathlib
import sys; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); import docmeta as dm

src = pathlib.Path("/home/claude/wetheusers/docs/founding-brief.md").read_text()
# Strip the leading title block (everything before the first horizontal rule);
# we rebuild it as a proper title page below.
parts = re.split(r'\n-{3,}\n', src, maxsplit=1)
body_md = parts[1] if len(parts) > 1 else src

html_body = markdown.markdown(
    body_md,
    extensions=['extra', 'smarty', 'sane_lists'],
    output_format='html5',
)
html_body = html_body.replace('<div class="footnote">',
                              '<div class="footnote"><div class="footnote-title">Sources &amp; notes</div>')

CSS = """
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; }
body {
  font-family: "Charter", "Bitstream Charter", "Georgia", "DejaVu Serif", serif;
  font-size: 11.4pt; line-height: 1.5; color: #1c1c1c; margin: 0;
}
.titlepage { page-break-after: always; text-align: center; padding-top: 34mm; }
.titlepage .kicker {
  font-family: "DejaVu Sans", sans-serif; text-transform: uppercase;
  letter-spacing: 0.34em; font-size: 10pt; color: #6b7280; margin-bottom: 15mm;
}
.titlepage .title {
  font-size: 60pt; line-height: 1; margin: 0; color: #1b2a4a;
  font-weight: 700; letter-spacing: 0.01em;
}
.titlepage .drule { width: 66px; height: 3px; background: #b08d3a; margin: 11mm auto 9mm auto; }
.titlepage .subtitle { font-size: 17pt; font-style: italic; color: #333; margin-bottom: 17mm; }
.titlepage .meta { font-size: 10.5pt; color: #444; margin-bottom: 3mm; }
.titlepage .meta-italic { font-size: 10pt; font-style: italic; color: #777; max-width: 112mm; margin: 0 auto; }

h2 {
  font-size: 15.5pt; font-weight: 700; color: #1b2a4a; margin: 1.7em 0 0.5em 0;
  padding-bottom: 0.18em; border-bottom: 1.5px solid #d8c79a;
  page-break-after: avoid; line-height: 1.25;
}
h3 { font-size: 12.5pt; font-weight: 700; color: #2a3a55; margin: 1.25em 0 0.35em 0; page-break-after: avoid; }
p { margin: 0 0 0.7em 0; }
strong { font-weight: 700; color: #141414; }
em { font-style: italic; }
ul, ol { margin: 0.3em 0 0.9em 0; padding-left: 1.45em; }
li { margin-bottom: 0.35em; }
code {
  font-family: "DejaVu Sans Mono", monospace; font-size: 0.85em;
  background: #f1f2f5; padding: 1px 4px; border-radius: 3px; color: #2a2a2a;
}
a { color: #1b2a4a; text-decoration: none; }
hr { border: 0; height: 1px; background: #dfe3ea; margin: 1.7em 0; }
table { width: 100%; border-collapse: collapse; margin: 0.6em 0 1.1em 0; font-size: 10.1pt; page-break-inside: avoid; }
th { background: #eef1f7; color: #1b2a4a; text-align: left; font-weight: 700; border: 1px solid #cfd6e4; padding: 6px 9px; vertical-align: top; }
td { border: 1px solid #cfd6e4; padding: 6px 9px; vertical-align: top; }
tr:nth-child(even) td { background: #fafbfd; }
table th:first-child, table td:first-child { font-weight: 600; }
blockquote { margin: 0.8em 0; padding: 0.2em 0 0.2em 1em; border-left: 3px solid #d8c79a; color: #444; font-style: italic; }
sup { font-size: 0.72em; line-height: 0; }
sup a, a.footnote-ref { color: #b08d3a; text-decoration: none; font-weight: 700; }
.footnote { margin-top: 9mm; border-top: 1px solid #cfd6e4; padding-top: 4.5mm; font-size: 9pt; line-height: 1.5; color: #555; }
.footnote-title { font-family: "DejaVu Sans",sans-serif; text-transform: uppercase; letter-spacing: 0.2em; font-size: 8.5pt; color: #6b7280; margin-bottom: 3.5mm; }
.footnote hr { display: none; }
.footnote ol { padding-left: 1.15em; margin: 0; }
.footnote li { margin: 0 0 0.5em 0; }
.footnote li p { margin: 0; }
.footnote a { color: #1b2a4a; word-break: break-word; }
.footnote-backref { color: #b08d3a; text-decoration: none; }
"""

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><style>__CSS__</style></head>
<body>
<section class="titlepage">
  <div class="kicker">Founding Brief</div>
  <div class="title">We the Users</div>
  <div class="drule"></div>
  <div class="subtitle">Reclaiming the internet &mdash; its power and its rewards &mdash; into one of, by, and for the people who use it</div>
  <div class="meta">__META__</div>
  <div class="meta-italic">A living document &mdash; meant to be marked up, argued with, and rewritten</div>
</section>
<main>
__BODY__
</main>
</body></html>"""

html = TEMPLATE.replace("__CSS__", CSS).replace("__BODY__", html_body).replace("__META__", dm.meta_html("founding-brief"))
pathlib.Path("/home/claude/founding-brief.html").write_text(html)
print("HTML written:", len(html), "chars; body tables:", html.count("<table"))
