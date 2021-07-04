# import chromedriver_autoinstaller
import winsound
from time import sleep
from tkinter import messagebox

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from Gadgets.multi_usage.bcolors import bcolors
from Gadgets.multi_usage.goToTab import goToTab
from Scripts.A2_loginButik24 import loginButik24
from Scripts.A3_embedDetails import embed_details
from Scripts.A4_createSticker import create_sticker


def string_cleaner(text):
    text = ' '.join([str(elem) for elem in text]) # String 2 str

    # Clean street to hebrew only (no numbers)
    alfabet_list = ["א", "ב", "ג", "ד", "ה", "ו", "ז", "ח", "ט", "י", "כ", "ל", "מ", "נ", "ס", "ע", "פ", "צ",
                    "ק", "ר", "ש",
                    "ת", " ", "ך", "ם", "ן", "ף", "צ", "'"]
    heb_street = []

    for l in text:
        if l in alfabet_list:
            heb_street.append(l)
    heb_street = ''.join([str(elem) for elem in heb_street])

    return heb_street[:-1] # to remove final no need space


# x = string_cleaner("חיפה 3292212")
# x = string_cleaner(['גוטל', 'לויון', '12'])
# print(x)



global buyer_name, buyer_phone, buyer_email, street, street_number, city, zip_city, local_pickup, full_cityList, full_streetList, heb_city, heb_street

