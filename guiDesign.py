import tkinter as tk
import winsound
from time import sleep
from tkinter import *
from tkinter import messagebox, ttk

from color_printer import printRed

from Gadgets.multi_usage.bcolors import bcolors
from Gadgets.pickup_sms import pickup_sms
from Scripts.A1_wooGetAPI import woo_api_get_processing
from Scripts.B1_complete_and_notifications import complete_and_notifications
from mainApi import main_api
# Need ...starter() because gui can't implement attributes (numOrder, numOfPacks)
from popupDesign import locker_popupDesign
import sys  # first of all import the module

global browser, finalOrderLink, buyer_name, butikTrackNumber, butikBarCode, buyer_phone, api_output

processing_num_api = woo_api_get_processing()

global hex_c, radioVar_selection
def main_starter():
    # sys.stdout = open("SpiderSticker_log.txt", "w", encoding='utf-8')
    print("Start SpiderSticker_log")

    _processing_num_api = woo_api_get_processing()
    processing_num.configure(text=f"{_processing_num_api}")

    # try:
    global browser, finalOrderLink, buyer_name, butikTrackNumber, butikBarCode, buyer_phone, api_output
    winsound.Beep(2000, 300)
    winsound.Beep(1000, 100)
    # mailButton['state'] = DISABLED
    # mailButton['state'] = NORMAL
    # sys.stdout = open("SpiderLog.txt", "w")
    print(f"orderLinkField = {orderLinkField.get()}")
    print(f"packNum = {packNum.get()}")
    # browser, finalOrderLink, buyer_name, butikTrackNumber, butikBarCode, buyer_phone =
    api_output = main_api(numOrder=orderLinkField.get(), numOfPacks=packNum.get())

    print("api_output is ", api_output)
    # if api_output == "pickup":
    if len(api_output) == 2:  #S == | AKA Only After localPickup
        print("len(api_output)")
        print(len(api_output)) # return phone & buyer name only
        locker_popupDesign(root=root, buyer_phone=api_output[0], locker_name=api_output[1], order_number=orderLinkField.get())

    else:  # When no pickup...
        browser, finalOrderLink, buyer_name, butikTrackNumber, \
        butikBarCode, buyer_phone = api_output

        main_label_frame.place(relx=0.05, rely=0.07, height=30, width=300, )
        main_label.config(text=f" שלח התראות מעקב להזמנה {orderLinkField.get()}# ")

    packNum.delete(0, END)
    packNum.insert(0, "1")  # Reset to 1 when finish
    print("Packs field reset to 1")

    if len(api_output) != 2:  #S != | AKA Only After delivery
        mailButton['state'] = NORMAL
    print(f"{bcolors.Yellow}{bcolors.BOLD}Done.{bcolors.Normal}")

    # sys.stdout.close()
    # except Exception as e:
    #     printRed(str(e))
    #     messagebox.showerror("שגיאה", f"{e}")
    #     api_output = "FAILED"
    #     # e = str(e)
    #     # print("ValueError:")
    #     # print(f"{bcolors.Red}e:{bcolors.Normal}")
    #     # print(e)
    #     sys.stdout.close()

def part_b_starter():
    global browser, finalOrderLink, buyer_name, butikTrackNumber, butikBarCode, buyer_phone, api_output
    try:
        browser.quit()
        print("orderLinkField.get() is ", orderLinkField.get())
    except:
        messagebox.showinfo("טעות", "¯\_(ツ)_/¯  לא זוהתה מס' הזמנה")

    ## Send track mail & change status to complete
    ## Send SMS confirmation & tracking link on SMS
    complete_and_notifications(
        browser=browser,
        numOrder=orderLinkField.get(), buyer_name=buyer_name, butikTrackNumber=butikTrackNumber,
        buyer_phone=buyer_phone, butikBarCode=butikBarCode)
    print(f"{bcolors.Yellow}{bcolors.BOLD}Track SMS & Mail sent\nOrder status changed to complete.{bcolors.Normal}")

    # orderLinkField.configure(foreground="#a5a5a5")
    # main_label.config(text=f"הזמנה #25550 הושלמה                     ")
    mailButton['state'] = DISABLED
    main_label_frame.place(relx=0.29, rely=0.07, height=30, width=300, )
    main_label.config(text=f"הזמנה #{orderLinkField.get()} הושלמה                     ")


## Design
# region הגדרות טקינטר
root = tk.Tk()  # המסך הראשי
# root.configure(background="#800000") # Recommended red
root.configure(background="#23964e")
root.title("Spider3D Stickers")
ttk.Style(root).configure('myStyle.TRadiobutton', background="#23964e", foreground='white', font = ("rubik", 9))
ttk.Style(root).configure('pickupPopup.TRadiobutton', background="#23964e", foreground='white', font = ("rubik", 9))
ttk.Style(root).configure('W.TButton', font =('rubik', 12,), justify="center", foreground = 'black')
# root.iconbitmap(r'C:\Users\idanb\Documents\MEGAsync\App4Sale\Spider3D\BlackLogoRoundedPNG.ico', )#לא בטוח למה צריך את הr
# root.iconbitmap(r'Assets/StickerApp.ico')#לא בטוח למה צריך את הr

canvas = tk.Canvas(root, height=150, width=300, bg="#23964e", highlightbackground="#23964e")
canvas.pack()
# endregion הגדרות טקינטר

# region כפתור "המשך" לתחילת פעולה
linkButtonSaver = tk.Frame(root, bg="#23964e")  # כפתור שמירת קישור ותחילת עבודה
linkButtonSaver.place(relx=0.035, rely=0.32, height=30, width=60, )
linkButton = ttk.Button(linkButtonSaver, text="המשך", style="W.TButton",
                        command=main_starter).pack()
