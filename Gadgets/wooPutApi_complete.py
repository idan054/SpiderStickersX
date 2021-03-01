import requests
from requests.structures import CaseInsensitiveDict
from Gadgets.bcolors import bcolors


def woocomarce_put_api(numOrder):
    url = f"https://spider3d.co.il/wp-json/wc/v3/orders/{numOrder}/notes"

    headers = CaseInsensitiveDict()
    headers["Authorization"] = \
        "Basic Y2tfMzAyZWJkYmQ4OTNjNzU2YTFlOTlmZjhlZmNjMzZiYjYzNWZjNDRjNzpjc19lMTUyMTc0MWJlNDYzMWZjMzljMTQyNzUwZDg0YmU2YTJiYWVlMWIx"

    data = {
        "status": "completed"
    }

    print(requests.put(url=url, headers=headers, data=data).json())