def makeSticker(order_id, pack_num, browser):
    # makeSticker(100012222 , 1, browser)
    # order_id = "100012222"
    # pack_num = 1
    # browser = browser
    global buyer_name, buyer_phone, buyer_email, street, street_number, city, zip_city, local_pickup, full_cityList, full_streetList, heb_city, heb_street

    winsound.Beep(2000, 110)
    winsound.Beep(1000, 100)

    # Will be tkinter input
    # order_id = input("Insert order number:") or "011086"
    if len(order_id) > 6:
        order_id = order_id[1:]
    print(order_id)

    print("order_id is " + str(order_id))
    # order_id = "11065"     # 100011087 ↓
    # if order_id[0] == "0": # 011087 - 22 = 11065
    order_id = int(order_id) - 22
    print(order_id)

    def login_magento():
        browser.switch_to.window(browser.window_handles[0])  # עובר לטאב פעיל כדי למנוע שגיאה במקרה שהטאב הפעיל נסגר

        ## לא ניתן להגיע לעמוד הזמנה ישירות
        browser.get("https://topirzul.co.il/admin-kivi")  # התחברות
        # admin
        # harel1234

        user_wordpress_field = browser.find_element_by_id("username")
        user_wordpress_field.send_keys("admin")

        pass_field = browser.find_element_by_id("login")
        pass_field.send_keys("harel1234")
        sleep(0.3)

        sleep(0.3)
        browser.find_element_by_class_name("form-button").click()
    login_magento()

    def get_data():
        global buyer_name, buyer_phone, buyer_email, street, street_number, city, zip_city, local_pickup, full_cityList, full_streetList, heb_city, heb_street
        goToTab(browser=browser, tabURL=f"https://topirzul.co.il/index.php/admin-kivi/sales_order/view/order_id/{order_id}/key/9d413f90f50ef2cc25fee3068e034f87/")

        # Just Color
        print(f"{bcolors.Blue}{bcolors.BOLD}")

        # איסוף עצמי
        local_pickup = browser.find_element_by_xpath('//*[@id="sales_order_view_tabs_order_info_content"]/div[1]/div[9]').text
        if "איסוף עצמי" in local_pickup:
            local_pickup = True
            print(f"local_pickup is {local_pickup}")
            messagebox.showinfo("איסוף עצמי", "¯\_(ツ)_/¯  אין צורך ביצירת משלוח, הזמנה זו היא איסוף עצמי")
            # exit()
        else:
            local_pickup = False
            print(f"local_pickup is {local_pickup}")
        # print(type(local_pickup))

        topRight_box = browser.find_element_by_class_name("hor-scroll").text
        topRight_boxList = topRight_box.split("\n")

        buyer_name = topRight_boxList[1].replace("שם לקוח ", "")
        print("buyer_name")
        print(buyer_name)

        buyer_email = topRight_boxList[3].replace("דואר אלקטרוני ", "")
        print("buyer_email")
        print(buyer_email)

        middleRight_box = browser.find_element_by_xpath('//*[@id="sales_order_view_tabs_order_info_content"]/div[1]/div[6]').text
        middleRight_boxList = middleRight_box.split("\n")
        # print(middleRight_boxList)

        full_streetList = middleRight_boxList[3].split(" ")
        street = full_streetList[0:-1]
        # print(f"X {street} X")
        print(f"X {full_streetList} X")
        street_number = full_streetList[-1]
        print("*full_streetList")
        print(*full_streetList)

        # heb_street = string_cleaner(full_streetList)
        # print(heb_street)

        streetAndNumber = ' '.join([str(elem) for elem in full_streetList])
        print(streetAndNumber)

        full_cityList = middleRight_boxList[4].split(",")
        city = full_cityList[0]
        zip_city = full_cityList[1].replace(" ","")
        print("*full_cityList")
        print(*full_cityList)

        heb_city = string_cleaner(full_cityList)
        print(heb_city)

        buyer_phone = middleRight_boxList[6].replace("T: ","")
        print("buyer_phone")
        print(buyer_phone)

        ## high_quantity_Checker (def..)
        print(f"{bcolors.Yellow}{bcolors.BOLD}")

        products_box = browser.find_element_by_xpath('//*[@id="sales_order_view_tabs_order_info_content"]/div[1]/div[13]/div').text
        products_box = products_box.split("\n") # List
        # print(*products_box)
        print("==================")

        quantity_items = []
        for item in products_box:
            if "הוזמן " in item and "₪" not in item:
                print(f"עמודת כמות (חשודה) זוהתה")
                quantity_items.append(item)

        print(quantity_items)

        whileIndex = 1
        high_quantity = False
        while whileIndex != 100:
            whileIndex += 1 # Start from 2 (high_quantity_Checker)
            # print("whileIndex is " + str(whileIndex))
            if str(whileIndex) in str(quantity_items):
                print("כמות גבוהה זוהתה!")
                # messagebox.showinfo("מוצר כפול", "╰(*°▽°*)╯  בהזמנה זו יש מוצרים בכמות גבוהה")
                high_quantity = True
                break
        if not high_quantity: print("לא זוהתה כמות גבוה.")


        # Cancel Color
        print(f"{bcolors.Normal}")

        return streetAndNumber
    streetAndNumber = get_data()
    # print(buyer_name, buyer_phone, buyer_email, street, street_number, city, zip_city, local_pickup)

    def complete_order():

        def button_finder(class_name, text):
            forIndex = 0
            for button in class_name:
                if button.text == text:
                    print(button.text)
                    break

                forIndex += 1
            print(forIndex)
            return forIndex


        try:
            # selenium python to scroll to the top of a page
            browser.execute_script("window.scrollTo(0, 0);")

            # כפתור שלח
            # browser.get(f"https://topirzul.co.il/index.php/admin-kivi/sales_order_shipment/start/order_id/{order_id}/key/8744d736269dab4be03588d7e5ca81eb/")
            # send_button = browser.find_element_by_id("id_3f1f84cbb95d0d7c992ef1d38f6977ef")
            # send_button = main_buttons_class.find_element_by_link_text('שלח')
            # send_button = browser.find_element_by_xpath('//*[@id="id_10fab9ed7d8866cd4b002073b940e907"]')

            send_buttons_page = browser.find_elements_by_tag_name('button')

            send_btn_num = button_finder(send_buttons_page, "שלח")
            print(send_buttons_page[send_btn_num].text)
            send_buttons_page[send_btn_num].click()


            ## PART 2
            # selenium python to scroll to the bottom of a page
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # כפתור צור תעודת משלוח
            # shipping_diploma = browser.find_element_by_id("id_71fa958dd1c14ea18c5180b3c59e2d24")
            # shipping_diploma = browser.find_element_by_xpath('//*[@id="id_da5c630b4cbd38ab989dfe0b0fad2419"]')
            # shipping_diploma.click()
            shipping_certificate_buttons_page = browser.find_elements_by_tag_name('button')
            # forIndex = 0
            # for i in shipping_certificate_buttons_page:
            #     print(i.text)
            #     forIndex += 1
            #     print(forIndex)
            shipping_certificate_btn_num = button_finder(shipping_certificate_buttons_page, "שלח תעודת משלוח")

            print(shipping_certificate_buttons_page[shipping_certificate_btn_num].text)
            shipping_certificate_buttons_page[shipping_certificate_btn_num].click()

        except:
            print("כפתור שלח נכשל.")
            print("כפתור בעמוד צור תעודת משלוח נכשל.")


        try:
            # selenium python to scroll to the top of a page
            browser.execute_script("window.scrollTo(0, 0);")

            # כפתור חשבונית
            # invoice_button = browser.find_element_by_id("id_41f5b1a3fd3c1957e07f90efa580c832")
            # invoice_button = browser.find_element_by_xpath('//*[@id="id_91193f552988454abbb8c6d87379c574"]')
            # invoice_button.click()
            invoice_buttons_page = browser.find_elements_by_tag_name('button')
            # forIndex = 0
            # for i in invoice_buttons_page:
            #     print(i.text)
            #     forIndex += 1
            #     print(forIndex)
            invoice_btn_num = button_finder(invoice_buttons_page, "חשבונית")
            print(invoice_buttons_page[invoice_btn_num].text)
            invoice_buttons_page[invoice_btn_num].click()

            ## PART 2
            # selenium python to scroll to the bottom of a page
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # כפתור שלח חשבונית
            # send_invoice = browser.find_element_by_id("id_256d34c521da6c9d5bb01b8dd42a6a1e""")
            # send_invoice = browser.find_element_by_xpath('//*[@id="id_2da4ff3917536565f94d527ed3a666b5"]')
            # send_invoice.click()
            send_invoice_buttons_page = browser.find_elements_by_tag_name('button')
            # forIndex = 0
            # for i in send_invoice_buttons_page:
            #     print(i.text)
            #     forIndex += 1
            #     print(forIndex)
            send_invoice_btn_num = button_finder(send_invoice_buttons_page, "שלח חשבונית")
            print(send_invoice_buttons_page[send_invoice_btn_num].text)
            send_invoice_buttons_page[send_invoice_btn_num].click()

        except:
            print("כפתור חשבונית נכשל.")
            print("כפתור בעמוד שלח חשבונית נכשל.")

    # complete_order func in try to enable "Make sticker" Also to not "processing" orders
    try: complete_order()
    except: print("Change status to complete not available!")

    def login_ydm():
        browser.switch_to.window(browser.window_handles[0])  # עובר לטאב פעיל כדי למנוע שגיאה במקרה שהטאב הפעיל נסגר

        browser.get("http://run.ydm.co.il/RunCom.Server/Request.aspx?APPNAME=run&PRGNAME=call_knisa")  # התחברות
        # הראל ביטון
        # הראל ביטון

        user_field = browser.find_element_by_id("run_user")
        user_field.send_keys("הראל ביטון")

        pass_field = browser.find_element_by_name("run_pass")
        pass_field.send_keys("הראל ביטון")
        sleep(0.3)

        browser.find_element_by_id("btnNext1").click() # login button
        sleep(0.3)

    def embed_data():
        browser.get("http://run.ydm.co.il/RunCom.Server/Request.aspx?APPNAME=run&PRGNAME=create_ship&ARGUMENTS=-N5520433,-N2859,-A%EB%E5%EC%ED,-A01/04/21,-A10,-A30")
        sleep(0.3)

        try: # Better way to get ri of alert (and maybe to print): https://www.guru99.com/alert-popup-handling-selenium.html
            page_body = browser.find_element_by_tag_name("body")
        except:
            print("Body not found, Alert dismiss!")

        fullname_field = browser.find_element_by_name("yaad")
        fullname_field.send_keys(buyer_name)

        packs_field = browser.find_element_by_name("arizot_haloch")
        packs_field.clear()
        packs_field.send_keys(pack_num)

        phone_field = browser.find_element_by_name("yaad_tl")
        phone_field.send_keys(buyer_phone)

        # heb_city = string Cleaner.string_cleaner(full_cityList)
        # print("A", heb_city)
        # heb_city = stringCleaner.string_cleaner(city)
        # print("B", heb_city)
        # heb_street = stringCleaner.string_cleaner(full_streetList)
        # print("A", heb_street)
        # heb_street = stringCleaner.string_cleaner(street)
        # print("B", heb_street)

        city_field = browser.find_element_by_name("yaad_city_name")
        city_field.send_keys(heb_city)
        sleep(0.3)
        city_field.send_keys(Keys.DOWN)  # Easy select from list
        city_field.send_keys(Keys.ENTER)

        try:
            print("Try")
            street_field = browser.find_element_by_name("yaad_street_name")
            # street_field.send_keys(heb_street)
            street_field.send_keys("ללא רחוב")
        except: # Add street from list again
            print("Except")
            city_field.clear()
            city_field.send_keys(heb_city)
            sleep(1.5)
            city_field.send_keys(Keys.DOWN)  # Easy select from list
            sleep(1.5)
            city_field.send_keys(Keys.ENTER)

            street_field = browser.find_element_by_name("yaad_street_name")
            # street_field.send_keys(heb_street)
            street_field.send_keys("ללא רחוב")
        # sleep(1.5)
        # street_field.send_keys(Keys.ENTER)
        sleep(1.5)
        street_field.send_keys(Keys.DOWN)  # Easy select from list
        sleep(1.5)
        street_field.send_keys(Keys.ENTER)

        house_field = browser.find_element_by_name("yaad_house")
        house_field.send_keys("0")

        # Notes
        notes_field = browser.find_element_by_name("yaad_rem")
        # notes_field.send_keys("הזמנה זו הינה ניסוי! אין להתייחס להזמנה זו")
        _full_cityString = ' '.join([str(elem) for elem in full_cityList])  # String 2 str
        _full_streetString = ' '.join([str(elem) for elem in full_streetList])  # String 2 str
        notes_field.send_keys(" ", _full_cityString,' ', _full_streetString, " ")
        # notes_field.send_keys("yaad_rem אין להתייחס להזמנה זו! הזמנה זו הינה ניסוי! חיפה 7047413 ויצמן 90")

        # # GENERAL Notes
        # general_notes_field = browser.find_element_by_name("ship_rem")
        # general_notes_field.send_keys("yaad_rem אין להתייחס להזמנה זו! הזמנה זו הינה ניסוי! חיפה 7047413 ויצמן 90")

        # כפתור "קליטה וחזרה לדף משלוחים"
        make_sticker_button = browser.find_element_by_name("ship_proceed")
        make_sticker_button.click()

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

    if not local_pickup:
        # login_ydm()
        # embed_data()

        # browser = setup_browser()

        ## A2 Login Butik 24
        loginButik24(browser=browser)

        # return for saturday without create delivery on Butik24
        # butikBarCode = "FDFRE232432"
        # butikTrackNumber = "1123445"
        # winsound.Beep(2000, 150), winsound.Beep(1500, 150), sleep(0.15), winsound.Beep(800, 150), winsound.Beep(800, 150), sleep(0.27), winsound.Beep(1400, 150), winsound.Beep(1400, 150)
        # return browser, finalOrderLink, buyer_name, butikTrackNumber, butikBarCode, buyer_phone

        goToTab(browser=browser, tabURL="https://members.lionwheel.com/tasks/new?locale=he")

        ## A3 Embed buyer details on order page
        # packNum = packNum.get()
        embed_details(browserr=browser,
                      buyer_city=city,
                      buyer_street=street,
                      buyer_street_number=street_number,
                      buyer_name=buyer_name,
                      clean_address=streetAndNumber,
                      buyer_phone=buyer_phone, buyer_email=buyer_email,
                      buyer_notes=f"{streetAndNumber}, {heb_city}", orderNum=order_id, packNum=pack_num)
        # embed_details(browser, city, full_streetList,
        #               "", buyer_name,
        #               heb_city, buyer_phone, buyer_email,
        #               "", order_id, pack_num)

        ## A4 Create delivery and redirect to sticker Tab
        # input("Make a sticker??") # ע"מ למנוע יצירת מדבקות לבדיקות כשאין צורך
        butikTrackNumber, butikBarCode = create_sticker(browser=browser)

    winsound.Beep(2000, 150)
    winsound.Beep(1500, 150)
    # browser.execute_script('window.print();')
    sleep(0.15)
    winsound.Beep(800, 150)
    winsound.Beep(800, 150)
    sleep(0.27)
    winsound.Beep(1400, 150)
    winsound.Beep(1400, 150)

# makeSticker("011087","2")

# while 1 == 1:
#     sleep(1.5)