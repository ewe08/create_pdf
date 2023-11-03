# -*- coding: utf-8 -*-
import fitz

WIDTH = 1200
HEIGHT = 1700

doc = fitz.open()
page = doc.new_page(0, WIDTH, HEIGHT)

page_index = 0
rect = (0, 0, WIDTH, HEIGHT)
imgpath = 'background.png'
page = doc[page_index]
page.insert_image(rect, filename=imgpath)

page.insert_font(fontname='Roboto-Bold', fontfile='./fonts/Roboto-Bold.ttf')
shape = page.new_shape()
header = "                       Справка\nо принятии статьи к публикации"
shape.insert_text((450,200), header, fontname='Roboto-Bold', fontsize=24)
shape.commit()



doc.save('output.pdf')