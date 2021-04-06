from tkinter import messagebox

from selenium import webdriver
from color_printer import *


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

    def get_web_Chromedriver():

        ## Get chrome ver
        try:
            webdriver.Chrome()
        except Exception as e:
            e = str(e)
            e = e.split(" ")
            printGreen(e[16])
            current_chrome_ver = e[16].split(".")
            current_chrome_ver = current_chrome_ver[0]
            messagebox.showinfo("chromedriver update", f'נא לעדכן לדרייבר {current_chrome_ver}.. בהתבסס האתר www.chromedriver.chromium.org')



            ## Download chromedriver zip based chrome ver
            import requests

            url = 'f"https://chromedriver.storage.googleapis.com/{e[16]}/chromedriver_win.zip'
            r = requests.get(url, allow_redirects=True)

            open('facebook.ico', 'wb').write(r.content)


            import zipfile
            with zipfile.ZipFile(f"https://chromedriver.storage.googleapis.com/{e[16]}/chromedriver_linux64.zip", 'r') as zip_ref:
                zip_ref.extractall()



    get_web_Chromedriver()

    breakpoint()



    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=550,1080")
    # args = ["hide_console", ]
    _browser = webdriver.Chrome(executable_path=fr"C:\Program Files (x86)\\chromedriver{chrome_ver}.exe",
                                # service_args=args,
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

# region based chromedriver_autoinstaller
# from selenium import webdriver
# import chromedriver_autoinstaller
#
#
# chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
#                                       # and if it doesn't exist, download it automatically,
#                                       # then add chromedriver to path
#
# options =webdriver.ChromeOptions()
# options.add_argument("--window-size=550,1080")
# args = ["hide_console", ]
# _browser = webdriver.Chrome(
#                             service_args=args,
#                             options=options)
#
# ChromeVer = _browser.capabilities['browserVersion']
# ChromeDriverVer = _browser.capabilities['chrome']['chromedriverVersion'].split(' ')[0]
# print("ChromeVer " + ChromeVer[0:2])
# print("ChromeDriverVer " + ChromeDriverVer[0:2])
#
# # driver = webdriver.Chrome(options=options)
# # driver.get("http://www.python.org")
# # assert "Python" in driver.title
# endregion based chromedriver_autoinstaller