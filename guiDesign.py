import tkinter as tk
import winsound
from time import sleep
from tkinter import *
from tkinter import messagebox, ttk

from Gadgets.multi_usage.bcolors import bcolors
from Gadgets.pickup_sms import pickup_sms
from Scripts.B1_complete_and_notifications import complete_and_notifications
from mainApi import main_api
# Need ...starter() because gui can't implement attributes (numOrder, numOfPacks)
from popupDesign import locker_popupDesign

global browser, finalOrderLink, buyer_name, butikTrackNumber, butikBarCode, buyer_phone, api_output

global hex_c, radioVar_selection
def main_starter():
    global browser, finalOrderLink, buyer_name, butikTrackNumber, butikBarCode, buyer_phone, api_output
    winsound.Beep(2000, 300)
    winsound.Beep(1000, 100)
    # mailButton['state'] = DISABLED
    # mailButton['state'] = NORMAL
    # sys.stdout = open("SpiderLog.txt", "w")
    print(f"deliveryCompany_radioVar = {deliveryCompany_radioVar.get()}")
    print(f"orderLinkField = {orderLinkField.get()}")
    print(f"packNum = {packNum.get()}")
    # browser, finalOrderLink, buyer_name, butikTrackNumber, butikBarCode, buyer_phone =
    try:
        api_output = main_api(numOrder=orderLinkField.get(), numOfPacks=packNum.get(),
                          deliveryCompany=deliveryCompany_radioVar.get())
    except Exception as e:
        print(e)
        # messagebox.showerror("שגיאה", "חלה שגיאה בהפעלת התוכנה")
        api_output = "FAILED"
        # e = str(e)
        # print("ValueError:")
        # print(f"{bcolors.Red}e:{bcolors.Normal}")
        # print(e)
        winsound.Beep(2000, 150)
        winsound.Beep(1500, 150)
        # browser.execute_script('window.print();')
        sleep(0.15)
        winsound.Beep(800, 150)
        winsound.Beep(800, 150)
        sleep(0.27)
        winsound.Beep(1400, 150)
        winsound.Beep(1400, 150)

    print("api_output is ",api_output)
    # if api_output == "pickup":
    if api_output[0] == "0": # return phone only
        locker_popupDesign(root=root, buyer_phone=api_output)

    else: # When no pickup...
        browser, finalOrderLink, buyer_name, butikTrackNumber,\
        butikBarCode, buyer_phone = api_output
        # print(api_output)
        print()
        print()
        print(api_output)


        main_label_frame.place(relx=0.05, rely=0.07, height=30, width=300, )
        main_label.config(text=f" שלח התראות מעקב להזמנה {orderLinkField.get()}# ")

    packNum.delete(0, END)
    packNum.insert(0, "1") # Reset to 1 when finish
    print("Packs field reset to 1")

    if api_output[0] != "0":               # After delivery
        mailButton['state'] = NORMAL
    print(f"{bcolors.Yellow}{bcolors.BOLD}Done.{bcolors.Normal}")

def part_b_starter():
    global browser, finalOrderLink, buyer_name, butikTrackNumber, butikBarCode, buyer_phone, api_output
    try:
        print("orderLinkField.get() is ", orderLinkField.get())
    except:
        messagebox.showinfo("טעות", "¯\_(ツ)_/¯  לא זוהתה מס' הזמנה")

    ## Send track mail & change status to complete
    ## Send SMS confirmation & tracking link on SMS
    print(butikTrackNumber)
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
root.configure(background="#236795")
root.title("ספיידר מדבקות מעורב")
ttk.Style(root).configure('myStyle.TRadiobutton', background="#236795", foreground='white', font = ("rubik", 9))
ttk.Style(root).configure('pickupPopup.TRadiobutton', background="#236795", foreground='white', font = ("rubik", 9))
ttk.Style(root).configure('W.TButton', font =('rubik', 12,), justify="center", foreground = 'black')
# root.iconbitmap(r'C:\Users\idanb\Documents\MEGAsync\App4Sale\Spider3D\BlackLogoRoundedPNG.ico', )#לא בטוח למה צריך את הr
# root.iconbitmap(r'Assets/StickerApp.ico')#לא בטוח למה צריך את הr

