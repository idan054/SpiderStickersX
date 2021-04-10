# -*- coding: utf-8 -*-


from reportlab.lib.colors import blue, black
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch, cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas

from selenium import webdriver


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

# canvas.showPage()
# Save the PDF file
canvas.save()

import os
# os.system('test.pdf')

# import webbrowser
# webbrowser.open(r'file:///test.pdf')

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
pdf_path = os.path.abspath("test.pdf")
browser.get(pdf_path)

