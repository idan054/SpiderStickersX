import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter import messagebox

from selenium import webdriver

from harelMain import makeSticker

global browser

def main_starter():
    global browser

    # Close chrome window if available
    try:
        # if browser is not None: # No Need.
        browser.quit()
        print(browser)
    except Exception as e:
        print("ERROR 1 : " + str(e))

    def install_chromeDriver():
        import requests
        import zipfile
        import os

        # url = "https://chromedriver.storage.googleapis.com/90.0.4430.24/chromedriver_win32.zip"
        url = "https://chromedriver.storage.googleapis.com/89.0.4389.23/chromedriver_win32.zip"
        r = requests.get(url, allow_redirects=True)

        open('chromedriver_win32.zip', 'wb').write(r.content)

        with zipfile.ZipFile("chromedriver_win32.zip", 'r') as zip_ref:
            zip_ref.extractall()

        os.replace("chromedriver.exe", "C:\Program Files (x86)\chromedriver.exe")
        os.remove("chromedriver_win32.zip")

    def setup_selenium():
        # chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists

        # option = webdriver.ChromeOptions()
        # option.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
        # option.binary_location = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'

        # user_field = "idanb"
        # chrome_ver = "90"  # 86/87/88/89/90
        # options = webdriver.ChromeOptions()  # פיתחת כרום דרך משתמש רגיל
        # options.add_argument(f"user-data-dir=C:\\Users\\{user_field.get()}\\AppData\\Local\\Google\\Chrome\\User Data")
        # browser = webdriver.Chrome(executable_path=fr"C:\Program Files (x86)\\chromedriver{chrome_ver}.exe", options=options)

        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1100,900")

        # _browser = webdriver.Chrome(executable_path=fr"C:\Program Files (x86)\\chromedriver{chrome_ver}.exe")

        chrome_ver = radioVar.get()
        if radioVar.get() == 0:
            chrome_ver = 91
        print(chrome_ver)

        _browser = webdriver.Chrome(executable_path=fr"C:\Program Files (x86)\chromedriver{chrome_ver}.exe",
                                    options=options)

        # browser = webdriver.Chrome(options=options)
        # ChromeVer = browser.capabilities['browserVersion']
        # ChromeDriverVer = browser.capabilities['chrome']['chromedriverVersion'].split(' ')[0]
        # print(ChromeVer)
        # print(ChromeDriverVer)
        # print("ChromeVer " + ChromeVer[0:2])
        # print("ChromeDriverVer " + ChromeDriverVer[0:2])
        # and if it doesn't exist, download it automatically,
        # then add chromedriver to path

        # chrome_ver = radioVar.get()  # 86/87/88
        # browser = webdriver.Chrome(executable_path=fr"C:\Program Files (x86)\chromedriver{chrome_ver}.exe")
        return _browser

    try:
        # install_chromeDriver()
        browser = setup_selenium()
        # print(browser, "B")
    except:
        messagebox.showerror("שגיאה", "Update ChromeDriver in Program Files (x86) \n from https://chromedriver.chromium.org/")

    # try:
    makeSticker(orderLinkField.get(), packNum.get(), browser)
        # makeSticker(100012222 , 1, browser)
    # except Exception as e:
    #     print("ERROR 2 : " + str(e))

root = tk.Tk()  # המסך הראשי
root.configure(background="#23964e")
root.title("Butik Stickers V1.5(1) HarelButik")
ttk.Style(root).configure('myStyle.TRadiobutton', background="#23964e", foreground='white', font = ("rubik", 9))
ttk.Style(root).configure('W.TButton', font =('rubik', 12,), foreground = 'black')
# root.iconbitmap(r'C:\Users\idanb\Documents\MEGAsync\App4Sale\Spider3D\BlackLogoRoundedPNG.ico', )#לא בטוח למה צריך את הr
# root.iconbitmap('.icon\\BlackLogoRoundedPNG.ico')#לא בטוח למה צריך את הr


canvas = tk.Canvas(root, height=150, width=300, bg="#23964e", highlightbackground="#23964e")
canvas.pack()



# packButtonSaver = tk.Frame(root, bg="#23964e", padx=10)  # כפתור עדכון כמות חבילות
# packButtonSaver.place(relx=0.565, rely=0.68, height=30 )
# packButton = ttk.Button(packButtonSaver, text=" שלח מייל מעקב ", style="W.TButton", command=main_starter).pack()

# packButtonSaver = tk.Frame(root, bg="#23964e")  # כפתור עדכון כמות חבילות
# packButtonSaver.place(relx=-0.44, rely=0.66, height=30, width=400, )
# packButton = ttk.Button(packButtonSaver, text="עדכן כמות חבילות", style="W.TButton", command=updatePackNum).pack()

