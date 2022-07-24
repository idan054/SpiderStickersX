import tkinter as tk
from time import sleep
from tkinter import *
from tkinter import ttk, messagebox
from Gadgets.multi_usage.textMeSMS import txtMe_sms
import winsound
from tkinter import messagebox

import requests
from requests.structures import CaseInsensitiveDict

## Send mail & change order to succeed
from Gadgets.multi_usage.textMeSMS import txtMe_sms

## get updated config
from Scripts.B1_complete_and_notifications import complete_and_notifications


def get_config():
    try:
        config = open("config.txt", "r")
    except:
        config = open("config.txt", "w")
        config.write("לוקר 1: 0000")
        config.write("\n")
        config.write("לוקר 2: 0000")
        config.write("\n")
        config.write("לוקר 3: 0000")
        config.write("\n")
        config.write("לוקר 4: 0000")
        config.write("\n")
        config.write("לוקר 5: 0000")
        config.write("\n")
        config.write("לוקר 6: 0000")
        config.write("\n")
        config.write("לוקר 7: 0000")
        config.write("\n")
        config.write("לוקר 8: 0000")
        config.write("\n")
        config = open("config.txt", "r")

    read_config = config.read()
    # print(type(read_config))

    config_list = read_config.splitlines()
    # print(config_list)

    _locker_code_list = []
    for item in config_list:
        digit_item = ''.join(filter(str.isdigit, item))[1:]
        # print('digit_item')
        # print(digit_item)
        _locker_code_list.append(digit_item)
    print('_locker_code_list')
    print(_locker_code_list)
    return _locker_code_list

