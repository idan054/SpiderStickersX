from functools import reduce
from tkinter import messagebox

import requests
from requests.structures import CaseInsensitiveDict

from Gadgets.bcolors import bcolors

def woocomarce_api(numOrder):
    # url = "https://spider3d.co.il/wp-json/wc/v3/orders/27975" # לקוח כולל הערה

    url = f"https://spider3d.co.il/wp-json/wc/v3/orders/{numOrder}"
    # numOrder = "27695" # איסוף עצמי
    # numOrder = "25560" # Eyal Biton הזמנה עבור
    # numOrder = "27692" # כולל הערות + כמות גבוהה

    headers = CaseInsensitiveDict()
    headers["Authorization"] = \
        "Basic Y2tfMzAyZWJkYmQ4OTNjNzU2YTFlOTlmZjhlZmNjMzZiYjYzNWZjNDRjNzpjc19lMTUyMTc0MWJlNDYzMWZjMzljMTQyNzUwZDg0YmU2YTJiYWVlMWIx"

    resp = requests.get(url, headers=headers)

    print(resp.status_code)
    order_details = resp.json()
    # print(order_details["billing"])

    first_name = order_details["billing"]["first_name"]
    print("first_name is ", first_name)

    last_name = order_details["billing"]["last_name"]
    print("last_name is ", last_name)

    address_1 = order_details["billing"]["address_1"]
    print("address_1 is ", address_1)

    street_num = int( ''.join(filter(str.isdigit, address_1)))
    print("street_num is ", street_num)

    street_list = order_details["billing"]["address_1"]
    street_list = street_list.split()
    street = ' '.join([str(item) for item in street_list[:-1]]) # List to str
    print("street is ", street)

    city = order_details["billing"]["city"]
    print("city is ", city)

    email = order_details["billing"]["email"]
    print("email is ", email)

    phone = order_details["billing"]["phone"]
    print("phone is ", phone)

    products_details = order_details["line_items"]
    high_quantity = False
    for product in products_details: # High quantity Checker
        # print(product["quantity"])
        if product["quantity"] != 1:
            high_quantity = True
        break

    deliveryNeeded = order_details["shipping_lines"][0]["method_title"]
    if "איסוף עצמי" in deliveryNeeded:
        deliveryNeeded = False  # אין צורך במשלוח
    else:
        deliveryNeeded = True
    print("deliveryNeeded? ", deliveryNeeded)

    customer_note = order_details["customer_note"]
    print("customer_note is ", customer_note)

    return first_name, last_name, address_1, street_num, street, city,\
           email, phone, high_quantity, deliveryNeeded, customer_note

# woocomarce_api(numOrder=27975)
# woocomarce_api(numOrder=25560)