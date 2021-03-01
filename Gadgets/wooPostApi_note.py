import requests
from requests.structures import CaseInsensitiveDict
from Gadgets.bcolors import bcolors


def woocomarce_post_api(numOrder, note):
    url = f"https://spider3d.co.il/wp-json/wc/v3/orders/{numOrder}/notes"


    headers = CaseInsensitiveDict()
    headers["Authorization"] = \
        "Basic Y2tfMzAyZWJkYmQ4OTNjNzU2YTFlOTlmZjhlZmNjMzZiYjYzNWZjNDRjNzpjc19lMTUyMTc0MWJlNDYzMWZjMzljMTQyNzUwZDg0YmU2YTJiYWVlMWIx"


    data = {
        "note": note,
        "customer_note": True  # נשלח אל הלקוח
    }

    print(requests.post(url=url, headers=headers, data=data).json())