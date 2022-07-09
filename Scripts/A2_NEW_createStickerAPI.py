import secrets
from pprint import pprint
import requests, pickle
import json
import os
import shutil
import random

from datetime import datetime


# def create_delivery():
def create_deliveryBaldar(
                  # delivery_company,
                  buyer_city, buyer_name,
                  clean_address, buyer_phone, buyer_email,
                  buyer_notes, orderNum, packNum,
                  browser=None,  buyer_street= "", buyer_street_number="",):
    session = requests.session()
    now = datetime.now()
    # print(now.strftime("%d/%m/%Y %H:%M:%S"))
    url = "https://www.cargo-ship.co.il/Baldar/NewDelivery.aspx/SaveDelivery1"

    payload = {
            "deliveryParams": [
                "2660",
                "7499",
                "חידקל",
                "11",
                "",
                "",
                "",
                "",
                "-1",
                "-1",
                "סתם רחוב",
                "233",
                "11",
                "",
                "",
                "0584770076",
                "idanbit80@gmail.com",
                "09/07/2022",
                "",
                "",
                "1",
                "1",
                "0",
                "0",
                "1",
                "אפרת",
                "1",
                "עידן בדיקה",
                "spider3d",
                "הערות מודגשות מסומן :: הערות והרבה כלליות :: ישוב יעד: סתם יישוב :: רחוב יעד: סתם רחוב",
                "",
                # True,
                "true",
                "false",
                "",
                "",
                0,
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                ""
            ]
    }

    import json
    # payload = json.dumps(payload)

    # from querystring_parser import builder as qsbuilder
    # payload = qsbuilder.build(payload)  # .replace("[", "%5B").replace("]", "%5D")
    # print(payload)

    response = session.post(url,
                            # headers=headers,  # No Need, already in session
                            data=payload)

    # print("response.text Has been copied to clipboard")
    # pyperclip.copy(response.text)

    if response.status_code == 200:
        print(response.status_code)
        pprint(response.url)
        print("Delivery has been created successfully")
    else:
        print(response.status_code)
        print(response.text)  # <title>The change you wanted was rejected (422)</title>
    return response.json()

# _status_code = create_deliveryBaldar(
#                   buyer_city="תל אביב", buyer_name="אח חינו",
#                   clean_address="ויצמן 90", buyer_phone="0585551234", buyer_email="EFE@GGEG.COM",
#                   buyer_notes="פילמנט כתום", orderNum="32045", packNum="2")
# pprint(_status_code)




