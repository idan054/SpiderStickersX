import callr


# Send confirmation & tracking link on SMS


def send_sms(message_value, buyer_phone):
    # Short track link
    # Not in use...
    # bit_link = bitly_shorter(
    #     link=f"https://members.lionwheel.com/locate/locate_task?locate%5Btask_public_id%5D={butikBarCode}",
    #     with_http=False)
    # print(bit_link)

    ## Send the SMS
    api = callr.Api("spider3d_1", "Idan05423")
    result = api.call("system.get_timestamp")
    print("result is ", result)

    _buyer_phone = f"+972{buyer_phone[1:]}"
    print(_buyer_phone)
    # print(type(_buyer_phone))

    # input("R u sure u want pay 0.26₪ to send SMS ?")
    # input("Please confirm again.")
    _sms_hash = api.call('sms.send', 'SMS', _buyer_phone, message_value, None)
    # _sms_hash = "0LWLNVLH"
    print("_sms_hash is ", _sms_hash)
    return _sms_hash