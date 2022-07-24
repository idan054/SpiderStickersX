import webbrowser
import winsound
from selenium import webdriver
from Gadgets.multi_usage.bcolors import bcolors
from Gadgets.multi_usage.locationChecker import location_checker
from Scripts.A1_wooGetAPI import woocomarce_api
from Scripts.A2_Cargo_createStickerAPI import create_deliveryCargo
from Scripts.A2_MahirLiButik_createStickerAPI import create_delivery_mahirLiButik
from pynput.keyboard import Controller
from time import sleep
from tkinter import messagebox

keyboard = Controller()

# global browser

global browser, finalOrderLink, buyer_name, butikTrackNumber, butikBarCode, buyer_phone, api_output


## main based wordpress woocomarce API
def main_api(numOrder, numOfPacks, deliveryCompany):
    global browser, finalOrderLink, buyer_name, butikTrackNumber, butikBarCode, buyer_phone, api_output

    print("delivery company from radio buttons:")
    print(deliveryCompany)

    if numOrder == "":
        numOrder = 28020 # Some default

    # global browser
    ## A0 setup browser & Gui
    print(f"{bcolors.Yellow}{bcolors.BOLD}Start{bcolors.Normal}")

    print("woocomarce_api Start")

    ## Get details from API (V2.0 Update)
    first_name, last_name, clean_address, buyer_street_number, buyer_street, buyer_city, \
    buyer_email, buyer_phone, high_quantity, deliveryNeeded, buyer_notes\
        = woocomarce_api(numOrder=numOrder)

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
        messagebox.showinfo("הערה מהלקוח", f"ಠ_ಠ שים לב להערה של הלקוח\n{buyer_notes}")

    ## Check if deliveryNeeded
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
        if value: # default is False - לא ליצור משלוח
            print("Fast return - No delivery needed.")
            return str(f'{buyer_phone}'),
            # return "pickup"

        else:
            delivery_confirm = messagebox.askyesno("יצירת משלוח", "?ליצור משלוח בכל זאת")
            if not delivery_confirm:
                return
    print(f"deliveryNeeded = {deliveryNeeded}")

    if deliveryCompany == 0:
        print("Fast return - delivery company unSelected.")
        messagebox.showinfo("בחר חברת משלוחים", "                   .המשלוח בוטל\n"
                                                "^o^ בחר חברת משלוחים והתחל מחדש")
        return

    print(f"deliveryCompany is {deliveryCompany}")


    ## rework buyer & address details + CHECK FOR BUYER NOTES
    # rework API Values to the traditional (from v1.0)
    buyer_name = f"{first_name} {last_name}"
    # buyer_city = city
    # buyer_street = street
    # buyer_street_number = street_num
    # clean_address = address_1
    # buyer_phone = phone
    # buyer_email = email
    # buyer_notes = customer_note


    if deliveryCompany == 24:
        messagebox.showinfo("חברת משלוחים", f"{buyer_city} - בוטיק 24")
        resp = create_delivery_mahirLiButik(
            delivery_company=deliveryCompany,
            buyer_city=buyer_city, buyer_name=buyer_name,
            clean_address=clean_address, buyer_phone=buyer_phone, buyer_email=buyer_email,
            buyer_notes=buyer_notes, orderNum=numOrder, packNum=numOfPacks)

    if deliveryCompany == 23:
        messagebox.showinfo("חברת משלוחים", f"{buyer_city} - מהיר לי")
        resp = create_delivery_mahirLiButik(
            delivery_company=deliveryCompany,
            buyer_city=buyer_city, buyer_name=buyer_name,
            clean_address=clean_address, buyer_phone=buyer_phone, buyer_email=buyer_email,
            buyer_notes=buyer_notes, orderNum=numOrder, packNum=numOfPacks)

    if deliveryCompany == 22:
        messagebox.showinfo("חברת משלוחים", f"{buyer_city} - CARGO שליחויות")
        resp = create_deliveryCargo(
            # delivery_company=deliveryCompany,
            buyer_city=buyer_city, buyer_name=buyer_name,
            clean_address=clean_address, buyer_phone=buyer_phone, buyer_email=buyer_email,
            buyer_notes=buyer_notes, orderNum=numOrder, packNum=numOfPacks)

    # 2
    # {'barcode': '1689379:',
    #  'destination_region_str': 'מרכז ודרום תל אביב - מערב',
    #  'label': 'https://members.lionwheel.com/tasks/print_public_label.pdf?public_id=CCQQAMXR5E',
    #  'public_id': 'CCQQAMXR5E',
    #  'task_id': 1689379}



    winsound.Beep(2000, 150)
    winsound.Beep(1500, 150)
    sleep(0.15)
    winsound.Beep(800, 150)
    winsound.Beep(800, 150)
    sleep(0.27)
    winsound.Beep(1400, 150)
    winsound.Beep(1400, 150)
    # Press and release space
    # keyboard.press(Key.enter)
    # keyboard.release(Key.enter)

    # if deliveryCompany == 22 : # Cargo
    #     return resp

    if deliveryCompany == 22:  # Cargo
        butikTrackNumber = resp
        butikBarCode = ''
        webbrowser.open('https://www.cargo-ship.co.il/Baldar/Deliveries.aspx')

    if deliveryCompany == 23 or deliveryCompany == 24:
        butikTrackNumber = resp["task_id"]
        butikBarCode = resp["barcode"]
        webbrowser.open(resp["label"])

    browser = "PlaceHolder"
    return browser, finalOrderLink, buyer_name, butikTrackNumber, butikBarCode, buyer_phone

# if __name__ == '__main__':
#     main()
