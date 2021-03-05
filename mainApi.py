import winsound
from selenium import webdriver
from Gadgets.multi_usage.bcolors import bcolors
from Scripts.A1_wooGetAPI import woocomarce_api
from Gadgets.multi_usage.goToTab import goToTab
from Scripts.A2_loginButik24 import loginButik24
from Scripts.A3_embedDetails import embed_details
from Scripts.A4_createSticker import create_sticker
from pynput.keyboard import Controller
from time import sleep
from tkinter import messagebox

keyboard = Controller()

global browser

## main based wordpress woocomarce API
def main_api(numOrder, numOfPacks):
    if numOrder == "":
        numOrder = 28020 # Some default

    global browser
    ## A0 setup browser & Gui
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

    print("woocomarce_api Start")

    ## Get details from API (V2.0 Update)
    first_name, last_name, address_1, street_num, street, city, \
    email, phone, high_quantity, deliveryNeeded, customer_note = woocomarce_api(numOrder=numOrder)

    print("woocomarce_api Done")

    finalOrderLink = f"https://www.spider3d.co.il/wp-admin/post.php?post={numOrder}&action=edit"
    print(finalOrderLink)
    print("Please Wait!")

    ## Check delivery method
    # (and stop running if delivery not needed)
    if not deliveryNeeded: # When deliveryNeeded = False
        print(f"{bcolors.Yellow}{bcolors.BOLD}"
              f' STOP! - עוצר. "איסוף עצמי" נמצא '
              f"{bcolors.Normal}")
        # messagebox.showinfo("איסוף עצמי", "¯\_(ツ)_/¯  אין צורך ביצירת משלוח, הזמנה זו היא איסוף עצמי")
        # from popupDesign import openNewWindow
        # openNewWindow(root)
        value = messagebox.askyesno(
            "איסוף עצמי", """.אין צורך ביצירת משלוח, הזמנה זו היא איסוף עצמי
                           .לחץ כן כדי להודיע ללקוח לאסוף
             ¯\_(ツ)_/¯ לחץ לא ליצירת משלוח בכל זאת """,
            default='yes')
        print(value)
        ## When delivery no needed.
        if value: # default is False - לא ליצור משלוח
            print("Fast return...")
            return phone
            # return "pickup"
            # return "browser", "finalOrderLink", "buyer_name", "butikTrackNumber", "butikBarCode", "buyer_phone"
    print(f"deliveryNeeded = {deliveryNeeded}")

    ## Check Quantity of items in order
    if high_quantity:
        print(f"{bcolors.Yellow}{bcolors.BOLD}"
              f"יש כפילות"
              f"{bcolors.Normal}")
        messagebox.showinfo("מוצר כפול", "╰(*°▽°*)╯  בהזמנה זו יש מוצרים בכמות גבוהה")
    print(f"high_quantity = {high_quantity}")

    ## Check customer note
    if customer_note != "":
        messagebox.showinfo("הערה מהלקוח", "ಠ_ಠ שים לב להערה של הלקוח")

    ## rework buyer & address details + CHECK FOR BUYER NOTES
    # rework API Values to the traditional (from v1.0)
    buyer_city = city
    buyer_street = street
    buyer_street_number = street_num
    buyer_name = f"{first_name} {last_name}"
    clean_address = address_1
    buyer_phone = phone
    buyer_email = email
    buyer_notes = customer_note

    browser = setup_browser()

    ## A2 Login Butik 24
    loginButik24(browser=browser)
    goToTab(browser=browser, tabURL="https://members.lionwheel.com/tasks/new?locale=he")

    ## A3 Embed buyer details on order page
    # packNum = packNum.get()
    embed_details(browser, buyer_city, buyer_street
                  , buyer_street_number, buyer_name,
                  clean_address, buyer_phone, buyer_email,
                  buyer_notes, numOrder, numOfPacks)

    ## A4 Create delivery and redirect to sticker Tab
    # input("Make a sticker??") # ע"מ למנוע יצירת מדבקות לבדיקות כשאין צורך
    butikTrackNumber, butikBarCode = create_sticker(browser=browser)


    winsound.Beep(2000, 150)
    winsound.Beep(1500, 150)
    browser.execute_script('window.print();')
    sleep(0.15)
    winsound.Beep(800, 150)
    winsound.Beep(800, 150)
    sleep(0.27)
    winsound.Beep(1400, 150)
    winsound.Beep(1400, 150)
    # Press and release space
    # keyboard.press(Key.enter)
    # keyboard.release(Key.enter)

    return browser, finalOrderLink, buyer_name, butikTrackNumber, butikBarCode, buyer_phone

# if __name__ == '__main__':
#     main()
