import requests


def bitly_shorter(link, with_http=True):
    headers = {
        'Authorization': '5edc2aab03c4e12e51109d9062941dfbc6ef0643',
        # Get it from profile settings ->  GENERIC ACCESS TOKEN (Enter your bitly pass)
        'Content-Type': 'application/json',
    }

    # link = "https://members.lionwheel.com/locate/locate_task?locate%5Btask_public_id%5D=OTFZBF7NQ5"

    dict_request = {}
    dict_request.update({
        "long_url": link,
        "domain": "bit.ly",
        "group_guid": "Bk52cRAPZ64"
    }
    )
    str_request = str(dict_request).replace("\'", "\"")
    # print("str_request")
    # json_printer(str_request)

    response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=str_request)
    # json_printer(response.text)
    if with_http:
        bit_link = response.json()["link"]
    else:
        bit_link = response.json()["link"].replace("https://", "")
    # print(bit_link)
    return bit_link

# # Get YOUR_guid
# response = requests.get('https://api-ssl.bitly.com/v4/groups', headers=headers)
# print(response.json()["groups"][0]["guid"])

# {
#   "groups": [
#     {
#       "created": "2020-05-02T12:02:36+0000",
#       "modified": "2020-05-02T12:02:36+0000",
#       "bsds": [
#
#       ],
#       "guid": "Bk52cRAPZ64",
#       "organization_guid": "Ok52coK6HHh",
#       "name": "o_25ur1pc2ka",
#       "is_active": true,
#       "role": "org-admin",
#       "references": {
#         "organization": "https://api-ssl.bitly.com/v4/organizations/Ok52coK6HHh"
#       }
#     }
#   ]
# }
#