#!/usr/bin/env python
# -*- coding: utf8 -*-
# coding=utf-8

import os
from fpdf import FPDF
from selenium import webdriver

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
    pdf.add_font('DejaVu', '', 'Assets\DejaVuSansCondensed.ttf', uni=True)
    pdf.set_font('DejaVu', '', 70)

    pdf.write(8, reverse_text("איסוף עצמי       "))
    pdf.write(30, "\n")
    pdf.write(8, f"        #{orderNum}")
    pdf.write(40, "\n")
    pdf.set_font('DejaVu', '', 50)
    # pdf.write(8, reverse_text('א.א אחזקות ותחזוקה בע"מ'))
    # pdf.write(8, reverse_text('בר כהן'))
    pdf.write(8, f'{name}')
    # pdf.set_font('DejaVu', '', 70)
    pdf.write(30, "\n")
    pdf.write(8, f"{phone}")
    pdf.ln(8)

    pdf.output("local_pickup_sticker.pdf", 'F')

    def setup_browser():
        # option = webdriver.ChromeOptions()
        # option.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
        # option.binary_location = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'

        # from selenium.webdriver.support import ui

        # user_field = "idanb"
        chrome_ver = "89"  # 86/87/88
        # global chrome_ver
        # options = webdriver.ChromeOptions()  # פיתחת כרום דרך משתמש רגיל
        # options.add_argument(f"user-data-dir=C:\\Users\\{user_field.get()}\\AppData\\Local\\Google\\Chrome\\User Data")
        # browser = webdriver.Chrome(executable_path=fr"C:\Program Files (x86)\\chromedriver{chrome_ver}.exe", options=options)

        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=550,1080")
        args = ["hide_console", ]
        _browser = webdriver.Chrome(executable_path=fr"C:\Program Files (x86)\\chromedriver{chrome_ver}.exe",
                                    service_args=args,
                                    options=options)

        # browser = webdriver.Chrome(options=options)
        ChromeVer = _browser.capabilities['browserVersion']
        ChromeDriverVer = _browser.capabilities['chrome']['chromedriverVersion'].split(' ')[0]
        # print(ChromeVer)
        # print(ChromeDriverVer)
        print("ChromeVer " + ChromeVer[0:2])
        print("ChromeDriverVer " + ChromeDriverVer[0:2])
        # and if it doesn't exist, download it automatically,
        # then add chromedriver to path

        # chrome_ver = radioVar.get()  # 86/87/88
        # browser = webdriver.Chrome(executable_path=fr"C:\Program Files (x86)\chromedriver{chrome_ver}.exe")
        return _browser

    browser = setup_browser()
    pdf_path = os.path.abspath("local_pickup_sticker.pdf")

    browser.get(pdf_path)

## Example
# import time
# localPickupSticker(name="Dudi halevi", orderNum="28090", phone="0542323167")
# # localPickupSticker(name="ישראל ישראלי", orderNum="28090", phone="0542323167")
# time.sleep(7)
