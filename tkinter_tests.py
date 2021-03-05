import winsound
import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk

# creates a Tk() object
from Scripts.A1_wooGetAPI import woocomarce_api

master = Tk()
# master.configure(background="blue")

# sets the geometry of main  
# root window 
master.geometry("200x200")

theGrey = "#f0f0f0" # Windows default grey
def openNewWindow():

    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(master)
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
    radioButtonFrame.place(relx=0.26, rely=0.28, height=500, width=200)

    titleFrame = tk.Frame(newWindow, bg="white")  # טקסט המלצה לווידוא פרטים
    titleFrame.place(relx=0.0, rely=0.03, height=40, width=200, )
    title_label = Label(titleFrame,
                text="בחר לוקר למסירת \nאיסוף עצמי",
                font=("rubik", 12, "bold"),
                bg="white",
                fg="black")
    title_label.pack(pady=0)

    # pickup_sms_with_args = pickup_sms(buyer_phone="0584770076", message_type=2)

    buttonSMSFrame = tk.Frame(newWindow, bg=theGrey)  # טקסט המלצה לווידוא פרטים
    buttonSMSFrame.place(relx=0, rely=0.77, height=50, width=200)
    ttk.Button(buttonSMSFrame,
               text="שלח סמס מעקב",
               command=openNewWindow).pack(pady=11)

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

    # green_code_frame = tk.Frame(newWindow, bg="#23964e")  # שדה טקסט כמות חבילות
    # green_code_frame.place(relx=0.12, rely=0.285, height=22, width=55, )
    # green_code_field = ttk.Entry(green_code_frame, font=("rubik", 14), width=30, justify="center", foreground="#23964e")
    # green_code_field.pack()
    # green_code_field.insert(0, "1478")
    #
    # blue_fields_frame = tk.Frame(newWindow, bg="#23964e")  # שדה טקסט כמות חבילות
    # blue_fields_frame.place(relx=0.12, rely=0.39, height=22, width=55, )
    # blue_code_field = ttk.Entry(blue_fields_frame, font=("rubik", 14), width=30, justify="center", foreground="#2d81be")
    # blue_code_field.pack()
    # blue_code_field.insert(0, "2580")
    #
    # orange_fields_frame = tk.Frame(newWindow, bg="#23964e")  # שדה טקסט כמות חבילות
    # orange_fields_frame.place(relx=0.12, rely=0.495, height=22, width=55, )
    # blue_code_field = ttk.Entry(orange_fields_frame, font=("rubik", 14), width=30, justify="center", foreground="#db8400")
    # blue_code_field.pack()
    # blue_code_field.insert(0, "2356")

def msg():
    first_name, last_name, address_1, street_num, street, city, \
    email, phone, high_quantity, deliveryNeeded, customer_note = woocomarce_api(numOrder=27695)

    if not deliveryNeeded:
        value = messagebox.askyesno(
            "איסוף עצמי", """"¯\_(ツ)_/¯  אין צורך ביצירת משלוח, הזמנה זו היא איסוף עצמי
                                                          ?ליצור משלוח בכל זאת""",
            default='no')
        print(value)
        ## When delivery no needed.
        if not value:  # default is False - לא ליצור משלוח
            openNewWindow()
            # browser.quit()  # סוגר את הכרום

# function to open a new window  
# on a button click
hex_c = "fbfbfb"
ttk.Style(master).configure('myStyle.TRadiobutton',
                            foreground='black',
                            font = ("rubik", 9, "bold"))

# a button widget which will open a  
# new window on button click 
btn = ttk.Button(master,
             text="Click to open a new window",
             command=openNewWindow)
btn.pack(pady=10)

# mainloop, runs infinitely 
mainloop() 