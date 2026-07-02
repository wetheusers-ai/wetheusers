import re, markdown, pathlib
import sys; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); import docmeta as dm

src = pathlib.Path("/home/claude/wetheusers/docs/outreach/framer-invitation.md").read_text()
parts = re.split(r'\n-{3,}\n', src, maxsplit=1)
body_md = parts[1] if len(parts) > 1 else src

html_body = markdown.markdown(body_md, extensions=['extra', 'smarty', 'sane_lists'], output_format='html5')

CSS = """
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; }
body {
  font-family: "Charter", "Bitstream Charter", "Georgia", "DejaVu Serif", serif;
  font-size: 11.5pt; line-height: 1.55; color: #1c1c1c; margin: 0;
}
.docheader { text-align: center; padding-top: 5mm; margin-bottom: 8mm; }
.docheader .kicker {
  font-family: "DejaVu Sans", sans-serif; text-transform: uppercase;
  letter-spacing: 0.34em; font-size: 9.5pt; color: #6b7280; margin-bottom: 8mm;
}
.docheader .title {
  font-size: 34pt; line-height: 1.06; margin: 0 auto; color: #1b2a4a;
  font-weight: 700; letter-spacing: 0.005em; max-width: 150mm;
}
.docheader .drule { width: 64px; height: 3px; background: #b08d3a; margin: 7mm auto 6mm auto; }
.docheader .subtitle { font-size: 13pt; font-style: italic; color: #333; margin: 0 auto 4mm auto; max-width: 150mm; }
.docheader .meta { font-size: 9.5pt; font-style: italic; color: #777; }
main { max-width: 165mm; margin: 0 auto; }
h2 {
  font-size: 13.5pt; color: #1b2a4a; font-weight: 700; letter-spacing: 0.005em;
  margin: 1.7em 0 0.5em 0; page-break-after: avoid; line-height: 1.25;
}
p { margin: 0 0 0.8em 0; }
strong { font-weight: 700; color: #1b2a4a; }
em { font-style: italic; }
ul { margin: 0.55em 0 1.0em 0; padding-left: 1.3em; }
li { margin-bottom: 0.5em; }
a { color: #1b2a4a; text-decoration: none; }
"""

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><style>__CSS__</style></head>
<body>
<section class="docheader">
  <div class="kicker">We the Users</div>
  <div class="title">An Invitation to the Framers</div>
  <div class="drule"></div>
  <div class="subtitle">Help frame an internet owned by the people who use it</div>
  <div class="meta">__META__</div>
</section>
<main>
__BODY__
</main>
</body></html>"""

html = TEMPLATE.replace("__CSS__", CSS).replace("__BODY__", html_body).replace("__META__", dm.meta_html("framer-invitation"))
pathlib.Path("/home/claude/invitation.html").write_text(html)
print("Invitation HTML written:", len(html), "chars")
