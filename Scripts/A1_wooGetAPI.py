import requests
from requests.structures import CaseInsensitiveDict


## A1 Get order details from Woo API


def woocomarce_api(numOrder):

    # url = "https://spider3d.co.il/wp-json/wc/v3/orders" # כלל ההזמנות
    url = f"https://spider3d.co.il/wp-json/wc/v3/orders/{numOrder}"
    # numOrder = "27695" # איסוף עצמי
    # numOrder = "25560" # Eyal Biton הזמנה עבור
    # numOrder = "27692" # כולל הערות + כמות גבוהה

    headers = CaseInsensitiveDict()
    headers["Authorization"] = \
        "Basic Y2tfMzAyZWJkYmQ4OTNjNzU2YTFlOTlmZjhlZmNjMzZiYjYzNWZjNDRjNzpjc19lMTUyMTc0MWJlNDYzMWZjMzljMTQyNzUwZDg0YmU2YTJiYWVlMWIx"

    # data = {
    #     "status": "completed",
    # }

    # resp = requests.get(url, headers=headers, data=data)
    resp = requests.get(url, headers=headers)

    print(resp.status_code)
    order_details = resp.json()
    # print(order_details)
    # print(len(order_details))

    def try_get_item(json_path):
        try:
            item = json_path
            return item
        except ValueError as e:
            e = str(e)
            print("just_try() Error:")
            print(e)
            item = ""
            return item

    first_name = try_get_item(order_details["billing"]["first_name"])
    print("first_name is ", first_name)

    last_name = try_get_item(order_details["billing"]["last_name"])
    print("last_name is ", last_name)

    address_1 = try_get_item(order_details["billing"]["address_1"])
    print("address_1 is ", address_1)

    # street_num = int(''.join(filter(str.isdigit, address_1)))
    street_num = ''.join(filter(str.isdigit, address_1))
    try: int(street_num)
    except: pass
    print("street_num is ", street_num)

    street_list = address_1
    street_list = street_list.split()
    street = ' '.join([str(item) for item in street_list[:-1]]) # List to str
    print("street is ", street)

    city = try_get_item(order_details["billing"]["city"])
    print("city is ", city)

    email = try_get_item(order_details["billing"]["email"])
    print("email is ", email)

    phone = try_get_item(order_details["billing"]["phone"])
    print("phone is ", phone)

    customer_note = try_get_item(order_details["customer_note"])
    print("customer_note is ", customer_note)

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

    return first_name, last_name, address_1, street_num, street, city,\
           email, phone, high_quantity, deliveryNeeded, customer_note

# woocomarce_api(numOrder=27975)
woocomarce_api(numOrder=25560)