canvas = tk.Canvas(root, height=150, width=300, bg="#236795", highlightbackground="#236795")
canvas.pack()
# endregion הגדרות טקינטר

# region כפתור "המשך" לתחילת פעולה
linkButtonSaver = tk.Frame(root, bg="#236795")  # כפתור שמירת קישור ותחילת עבודה
linkButtonSaver.place(relx=0.035, rely=0.32, height=30, width=60, )
linkButton = ttk.Button(linkButtonSaver, text="המשך", style="W.TButton",
                        command=main_starter).pack()
# endregion כפתור המשך לתחילת פעולה

# region כפתור מייל מעקב
packButtonSaver = tk.Frame(root, bg="#236795", padx=20)  # כפתור עדכון כמות חבילות
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
entry_link_Frame = tk.Frame(root, bg="#236795")  # שדה טקסט לקישור
entry_link_Frame.place(relx=0.25, rely=0.32, height=30, width=184, )
orderLinkField = ttk.Entry(entry_link_Frame, font=("rubik", 14 ), width=30, justify="center")
orderLinkField.pack()
# endregion שדה מס' הזמנה
# איסוף עצמי "27695"
# "25560" # Eyal Biton הזמנה עבור
# כולל הערות + כמות גבוהה # "27692"

# region שדה מס' אריזות
entry_pack_Frame = tk.Frame(root, bg="#236795")  # שדה טקסט כמות חבילות
entry_pack_Frame.place(relx=0.87, rely=0.32, height=30, width=33, )
packNum = ttk.Entry(entry_pack_Frame, font=("rubik", 14 ), width=33, justify="center")
packNum.pack()
packNum.insert(0, "1")
# endregion

# region כפתורי רדיו
def change_deliveryCompany_selection():
   selection = "You selected the option " + str(deliveryCompany_radioVar.get())
   Label(root).config(text = selection)
   print(deliveryCompany_radioVar.get())
   deliveryCompany = deliveryCompany_radioVar.get()
   print("deliveryCompany is " + str(deliveryCompany))
# ----
RadioFrame = tk.Frame(root, bg="#236795")  # טקסט המלצה לווידוא פרטים
RadioFrame.place(relx=0.03, rely=0.56, height=100, width=100, )
# style = Style(root)
# style.configure("TRadiobutton", background = "light green",
#                 foreground = "red", font = ("arial", 10, "bold"))
deliveryCompany_radioVar = IntVar()
# R1 = ttk.Radiobutton(RadioFrame, text="Chrome 86", variable=chrome_radioVar, value="86", command=change_chrome_selection, style="myStyle.TRadiobutton")
# ----
# R1.pack( anchor = W )
# ----
R2 = ttk.Radiobutton(RadioFrame, text="בוטיק 24", variable=deliveryCompany_radioVar, value="24", command=change_deliveryCompany_selection, style="myStyle.TRadiobutton")
R2.pack( anchor = W )
R2.state(['selected'])
# ----
R3 = ttk.Radiobutton(RadioFrame, text="מהיר לי", variable=deliveryCompany_radioVar, value="23", command=change_deliveryCompany_selection, style="myStyle.TRadiobutton")
R3.pack( anchor = W)
# endregion

# region כותרת "הכנס מס' הזמנה"
## Official green V1. #23964e
main_label_frame = tk.Frame(root, bg="#236795")  # טקסט המלצה לווידוא פרטים
main_label_frame.place(relx=0.29, rely=0.07, height=30, width=300, )
main_label = Label(main_label_frame, text="הכנס מס' הזמנה", font=("rubik", 12, "bold"), bg="#236795", fg="white")
main_label.pack()

subTextFrame = tk.Frame(root, bg="#236795")  # טקסט המלצה לווידוא פרטים
subTextFrame.place(relx=0.45, rely=0.88, height=20, width=200, )
subTextLabel = Label(subTextFrame, text="עלות סמס מעקב 0.06₪", font=("rubik", 9), bg="#236795", fg="white").pack()
# endregion "כותרת "הכנס מס' הזמנה

root.mainloop()