# alertBottomFrame = tk.Frame(root, bg="#23964e")  # טקסט המלצה לווידוא פרטים
# alertBottomFrame.place(relx=0.00, rely=0.65, height=30, width=400, )
# alertLabel = Label(alertBottomFrame, text="לפני ההדפסה, כדאי לוודא שהפרטים תקינים", font=("rubik", 12,), bg="#23964e", fg="white").pack()

###################################################################################

def sel():
   selection = "You selected the option " + str(radioVar.get())
   Label(root).config(text = selection)
   print(radioVar.get())
   chrome_ver = radioVar.get()
   print("Chrom_ver is " + str(chrome_ver))


# user_field_Frame = tk.Frame(root, bg="#23964e")  # שדה טקסט כמות חבילות
# user_field_Frame.place(relx=0.23, rely=0.88, height=30, width=75, )
# user_field = tk.Entry(user_field_Frame, font=("rubik", 12))
# user_field.pack()
# user_field.insert(0, "Spider3D")

# userButtonSaver = tk.Frame(root, bg="#23964e", width=100)  # כפתור עדכון כמות חבילות
# userButtonSaver.place(relx=-0.15, rely=0.78, height=30, width=400, )
# userButton = tk.Button(userButtonSaver, text="עדכון משתמש", font=("rubik", 12), command=updateUser)
# userButton.pack()

# orderID_Frame = tk.Frame(root, bg="#23964e")  # שדה טקסט כמות חבילות
# orderID_Frame.place(relx=0.23, rely=0.88, height=30, width=75, )
# orderID = tk.Entry(orderID_Frame, font=("rubik", 12))
# orderID.pack()
# orderID.insert(0, "OrderId")


RadioFrame = tk.Frame(root, bg="#23964e")  # טקסט המלצה לווידוא פרטים
RadioFrame.place(relx=0.03, rely=0.55, height=100, width=100, )
# style = Style(root)
# style.configure("TRadiobutton", background = "light green",
#                 foreground = "red", font = ("arial", 10, "bold"))

radioVar = IntVar()
R1 = ttk.Radiobutton(RadioFrame, text="Chrome 89", variable=radioVar, value="89", command=sel, style="myStyle.TRadiobutton")
# R1.focus()
R1.pack( anchor = W )

R2 = ttk.Radiobutton(RadioFrame, text="Chrome 90", variable=radioVar, value="90", command=sel, style="myStyle.TRadiobutton")
R2.pack( anchor = W )

R3 = ttk.Radiobutton(RadioFrame, text="Chrome 91", variable=radioVar, value="91", command=sel, style="myStyle.TRadiobutton")
R3.pack( anchor = W)
R3.state(['selected'])

###################################################################################

entry_pack_Frame = tk.Frame(root, bg="#23964e")  # שדה טקסט כמות חבילות
entry_pack_Frame.place(relx=0.87, rely=0.32, height=30, width=33, )
packNum = ttk.Entry(entry_pack_Frame, font=("rubik", 14 ), width=33, justify="center")
packNum.pack()
packNum.insert(0, "1")

alertBottomFrame = tk.Frame(root, bg="#23964e")  # טקסט המלצה לווידוא פרטים
alertBottomFrame.place(relx=0.45, rely=0.05, height=30, width=200, )
alertLabel = Label(alertBottomFrame, text="הכנס מס' הזמנה", font=("rubik", 12, "bold"), bg="#23964e", fg="white").pack()

linkButtonSaver = tk.Frame(root, bg="#23964e")  # כפתור שמירת קישור ותחילת עבודה
linkButtonSaver.place(relx=0.035, rely=0.32, height=30, width=60, )
linkButton = ttk.Button(linkButtonSaver, text="המשך", style="W.TButton", command=main_starter).pack()

entry_link_Frame = tk.Frame(root, bg="#23964e")  # שדה טקסט לקישור
entry_link_Frame.place(relx=0.25, rely=0.32, height=35, width=184, )
orderLinkField = ttk.Entry(entry_link_Frame, font=("rubik", 14 ), width=30, justify="center")
orderLinkField.pack()
# orderLinkField.insert(0, "011086")

# cleanButtonFrame = tk.Frame(root, bg="#23964e")  # כפתור ניקיון והתחלה מחדש
# cleanButtonFrame.place(relx=0.25, rely=0.80, height=30, width=200, )
# cleanButton = tk.Button(cleanButtonFrame, text="ניקוי והפעלה מחדש", font=("rubik", 12), command=clean_AndGoTo_OrderPage).pack()
root.mainloop()