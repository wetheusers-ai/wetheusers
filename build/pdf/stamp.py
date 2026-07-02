import io
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas

base = PdfReader("/home/claude/base.pdf")
N = len(base.pages)
writer = PdfWriter()
for i, page in enumerate(base.pages):
    if i > 0:  # leave the title page clean
        w = float(page.mediabox.width); h = float(page.mediabox.height)
        buf = io.BytesIO()
        c = canvas.Canvas(buf, pagesize=(w, h))
        c.setFont("Times-Roman", 9)
        c.setFillColorRGB(0.60, 0.63, 0.67)
        c.drawCentredString(w/2.0, 30, f"{i+1}  /  {N}")
        c.save(); buf.seek(0)
        page.merge_page(PdfReader(buf).pages[0])
    writer.add_page(page)

# Document metadata
writer.add_metadata({
    "/Title": "We the Users — Founding Brief",
    "/Author": "We the Users",
    "/Subject": "Founding brief / project charter",
    "/Creator": "We the Users",
})
with open("/mnt/user-data/outputs/We-the-Users-Founding-Brief.pdf", "wb") as f:
    writer.write(f)
print(f"stamped {N} pages; title page left clean")
