import winsound
from time import sleep
from tkinter import messagebox
from threading import Thread
from callr import callr
from selenium.webdriver.common.keys import Keys
import requests
from requests.structures import CaseInsensitiveDict
from Gadgets.bcolors import bcolors

## Send mail & change order to succeed
from Gadgets.bitlyShorter import bitly_shorter
from Gadgets.jsonPrinter import json_printer

global api, sms_hash
def complete_and_notifications(browser, numOrder, buyer_name, butikTrackNumber,
                               buyer_phone, butikBarCode):

    winsound.Beep(2000, 110)
    winsound.Beep(1000, 100)

    def wooApi_mail_complete():
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

        ## 1 Post mail based POST Api
        data = {
            "note": mailValue,
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
    wooApi_mail_complete()

    def send_sms():
        global api, sms_hash
        ## Short track link
        bit_link = bitly_shorter(
            link=f"https://members.lionwheel.com/locate/locate_task?locate%5Btask_public_id%5D={butikBarCode}",
            with_http=False)
        print(bit_link)

        ## Send the SMS
        api = callr.Api("spider3d_1", "Idan05423")
        result = api.call("system.get_timestamp")
        print("result is ", result)

        # 60 Character Example ( Until 70 -> 0.078$ = 0.26₪ )
        text = (
            # 'ההזמנה שלך מספיידר 3D נאספה למשלוח מהיר ' + # 39 cha
                'משלוח מהיר עם ההזמנה שלך נאסף מספיידר 3D. ' +  # 40 cha
                f'למעקב:\n {bit_link}')

        _buyer_phone = f"+972{buyer_phone[1:]}"
        print(_buyer_phone)
        # print(type(_buyer_phone))

        # input("R u sure u want pay 0.26₪ to send SMS ?")
        # input("Please confirm again.")
        sms_hash = api.call('sms.send', 'SMS', _buyer_phone, text, None)
        # sms_hash = "0LWLNVLH"
        print("sms_hash is ", sms_hash)
    ## Run in background!
    Thread(target=send_sms).start()

    messagebox.showinfo("נשלח בהצלחה", "(●'◡'●)  מייל נשלח בהצלחה ללקוח \n        סטטוס ההזמנה שונה להושלם")

    def check_sms():
        ## Make sure sms is RECEIVED

        global api, sms_hash
        whileIndex = 0
        sms_details = api.call('sms.get', sms_hash)
        # json_printer(sms_details)
        while True:
            whileIndex += 1
            sms_status = sms_details["status_history"][-1]["new_status"]
            print("sms_status is ", sms_status, "...")

            ## Check sms status
            if sms_status == "SENT" or sms_status == "REMOTE_QUEUED" or sms_status == "RECEIVED":
                print(f"{bcolors.Yellow}SMS Delivered to customer!{bcolors.Normal}")
                delivery_time = sms_details["status_history"][-1]["updated_at"]
                print(sms_status)
                print(delivery_time)
                json_printer(sms_details)
                messagebox.showinfo("אישור סמס", "(●'◡'●)  סמס מעקב נשלח ללקוח")
                break

            ## break while loop
            sleep(1)
            if whileIndex > 7:
                print(f"{bcolors.Red}Already checked many times.{bcolors.Normal}")
                print("sms_status is ", sms_status)

                messagebox_text = f"""{sms_status} שימו לב, מצב הודעת הסמס שזוהה הוא
                         www.callr.com ניתן לקבל מידע נוסף באתר
                Idan05423 :סיסמא  |   spider3d_1 :שם משתמש """

                messagebox.showerror("שגיאה בשליחת סמס", messagebox_text)
                json_printer(sms_details)
                break
    check_sms()

    # sleep(0.12)
    winsound.Beep(2000, 150)
    winsound.Beep(1500, 150)
    browser.quit()  # סוגר את הכרום
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