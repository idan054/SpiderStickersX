import tkinter as tk
from time import sleep
from tkinter import *
from tkinter import ttk, messagebox
from Gadgets.multi_usage.textMeSMS import txtMe_sms

## get updated config
def write_config():
    config = open("config.txt", "w")
    config.write("לוקר ירוק: 0000")
    config.write("\n")
    config.write("לוקר כחול: 0000")
    config.write("\n")
    config.write("לוקר כתום: 0000")

def get_config():
    try:
        config = open("config.txt", "r")
        print("CONFIG.TXT")
        print(config.read())
    except:
        print("write_config()...")
        write_config()

    config = open("config.txt", "r")
    read_config = config.read()

    config_list = read_config.splitlines()
    print("config_list")
    print(*config_list)

    if len(config_list) == 0:
        write_config()
        config = open("config.txt", "r")
        read_config = config.read()

        config_list = read_config.splitlines()
        print("config_list update")
        print(*config_list)

    _locker_code_list = []
    for item in config_list:
        digit_item = ''.join(filter(str.isdigit, item))
        # print(digit_item)
        _locker_code_list.append(digit_item)
    print(_locker_code_list)
    return _locker_code_list

global hex_c, radioVar_selection, radioVar, color_title
theGrey = "#f0f0f0" # Windows default grey
def locker_popupDesign(root, buyer_phone):
    global hex_c, radioVar_selection, radioVar, color_title
    radioVar_selection = 99  # איפוס לפני בחירה

    locker_code_list = get_config()

    # Toplevel object which will
    # be treated as a new window
    lockerPopup = Toplevel(root)
    lockerPopup.focus_force()
    lockerPopup.configure(background="white")
    lockerPopup.title("א.ע")
    lockerPopup.geometry("200x200")

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
        global hex_c, radioVar_selection, radioVar, color_title
        radioVar_selection = int(radioVar.get())
        print(radioVar_selection)
        color_title = ""
        hex_c = "bdbdbd"
        # 0 = יש לבחור
        if radioVar_selection == 1:
            hex_c = "23964e" # Green
            color_title = "לוקר ירוק"
            radioVar_selection = int(radioVar.get())
        if radioVar_selection == 2:
            hex_c = "2d81be" # Blue
            color_title = "לוקר כחול"
            radioVar_selection = int(radioVar.get())
        if radioVar_selection == 3:
            hex_c = "db8400" # Orange
            color_title = "לוקר כתום"
            radioVar_selection = int(radioVar.get())
        if radioVar_selection == 4:
            hex_c = "333333"  # Orange
            color_title = "תיאום טלפוני"
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
                           text=color_title,
                           font = ("rubik", 14, "bold"),
                           )
        titleFrame.place(relx=-0.02, rely=0.07, height=40, width=200)

    radioVar = IntVar()
    ttk.Radiobutton(radioButtonFrame,
                     text="      לוקר ירוק",
                     variable=radioVar,
                     value=1,
                     command=change_selection,
                     style="pickupPopup.TRadiobutton").pack(anchor=W) #.state(['selected'])
    # ----
    ttk.Radiobutton(radioButtonFrame,
                     text="     לוקר כחול",
                     variable=radioVar,
                     value=2,
                     command=change_selection,
                     style="pickupPopup.TRadiobutton").pack(anchor=W) #.state(['selected'])

    # ----
    ttk.Radiobutton(radioButtonFrame,
                     text="    לוקר כתום",
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

    def txtMe_sms_starter():
        global hex_c, radioVar_selection
        # מוודא שנבחר צבע לוקר

        if radioVar_selection > 5:
            title_label.config(background="white",
                               foreground="#333333",
                               text="נא לבחור צבע לוקר",
                               font=("rubik", 14, "bold"))
            # return



        # מוודא שהוכנסו קודי לוקרים
        if green_code_field.get() == "0000" or blue_code_field.get() == "0000" or orange_code_field.get() == "0000":
            print("יש לעדכן קוד לוקרים!")
            # print(green_code_field.get())
            title_label.config(background="white",
                               foreground="#333333",
                               text="נא לעדכן קוד לוקרים",
                               font=("rubik", 14, "bold"))
            return


        # מגדיר לקונפיג קודי לוקרים
        new_config = open("config.txt", "w")
        new_config.write(f"לוקר ירוק: {green_code_field.get()}")
        new_config.write("\n")
        new_config.write(f"לוקר כחול: {blue_code_field.get()}")
        new_config.write("\n")
        new_config.write(f"לוקר כתום: {orange_code_field.get()}")

        _locker_code_field = ""
        if radioVar_selection == 1:
            _locker_code_field = green_code_field.get()
        if radioVar_selection == 2:
            _locker_code_field = blue_code_field.get()
        if radioVar_selection == 3:
            _locker_code_field = orange_code_field.get()
        print("_locker_code_field")
        print(type(_locker_code_field))
        print(_locker_code_field)
            # return

        if radioVar_selection < 10:
            txtMe_sms(message_type = int(radioVar_selection), phone = buyer_phone, locker_code_field = _locker_code_field)
            messagebox.showinfo("אישור סמס", f"(●'◡'●)  סמס הגעה ל{color_title} נשלח ללקוח")
            sleep(0.15)
            lockerPopup.destroy()

    buttonSMSFrame = tk.Frame(lockerPopup, bg=theGrey)  # טקסט המלצה לווידוא פרטים
    buttonSMSFrame.place(relx=0, rely=0.77, height=50, width=200)
    from functools import partial # To add args for the command
    ttk.Button(buttonSMSFrame,
               text="שלח סמס מעקב",
               command= txtMe_sms_starter).pack(pady=11)
               # command= partial(txtMe_sms, message_type=int(radioVar_selection), phone="0584770076")).pack(pady=11)

    green_code_frame = tk.Frame(lockerPopup, bg="#23964e")  # שדה טקסט כמות חבילות
    green_code_frame.place(relx=0.12, rely=0.285, height=22, width=55, )
    green_code_field = ttk.Entry(green_code_frame, font=("rubik", 14), width=30, justify="center", foreground="#23964e")
    green_code_field.pack()
    green_code_field.insert(0, locker_code_list[0]) #Green 1478

    blue_fields_frame = tk.Frame(lockerPopup, bg="#23964e")  # שדה טקסט כמות חבילות
    blue_fields_frame.place(relx=0.12, rely=0.39, height=22, width=55, )
    blue_code_field = ttk.Entry(blue_fields_frame, font=("rubik", 14), width=30, justify="center", foreground="#2d81be")
    blue_code_field.pack()
    blue_code_field.insert(0, locker_code_list[1]) #Blue 2580

    orange_fields_frame = tk.Frame(lockerPopup, bg="#23964e")  # שדה טקסט כמות חבילות
    orange_fields_frame.place(relx=0.12, rely=0.495, height=22, width=55, )
    orange_code_field = ttk.Entry(orange_fields_frame, font=("rubik", 14), width=30, justify="center", foreground="#db8400")
    orange_code_field.pack()
    orange_code_field.insert(0, locker_code_list[2]) #Orange 2356

## Example
# master = Tk()
# locker_popupDesign(master, "0584770076")
# mainloop()