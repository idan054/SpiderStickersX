# -*- coding: utf-8 -*-


from reportlab.lib.colors import blue, black
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch, cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas

canvas = Canvas("test.pdf", pagesize=(400.0 * 0.7, 500.0 * 0.7))

pdfmetrics.registerFont(TTFont('Hebrew', 'Arial.ttf'))

# Set font to Times New Roman with 12-point size
canvas.setFont("Helvetica", 18)

# Draw blue text one inch from the left and ten
# inches from the bottom
canvas.setFillColor(blue)
canvas.drawString(20, 300, "איסוף עצמי")
canvas.setFillColor(black)
canvas.drawString(20, 320, "הזמנה #12345")

# Save the PDF file
canvas.save()
canvas.showPage()
