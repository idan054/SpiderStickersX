import tkinter as tk
from time import sleep
from tkinter import *
from tkinter import ttk, messagebox
#
# from Gadgets.pickup_sms import pickup_sms
#
from Gadgets.multi_usage.textMeSMS import txtMe_sms

theGrey = "#f0f0f0" # Windows default grey

## Not in use.
global hex_c, radioVar_selection, radioVar, color_title

def locker_popupDesign(root, buyer_phone):
    global hex_c, radioVar_selection, radioVar, color_title

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
    radioButtonFrame.place(relx=0.26, rely=0.28, height=500, width=200)

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
        if radioVar.get() == 1:
            hex_c = "23964e" # Green
            color_title = "לוקר ירוק"
            radioVar_selection = int(radioVar.get())
        if radioVar.get() == 2:
            hex_c = "2d81be" # Blue
            color_title = "לוקר כחול"
            radioVar_selection = int(radioVar.get())
        if radioVar.get() == 3:
            hex_c = "db8400" # Orange
            color_title = "לוקר כתום"
            radioVar_selection = int(radioVar.get())
        if radioVar.get() == 4:
            hex_c = "333333"  # Orange
            color_title = "תיאום טלפוני"
            radioVar_selection = int(radioVar.get())

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
        try:
            print(f"radioVar_selection is {radioVar_selection} (from txtMe_sms_starter)")
        except:
            title_label.config(background="white",
                               foreground="#333333",
                               text="נא לבחור אופציה",
                               font=("rubik", 14, "bold"))
        txtMe_sms(message_type = int(radioVar_selection), phone = buyer_phone)
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

    # green_code_frame = tk.Frame(lockerPopup, bg="#23964e")  # שדה טקסט כמות חבילות
    # green_code_frame.place(relx=0.12, rely=0.285, height=22, width=55, )
    # green_code_field = ttk.Entry(green_code_frame, font=("rubik", 14), width=30, justify="center", foreground="#23964e")
    # green_code_field.pack()
    # green_code_field.insert(0, "1478")
    #
    # blue_fields_frame = tk.Frame(lockerPopup, bg="#23964e")  # שדה טקסט כמות חבילות
    # blue_fields_frame.place(relx=0.12, rely=0.39, height=22, width=55, )
    # blue_code_field = ttk.Entry(blue_fields_frame, font=("rubik", 14), width=30, justify="center", foreground="#2d81be")
    # blue_code_field.pack()
    # blue_code_field.insert(0, "2580")
    #
    # orange_fields_frame = tk.Frame(lockerPopup, bg="#23964e")  # שדה טקסט כמות חבילות
    # orange_fields_frame.place(relx=0.12, rely=0.495, height=22, width=55, )
    # blue_code_field = ttk.Entry(orange_fields_frame, font=("rubik", 14), width=30, justify="center", foreground="#db8400")
    # blue_code_field.pack()
    # blue_code_field.insert(0, "2356")

## Example
# master = Tk()
# locker_popupDesign(master, "0584770076")
# mainloop()