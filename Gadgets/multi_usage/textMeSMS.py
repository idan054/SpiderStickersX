import xml.etree.ElementTree as ET
import requests

from Gadgets.multi_usage.bcolors import bcolors


def txtMe_sms(message, phone):
    url = "https://my.textme.co.il/api"

    payload = f"""
    <?xml version="1.0" encoding="UTF-8"?>
    <sms>
    <user>
    <username>idanbit80@gmail.com</username>
    <password>On4WP2F5</password>
    </user>
    <source>Spider 3D</source>
    <destinations>
    <phone>{phone}</phone>
    </destinations>
    <message>{message}</message>
    </sms>
    """
    # print(payload)

    headers = {
        'Content-Type': 'application/xml',
        'Cookie': 'incap_ses_892_2155087=jb7rUkSp2k9nKrQDhQVhDLTyQWAAAAAAnpxXW32Fp3EUK4vulboq6w==; nlbi_2155087=9PrGSQ6vuly5J6gJlxrJ6wAAAADCxR/P7O6yQgSrYVOLd0g7; visid_incap_2155087=Nz2nCoofQyS9ZAulTLmrS7PyQWAAAAAAQUIPAAAAAABmlFA4hVbzDOUXBW/GMQYi; ci_session=a%3A5%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%226e5d70edde47cff3d8f6ec5910925f81%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A7%3A%220.0.0.0%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A22%3A%22PostmanRuntime%2F7.26.10%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1614934708%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7Ded4595a1617c74180210add2c9fb5dcd'
    }

    response = requests.request("POST", url, headers=headers, data=payload.encode('utf-8'))
    # print(response.content)
    print(f"{bcolors.Yellow}SMS will be sent{bcolors.Normal}")
    # return response

# response_content = """b'<?xml version="1.0" encoding="utf-8"?>\n<sms><status>0</status><message>SMS will be sent</message><shipment_id>890578760</shipment_id></sms>\n'"""

## Example
# txtMe_sms(message="עוד דוגמא", phone="0584770076")

