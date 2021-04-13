#!/usr/bin/env python
# -*- coding: utf8 -*-
# coding=utf-8
import datetime
import os
from fpdf import FPDF
from selenium import webdriver
from Gadgets.setup_browser import setup_browser
import requests
from requests.structures import CaseInsensitiveDict

import time


def reverse_text(text):
    if text.isascii(): # in English OR Numbers
        return text
    else:
        string_list = []
        for l in reversed(text):
            # print(l)
            string_list.append(l)
        listToStr = ''.join([str(elem) for elem in string_list])
        # print(listToStr)
        return listToStr

# Get payment option only
def woocomarce_api_mini(numOrder):
    url = f"https://spider3d.co.il/wp-json/wc/v3/orders/{numOrder}"

    headers = CaseInsensitiveDict()
    headers["Authorization"] = \
        "Basic Y2tfMzAyZWJkYmQ4OTNjNzU2YTFlOTlmZjhlZmNjMzZiYjYzNWZjNDRjNzpjc19lMTUyMTc0MWJlNDYzMWZjMzljMTQyNzUwZDg0YmU2YTJiYWVlMWIx"

    resp = requests.get(url, headers=headers)
    # print(resp.status_code)

    order_details = resp.json()

    # print(order_details)

    def try_get_item(json_path):
        try:
            item = json_path
            return item
        except ValueError as e:
            e = str(e)
            print("just_try() Error:")
            print(e)
            item = ""
            return item

    payment_method = try_get_item(order_details["payment_method_title"])
    print("payment_method is ", payment_method)

    return payment_method

def localPickupSticker(name, orderNum, phone):

    pdf = FPDF()
    pdf.add_page(('P', 'mm', (100, 150)))

    # Add a DejaVu Unicode font (uses UTF-8)
    # Supports more than 200 languages. For a coverage status see:
    # http://dejavu.svn.sourceforge.net/viewvc/dejavu/trunk/dejavu-fonts/langcover.txt

    # pdf.add_font('DejaVu', '', 'Assets\DejaVuSansCondensed.ttf', uni=True)
    pdf.add_font('DejaVu', '', 'C:\Windows\Fonts\Arial.ttf', uni=True)
    pdf.set_font('DejaVu', '', 40)

    pdf.write(40, "\n")
    pdf.write(8, reverse_text("איסוף עצמי"))
    pdf.write(20, "\n")
    pdf.write(8, f" #{orderNum}")
    pdf.write(16, "\n")
    pdf.set_font('DejaVu', '', 30)
    # pdf.write(8, reverse_text('א.א אחזקות ותחזוקה בע"מ'))
    # pdf.write(8, reverse_text('בר כהן'))
    pdf.write(8, f'{reverse_text(name)}')
    # pdf.set_font('DejaVu', '', 70)
    pdf.write(10, "\n")
    pdf.write(8, f"{phone}")

    current_time = datetime.datetime.now()
    # print ("Current date and time : ")
    print(current_time.strftime("%d/%m/%Y %H:%M:%S"))
    current_time = current_time.strftime("%d/%m/%Y %H:%M:%S")

    # Get payment option only
    payment_method = woocomarce_api_mini(orderNum)

    pdf.write(10, "\n")
    pdf.write(8, f"{reverse_text(payment_method)}")
    pdf.ln(8)

    pdf.write(10, "\n")
    pdf.write(8, f"{current_time}")
    pdf.ln(8)

    pdf.output("local_pickup_sticker.pdf", 'F')

    browser = setup_browser()
    pdf_path = os.path.abspath("local_pickup_sticker.pdf")

    browser.get(pdf_path)
    return browser

# Example
import time
# woocomarce_api_mini(28021)
# localPickupSticker(name="ישראל ישראלי", orderNum="28021", phone="0542323167")
# time.sleep(20)
