# Import stuff that we need
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.colors import black, blue

# Create the A4 canvas
canvas = Canvas("Test_File.pdf", pagesize = A4)

# Define distances / sizes
large_border_width = 2.023791 * cm
small_border_width = 1.354839 * cm
image_width_height = 4.970564 * cm
top_row_image_height = 22.698318 * cm
middle_row_image_height = 13.698575 * cm
bottom_row_image_height = 4.707298 * cm

# Register Fonts
pdfmetrics.registerFont(TTFont('Work-Sans-Bold', 'fonts/WorkSans-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Work-Sans-Medium-Italic', 'fonts/WorkSans-MediumItalic.ttf'))
pdfmetrics.registerFont(TTFont('Work-Sans-Regular', 'fonts/WorkSans-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Work-Sans-Light-Italic', 'fonts/WorkSans-LightItalic.ttf'))
pdfmetrics.registerFont(TTFont('Work-Sans-SemiBold', 'fonts/WorkSans-SemiBold.ttf'))
pdfmetrics.registerFont(TTFont('DM-Mono-Light', 'fonts/DMMono-Light.ttf'))

# Fonts:
# Name - Work Sans Bold 36
# Job Title - Work Sans Medium Italic 36
# Core Degree - Work Sans Regular 36
# Quote - Work Sans Light Italic 36
# Page Number - Work Sans SemiBold 36
# Book / Category Label - DM Mono Light 36

def createCentredText(font, size, colour, x, y, text):
    canvas.setFont(font, size)
    canvas.setFillColor(colour)
    canvas.drawCentredString(x, y, text)

# Top Row
canvas.drawImage('test_image.jpg', large_border_width, top_row_image_height, image_width_height, image_width_height)
createCentredText('Work-Sans-Bold', 9, black, large_border_width + image_width_height/2, top_row_image_height-20, "Insert Name Here")

canvas.drawImage('test_image.jpg', large_border_width + image_width_height + small_border_width, top_row_image_height, image_width_height, image_width_height)
createCentredText('Work-Sans-Bold', 9, black, large_border_width + image_width_height + small_border_width + image_width_height/2, top_row_image_height-20, "Insert Name Here")

canvas.drawImage('test_image.jpg', large_border_width + image_width_height*2 + small_border_width*2, top_row_image_height, image_width_height, image_width_height)
createCentredText('Work-Sans-Bold', 9, black, large_border_width + image_width_height*2 + small_border_width*2 + image_width_height/2, top_row_image_height-20, "Insert Name Here")

# Middle Row
canvas.drawImage('test_image.jpg', large_border_width, middle_row_image_height, image_width_height, image_width_height)
createCentredText('Work-Sans-Bold', 9, black, large_border_width + image_width_height/2, middle_row_image_height-20, "Insert Name Here")

canvas.drawImage('test_image.jpg', large_border_width + image_width_height + small_border_width, middle_row_image_height, image_width_height, image_width_height)
createCentredText('Work-Sans-Bold', 9, black, large_border_width + image_width_height + small_border_width + image_width_height/2, middle_row_image_height-20, "Insert Name Here")

canvas.drawImage('test_image.jpg', large_border_width + image_width_height*2 + small_border_width*2, middle_row_image_height, image_width_height, image_width_height)
createCentredText('Work-Sans-Bold', 9, black, large_border_width + image_width_height*2 + small_border_width*2 + image_width_height/2, middle_row_image_height-20, "Insert Name Here")

# Bottom Row
canvas.drawImage('test_image.jpg', large_border_width, bottom_row_image_height, image_width_height, image_width_height)
createCentredText('Work-Sans-Bold', 9, black, large_border_width + image_width_height/2, bottom_row_image_height-20, "Insert Name Here")

canvas.drawImage('test_image.jpg', large_border_width + image_width_height + small_border_width, bottom_row_image_height, image_width_height, image_width_height)
createCentredText('Work-Sans-Bold', 9, black, large_border_width + image_width_height + small_border_width + image_width_height/2, bottom_row_image_height-20, "Insert Name Here")

canvas.drawImage('test_image.jpg', large_border_width + image_width_height*2 + small_border_width*2, bottom_row_image_height, image_width_height, image_width_height)
createCentredText('Work-Sans-Bold', 9, black, large_border_width + image_width_height*2 + small_border_width*2 + image_width_height/2, bottom_row_image_height-20, "Insert Name Here")



#canvas.drawImage("test_image.jpg", 5*cm, 5*cm, 4*cm, 4*cm)

#canvas.rotate(90)
#canvas.setFillColorRGB(0,0,0.77)
#canvas.drawString(0.3*cm,-1*cm,"Hello World")


canvas.save()
