from threading import Thread
from time import sleep
from selenium import webdriver


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

from tkinter import messagebox

messagebox.showinfo("נשלח בהצלחה", "(●'◡'●)  מייל נשלח בהצלחה ללקוח \n        סטטוס ההזמנה שונה להושלם")
sleep(0.12)
browser.quit()  # סוגר את הכרום
