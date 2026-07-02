import re, markdown, pathlib
import sys; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); import docmeta as dm

src = pathlib.Path("/home/claude/wetheusers/docs/declaration/declaration.md").read_text()
# Strip the leading header block (title + framing lines, before the first rule);
# rebuild it as a styled document header. The epigraph + body follow.
parts = re.split(r'\n-{3,}\n', src, maxsplit=1)
body_md = parts[1] if len(parts) > 1 else src

html_body = markdown.markdown(body_md, extensions=['extra', 'smarty', 'sane_lists'], output_format='html5')

CSS = """
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; }
body {
  font-family: "Charter", "Bitstream Charter", "Georgia", "DejaVu Serif", serif;
  font-size: 11.6pt; line-height: 1.58; color: #1c1c1c; margin: 0;
}
.docheader { text-align: center; padding-top: 4mm; margin-bottom: 7mm; }
.docheader .kicker {
  font-family: "DejaVu Sans", sans-serif; text-transform: uppercase;
  letter-spacing: 0.34em; font-size: 9.5pt; color: #6b7280; margin-bottom: 9mm;
}
.docheader .title {
  font-size: 33pt; line-height: 1.08; margin: 0 auto; color: #1b2a4a;
  font-weight: 700; letter-spacing: 0.01em; max-width: 150mm;
}
.docheader .drule { width: 64px; height: 3px; background: #b08d3a; margin: 8mm auto 6.5mm auto; }
.docheader .subtitle { font-size: 13.5pt; font-style: italic; color: #333; margin: 0 auto 4mm auto; max-width: 150mm; }
.docheader .meta { font-size: 9.5pt; font-style: italic; color: #777; }
main { max-width: 165mm; margin: 0 auto; }
p { margin: 0 0 0.85em 0; }
strong { font-weight: 700; color: #1b2a4a; }
em { font-style: italic; }
ul { margin: 0.6em 0 1.1em 0; padding-left: 1.3em; }
li { margin-bottom: 0.5em; }
a { color: #1b2a4a; text-decoration: none; }
blockquote {
  margin: 0.4em auto 2.2em auto; max-width: 150mm; font-style: italic;
  color: #555; font-size: 10.7pt; line-height: 1.5;
  border-left: 3px solid #d8c79a; padding: 0.1em 0 0.1em 1.1em;
}
blockquote p { margin: 0 0 0.4em 0; }
hr { border: 0; height: 2px; width: 64px; background: #d8c79a; margin: 2.4em auto; }
"""

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><style>__CSS__</style></head>
<body>
<section class="docheader">
  <div class="kicker">We the Users</div>
  <div class="title">A Declaration of Internet Independence</div>
  <div class="drule"></div>
  <div class="subtitle">Reclaiming the internet &mdash; its power and its rewards &mdash; into one of, by, and for the people who use it</div>
  <div class="meta">__META__</div>
</section>
<main>
__BODY__
</main>
</body></html>"""

html = TEMPLATE.replace("__CSS__", CSS).replace("__BODY__", html_body).replace("__META__", dm.meta_html("declaration", publication="July 2, 2026"))
pathlib.Path("/home/claude/declaration.html").write_text(html)
print("Declaration HTML written:", len(html), "chars")
