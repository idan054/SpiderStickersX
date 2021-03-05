import winsound
import tkinter as tk
from tkinter import *

from Gadgets.pickup_sms import pickup_sms
from mainApi import main_api
from Gadgets.multi_usage.bcolors import bcolors
from tkinter import messagebox, ttk
from Scripts.B1_complete_and_notifications import complete_and_notifications


# Need ...starter() because gui can't implement attributes (numOrder, numOfPacks)
from tests import a

global browser, finalOrderLink, buyer_name, butikTrackNumber, butikBarCode, buyer_phone, api_output
def main_starter():
    global browser, finalOrderLink, buyer_name, butikTrackNumber, butikBarCode, buyer_phone, api_output

    # sys.stdout = open("SpiderLog.txt", "w")
    winsound.Beep(2000, 300)
    winsound.Beep(1000, 100)
    print(f"orderLinkField = {orderLinkField.get()}")
    print(f"packNum = {packNum.get()}")
    try:
        # browser, finalOrderLink, buyer_name, butikTrackNumber, butikBarCode, buyer_phone =
        api_output = main_api(numOrder=orderLinkField.get(), numOfPacks=packNum.get())
        print("api_output is ",api_output)
        # if api_output == "pickup":
        if api_output[0] == "0":
            openNewWindow()
        else: # When no pickup...
            browser, finalOrderLink, buyer_name, butikTrackNumber,\
            butikBarCode, buyer_phone = api_output
            print(f"buyer_name is {buyer_name} from api_output (main_api def)")
    except ValueError as e:
        e = str(e)
        print(f"{bcolors.Red}e:{bcolors.Normal}")
        print("ValueError:")
        print(e)
        # sys.stdout.close()  # Close log
        messagebox.showerror("שגיאה", e)

    packNum.delete(0, END)
    packNum.insert(0, "1") # Reset to 1 when finish
    print("Packs field reset to 1")
    print(f"{bcolors.Yellow}{bcolors.BOLD}Done.{bcolors.Normal}")

def part_b_starter():
    # try:
    global browser, finalOrderLink, buyer_name, butikTrackNumber, butikBarCode, buyer_phone, api_output

    ## Send track mail & change status to complete
    ## Send SMS confirmation & tracking link on SMS
    complete_and_notifications(
        browser=browser,
        numOrder=orderLinkField.get(), buyer_name=buyer_name, butikTrackNumber=butikTrackNumber,
        buyer_phone=buyer_phone, butikBarCode=butikBarCode)
    print(f"{bcolors.Yellow}{bcolors.BOLD}Track SMS & Mail sent\nOrder status changed to complete.{bcolors.Normal}")

    # except:
    #     messagebox.showinfo("טעות", "¯\_(ツ)_/¯  לא זוהתה מס' הזמנה")

def pickup_sms_starter():
    print(api_output, f"from pickup_sms_starter...")
    pickup_sms(buyer_phone=api_output,
               message_type=radioVar_selection)

## Design
# region הגדרות טקינטר
root = tk.Tk()  # המסך הראשי
root.configure(background="#23964e")
root.title("Spider3D Stickers")
ttk.Style(root).configure('myStyle.TRadiobutton', background="#23964e", foreground='white', font = ("rubik", 9))
ttk.Style(root).configure('pickupPopup.TRadiobutton', background="#23964e", foreground='white', font = ("rubik", 9))
ttk.Style(root).configure('W.TButton', font =('rubik', 12,), justify="center", foreground = 'black')
# root.iconbitmap(r'C:\Users\idanb\Documents\MEGAsync\App4Sale\Spider3D\BlackLogoRoundedPNG.ico', )#לא בטוח למה צריך את הr
# root.iconbitmap('.icon\\BlackLogoRoundedPNG.ico')#לא בטוח למה צריך את הr

canvas = tk.Canvas(root, height=150, width=300, bg="#23964e", highlightbackground="#23964e")
canvas.pack()
# endregion הגדרות טקינטר

