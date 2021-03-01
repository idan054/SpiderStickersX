import winsound
from time import sleep
from tkinter import messagebox

from selenium.webdriver.common.keys import Keys

from Gadgets.wooPostApi_note import woocomarce_post_api


## Send mail and change order to succeed
from Gadgets.wooPutApi_complete import woocomarce_put_api
import requests
from requests.structures import CaseInsensitiveDict
from Gadgets.bcolors import bcolors

def send_track_mail_api(browser, numOrder ,buyer_name, butikTrackNumber):

    headers = CaseInsensitiveDict()
    headers["Authorization"] = \
        "Basic Y2tfMzAyZWJkYmQ4OTNjNzU2YTFlOTlmZjhlZmNjMzZiYjYzNWZjNDRjNzpjc19lMTUyMTc0MWJlNDYzMWZjMzljMTQyNzUwZDg0YmU2YTJiYWVlMWIx"
    url = f"https://spider3d.co.il/wp-json/wc/v3/orders/{numOrder}/notes"


    winsound.Beep(2000, 110)
    winsound.Beep(1000, 100)

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

    ## Post mail based POST Api
    data = {
        "note": mailValue,
        "customer_note": True  # נשלח אל הלקוח
    }
    print(requests.post(url=url, headers=headers, data=data).json())

    ## Put status complete mail based PUT Api
    data = {
        "status": "completed"
    }
    print(requests.put(url=url, headers=headers, data=data).json())

    messagebox.showinfo("נשלח בהצלחה", "(●'◡'●)  מייל נשלח בהצלחה ללקוח \n        סטטוס ההזמנה שונה להושלם")

    winsound.Beep(2000, 150)
    winsound.Beep(1500, 150)
    winsound.Beep(1500, 150)
    winsound.Beep(2000, 150)
    browser.quit()  # סוגר את הכרום