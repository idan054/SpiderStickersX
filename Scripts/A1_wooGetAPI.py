import requests
from requests.structures import CaseInsensitiveDict
from woocommerce import API

## A1 Get order details from Woo API
# To get headers["Authorization"] Token: insert Woo Api customer_key & secret_key
# as user & pass in https://reqbin.com/ with the url above
woo_token = "Basic Y2tfYjk2M2MwNTMzMTQwNTY2MmQzYmJlNzlkZDhiMjA1MTJiNTZkN2UxNTpjc19mYThkNTU0ZGYxNzZmN2I0NDllZjZhM2Q4Y2U0MDM4OTU4ZjJhZTQx"

def woocomarce_api(numOrder):

    # FUCK I JUST FOUND THERE WAS A PACAKGE! Well, What was I thinking?..
    #     wcapi = API(
    #         url="https://www.spider3d.co.il",
    #         consumer_key="ck_b963c05331405662d3bbe79dd8b20512b56d7e15",
    #         consumer_secret="cs_fa8d554df176f7b449ef6a3d8ce4038958f2ae41",
    #         wp_api=True,
    #         version="wc/v3",
    #         query_string_auth=True
    #     )


    # url = "https://spider3d.co.il/wp-json/wc/v3/orders" # כלל ההזמנות
    url = f"https://www.spider3d.co.il/wp-json/wc/v3/orders/{numOrder}"
    # numOrder = "27695" # איסוף עצמי
    # numOrder = "25560" # Eyal Biton הזמנה עבור
    # numOrder = "27692" # כולל הערות + כמות גבוהה

    headers = CaseInsensitiveDict()
    # To get headers["Authorization"] Token: insert Woo Api customer_key & secret_key
    # as user & pass in https://reqbin.com/ with the url above
    headers["Authorization"] = woo_token
    # data = {
    #     "status": "completed",
    # }

    # resp = requests.get(url, headers=headers, data=data)
    resp = requests.get(url, headers=headers)

    print(resp.status_code)
    print(resp.text)
    order_details = resp.json()
    # print('order_details')
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

    first_name = try_get_item(order_details ["billing"]["first_name"])
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
    print("products_details length is ", len(products_details))
    high_quantity = False
    for product in products_details: # High quantity Checker
        if product["quantity"] != 1:
            print('product["quantity"]' , product["quantity"])
            high_quantity = True
        break

    # print('deliveryNeeded' , deliveryNeeded)
    try:
        deliveryNeeded = order_details["shipping_lines"][0]["method_title"]
    except: # when Null
        deliveryNeeded = "איסוף עצמי"

    if "איסוף עצמי" in deliveryNeeded:
        deliveryNeeded = False  # אין צורך במשלוח
    else:
        deliveryNeeded = True
    print("deliveryNeeded? ", deliveryNeeded)

    return first_name, last_name, address_1, street_num, street, city,\
           email, phone, high_quantity, deliveryNeeded, customer_note

# woocomarce_api(numOrder=28020)
# woocomarce_api(numOrder=45026)