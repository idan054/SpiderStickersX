import xml.etree.ElementTree as ET
import requests
from Gadgets.multi_usage.bcolors import bcolors

global locker_color, locker_code, final_msg
def txtMe_sms(message_type, phone, butikTrackNumber=None, locker_code_field="0110"): #butikTrackNumber no needed on pickup
    global locker_color, locker_code, final_msg
    print("message_type = ", message_type)

    # locker_color = "הירוק 🟢"
    # locker_color = "הכחול 🔵"
    # locker_color = "הכתום 🟠"

    # message_type = 0 # no selection

    if message_type == 1 : # locker
        locker_color = "הירוק 🟢"
        # locker_code =  "1478"
        locker_code =  locker_code_field
    if message_type == 2 : # locker
        locker_color = "הכחול 🔵"
        # locker_code =  "2580"
        locker_code =  locker_code_field
    if message_type == 3 : # locker
        locker_color = "הכתום 🟠"
        # locker_code =  "2356"
        locker_code =  locker_code_field
    if message_type < 4 : # phone pickup
        final_msg = f"""איזה כיף, ההזמנה שלך מוכנה לאיסוף :)
ניתן לאסוף כעת בכתובת חבקוק 114, גדרה
החבילה זמינה 24/7 בלוקר {locker_color}
קוד: *️⃣ {locker_code} ומפתח 🔑
בברכה, צוות ספיידר 3D"""
    if message_type == 4:  # delivery
        final_msg = f"""איזה כיף, ההזמנה שלך מוכנה לאיסוף :)
        ניתן לאסוף כעת בכתובת חבקוק 114, גדרה
        אנא צור קשר לפני הגעה כדי שנוציא לך את החבילה
        052-2509900
        בברכה, צוות ספיידר 3D"""
    if message_type == 5 : # delivery
        # 60 Character Example ( Until 70 -> 0.078$ = 0.26₪ On callr)
        final_msg = f"""משלוח מהיר עם ההזמנה שלך נאסף מספיידר 3D
        מס' מעקב {butikTrackNumber}
        טל' 035109114"""

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
    <message>{final_msg}</message>
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


# pickup_msg_123 = f"""איזה כיף, ההזמנה שלך מוכנה לאיסוף :)
# ניתן לאסוף כעת בכתובת חבקוק 114, גדרה
# החבילה זמינה 24/7 בלוקר {locker_color}
# קוד: *️⃣ 1478 ומפתח 🔑
# בברכה, צוות ספיידר 3D"""
#
# # 174 cha
# communicate_msg_4 = """איזה כיף, ההזמנה שלך מוכנה לאיסוף :)
# ניתן לאסוף כעת בכתובת חבקוק 114, גדרה
# *עקב גודל החבילה יש לתאם טלפונית
# 0522509900
# ניתן להגיע עד השעה 17:00 (14:00 בשישי)
# בברכה, צוות ספיידר 3D"""

## Example
# txtMe_sms(message_type=2, phone="0584770076")


