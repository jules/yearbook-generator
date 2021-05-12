# Import stuff that we need
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib.colors import black, blue, Color
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER, TA_RIGHT

# Define distances / sizes
large_border_width = 2.023791 * cm
small_border_width = 1.354839 * cm
image_width_height = 4.970564 * cm
top_row_image_height = 22.698318 * cm
middle_row_image_height = 13.698575 * cm
bottom_row_image_height = 4.707298 * cm

# Define row and column coordinates
left_page_x_layout = [large_border_width, large_border_width + image_width_height + small_border_width, large_border_width + image_width_height*2 + small_border_width*2]
right_page_x_layout = [small_border_width, small_border_width*2 + image_width_height, small_border_width*3 + image_width_height*2]
page_y_layout = [top_row_image_height, middle_row_image_height, bottom_row_image_height]

# Register Fonts
pdfmetrics.registerFont(TTFont('Work-Sans-Bold', 'fonts/WorkSans-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Work-Sans-Medium-Italic', 'fonts/WorkSans-MediumItalic.ttf'))
pdfmetrics.registerFont(TTFont('Work-Sans-Regular', 'fonts/WorkSans-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Work-Sans-Light-Italic', 'fonts/WorkSans-LightItalic.ttf'))
pdfmetrics.registerFont(TTFont('Work-Sans-SemiBold', 'fonts/WorkSans-SemiBold.ttf'))
pdfmetrics.registerFont(TTFont('DM-Mono-Light', 'fonts/DMMono-Light.ttf'))

# Define our custom font colour
fontColour = Color(red=(17/255), green=(31/255), blue=(68/255))

# Fonts:
# Name - Work Sans Bold 36
# Job Title - Work Sans Medium Italic 36
# Core Degree - Work Sans Regular 36
# Quote - Work Sans Light Italic 36
# Page Number - Work Sans SemiBold 36
# Book / Category Label - DM Mono Light 36

# Creates our canvas
def init_pdf(filename, size):
    return Canvas(filename, pagesize = size)

# Draws a centered text string (one line)
def drawCentredText(canvas, font, size, colour, x, y, text):
    canvas.setFont(font, size)
    canvas.setFillColor(colour)
    canvas.drawCentredString(x, y, text)

# Draws a centered paragraph of defined width and height (multiple lines)
def draw_paragraph(canvas, msg, x, y, max_width, max_height):
    message_style = ParagraphStyle(name="CenterStyle", alignment=TA_CENTER, fontName="Work-Sans-Light-Italic", fontSize=9, textColor=fontColour)
    message = msg.replace('\n', '<br />')
    message = Paragraph(message, style=message_style)
    w, h = message.wrap(max_width, max_height)
    canvas.setFillColorRGB(0.066,0.121,0.266)
    message.drawOn(canvas, x, y - h)

# Draws a profile using given image, coordinates, sizing and text information
def draw_profile(canvas, image, name, job_title, core_degree, quote, x, y):
    canvas.drawImage(image, x, y, image_width_height, image_width_height)
    drawCentredText(canvas, 'Work-Sans-Bold', 9, fontColour, x + image_width_height/2, y-20, name)
    drawCentredText(canvas, 'Work-Sans-Medium-Italic', 9, fontColour, x + image_width_height/2, y-30, job_title)
    drawCentredText(canvas, 'Work-Sans-Regular', 9, fontColour, x + image_width_height/2, y-40, core_degree)
    draw_paragraph(canvas, quote, x, y - 41, image_width_height, top_row_image_height-bottom_row_image_height-image_width_height)

def draw_left_page(canvas, profiles):
    x_iteration = 0
    y_iteration = 0
    for profile in profiles:
        draw_profile(canvas, profile["image"], profile["name"], profile["core-degree"], profile["job-title"], profile["quote"], left_page_x_layout[x_iteration], page_y_layout[y_iteration])
        x_iteration = x_iteration + 1
        if x_iteration == 3:
            x_iteration = 0
            y_iteration = y_iteration + 1
        if y_iteration == 3:
            y_iteration = 0

