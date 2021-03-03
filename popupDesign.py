import winsound
from time import sleep
import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk

theGrey = "#f0f0f0" # Windows default grey

master = Tk()

def openNewWindow(root):
    print("Opening new window...")
    # Toplevel object which will
    # be treated as a new window

    newWindow = Toplevel(root)
    # newWindow = Tk()
    newWindow.configure(background="white")
    newWindow.geometry("200x160")
    newWindow.title("א.ע")
    newWindow.focus_force()
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
openNewWindow(master)

mainloop()