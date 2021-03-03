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
    newWindow.configure(background="white")
    newWindow.title("New Window")
    newWindow.focus_force()
    newWindow.geometry("200x160")

    # sets the geometry of toplevel

    ttk.Style(newWindow).configure('myStyle.TRadiobutton',
                                foreground='black',
                                background="white",
                                font=("rubik", 10))

    # sets the geometry of toplevel

    # A Label widget to show in toplevel
    radioButtonFrame = tk.Frame(newWindow, bg="white")  # טקסט המלצה לווידוא פרטים
    radioButtonFrame.place(relx=0.27, rely=0.32, height=500, width=200)

    titleFrame = tk.Frame(newWindow, bg="white")  # טקסט המלצה לווידוא פרטים
    titleFrame.place(relx=0.0, rely=0.03, height=40, width=200, )
    title_label = Label(titleFrame,
                text="בחר לוקר למסירת \nאיסוף עצמי",
                font=("rubik", 12, "bold"),
                bg="white",
                fg="black")
    title_label.pack(pady=0)

    buttonSMSFrame = tk.Frame(newWindow, bg=theGrey)  # טקסט המלצה לווידוא פרטים
    buttonSMSFrame.place(relx=0, rely=0.77, height=45, width=200)
    ttk.Button(buttonSMSFrame,
               text="שלח סמס מעקב",
               command=openNewWindow).pack(pady=5)

    # region כפתורי רדיו
    def change_selection():
        global hex_c
        selection = "You selected the option " + str(radioVar.get())
        print(selection)
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

        ## Change backgrounds & frames
        # radioButtonFrame.configure(background=f"#{hex_c}")
        # titleFrame.configure(background=f"#{hex_c}")
        # newWindow.configure(background=f"#{hex_c}") # Green
        # ttk.Style(master).configure('myStyle.TRadiobutton', background=f"#{hex_c}", foreground='white', font=("rubik", 9, "bold"))
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
                     text="לוקר ירוק",
                     variable=radioVar,
                     value=1,
                     command=change_selection,
                     style="myStyle.TRadiobutton").pack(anchor=W) #.state(['selected'])
    # ----
    ttk.Radiobutton(radioButtonFrame,
                     text="לוקר כחול",
                     variable=radioVar,
                     value=2,
                     command=change_selection,
                     style="myStyle.TRadiobutton").pack(anchor=W) #.state(['selected'])

    # ----
    ttk.Radiobutton(radioButtonFrame,
                     text="לוקר כתום",
                     variable=radioVar,
                     value=3,
                     command=change_selection,
                     style="myStyle.TRadiobutton").pack(anchor=W) #.state(['selected'])

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
             command=msg)
btn.pack(pady=10)

# mainloop, runs infinitely 
mainloop() 