def draw_right_page(canvas, profiles):
    x_iteration = 0
    y_iteration = 0
    for profile in profiles:
        draw_profile(canvas, profile["image"], profile["name"], profile["core-degree"], profile["job-title"], profile["quote"], right_page_x_layout[x_iteration], page_y_layout[y_iteration])
        x_iteration = x_iteration + 1
        if x_iteration == 3:
            x_iteration = 0
            y_iteration = y_iteration + 1
        if y_iteration == 3:
            y_iteration = 0

def save_pdf(canvas):
    canvas.save()

# # Top Row
#     canvas.drawImage('test_image.jpg', large_border_width, top_row_image_height, image_width_height, image_width_height)
#     drawCentredText('Work-Sans-Bold', 9, fontColour, large_border_width + image_width_height/2, top_row_image_height-20, "Insert Name Here")
#     drawCentredText('Work-Sans-Medium-Italic', 9, fontColour, large_border_width + image_width_height/2, top_row_image_height-30, "Insert Job Title Here")
#     drawCentredText('Work-Sans-Regular', 9, fontColour, large_border_width + image_width_height/2, top_row_image_height-40, "Insert Core Degree Here")
#     draw_paragraph('Here is my very long quote that i dont want to stretch out too far or else it will not look good', large_border_width, top_row_image_height - 42, image_width_height, top_row_image_height-bottom_row_image_height-image_width_height)
#
# canvas.drawImage('test_image.jpg', large_border_width + image_width_height + small_border_width, top_row_image_height, image_width_height, image_width_height)
# drawCentredText('Work-Sans-Bold', 9, fontColour, large_border_width + image_width_height + small_border_width + image_width_height/2, top_row_image_height-20, "Insert Name Here")
#
# canvas.drawImage('test_image.jpg', large_border_width + image_width_height*2 + small_border_width*2, top_row_image_height, image_width_height, image_width_height)
# drawCentredText('Work-Sans-Bold', 9, fontColour, large_border_width + image_width_height*2 + small_border_width*2 + image_width_height/2, top_row_image_height-20, "Insert Name Here")
#
# # Middle Row
# canvas.drawImage('test_image.jpg', large_border_width, middle_row_image_height, image_width_height, image_width_height)
# drawCentredText('Work-Sans-Bold', 9, fontColour, large_border_width + image_width_height/2, middle_row_image_height-20, "Insert Name Here")
#
#
# canvas.drawImage('test_image.jpg', large_border_width + image_width_height + small_border_width, middle_row_image_height, image_width_height, image_width_height)
# drawCentredText('Work-Sans-Bold', 9, fontColour, large_border_width + image_width_height + small_border_width + image_width_height/2, middle_row_image_height-20, "Insert Name Here")
#
# canvas.drawImage('test_image.jpg', large_border_width + image_width_height*2 + small_border_width*2, middle_row_image_height, image_width_height, image_width_height)
# drawCentredText('Work-Sans-Bold', 9, fontColour, large_border_width + image_width_height*2 + small_border_width*2 + image_width_height/2, middle_row_image_height-20, "Insert Name Here")
#
# # Bottom Row
# canvas.drawImage('test_image.jpg', large_border_width, bottom_row_image_height, image_width_height, image_width_height)
# drawCentredText('Work-Sans-Bold', 9, fontColour, large_border_width + image_width_height/2, bottom_row_image_height-20, "Insert Name Here")
#
# canvas.drawImage('test_image.jpg', large_border_width + image_width_height + small_border_width, bottom_row_image_height, image_width_height, image_width_height)
# drawCentredText('Work-Sans-Bold', 9, fontColour, large_border_width + image_width_height + small_border_width + image_width_height/2, bottom_row_image_height-20, "Insert Name Here")
#
# canvas.drawImage('test_image.jpg', large_border_width + image_width_height*2 + small_border_width*2, bottom_row_image_height, image_width_height, image_width_height)
# drawCentredText('Work-Sans-Bold', 9, fontColour, large_border_width + image_width_height*2 + small_border_width*2 + image_width_height/2, bottom_row_image_height-20, "Insert Name Here")
#
#
#
# #canvas.drawImage("test_image.jpg", 5*cm, 5*cm, 4*cm, 4*cm)
#
# #canvas.rotate(90)
# #canvas.setFillColorRGB(0,0,0.77)
# #canvas.drawString(0.3*cm,-1*cm,"Hello World")
#
#
# canvas.save()
