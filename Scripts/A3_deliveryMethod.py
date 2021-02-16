from tkinter import messagebox
# deliveryMethod = browser.find_element_by_id("order_shipping_line_items").text
from Gadgets.bcolors import bcolors

def deliveryMethod_checker(deliveryMethod):
    # אם "איסוף עצמי" נמצא בשיטת המשלוח, עצור את ה Def כולו
    if "איסוף עצמי" in deliveryMethod:
        print(f"{bcolors.Yellow}{bcolors.BOLD}"
              f' STOP! - עוצר. "איסוף עצמי" נמצא '
              f"{bcolors.Normal}")
        messagebox.showinfo("איסוף עצמי", "¯\_(ツ)_/¯  אין צורך ביצירת משלוח, הזמנה זו היא איסוף עצמי")
        # return # אם איסוף עצמי - הפסק את ה Def של MakeSticker
        return False
    else:
        print("Keep Going - !איסוף עצמי לא נמצא, ממשיך לעבוד")
        return True