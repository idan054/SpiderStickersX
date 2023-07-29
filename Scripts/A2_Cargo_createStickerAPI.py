from pprint import pprint

import html_to_json
import requests, pickle
from datetime import datetime

global browser, finalOrderLink, buyer_name, butikTrackNumber, butikBarCode, buyer_phone, api_output

# def create_delivery():\
# Woo order 28728
def create_deliveryCargo(
                  delivery_company,
                  buyer_city, buyer_name,
                  clean_address, buyer_phone, buyer_email,
                  buyer_notes, orderNum, packNum,
                  browser=None,  buyer_street= "", buyer_street_number="",):
    session = requests.session()
    now = datetime.now()
    # print(now.strftime("%d/%m/%Y %H:%M:%S"))
    print('create_deliveryCargo() delivery_company:')
    print(delivery_company)

    # url = "http://185.241.7.143/Baldarp/service.asmx/SaveData" # CARGO OLD
    url = "http://45.83.40.28/Baldarp/service.asmx/SaveData" # CARGO NEW
    payload = f'pParam=' \
              f'1;חידקל;11;יבנה ;{buyer_street}' \
              f';{clean_address};{buyer_city} ;ספיידר 3D' \
              f';{buyer_name} ; - {buyer_notes}' \
              f';1' \
              f';1' \
              f';1' \
              f';{packNum}' \
              f';1' \
              f';0' \
              f';Woo #{orderNum};' \
              f'3131;' \
              f'0' \
              f';' \
              f';0;עיר-מוצא-2' \
              f';;{buyer_email} - {buyer_phone};;0'

    if delivery_company == 40: # Sales4U
        url = "http://185.108.80.50:8050/Baldarp/service.asmx/SaveData"

        payload = f'pParam=' \
                  f'1;חידקל;11;יבנה ;{buyer_street}' \
                  f';{clean_address};{buyer_city} ;ספיידר 3D' \
                  f';{buyer_name} ; - {buyer_notes}' \
                  f';1' \
                  f';1' \
                  f';1' \
                  f';{packNum}' \
                  f';1' \
                  f';0' \
                  f';Woo #{orderNum};' \
                  f'118;' \
                  f'0' \
                  f';' \
                  f';0;עיר-מוצא-2' \
                  f';;{buyer_email} - {buyer_phone};;0'

    print('U R L')
    print(url)

    headers = { 'Content-Type': 'application/x-www-form-urlencoded' }

    print('PAYLOAD')
    print(payload)

    response = session.post(url,headers=headers, data=payload.encode())

    if response.status_code == 200:
        print(response.status_code)
        pprint(response.url)
        print("Delivery has been created successfully")
        print(response.text)  #
    else:
        print(response.status_code)
        print(response.text)  # <title>The change you wanted was rejected (422)</title>

    # ITS ACTUALLY XML (LOL)
    output_json = html_to_json.convert(response.text)
    print("output_json['int'][0]['_value']")
    print(output_json['int'][0]['_value'])

    # return response.json()
    return output_json['int'][0]['_value'] # 53473415

# _status_code =\

# create_deliveryCargo(
#               buyer_city="תל אביב", buyer_name="אח חינו",
#               clean_address="ויצמן 90", buyer_phone="0585551234", buyer_email="EFE@GGEG.COM",
#               buyer_notes="פילמנט כתום", orderNum="32045", packNum="2")

# pprint(_status_code)




