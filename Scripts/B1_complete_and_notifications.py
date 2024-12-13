# import winsound
from tkinter import messagebox

import requests
from requests.structures import CaseInsensitiveDict

from Gadgets.beeper import beep
## Send mail & change order to succeed
from Gadgets.multi_usage.textMeSMS import txtMe_sms
from Scripts.A1_wooGetAPI import woo_token


def complete_and_notifications(browser, numOrder, buyer_name, butikTrackNumber,
                               buyer_phone, includeAppAd, deliveryCompany):
    beep(2000, 110)
    beep(1000, 100)

    print('Start wooApi_mail_complete()')
    wooApi_mail_complete(isDelivery=True,
                         buyer_name=buyer_name,
                         butikTrackNumber=butikTrackNumber,
                         numOrder=numOrder,
                         lockerNum=None,
                         lockerPass=None)

    # message_type means delivery
    print('Start textMe_sms()')
    # if sendSms:
    txtMe_sms(message_type='Delivery', phone=buyer_phone,
              butikTrackNumber=butikTrackNumber,
              includeAppAd=includeAppAd, deliveryCompany=deliveryCompany)
    messagebox.showinfo("המשימה הושלמה",
                        "(●'◡'●)  מייל וסמס נשלח בהצלחה ללקוח \n                 סטטוס ההזמנה שונה להושלם")

    # sleep(0.12)
    beep(2000, 150)
    beep(1500, 150)
    try:
        browser.quit()  # סוגר את הכרום
    except:
        print("Failed to browser.quit() - PASS")
    beep(1500, 150)
    beep(2000, 150)


## Example
# complete_and_notifications(numOrder=45193, buyer_name="עומרי",butikTrackNumber="1117365",
#                            buyer_phone="0584770076", butikBarCode="NZW7T3WW4U", browser=None, includeAppAd=True)

# Disable browser before use
# send_track_mail_api(numOrder=28009,
#                     buyer_name="Example",
#                     butikTrackNumber="000000"
#                     )

def wooApi_mail_complete(buyer_name, numOrder, butikTrackNumber, lockerNum, lockerPass, isDelivery):
    headers = CaseInsensitiveDict()
    headers["Authorization"] = woo_token
    notes_url = f"https://spider3d.co.il/wp-json/wc/v3/orders/{numOrder}/notes"

    # butikTrackNumber = str(butikTrackNumber)
    # print(butikTrackNumber)
    print("\nPlease Wait!")


    pickupMailValue = str(f"""
איזה כיף 😍 הזמנתך מוכנה וזמינה 24/7
לאיסוף עצמי ביבנה, חידקל 11 (בניין מס' 15)
{str(lockerNum)}לוקר מס': 
{str(lockerPass)}קוד לפתיחת הלוקר: 

*יש לאסוף תוך 48 שעות*
קישור ל Waze
Https://waze.com/ul/hsv8tqmxhf
סרטון הסבר להגעה
Https://bit.ly/3p7YVYQ

תודה רבה לך שבחרת בנו ❤️ ספיידר תלת מימד
        """)

    phonePickup = str(
        """
איזה כיף 😍 הזמנתך מוכנה וזמינה 24/7
לאיסוף עצמי ביבנה, חידקל 11 (בניין מס' 15)

 *יש לתאם טלפונית לפני הגעה בין השעות 9:00 - 14:00
0522509900

קישור ל Waze
Https://waze.com/ul/hsv8tqmxhf
סרטון הסבר להגעה
Https://bit.ly/3p7YVYQ

תודה רבה לך שבחרת בנו ❤️ ספיידר תלת מימד
    """
)

    deliveryMailValue = f"""
היי איזה כיף לנו שבחרת בספיידר תלת מימד
אנו עושים הכל שתהנה מהחוויה שלך 
הזדרזנו והכנו את ההזמנה שלך לאיסוף השליח

משלוח מהיר יגיע אליך אליך *בהתאם לסוג המשלוח שבחרת*, 
לא ניתן לדעת שעה מדוייקת 
אך אל דאגה
השליח יתקשר להודיע ולתאם לפני ההגעתו

בכדי שתוכל לעקוב אחר מבצעים, מוצרים חדשים, 
קבצי STL להורדה ועוד אני מזמין אותך להוריד את האפליקציה
המדהימה שלנו 
https://rebrand.ly/Spider3D-App 
תודה רבה לך 
צוות ספיידר תלת מימד 
וממני אייל ביטון :-)
            """

    # deliveryMailValue = str("""
    #     היי """ + str(buyer_name) + """,
    # המשלוח שלך נאסף ממחסנינו ע"י חברת המשלוחים
    # וצפוי להגיע אליך תוך 2-3 ימי עסקים.
    # **במידה ובחרת במשלוח מהיר, המשלוח יגיע אליך תוך יום עסקים 1**
    # מס' המשלוח שלך הינו """ + str(butikTrackNumber) + """
    # במקרה הצורך ניתן ליצור קשר עם חברת המשלוחים ב- 03-5555833
    # תודה לך, צוות ספיידר תלת מימד
    #     """)

    ## 1 Post mail based POST Api
    if isDelivery:
        data = {
            "note": deliveryMailValue,
            "customer_note": True  # נשלח אל הלקוח
        }
    else:
        data = {
            "note": pickupMailValue,
            "customer_note": True  # נשלח אל הלקוח
        }

    if str(lockerNum) == '9':
        data = {
            "note": phonePickup,
            "customer_note": True  # נשלח אל הלקוח
        }

    requests.post(url=notes_url, headers=headers, data=data).json()

    ## 1 Put status complete mail based PUT Api
    data = {
        "status": "completed"
    }
    order_url = f"https://spider3d.co.il/wp-json/wc/v3/orders/{numOrder}"
    # print(requests.put(url=order_url, headers=headers, data=data).json())
    requests.put(url=order_url, headers=headers, data=data).json()
