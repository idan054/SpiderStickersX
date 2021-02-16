import winsound
from time import sleep
from tkinter import *
from tkinter import messagebox, ttk
import tkinter as tk
import keyboard
from selenium import webdriver
from Gadgets.bcolors import bcolors
from Scripts.A1_loginWordpress import loginWordpress
from Scripts.A2_goToTab import goToTab
from Scripts.A3_deliveryMethod import deliveryMethod_checker
from Scripts.A4_quantityChecker import quantityChecker
from Scripts.A5_defineDetails import define_address_details
from Scripts.A6_loginButik24 import loginButik24
from Scripts.A7_embedDetails import embed_details
from Scripts.A8_createDelivery import create_delivery, goToSticker
from selenium.webdriver.common.keys import Keys

global browser

def main(numOrder, numOfPacks):
    global browser
    ## 0 setup browser & Gui
    print(f"{bcolors.Yellow}{bcolors.BOLD}Start{bcolors.Normal}")
    def setup_browser():
        # option = webdriver.ChromeOptions()
        # option.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
        # option.binary_location = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'

        # from selenium.webdriver.support import ui

        # user_field = "idanb"
        chrome_ver = "87"  # 86/87/88
        # global chrome_ver
        # options = webdriver.ChromeOptions()  # פיתחת כרום דרך משתמש רגיל
        # options.add_argument(f"user-data-dir=C:\\Users\\{user_field.get()}\\AppData\\Local\\Google\\Chrome\\User Data")
        # browser = webdriver.Chrome(executable_path=fr"C:\Program Files (x86)\\chromedriver{chrome_ver}.exe", options=options)

        args = ["hide_console", ]
        _browser = webdriver.Chrome(executable_path=fr"C:\Program Files (x86)\\chromedriver{chrome_ver}.exe",
                                   service_args=args)

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

    ## 1 Login Wordpress
    loginWordpress(browser=browser)

    ## 2 Go to order page
    # numOrder = orderLinkField.get()
    # numOrder = "27695" # איסוף עצמי
    # numOrder = "25560" # Eyal Biton הזמנה עבור
    # numOrder = "27692" # כולל הערות + כמות גבוהה
    finalOrderLink = f"https://www.spider3d.co.il/wp-admin/post.php?post={numOrder}&action=edit"
    goToTab(tabURL=finalOrderLink, browser=browser)
    print(finalOrderLink)
    print("Please Wait!")

    ## 3 Check delivery method
    # (and stop running if delivery not needed)
    deliveryMethod = browser.find_element_by_id("order_shipping_line_items").text
    deliveryNeeded = deliveryMethod_checker(deliveryMethod=deliveryMethod)
    if not deliveryNeeded: # When deliveryNeeded = False
        browser.quit()  # סוגר את הכרום
        return
    print(f"deliveryNeeded  = {deliveryNeeded}")

    ## 4 Check Quantity of items in order
    # (and alert if quantity > 1)
    quantityChecker(browser=browser)

    ## 5 Get buyer & address details + CHECK FOR BUYER NOTES
    buyer_city, buyer_street ,buyer_street_number,\
        buyer_name, clean_address ,buyer_phone, buyer_email,\
        buyer_notes = define_address_details(browser=browser)

    ## 6 Login Butik 24
    loginButik24(browser=browser)
    goToTab(browser=browser, tabURL="https://members.lionwheel.com/tasks/new?locale=he")

    ## 7 Embed buyer details on order page
    # packNum = packNum.get()
    embed_details(browser, buyer_city, buyer_street
                  , buyer_street_number, buyer_name,
                  clean_address, buyer_phone, buyer_email,
                  buyer_notes, numOrder, numOfPacks)

    ## 8 Create delivery and redirect to sticker Tab
    # input("Make a sticker??") # ע"מ למנוע יצירת מדבקות לבדיקות כשאין צורך
    # (and get butikTrackNumber for tracking mail)
    butikTrackNumber = create_delivery(browser=browser)
    goToSticker(browser=browser)

    winsound.Beep(2000, 150)
    winsound.Beep(1500, 150)
    browser.execute_script('window.print();')
    sleep(0.15)
    winsound.Beep(800, 150)
    winsound.Beep(800, 150)
    sleep(0.27)
    winsound.Beep(1400, 150)
    winsound.Beep(1400, 150)

    return browser, finalOrderLink, buyer_name, butikTrackNumber # Needs to send the tracking mail

# if __name__ == '__main__':
#     main()
