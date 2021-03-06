import winsound
from tkinter import messagebox

import requests
from requests.structures import CaseInsensitiveDict

from Gadgets.multi_usage.textMeSMS import txtMe_sms

## Send mail & change order to completed
def wooApi_mail_complete(numOrder, buyer_name, butikTrackNumber, sendMailNeeded):
    print("START wooApi_mail_complete()")

    headers = CaseInsensitiveDict()
    headers["Authorization"] = \
        "Basic Y2tfMzAyZWJkYmQ4OTNjNzU2YTFlOTlmZjhlZmNjMzZiYjYzNWZjNDRjNzpjc19lMTUyMTc0MWJlNDYzMWZjMzljMTQyNzUwZDg0YmU2YTJiYWVlMWIx"
    notes_url = f"https://spider3d.co.il/wp-json/wc/v3/orders/{numOrder}/notes"

    # butikTrackNumber = str(butikTrackNumber)
    # print(butikTrackNumber)
    print("\nPlease Wait!")

    mailValue = str("""
        היי """ + str(buyer_name) + """, 
    המשלוח שלך נאסף ממחסנינו ע"י חברת המשלוחים 
    וצפוי להגיע אליך תוך 2-3 ימי עסקים. 
    **במידה ובחרת במשלוח מהיר, המשלוח יגיע אליך תוך יום עסקים 1**
    מס' המשלוח שלך הינו """ + str(butikTrackNumber) + """
    במקרה הצורך ניתן ליצור קשר עם חברת המשלוחים ב- 03-5109114
    תודה לך, צוות ספיידר תלת מימד
        """)

    if sendMailNeeded:
        ## 1 Post mail based POST Api
        data = {
            "note": mailValue,
            "customer_note": True  # נשלח אל הלקוח
        }
        requests.post(url=notes_url, headers=headers, data=data).json()

    ## 2 Put status complete mail based PUT Api
    data = {
        "status": "completed"
    }
    order_url = f"https://spider3d.co.il/wp-json/wc/v3/orders/{numOrder}"
    # print(requests.put(url=order_url, headers=headers, data=data).json())
    requests.put(url=order_url, headers=headers, data=data).json()

    print("DONE wooApi_mail_complete()")

def complete_and_notifications(browser, numOrder, buyer_name, butikTrackNumber,
                               buyer_phone, butikBarCode):

    # winsound.Beep(2000, 110)
    # winsound.Beep(1000, 100)


    wooApi_mail_complete(numOrder=numOrder, buyer_name=buyer_name,
                         butikTrackNumber=butikTrackNumber, sendMailNeeded=True)

    # message_type means delivery
    txtMe_sms(message_type=5, phone=buyer_phone, butikTrackNumber=butikTrackNumber)

    messagebox.showinfo("המשימה הושלמה",
                        "(●'◡'●)  מייל וסמס נשלח בהצלחה ללקוח \n                 סטטוס ההזמנה שונה להושלם")

    # sleep(0.12)
    winsound.Beep(2000, 150)
    winsound.Beep(1500, 150)
    # try: browser.quit()  # סוגר את הכרום
    # except: print("Failed to browser.quit() - PASS")
    winsound.Beep(1500, 150)
    winsound.Beep(2000, 150)


## Example
# complete_and_notifications(numOrder=22560, buyer_name="עומרי", butikTrackNumber="1117365",
#                                buyer_phone="0584770076", butikBarCode="NZW7T3WW4U")



# Disable browser before use
# send_track_mail_api(numOrder=28009,
#                     buyer_name="Example",
#                     butikTrackNumber="000000"
#                     )