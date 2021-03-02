import callr, os, sys

## Sms service from callr

api = callr.Api("spider3d_1", "Idan05423")
# result = api.call("system.get_timestamp")

# 60 Character Example ( Until 70 -> 0.078$ = 0.26₪ )
text = ('ההזמנה שלך מספיידר 3D נאספה למשלוח מהיר ' +
       f'למעקב: bit.ly/2MHCASy ')


input("R u sure u want pay 0.26₪ to send SMS ?")
input("Please confirm again.")
result = api.call('sms.send', 'SMS', '+972584770076', text, None)
print(result)