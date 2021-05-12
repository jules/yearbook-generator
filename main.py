from pdf_funcs import *

profiles = [ \
    {"name": "name1", "core-degree": "degree-1", "job-title": "job-title1", "quote": "quote1", "image": "test_image.jpg"}, \
    {"name": "name2", "core-degree": "degree-2", "job-title": "job-title2", "quote": "quote2", "image": "test_image.jpg"}, \
    {"name": "name3", "core-degree": "degree-3", "job-title": "job-title3", "quote": "quote3", "image": "test_image.jpg"}, \
    {"name": "name4", "core-degree": "degree-4", "job-title": "job-title4", "quote": "quote4", "image": "test_image.jpg"}, \
    {"name": "name5", "core-degree": "degree-5", "job-title": "job-title5", "quote": "quote5", "image": "test_image.jpg"}, \
    {"name": "name6", "core-degree": "degree-6", "job-title": "job-title6", "quote": "quote6", "image": "test_image.jpg"}, \
    {"name": "name7", "core-degree": "degree-7", "job-title": "job-title7", "quote": "quote7", "image": "test_image.jpg"}, \
    {"name": "name8", "core-degree": "degree-8", "job-title": "job-title8", "quote": "quote8", "image": "test_image.jpg"}, \
    {"name": "name9", "core-degree": "degree-9", "job-title": "job-title9", "quote": "quote9", "image": "test_image.jpg"}  \
]

canvas = init_pdf("Yearbook.pdf", A4)
draw_left_page(canvas, profiles)
save_pdf(canvas)
