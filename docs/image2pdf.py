from PIL import Image
from reportlab.pdfgen import canvas

# Load the image
image = Image.open("tese3 001 compressed.png")

# Get image dimensions
width, height = image.size

# Create a PDF with the same dimensions as the image
c = canvas.Canvas("declaracao_de_honra.pdf", pagesize=(width, height))
c.drawImage("tese3 001 compressed.png", 0, 0, width, height)
c.save()