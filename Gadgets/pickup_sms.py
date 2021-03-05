import winsound

from Gadgets.examples.smsCaller.check_sms import check_sms
from Gadgets.examples.smsCaller.sendSms import send_sms


def pickup_sms(buyer_phone, message_type):
    if message_type == 1:
        message_type = "ירוק"
    if message_type == 2:
        message_type = "כחול"
    if message_type == 3:
        message_type = "כתום"
    if message_type == 4:
        message_type = "תיאום טלפוני"

    # pickup_message = ("""
    # איסוף עצמי מספיידר 3D זמין 24/7
    # כתובת וקוד ללוקר:
    # bit.ly/3bRe1uU
    #     """)

    sms_hash = send_sms(message_value=message_type,
                        buyer_phone=buyer_phone)
    check_sms(sms_hash)

    # sleep(0.12)
    winsound.Beep(2000, 150)
    winsound.Beep(1500, 150)
    winsound.Beep(1500, 150)
    winsound.Beep(2000, 150)