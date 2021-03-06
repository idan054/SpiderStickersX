import winsound

from color_printer import printRed
from selenium import webdriver
from Gadgets.multi_usage.bcolors import bcolors
from Gadgets.setup_browser import setup_browser
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

    print("woocomarce_api Start")

    ## Get details from API (V2.0 Update)
    first_name, last_name, clean_address, buyer_street_number, buyer_street, buyer_city, \
    buyer_email, buyer_phone, high_quantity, deliveryNeeded, buyer_notes = woocomarce_api(numOrder=numOrder)

    buyer_name = f"{first_name} {last_name}"

    print("woocomarce_api Done")

    finalOrderLink = f"https://www.spider3d.co.il/wp-admin/post.php?post={numOrder}&action=edit"
    print(finalOrderLink)
    print("Please Wait!")

    ## Check Quantity of items in order
    if high_quantity:
        print(f"{bcolors.Yellow}{bcolors.BOLD}"
              f"יש כפילות"
              f"{bcolors.Normal}")
        messagebox.showinfo("מוצר כפול", "╰(*°▽°*)╯  בהזמנה זו יש מוצרים בכמות גבוהה")
    print(f"high_quantity = {high_quantity}")

    ## Check customer note
    if buyer_notes != "":
        # messagebox.showinfo("הערה מהלקוח", buyer_notes)
        # messagebox.showinfo("הערה מהלקוח", f"ಠ_ಠ שים לב להערה של הלקוח")
        messagebox.showinfo("הערה מהלקוח", f"""                       ಠ_ಠ :שים לב להערה של הלקוח
        "{buyer_notes}" """)

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
            "איסוף עצמי", """"¯\_(ツ)_/¯  אין צורך ביצירת משלוח, הזמנה זו היא איסוף עצמי
                                                  ?להודיע ללקוח לאסוף בסמס""",
            default='yes')
        print(value)
        ## When delivery no needed.
        if value: # default is False - לא ליצור משלוח
            print("Fast return...")
            return buyer_phone, buyer_name
            # return "pickup"
            # return "browser", "finalOrderLink", "buyer_name", "butikTrackNumber", "butikBarCode", "buyer_phone"
        else:
            delivery_confirm =   messagebox.askyesno("יצירת משלוח", "?ליצור משלוח בכל זאת")
            if not delivery_confirm:
                return
    print(f"deliveryNeeded = {deliveryNeeded}")

    ## rework buyer & address details + CHECK FOR BUYER NOTES
    # rework API Values to the traditional (from v1.0)
    # buyer_name = f"{first_name} {last_name}"
    # buyer_city = city
    # buyer_street = street
    # buyer_street_number = street_num
    # clean_address = address_1
    # buyer_phone = phone
    # buyer_email = email
    # buyer_notes = customer_note

    browser = setup_browser()

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
    embed_details(browser, buyer_city, buyer_street
                  , buyer_street_number, buyer_name,
                  clean_address, buyer_phone, buyer_email,
                  buyer_notes, numOrder, numOfPacks)

    ## A4 Create delivery and redirect to sticker Tab
    # input("Make a sticker??") # ע"מ למנוע יצירת מדבקות לבדיקות כשאין צורך
    butikTrackNumber, butikBarCode = create_sticker(browser=browser)

    return browser, finalOrderLink, buyer_name, butikTrackNumber, butikBarCode, buyer_phone

# main_api(28020,1)

# if __name__ == '__main__':
#     main()
