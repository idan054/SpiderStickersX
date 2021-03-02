from time import sleep
from tkinter import messagebox

from Gadgets.bcolors import bcolors
from Gadgets.bitlyShorter import bitly_shorter
import callr, os, sys


# Send confirmation & tracking link on SMS
from Gadgets.jsonPrinter import json_printer


def send_sms(butikBarCode, buyer_phone):
    ## Short track link
    bit_link = bitly_shorter(
        link=f"https://members.lionwheel.com/locate/locate_task?locate%5Btask_public_id%5D={butikBarCode}",
        with_http=False)
    print(bit_link)

    ## Send the SMS
    api = callr.Api("spider3d_1", "Idan05423")
    # result = api.call("system.get_timestamp")

    # 60 Character Example ( Until 70 -> 0.078$ = 0.26₪ )
    text = (
            # 'ההזמנה שלך מספיידר 3D נאספה למשלוח מהיר ' + # 39 cha
            'משלוח מהיר עם ההזמנה שלך נאסף מספיידר 3D. ' + # 40 cha
            f'למעקב:\n {bit_link}')

    _buyer_phone = f"+972{buyer_phone[1:]}"
    # print(_buyer_phone)
    # print(type(_buyer_phone))

    # input("R u sure u want pay 0.26₪ to send SMS ?")
    # input("Please confirm again.")
    sms_hash = api.call('sms.send', 'SMS', _buyer_phone, text, None)
    # sms_hash = "0LWLNVLH"
    print("sms_hash is ", sms_hash)

    ## Make sure sms is RECEIVED
    sleep(1)
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
        sleep(1.5)
        if whileIndex > 10:
            print(f"{bcolors.Red}Already checked many times.{bcolors.Normal}")
            print("sms_status is ", sms_status)
            json_printer(sms_details)
            break


# Json view:
# Try method A...
# Try method B...
# {
#   "type": "OUT",
#   "hash": "0LWLNVLH",
#   "from": "SMS",
#   "to": "+972584770076",
#   "text": "\u05de\u05e9\u05dc\u05d5\u05d7 \u05de\u05d4\u05d9\u05e8 \u05e2\u05dd \u05d4\u05d4\u05d6\u05de\u05e0\u05d4 \u05e9\u05dc\u05da \u05e0\u05d0\u05e1\u05e3 \u05de\u05e1\u05e4\u05d9\u05d9\u05d3\u05e8 3D\u05dc\u05de\u05e2\u05e7\u05d1:\n bit.ly/3uM0ugS",
#   "options": null,
#   "encoding": "UNICODE",
#   "user_data": "",
#   "b_customer_mode": "PREPAID",
#   "b_customer_debit": "7.80",
#   "network": "42509",
#   "status": "REMOTE_QUEUED",
#   "status_error": "",
#   "parts": 1,
#   "nature": "MARKETING",
#   "date_creation": "2021-03-02 16:56:04",
#   "date_update": "2021-03-02 16:56:07",
#   "date_sent": "2021-03-02 16:56:06",
#   "date_received": "0000-00-00 00:00:00",
#   "status_history": [
#     {
#       "old_status": "CREATED",
#       "new_status": "PENDING",
#       "updated_at": "2021-03-02 16:56:04.912"
#     },
#     {
#       "old_status": "PENDING",
#       "new_status": "SENT",
#       "updated_at": "2021-03-02 16:56:06.531"
#     },
#     {
#       "old_status": "SENT",
#       "new_status": "REMOTE_QUEUED",
#       "updated_at": "2021-03-02 16:56:07.112"
#     }
#   ]
# }