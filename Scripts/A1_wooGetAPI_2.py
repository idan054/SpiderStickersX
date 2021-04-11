import requests
from requests.structures import CaseInsensitiveDict


## A1 Get order details from Woo API


def woocomarce_api():

    url = "https://spider3d.co.il/wp-json/wc/v3/orders/?status=processing&per_page=99" # כלל ההזמנות
    # url = f"https://spider3d.co.il/wp-json/wc/v3/orders/{numOrder}"
    # numOrder = "27695" # איסוף עצמי
    # numOrder = "25560" # Eyal Biton הזמנה עבור
    # numOrder = "27692" # כולל הערות + כמות גבוהה

    headers = CaseInsensitiveDict()
    headers["Authorization"] = \
        "Basic Y2tfMzAyZWJkYmQ4OTNjNzU2YTFlOTlmZjhlZmNjMzZiYjYzNWZjNDRjNzpjc19lMTUyMTc0MWJlNDYzMWZjMzljMTQyNzUwZDg0YmU2YTJiYWVlMWIx"

    # resp = requests.get(url, headers=headers, data=data)
    resp = requests.get(url, headers=headers)

    print(resp.status_code)
    order_details = resp.json()
    print(len(order_details))
    print(order_details)


# woocomarce_api(numOrder=27975)
# woocomarce_api(numOrder=25560)
woocomarce_api()