global hex_c, radioVar_selection, radioVar, title_text
theGrey = "#f0f0f0" # Windows default grey
selectedPassCode = ''
def locker_popupDesign(root, buyer_phone, numOrder):
    global hex_c, radioVar_selection, radioVar, title_text
    radioVar_selection = 99  # איפוס לפני בחירה

    locker_code_list = get_config()

    # Toplevel object which will
    # be treated as a new window
    lockerPopup = Toplevel(root)
    lockerPopup.focus_force()
    lockerPopup.configure(background="white")
    lockerPopup.title("א.ע")
    lockerPopup.geometry("200x420")

    # sets the geometry of toplevel

    ttk.Style(lockerPopup).configure('pickupPopup.TRadiobutton',
                                foreground='black',
                                background="white",
                                font=("rubik", 10))

    # sets the geometry of toplevel

    # A Label widget to show in toplevel
    radioButtonFrame = tk.Frame(lockerPopup, bg="white")  # טקסט המלצה לווידוא פרטים
    radioButtonFrame.place(relx=0.43, rely=0.28, height=500, width=200)

    titleFrame = tk.Frame(lockerPopup, bg="white")  # טקסט המלצה לווידוא פרטים
    titleFrame.place(relx=0.0, rely=0.03, height=40, width=200, )
    title_label = Label(titleFrame,
                text="בחר לוקר למסירת \nאיסוף עצמי",
                font=("rubik", 12, "bold"),
                bg="white",
                fg="black")
    title_label.pack(pady=0)

    # region כפתורי רדיו

    def change_selection():
        global hex_c, radioVar_selection, radioVar, title_text, selectedPassCode
        radioVar_selection = int(radioVar.get())
        print(radioVar_selection)
        title_text = ""
        hex_c = "bdbdbd"
        # 0 = יש לבחור
        if radioVar_selection == 1:
            hex_c = "236795" # Green
            title_text = "לוקר 1"
            selectedPassCode = code_field1.get()
            radioVar_selection = int(radioVar.get())
        if radioVar_selection == 2:
            hex_c = "2d81be" # Blue
            title_text = "לוקר 2"
            selectedPassCode = code_field2.get()
            radioVar_selection = int(radioVar.get())
        if radioVar_selection == 3:
            hex_c = "db8400" # Orange
            title_text = "לוקר 3"
            selectedPassCode = code_field3.get()
            radioVar_selection = int(radioVar.get())
        if radioVar_selection == 4:
            hex_c = "db8400" # Orange
            title_text = "לוקר 4"
            selectedPassCode = code_field4.get()
            radioVar_selection = int(radioVar.get())
        if radioVar_selection == 5:
            hex_c = "db8400" # Orange
            title_text = "לוקר 5"
            selectedPassCode = code_field5.get()
            radioVar_selection = int(radioVar.get())
        if radioVar_selection == 6:
            hex_c = "db8400" # Orange
            title_text = "לוקר 6"
            selectedPassCode = code_field6.get()
            radioVar_selection = int(radioVar.get())
        if radioVar_selection == 7:
            hex_c = "db8400" # Orange
            title_text = "לוקר 7"
            selectedPassCode = code_field7.get()
            radioVar_selection = int(radioVar.get())
        if radioVar_selection == 8:
            hex_c = "db8400" # Orange
            title_text = "לוקר 8"
            selectedPassCode = code_field8.get()
            radioVar_selection = int(radioVar.get())
        if radioVar_selection == 9:
            hex_c = "333333"  # Orange
            title_text = "תיאום טלפוני"
            radioVar_selection = int(radioVar.get())
            # 5 = משלוח

        ## Change backgrounds & frames
        # radioButtonFrame.configure(background=f"#{hex_c}")
        # titleFrame.configure(background=f"#{hex_c}")
        # lockerPopup.configure(background=f"#{hex_c}") # Green
        # ttk.Style(master).configure('pickupPopup.TRadiobutton', background=f"#{hex_c}", foreground='white', font=("rubik", 9, "bold"))
        # title_label.config(background=f"#{hex_c}", foreground="white")

        ## Change title color_title only
        title_label.config(background="white",
                           foreground=f"#{hex_c}",
                           text=title_text,
                           font = ("rubik", 14, "bold"),
                           )
        titleFrame.place(relx=-0.02, rely=0.07, height=40, width=200)

    radioVar = IntVar()
    ttk.Radiobutton(radioButtonFrame,
                     text="      לוקר 1",
                     variable=radioVar,
                     value=1,
                     command=change_selection,
                     style="pickupPopup.TRadiobutton").pack(anchor=W) #.state(['selected'])
    # ----
    ttk.Radiobutton(radioButtonFrame,
                     text="     לוקר 2",
                     variable=radioVar,
                     value=2,
                     command=change_selection,
                     style="pickupPopup.TRadiobutton").pack(anchor=W) #.state(['selected'])

    # ----
    ttk.Radiobutton(radioButtonFrame,
                     text="    לוקר 3",
                     variable=radioVar,
                     value=3,
                     command=change_selection,
                     style="pickupPopup.TRadiobutton").pack(anchor=W) #.state(['selected'])

    ttk.Radiobutton(radioButtonFrame,
                    text="    לוקר 4",
                    variable=radioVar,
                    value=4,
                    command=change_selection,
                    style="pickupPopup.TRadiobutton").pack(anchor=W)  # .state(['selected'])

    ttk.Radiobutton(radioButtonFrame,
                    text="    לוקר 5",
                    variable=radioVar,
                    value=5,
                    command=change_selection,
                    style="pickupPopup.TRadiobutton").pack(anchor=W)  # .state(['selected'])

    ttk.Radiobutton(radioButtonFrame,
                    text="    לוקר 6",
                    variable=radioVar,
                    value=6,
                    command=change_selection,
                    style="pickupPopup.TRadiobutton").pack(anchor=W)  # .state(['selected'])

    ttk.Radiobutton(radioButtonFrame,
                    text="    לוקר 7",
                    variable=radioVar,
                    value=7,
                    command=change_selection,
                    style="pickupPopup.TRadiobutton").pack(anchor=W)  # .state(['selected'])

    ttk.Radiobutton(radioButtonFrame,
                    text="    לוקר 8",
                    variable=radioVar,
                    value=8,
                    command=change_selection,
                    style="pickupPopup.TRadiobutton").pack(anchor=W)  # .state(['selected'])

    ttk.Radiobutton(radioButtonFrame,
                     text="תיאום טלפוני",
                     variable=radioVar,
                     value=9,
                     command=change_selection,
                     style="pickupPopup.TRadiobutton").pack(anchor=W) #.state(['selected'])
    # endregion כפתורי רדיו

    def txtMe_sms_starter():
        global hex_c, radioVar_selection
        # מוודא שנבחר צבע לוקר

        if selectedPassCode == '':
            title_label.config(background="white",
                               foreground="#333333",
                               text="נא לבחור מס' לוקר",
                               font=("rubik", 14, "bold"))

        # מוודא שהוכנסו קודי לוקרים
        if code_field1.get() == "0000" or code_field2.get() == "0000":
            print("יש לעדכן קוד לוקרים!")
            title_label.config(background="white",
                               foreground="#333333",
                               text="נא לעדכן קוד לוקרים",
                               font=("rubik", 14, "bold"))
            # return

        # מגדיר לקונפיג קודי לוקרים
        new_config = open("config.txt", "w")
        new_config.write(f"לוקר 1: {code_field1.get()}")
        new_config.write("\n")
        new_config.write(f"לוקר 2: {code_field2.get()}")
        new_config.write("\n")
        new_config.write(f"לוקר 3: {code_field3.get()}")
        new_config.write("\n")
        new_config.write(f"לוקר 4: {code_field4.get()}")
        new_config.write("\n")
        new_config.write(f"לוקר 5: {code_field5.get()}")
        new_config.write("\n")
        new_config.write(f"לוקר 6: {code_field6.get()}")
        new_config.write("\n")
        new_config.write(f"לוקר 7: {code_field7.get()}")
        new_config.write("\n")
        new_config.write(f"לוקר 8: {code_field8.get()}")

        change_selection() # to update selectedPassCode
        # ttodo Add "Completed & Email notify" here

        if radioVar_selection < 10:
            print('textMe_sms() Pickup Details:')
            print(f'radioVar_selection {radioVar_selection}')
            print(f'selectedPassCode {selectedPassCode}')
            print(f'buyer_phone {buyer_phone}')

            txtMe_sms(message_type = 'Pickup', # LocalPickUp
                      localLockerNum= int(radioVar_selection),
                      localLockerPass= selectedPassCode,
                      phone = buyer_phone, includeAppAd=True) # AKA True BUT doesn't matter
            messagebox.showinfo("אישור סמס", f"(●'◡'●)  סמס הגעה ל{title_text} נשלח ללקוח")
            sleep(0.15)

            headers = CaseInsensitiveDict()
            headers["Authorization"] = \
                woo_token = "Basic Y2tfNzkwYmQ2ZTQ4Zjc5ODYxZjNmYjA0ZTIxNjI5NTBiODc5N2YwNjFkOTpjc18xMmE3OGU1M2U2ZThiZDNhMjZlNjQ3NjFlMGVmNjAwMmI1NDEzMTI5"

            data = { "status": "completed" }
            order_url = f"https://spider3d.co.il/wp-json/wc/v3/orders/{numOrder}"
            # print(requests.put(url=order_url, headers=headers, data=data).json())
            requests.put(url=order_url, headers=headers, data=data).json()

            sleep(0.15)
            lockerPopup.destroy()

    buttonSMSFrame = tk.Frame(lockerPopup, bg=theGrey)  # טקסט המלצה לווידוא פרטים
    buttonSMSFrame.place(relx=0, rely=0.77, height=50, width=200)
    from functools import partial # To add args for the command
    ttk.Button(buttonSMSFrame,
               text="שלח סמס מעקב",
               command= txtMe_sms_starter).pack(pady=11)
               # command= partial(txtMe_sms, message_type=int(radioVar_selection), phone="0584770076")).pack(pady=11)

    code_frame1 = tk.Frame(lockerPopup, bg="#236795")  # שדה טקסט כמות חבילות
    code_frame1.place(relx=0.12, rely=0.280, height=19, width=55, )
    code_field1 = ttk.Entry(code_frame1, font=("rubik", 14), width=30, justify="center", foreground="#236795")
    code_field1.pack()
    code_field1.insert(0, locker_code_list[0])  # Green 1478

    code_frame2 = tk.Frame(lockerPopup, bg="#236795")  # שדה טקסט כמות חבילות
    code_frame2.place(relx=0.12, rely=0.330, height=19, width=55, )
    code_field2 = ttk.Entry(code_frame2, font=("rubik", 14), width=30, justify="center", foreground="#236795")
    code_field2.pack()
    code_field2.insert(0, locker_code_list[1])  # Green 1478

    code_frame3 = tk.Frame(lockerPopup, bg="#236795")  # שדה טקסט כמות חבילות
    code_frame3.place(relx=0.12, rely=0.380, height=19, width=55, )
    code_field3 = ttk.Entry(code_frame3, font=("rubik", 14), width=30, justify="center", foreground="#236795")
    code_field3.pack()
    code_field3.insert(0, locker_code_list[2])  # Green 1478

    code_frame4 = tk.Frame(lockerPopup, bg="#236795")  # שדה טקסט כמות חבילות
    code_frame4.place(relx=0.12, rely=0.430, height=19, width=55, )
    code_field4 = ttk.Entry(code_frame4, font=("rubik", 14), width=30, justify="center", foreground="#236795")
    code_field4.pack()
    code_field4.insert(0, locker_code_list[3])  # Green 1478

    code_frame5 = tk.Frame(lockerPopup, bg="#236795")  # שדה טקסט כמות חבילות
    code_frame5.place(relx=0.12, rely=0.490, height=19, width=55, )
    code_field5 = ttk.Entry(code_frame5, font=("rubik", 14), width=30, justify="center", foreground="#236795")
    code_field5.pack()
    code_field5.insert(0, locker_code_list[4])  # Green 1478

    code_frame6 = tk.Frame(lockerPopup, bg="#236795")  # שדה טקסט כמות חבילות
    code_frame6.place(relx=0.12, rely=0.545, height=19, width=55, )
    code_field6 = ttk.Entry(code_frame6, font=("rubik", 14), width=30, justify="center", foreground="#236795")
    code_field6.pack()
    code_field6.insert(0, locker_code_list[5])  # Green 1478

    code_frame7 = tk.Frame(lockerPopup, bg="#236795")  # שדה טקסט כמות חבילות
    code_frame7.place(relx=0.12, rely=0.595, height=19, width=55, )
    code_field7 = ttk.Entry(code_frame7, font=("rubik", 14), width=30, justify="center", foreground="#236795")
    code_field7.pack()
    code_field7.insert(0, locker_code_list[6])  # Green 1478

    code_frame8 = tk.Frame(lockerPopup, bg="#236795")  # שדה טקסט כמות חבילות
    code_frame8.place(relx=0.12, rely=0.650, height=19, width=55, )
    code_field8 = ttk.Entry(code_frame8, font=("rubik", 14), width=30, justify="center", foreground="#236795")
    code_field8.pack()
    code_field8.insert(0, locker_code_list[7])  # Green 1478


## Example
# master = Tk()
# locker_popupDesign(master, "0584770076")
# mainloop()