import winsound
import tkinter as tk
from tkinter import *

from Gadgets.sendSms import send_sms
from mainApi import main_api
from Gadgets.bcolors import bcolors
from tkinter import messagebox, ttk
from Scripts.B1_complete_and_notifications import complete_and_notifications


# Need ...starter() because gui can't implement attributes (numOrder, numOfPacks)
global browser, finalOrderLink, buyer_name, butikTrackNumber, butikBarCode, buyer_phone
def main_starter():
    global browser, finalOrderLink, buyer_name, butikTrackNumber, butikBarCode, buyer_phone
    winsound.Beep(2000, 300)
    winsound.Beep(1000, 100)
    print(f"orderLinkField = {orderLinkField.get()}")
    print(f"packNum = {packNum.get()}")
    browser, finalOrderLink, \
    buyer_name, butikTrackNumber, butikBarCode, buyer_phone =\
        main_api(numOrder=orderLinkField.get(), numOfPacks=packNum.get())

    packNum.delete(0, END)
    packNum.insert(0, "1") # Reset to 1 when finish
    print("Packs field reset to 1")
    print(f"{bcolors.Yellow}{bcolors.BOLD}Done.{bcolors.Normal}")

def send_mail_Starter():
    # try:
    global browser, finalOrderLink, buyer_name, butikTrackNumber, butikBarCode, buyer_phone

    ## Send track mail & change status to complete
    ## Send SMS confirmation & tracking link on SMS
    complete_and_notifications(
        browser=browser,
        numOrder=orderLinkField.get(), buyer_name=buyer_name, butikTrackNumber=butikTrackNumber,
        buyer_phone=buyer_phone, butikBarCode=butikBarCode)
    print(f"{bcolors.Yellow}{bcolors.BOLD}Track SMS & Mail sent\nOrder status changed to complete.{bcolors.Normal}")

    # except:
    #     messagebox.showinfo("טעות", "¯\_(ツ)_/¯  לא זוהתה מס' הזמנה")

## Design

# region הגדרות טקינטר
root = tk.Tk()  # המסך הראשי
root.configure(background="#23964e")
root.title("Spider Stickers 2")
ttk.Style(root).configure('myStyle.TRadiobutton', background="#23964e", foreground='white', font = ("rubik", 9))
ttk.Style(root).configure('W.TButton', font =('rubik', 12,), justify="center", foreground = 'black')
# root.iconbitmap(r'C:\Users\idanb\Documents\MEGAsync\App4Sale\Spider3D\BlackLogoRoundedPNG.ico', )#לא בטוח למה צריך את הr
# root.iconbitmap('.icon\\BlackLogoRoundedPNG.ico')#לא בטוח למה צריך את הr

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
packButton = ttk.Button(packButtonSaver,
                text="שלח התראות מעקב \n !ומכתב תודה ▶⦿◀", #◍ ✪ ⊛
                style="W.TButton",
                command=send_mail_Starter).pack()
# endregion כפתור מייל מעקב

# region שדה מס' הזמנה
entry_link_Frame = tk.Frame(root, bg="#23964e")  # שדה טקסט לקישור
entry_link_Frame.place(relx=0.25, rely=0.32, height=30, width=184, )
orderLinkField = ttk.Entry(entry_link_Frame, font=("rubik", 14 ), width=30, justify="center")
orderLinkField.pack()
# orderLinkField.insert(0, "28020")
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
def change_selection():
   selection = "You selected the option " + str(radioVar.get())
   Label(root).config(text = selection)
   print(radioVar.get())
   chrome_ver = radioVar.get()
   print("Chrome_ver is " + str(chrome_ver))
# ----
RadioFrame = tk.Frame(root, bg="#23964e")  # טקסט המלצה לווידוא פרטים
RadioFrame.place(relx=0.03, rely=0.56, height=100, width=100, )
# style = Style(root)
# style.configure("TRadiobutton", background = "light green",
#                 foreground = "red", font = ("arial", 10, "bold"))
radioVar = IntVar()
R1 = ttk.Radiobutton(RadioFrame, text="Chrome 86", variable=radioVar, value="86", command=change_selection, style="myStyle.TRadiobutton")
# ----
R1.pack( anchor = W )
# ----
R2 = ttk.Radiobutton(RadioFrame, text="Chrome 87", variable=radioVar, value="87", command=change_selection, style="myStyle.TRadiobutton")
R2.pack( anchor = W )
R2.state(['selected'])
# ----
R3 = ttk.Radiobutton(RadioFrame, text="Chrome 88", variable=radioVar, value="88", command=change_selection, style="myStyle.TRadiobutton")
R3.pack( anchor = W)
# endregion

# region כותרת "הכנס מס' הזמנה"
## Official green V1. #23964e
alertBottomFrame = tk.Frame(root, bg="#23964e")  # טקסט המלצה לווידוא פרטים
alertBottomFrame.place(relx=0.45, rely=0.07, height=30, width=200, )
alertLabel = Label(alertBottomFrame, text="הכנס מס' הזמנה", font=("rubik", 12, "bold"), bg="#23964e", fg="white").pack()

subTextFrame = tk.Frame(root, bg="#23964e")  # טקסט המלצה לווידוא פרטים
subTextFrame.place(relx=0.45, rely=0.88, height=20, width=200, )
subTextLabel = Label(subTextFrame, text="עלות סמס מעקב 0.26₪", font=("rubik", 9), bg="#23964e", fg="white").pack()
# endregion "כותרת "הכנס מס' הזמנה

root.mainloop()