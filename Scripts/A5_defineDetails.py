from functools import reduce
from tkinter import messagebox


def tween(_list): #פעולה מהאינטרנט להוספת רווח בין ערכים ברשימה
    return reduce(lambda r,v: r+[" ",v], _list[1:], _list[:1])

def define_address_details(browser):

    # פרטי משלוח מבוססים מידע הזמנה בוורדפרס
    address_class = browser.find_element_by_class_name("address")
    print(address_class.text)
    address_p = address_class.find_element_by_tag_name("p")
    print(address_p.text)
    print("-------------------")
    # print(address_p.text.splitlines())
    address_attributes = address_p.text.splitlines()  # יוצר רשימה שכל שורה בטקסט היא ערך
    clean_address = address_attributes[1:]  # .replace("[", "").replace("]", "")  # כל הערכים ללא הראשון (עד הסוף)
    print(*clean_address)  # כל הערכים ללא הראשון (עד הסוף)
    print("פרטי המשלוח הם " + str(address_attributes))

    print("שם הלקוח הוא " + address_attributes[0])
    buyer_name = address_attributes[0]  # שם הלקוח

    fullStreet = address_attributes[1]
    print("רחוב, דירה..: " + fullStreet)

    # using join and isdigit
    # to remove numeric digits from string
    # .תצרף (לערך המעודכן) אם לא מספר
    # buyer_street = ''.join([local_x for local_x in address_attributes[1] if not local_x.isdigit()])

    parts_of_buyer_street = address_attributes[1].split()
    print(address_attributes[1].split())

    print("מס הרחוב הוא " + parts_of_buyer_street[-1])
    buyer_street_number = parts_of_buyer_street[-1]

    print \
        ("שם הרחוב הוא " + str(parts_of_buyer_street[0:-1]))  # תדפיס את כל חלקי הרחוב חוץ מהאחרון (שמייצג את מס' הרחוב)
    buyer_street =  parts_of_buyer_street[0:-1]  # ["אבו","דאבי"]
    buyer_street = tween(buyer_street)

    buyer_city = address_attributes[-1]  # הערך האחרון בחלקי המשלוח הוא העיר
    print("העיר היא " + buyer_city)

    buyer_details = address_class.text.replace(address_p.text, "")  # הפרטים הנקיים של הלקוח
    buyer_details = buyer_details.splitlines()
    print(buyer_details)

    ## PART 2

    buyer_phone = browser.find_element_by_xpath('//*[@id="order_data"]/div[1]/div[2]/div[1]/p[3]/a')
    buyer_phone = buyer_phone.text
    print("buyer_phone is " + buyer_phone)
    # buyer_phone = buyer_details[4]
    # print(buyer_details[4] + " טלפון הלקוח ")

    buyer_email = browser.find_element_by_xpath('//*[@id="order_data"]/div[1]/div[2]/div[1]/p[2]/a')
    buyer_email = buyer_email.text
    print("buyer_email is " + buyer_email)
    # buyer_email = buyer_details[2]
    # print(buyer_details[2] + " מייל הלקוח ")

    try:
        buyer_notes = browser.find_element_by_class_name("order_note")
        buyer_notes = buyer_notes.text
        print(buyer_notes)
        messagebox.showinfo("הערה מהלקוח", "ಠ_ಠ שים לב להערה של הלקוח")
    except:
        print("no  notes from buyer")
        buyer_notes = ""

    # global buyer_city
    # global buyer_street
    # global buyer_street_number
    # global buyer_name
    # global clean_address
    #
    # global buyer_phone
    # global buyer_email
    # global buyer_notes

    return  buyer_city, buyer_street ,buyer_street_number,\
            buyer_name, clean_address ,buyer_phone, buyer_email, buyer_notes