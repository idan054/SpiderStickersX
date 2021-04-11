#!/usr/bin/env python
# -*- coding: utf8 -*-
# coding=utf-8

import os
from fpdf import FPDF
from selenium import webdriver
from Gadgets.setup_browser import setup_browser


def reverse_text(text):
    string_list = []
    for l in reversed(text):
        # print(l)
        string_list.append(l)
    listToStr = ''.join([str(elem) for elem in string_list])
    # print(listToStr)
    return listToStr

def localPickupSticker(name, orderNum, phone):
    if name.isascii(): # is English
        pass
    else: #When hebrew
        name = reverse_text(name)

    pdf = FPDF()
    pdf.add_page(('P', 'mm', (100, 150)))

    # Add a DejaVu Unicode font (uses UTF-8)
    # Supports more than 200 languages. For a coverage status see:
    # http://dejavu.svn.sourceforge.net/viewvc/dejavu/trunk/dejavu-fonts/langcover.txt

    # pdf.add_font('DejaVu', '', 'Assets\DejaVuSansCondensed.ttf', uni=True)
    pdf.add_font('DejaVu', '', 'C:\Windows\Fonts\Arial.ttf', uni=True)
    pdf.set_font('DejaVu', '', 40)

    pdf.write(8, reverse_text("איסוף עצמי"))
    pdf.write(20, "\n")
    pdf.write(8, f" #{orderNum}")
    pdf.write(20, "\n")
    pdf.set_font('DejaVu', '', 30)
    # pdf.write(8, reverse_text('א.א אחזקות ותחזוקה בע"מ'))
    # pdf.write(8, reverse_text('בר כהן'))
    pdf.write(8, f'{name}')
    # pdf.set_font('DejaVu', '', 70)
    pdf.write(15, "\n")
    pdf.write(8, f"{phone}")
    pdf.ln(8)

    pdf.output("local_pickup_sticker.pdf", 'F')

    browser = setup_browser()
    pdf_path = os.path.abspath("local_pickup_sticker.pdf")

    browser.get(pdf_path)

## Example
# import time
# localPickupSticker(name="Dudi halevi", orderNum="28090", phone="0542323167")
# # localPickupSticker(name="ישראל ישראלי", orderNum="28090", phone="0542323167")
# time.sleep(7)
