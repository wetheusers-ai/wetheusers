import re, markdown, pathlib
import sys; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); import docmeta as dm

CSS = """
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; }
body { font-family: "Charter","Bitstream Charter","Georgia","DejaVu Serif",serif; font-size: 11.6pt; line-height: 1.62; color: #1c1c1c; margin: 0; }
.docheader { text-align: center; padding-top: 6mm; margin-bottom: 9mm; }
.docheader .kicker { font-family: "DejaVu Sans",sans-serif; text-transform: uppercase; letter-spacing: 0.34em; font-size: 9.5pt; color: #6b7280; margin-bottom: 9mm; }
.docheader .title { font-size: 43pt; line-height: 1.05; margin: 0 auto; color: #1b2a4a; font-weight: 700; max-width: 150mm; }
.docheader .drule { width: 64px; height: 3px; background: #b08d3a; margin: 8mm auto 6.5mm auto; }
.docheader .subtitle { font-size: 13pt; font-style: italic; color: #333; margin: 0 auto 4mm auto; max-width: 154mm; }
.docheader .meta { font-size: 9.5pt; font-style: italic; color: #777; }
main { max-width: 172mm; margin: 0 auto; }
h2 { font-size: 15pt; color: #1b2a4a; font-weight: 700; margin: 1.95em 0 0.5em 0; page-break-after: avoid; line-height: 1.25; }
p { margin: 0 0 0.9em 0; }
strong { font-weight: 700; color: #1b2a4a; }
em { font-style: italic; }
a { color: #1b2a4a; text-decoration: none; }
hr { border: 0; height: 2px; width: 64px; background: #d8c79a; margin: 2.2em auto; }
ol, ul { margin: 0.2em 0 1.0em 0; padding-left: 1.45em; }
li { margin: 0 0 0.45em 0; padding-left: 0.15em; }
li strong { color: #1b2a4a; }
.note-aside { font-size: 10.2pt; color: #6b6b6b; font-style: italic; background: #faf7ef; border-left: 3px solid #d8c79a; padding: 0.7em 0.9em; margin: 0 0 1.4em 0; line-height: 1.5; }
.note-aside em { font-style: italic; }
.signoff { margin-top: 1.3em; }
"""

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><style>__CSS__</style></head>
<body>
<section class="docheader">
  <div class="kicker">We the Users</div>
  <div class="title">__TITLE__</div>
  <div class="drule"></div>
  __SUBOPT__
  __METAOPT__
</section>
<main>
__BODY__
</main>
</body></html>"""


def strip_h1(md_text):
    lines = md_text.split("\n")
    out, dropped = [], False
    for ln in lines:
        if not dropped and ln.startswith("# "):
            dropped = True
            continue
        out.append(ln)
    return "\n".join(out).strip()


def render(src_path, title, subtitle, out_html, key, second_ol_start=None, first_para_aside=False):
    md_text = pathlib.Path(src_path).read_text()
    body_md = strip_h1(md_text)
    html_body = markdown.markdown(body_md, extensions=['extra', 'smarty', 'sane_lists'], output_format='html5')

    # Preserve an explicit start number on the second ordered list (the 4-6 sequence).
    if second_ol_start:
        idxs = [m.start() for m in re.finditer(r'<ol(?:\s[^>]*)?>', html_body)]
        if len(idxs) >= 2:
            m2 = re.match(r'<ol(?:\s[^>]*)?>', html_body[idxs[1]:])
            tag = m2.group(0)
            if 'start=' not in tag:
                html_body = html_body[:idxs[1]] + tag[:-1] + f' start="{second_ol_start}">' + html_body[idxs[1] + len(tag):]

    # Style the leading instruction paragraph (the "before sending" note) as a muted aside.
    if first_para_aside:
        html_body = re.sub(r'^<p>(.*?)</p>', r'<div class="note-aside">\1</div>', html_body, count=1, flags=re.S)

    # Put the signature block (last paragraph) on its own lines.
    html_body = re.sub(r'<p>(\[Your name\][^<]*)</p>\s*$',
                       lambda m: '<p class="signoff">' + m.group(1).replace("\n", "<br>") + '</p>',
                       html_body, flags=re.S)

    subopt = f'<div class="subtitle">{subtitle}</div>' if subtitle else ''
    html = (TEMPLATE
            .replace("__CSS__", CSS)
            .replace("__TITLE__", title)
            .replace("__SUBOPT__", subopt)
            .replace("__METAOPT__", f'<div class="meta">{dm.meta_html(key)}</div>')
            .replace("__BODY__", html_body))
    pathlib.Path(out_html).write_text(html)
    print("HTML written:", out_html, len(html), "chars")


render("/home/claude/wetheusers/docs/outreach/packet-start-here.md",
       "Start here", "", "/home/claude/starthere.html", "packet-start-here", second_ol_start=4)

render("/home/claude/wetheusers/docs/outreach/cover-note.md",
       "Cover note", "Email template &mdash; personalize before sending",
       "/home/claude/covernote.html", "cover-note", first_para_aside=True)
