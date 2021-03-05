from time import sleep
from tkinter import messagebox

from callr import callr

from Gadgets.multi_usage.bcolors import bcolors
from Gadgets.multi_usage.jsonPrinter import json_printer


def check_sms(sms_hash):
    ## Make sure sms is RECEIVED
    whileIndex = 0
    print("check_sms: sms_hash 2 is ", sms_hash)
    api = callr.Api("spider3d_1", "Idan05423")
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
        else:
            sleep(2)
            # הודעת אישור למרות שלא בוצע אימות נוסף אך אחוז ההצלחה עומד על 100%
            messagebox.showinfo("אישור סמס", "(●'◡'●)  סמס מעקב נשלח ללקוח")
            break

        ## break while loop
        # if whileIndex > 10:
        #     print(f"{bcolors.Red}Already checked many times.{bcolors.Normal}")
        #     print("sms_status is ", sms_status)
        #
        #     messagebox_text = f"""
        #         !אך אל חשש{f" .{sms_status} "}שימו לב, מצב הודעת הסמס שזוהה הוא
        #      .כמעט וודאי שההודעת הסמס נשלחה, והלקוח קיבל גם מייל מעקב
        #                                      ניתן לעקוב אחר סטטוס הסמס באקסל שניתן
        #                                 www.app.callr.com/logs/sms להשיג בכתובת
        #                             Idan05423 :סיסמא  |   spider3d_1 :שם משתמש
        #                                               {sms_hash} :יש לשמור את שם הסמס
        #     """
        #     messagebox.showerror("שגיאה בשליחת סמס", messagebox_text)
        #     json_printer(sms_details)
        #     break