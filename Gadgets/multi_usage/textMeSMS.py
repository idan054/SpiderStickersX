import xml.etree.ElementTree as ET
import requests
from Gadgets.multi_usage.bcolors import bcolors

global locker_num, locker_code, final_msg
def txtMe_sms(
        includeAppAd,
        message_type, # 4 = Local pickup SMS, 5 = Delivery SMS
        phone,
        deliveryCompany=None,
        localLockerPass=None,
        localLockerNum=None,
        butikTrackNumber=None): #butikTrackNumber no needed on pickup
    global locker_num, locker_code, final_msg
    print("message_type = ", message_type)
    print("includeAppAd = ", includeAppAd)
    print("localLockerNum = ", localLockerNum)
    print("deliveryCompany = ", deliveryCompany)

    # debug
    # if str(phone) == '0584880076':
    #     phone = str('0584770076')

    # if message_type == 2 : # locker
    #     locker_num = "הכחול 🔵"
    #     locker_code =  "2580"

    if message_type == 'Pickup' : # phone pickup

        final_msg = str(f"""
איזה כיף 😍 הזמנתך מוכנה וזמינה 24/7
לאיסוף עצמי ביבנה, חידקל 11 (בניין מס' 15)
{str(localLockerNum)}לוקר מס': 
{str(localLockerPass)}קוד לפתיחת הלוקר: 

*יש לאסוף תוך 48 שעות*
קישור ל Waze
Https://waze.com/ul/hsv8tqmxhf
סרטון הסבר להגעה
Https://bit.ly/3p7YVYQ

תודה רבה לך שבחרת בנו ❤️ ספיידר תלת מימד
            """)

#         final_msg = f"""איזה כיף, ההזמנה שלך מוכנה לאיסוף :)
# ניתן לאסוף כעת בכתובת חידקל 11, יבנה (בניין 15)
# החבילה זמינה 24/7 בלוקר מס' {localLockerNum}
# קוד:  {localLockerPass}
# בברכה, צוות ספיידר 3D"""

    if message_type == 'Delivery' : # delivery
        if deliveryCompany == 22:  # Cargo

            #   מס' מעקב {butikTrackNumber}
            final_msg = f"""
 ההזמנה מספיידר 3D יצאה ותגיע תוך 3-4 ימי עסקים!

חדש! למבצעים סודיים, מעקב הזמנות, חיפוש מודלים בעברית הורידו את אפליקציה החדשה 
https://rebrand.ly/Spider3D-App

מס' מעקב {butikTrackNumber}
 למעקב המשלוח: https://rebrand.ly/Spider3D-Shipping
                    """

        if deliveryCompany == 23 : # Mahir Li

            # if includeAppAd: # AKA True
                # 60 Character Example ( Until 70 -> 0.078$ = 0.26₪ On callr)

            #   מס' מעקב {butikTrackNumber}
            final_msg = f"""
משלוח מהיר  מספיידר 3D יגיע אליך היום אחר הצהריים, השליח יתקשר לתאם לפני ההגעה

חדש! למעקב ומבצעים מיוחדים, מומלץ להצטרף לאפליקציה!
https://rebrand.ly/Spider3D-App 
            """
            # else:
            #     # 60 Character Example ( Until 70 -> 0.078$ = 0.26₪ On callr)
            #     final_msg = f"""משלוח מהיר עם ההזמנה שלך נאסף מספיידר 3D
            #     מס' מעקב {butikTrackNumber}
            #     """

    if localLockerNum == 9 : # overSize - תיאום טלפוני
        final_msg = """איזה כיף, ההזמנה שלך מוכנה לאיסוף :)
        ניתן לאסוף כעת בכתובת חידקל 11, יבנה (בניין 15)
        *עקב גודל החבילה יש לתאם טלפונית
        0522509900
        בברכה, צוות ספיידר 3D"""

        #        ניתן להגיע עד השעה 17:00 (14:00 בשישי)

    url = "https://my.textme.co.il/api"
    print("final_msg = ", final_msg)

    payload = f"""
    <?xml version="1.0" encoding="UTF-8"?>
    <sms>
    <user>
    <username>idanbit80+1@gmail.com</username>
    <password>2gS"TEfU</password>
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
# message_type 5 = משלוח
# message_type 4 = א.ע

# txtMe_sms(message_type=5,
#           phone="0584770076",
#           includeAppAd=True,
#           localLockerPass='0542',
#           localLockerNum='2',
#           butikTrackNumber='45192'
#           )