theGrey = "#f0f0f0" # Windows default grey
global hex_c, radioVar_selection
def openNewWindow():

    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(root)
    newWindow.focus_force()
    newWindow.configure(background="white")
    newWindow.title("א.ע")
    newWindow.geometry("200x200")

    # sets the geometry of toplevel

    ttk.Style(newWindow).configure('pickupPopup.TRadiobutton',
                                foreground='black',
                                background="white",
                                font=("rubik", 10))

    # sets the geometry of toplevel

    # A Label widget to show in toplevel
    radioButtonFrame = tk.Frame(newWindow, bg="white")  # טקסט המלצה לווידוא פרטים
    radioButtonFrame.place(relx=0.27, rely=0.28, height=500, width=200)

    titleFrame = tk.Frame(newWindow, bg="white")  # טקסט המלצה לווידוא פרטים
    titleFrame.place(relx=0.0, rely=0.03, height=40, width=200, )
    title_label = Label(titleFrame,
                text="בחר לוקר למסירת \nאיסוף עצמי",
                font=("rubik", 12, "bold"),
                bg="white",
                fg="black")
    title_label.pack(pady=0)

    buttonSMSFrame = tk.Frame(newWindow, bg=theGrey)  # טקסט המלצה לווידוא פרטים
    buttonSMSFrame.place(relx=0, rely=0.77, height=50, width=200)
    ttk.Button(buttonSMSFrame,
               text="שלח סמס מעקב",
               command=pickup_sms_starter).pack(pady=11)

    # region כפתורי רדיו

    def change_selection():
        global hex_c, radioVar_selection
        radioVar_selection = int(radioVar.get())
        print(radioVar_selection)
        color_title = ""
        hex_c = "bdbdbd"
        if radioVar.get() == 1:
            hex_c = "23964e" # Green
            color_title = "לוקר ירוק"
        if radioVar.get() == 2:
            hex_c = "2d81be" # Blue
            color_title = "לוקר כחול"
        if radioVar.get() == 3:
            hex_c = "db8400" # Orange
            color_title = "לוקר כתום"
        if radioVar.get() == 4:
            hex_c = "333333"  # Orange
            color_title = "תיאום טלפוני"

        ## Change backgrounds & frames
        # radioButtonFrame.configure(background=f"#{hex_c}")
        # titleFrame.configure(background=f"#{hex_c}")
        # newWindow.configure(background=f"#{hex_c}") # Green
        # ttk.Style(master).configure('pickupPopup.TRadiobutton', background=f"#{hex_c}", foreground='white', font=("rubik", 9, "bold"))
        # title_label.config(background=f"#{hex_c}", foreground="white")

        ## Change title color_title only
        title_label.config(background="white",
                           foreground=f"#{hex_c}",
                           text=color_title,
                           font = ("rubik", 14, "bold"),
                           )
        titleFrame.place(relx=-0.02, rely=0.07, height=40, width=200)

    radioVar = IntVar()
    ttk.Radiobutton(radioButtonFrame,
                     text="     לוקר ירוק",
                     variable=radioVar,
                     value=1,
                     command=change_selection,
                     style="pickupPopup.TRadiobutton").pack(anchor=W) #.state(['selected'])
    # ----
    ttk.Radiobutton(radioButtonFrame,
                     text="    לוקר כחול",
                     variable=radioVar,
                     value=2,
                     command=change_selection,
                     style="pickupPopup.TRadiobutton").pack(anchor=W) #.state(['selected'])

    # ----
    ttk.Radiobutton(radioButtonFrame,
                     text="   לוקר כתום",
                     variable=radioVar,
                     value=3,
                     command=change_selection,
                     style="pickupPopup.TRadiobutton").pack(anchor=W) #.state(['selected'])

    ttk.Radiobutton(radioButtonFrame,
                     text="תיאום טלפוני",
                     variable=radioVar,
                     value=4,
                     command=change_selection,
                     style="pickupPopup.TRadiobutton").pack(anchor=W) #.state(['selected'])
    # endregion כפתורי רדיו

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
                        text="שלח התראות מעקב \n !ומכתב תודה ▶⦿◀",  #◍ ✪ ⊛
                        style="W.TButton",
                        command=part_b_starter).pack()
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
def change_chrome_selection():
   selection = "You selected the option " + str(chrome_radioVar.get())
   Label(root).config(text = selection)
   print(chrome_radioVar.get())
   chrome_ver = chrome_radioVar.get()
   print("Chrome_ver is " + str(chrome_ver))
# ----
RadioFrame = tk.Frame(root, bg="#23964e")  # טקסט המלצה לווידוא פרטים
RadioFrame.place(relx=0.03, rely=0.56, height=100, width=100, )
# style = Style(root)
# style.configure("TRadiobutton", background = "light green",
#                 foreground = "red", font = ("arial", 10, "bold"))
chrome_radioVar = IntVar()
R1 = ttk.Radiobutton(RadioFrame, text="Chrome 86", variable=chrome_radioVar, value="86", command=change_chrome_selection, style="myStyle.TRadiobutton")
# ----
R1.pack( anchor = W )
# ----
R2 = ttk.Radiobutton(RadioFrame, text="Chrome 87", variable=chrome_radioVar, value="87", command=change_chrome_selection, style="myStyle.TRadiobutton")
R2.pack( anchor = W )
R2.state(['selected'])
# ----
R3 = ttk.Radiobutton(RadioFrame, text="Chrome 88", variable=chrome_radioVar, value="88", command=change_chrome_selection, style="myStyle.TRadiobutton")
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