# endregion כפתור המשך לתחילת פעולה

# region כפתור מייל מעקב
packButtonSaver = tk.Frame(root, bg="#23964e", padx=20)  # כפתור עדכון כמות חבילות
packButtonSaver.place(relx=0.43, rely=0.55, height=60)
mailButton = ttk.Button(packButtonSaver,
                        text="שלח התראות מעקב \n !ומכתב תודה ▶⦿◀",  #◍ ✪ ⊛
                        style="W.TButton",
                        state=DISABLED,
                        command=part_b_starter)
mailButton.pack()
# mailButton.configure(state=DISABLED)
# mailButton.config(state=DISABLED)
# endregion כפתור מייל מעקב

# region שדה מס' הזמנה
entry_link_Frame = tk.Frame(root, bg="#23964e")  # שדה טקסט לקישור
entry_link_Frame.place(relx=0.25, rely=0.32, height=30, width=184, )
orderLinkField = ttk.Entry(entry_link_Frame, font=("rubik", 14 ), width=30, justify="center")
orderLinkField.pack()
# endregion שדה מס' הזמנה
# איסוף עצמי "27695"
# "25560" # Eyal Biton הזמנה עבור
# כולל הערות + כמות גבוהה # "27692"

# region שדה מס' אריזות
entry_pack_Frame = tk.Frame(root, bg="#23964e")  # שדה טקסט כמות חבילות
entry_pack_Frame.place(relx=0.87, rely=0.32, height=30, width=33, )
packNum = ttk.Entry(entry_pack_Frame, font=("rubik", 14 ), width=33, justify="center")
packNum.pack()
packNum.insert(0, "1")
# endregion

# region כפתורי רדיו
# def change_chrome_selection():
#    selection = "You selected the option " + str(chrome_radioVar.get())
#    Label(root).config(text = selection)
#    print(chrome_radioVar.get())
#    chrome_ver = chrome_radioVar.get()
#    print("Chrome_ver is " + str(chrome_ver))
# # ----
# RadioFrame = tk.Frame(root, bg="#23964e")  # טקסט המלצה לווידוא פרטים
# RadioFrame.place(relx=0.03, rely=0.56, height=100, width=100, )
# # style = Style(root)
# # style.configure("TRadiobutton", background = "light green",
# #                 foreground = "red", font = ("arial", 10, "bold"))
# chrome_radioVar = IntVar()
# R1 = ttk.Radiobutton(RadioFrame, text="Chrome 86", variable=chrome_radioVar, value="86", command=change_chrome_selection, style="myStyle.TRadiobutton")
# # ----
# R1.pack( anchor = W )
# # ----
# R2 = ttk.Radiobutton(RadioFrame, text="Chrome 87", variable=chrome_radioVar, value="87", command=change_chrome_selection, style="myStyle.TRadiobutton")
# R2.pack( anchor = W )
# R2.state(['selected'])
# # ----
# R3 = ttk.Radiobutton(RadioFrame, text="Chrome 88", variable=chrome_radioVar, value="88", command=change_chrome_selection, style="myStyle.TRadiobutton")
# R3.pack( anchor = W)
# endregion

# region שדה מס' אריזות
# entry_chromeDriver_Frame = tk.Frame(root, bg="#23964e")  # שדה טקסט כמות חבילות
# entry_chromeDriver_Frame.place(relx=0.04, rely=0.72, height=25, width=115, )
# chromeDriver = ttk.Entry(entry_chromeDriver_Frame, font=("rubik", 13), width=33, justify="center", foreground='grey')
# chromeDriver.pack()
# chromeDriver.insert(0, "89.0.4389.23")
# endregion

# region כותרת "הכנס מס' הזמנה"
## Official green V1. #23964e
main_label_frame = tk.Frame(root, bg="#23964e")  # טקסט המלצה לווידוא פרטים
main_label_frame.place(relx=0.29, rely=0.07, height=30, width=300, )
main_label = Label(main_label_frame, text="הכנס מס' הזמנה", font=("rubik", 12, "bold"), bg="#23964e", fg="white")
main_label.pack()

processing_label_frame = tk.Frame(root, bg="#23964e")  # טקסט המלצה לווידוא פרטים
processing_label_frame.place(relx=0.085, rely=0.55, height=30, width=60, )
processing_label = Label(processing_label_frame, text=":בטיפול", font=("rubik", 12, "bold"), bg="#23964e", fg="white")
# processing_label.configure(text="8")
processing_label.pack()

processing_num_label_frame = tk.Frame(root, bg="#23964e")  # טקסט המלצה לווידוא פרטים
processing_num_label_frame.place(relx=0.02, rely=0.56, height=30, width=20, )
processing_num = Label(processing_num_label_frame, text=f"{processing_num_api}", font=("rubik", 12, "bold"), bg="#23964e", fg="white")
# processing_num.configure(text="8")
processing_num.pack()

subTextFrame = tk.Frame(root, bg="#23964e")  # טקסט המלצה לווידוא פרטים
subTextFrame.place(relx=0.45, rely=0.88, height=20, width=200, )
subTextLabel = Label(subTextFrame, text="עלות סמס מעקב 0.06₪", font=("rubik", 9), bg="#23964e", fg="white").pack()

# driverTextFrame = tk.Frame(root, bg="#23964e")  # טקסט המלצה לווידוא פרטים
# driverTextFrame.place(relx=0.04, rely=0.88, height=20, width=150, )
# driverTextLabel = Label(driverTextFrame, text="מס' כרום דרייבר", font=("rubik", 9), bg="#23964e", fg="white").pack()
# endregion "כותרת "הכנס מס' הזמנה

root.mainloop()