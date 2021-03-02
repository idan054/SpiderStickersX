# This will import all the widgets 
# and modules which are available in 
# tkinter and ttk module 
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

# creates a Tk() object 
master = Tk()
master.configure(background="#ffffff")
hex_c = "fbfbfb"
ttk.Style(master).configure('myStyle.TRadiobutton', background=f"#{hex_c}", foreground='white', font = ("rubik", 9))

# sets the geometry of main  
# root window 
master.geometry("200x200")


# function to open a new window  
# on a button click 
def openNewWindow():
    # Toplevel object which will
    # be treated as a new window 
    newWindow = Toplevel(master)

    # sets the title of the 
    # Toplevel widget 
    newWindow.title("New Window")

    # sets the geometry of toplevel 
    newWindow.geometry("200x200")

    # A Label widget to show in toplevel 
    Label(newWindow,text="This is a new window").pack()

    # region כפתורי רדיו
    def change_selection():
        hex_c = "000000"
        ttk.Style(master).configure('myStyle.TRadiobutton', background=f"#{hex_c}", foreground='white',
                                    font=("rubik", 9))
        newWindow.configure(background="#23964e")
        selection = "You selected the option " + str(radioVar.get())
        Label(master).config(text=selection)
        print(radioVar.get())
        chrome_ver = radioVar.get()
        print("Chrome_ver is " + str(chrome_ver))


    radioVar = IntVar()
    R1 = ttk.Radiobutton(newWindow, text="לוקר ירוק", variable=radioVar, value=1, command=change_selection,
                         style="myStyle.TRadiobutton")
    # ----
    R1.pack(anchor=W)
    # ----
    R2 = ttk.Radiobutton(newWindow, text="לוקר כחול", variable=radioVar, value=2, command=change_selection,
                         style="myStyle.TRadiobutton")
    R2.pack(anchor=W)
    R2.state(['selected'])
    # ----
    R3 = ttk.Radiobutton(newWindow, text="לוקר כתום", variable=radioVar, value=3, command=change_selection,
                         style="myStyle.TRadiobutton")
    R3.pack(anchor=W)


label = Label(master,
              text="This is the main window")

label.pack(pady=10)

# a button widget which will open a  
# new window on button click 
btn = Button(master,
             text="Click to open a new window",
             command=openNewWindow)
btn.pack(pady=10)

# mainloop, runs infinitely 
mainloop() 