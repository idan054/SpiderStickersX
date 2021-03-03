import winsound

from Gadgets.check_sms import check_sms
from Gadgets.sendSms import send_sms

pickup_message = ("""
איסוף עצמי מספיידר 3D זמין 24/7
כתובת וקוד ללוקר:
bit.ly/3bRe1uU
    """)

sms_hash = send_sms(message_value=pickup_message,
                    buyer_phone="0584770076")
check_sms(sms_hash)

# sleep(0.12)
winsound.Beep(2000, 150)
winsound.Beep(1500, 150)
winsound.Beep(1500, 150)
winsound.Beep(2000, 150)