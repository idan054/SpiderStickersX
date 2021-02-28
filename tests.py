from tkinter import messagebox

# messagebox.showinfo("איסוף עצמי", "¯\_(ツ)_/¯  אין צורך ביצירת משלוח, הזמנה זו היא איסוף עצמי")

x = messagebox.askyesno(
    "איסוף עצמי", """"¯\_(ツ)_/¯  אין צורך ביצירת משלוח, הזמנה זו היא איסוף עצמי
                                                          ?ליצור משלוח בכל זאת""",
default='no')
print(x)
