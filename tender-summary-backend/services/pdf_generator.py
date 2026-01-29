from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from textwrap import wrap

def generate_pdf(text, output_path):
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4

    x_margin = 40
    y_margin = 40
    max_width = width - 2 * x_margin

    y = height - y_margin

    for line in text.split("\n"):
        wrapped_lines = wrap(line, 90) if line else [""]

        for wline in wrapped_lines:
            if y < y_margin:
                c.showPage()
                y = height - y_margin

            c.drawString(x_margin, y, wline)
            y -= 14

    c.save()
