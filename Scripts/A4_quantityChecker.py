from tkinter import messagebox

from Gadgets.bcolors import bcolors


def quantityChecker(browser):
    productList = browser.find_element_by_id("order_line_items")
    productListString = productList.text
    # print(str(productList.text))
    print("------------------------")
    quantity = 2
    while quantity < 999:
        # print(str(quantity) +  "מנסה לחפש כמות ")
        if "× " + str(quantity) in str(productListString):
            print(f"{bcolors.Yellow}{bcolors.BOLD}"
                  f"יש כפילות"
                  f"{bcolors.Normal}")
            messagebox.showinfo("מוצר כפול", "╰(*°▽°*)╯  בהזמנה זו יש מוצרים בכמות גבוהה")
            break
        quantity += 1