import requests

url = "http://185.241.7.143/Baldarp/service.asmx/SaveData"

# Working example:
# payload='pParam=1;חרמון;9;לוד ;אישים ;99;תל אביב ;בדיקה ;לקוח מקבל ;Testing comme;1;1;1;1;1;0;m23946;2808;0;בלהבלה ;3;בדיקה ;0521234567;ab@gmail.com;2022-07-05;0'

# Real Spider!:
# delivery_company,
# buyer_city, buyer_name,
# clean_address, buyer_phone, buyer_email,
# buyer_notes, orderNum, packNum,
# browser = None, buyer_street = "", buyer_street_number = "",):

payload=f'pParam=' \
        '1;חידקל;11;יבנה ;buyer_street' \
        ';99;buyer_city ;ספיידר 3D' \
        ';IDAN_TEST ;clean_address - buyer_notes' \
        ';1' \
        ';1' \
        ';1' \
        ';12' \
        ';1' \
        ';0' \
        ';orderNum;' \
        '3131;' \
        '0' \
        ';' \
        ';0;עיר-מוצא-2' \
        ';;buyer_email - buyer_phone;;0'

# Explain
# # payload='pParam=' \
#         '1;' \ סוג משלוח
#         'חרמון;' \ רחוב מוצא
#         '9' \ מס' בית מוצא
#         ';לוד ' \ עיר מוצא
#         ';אישים ' \ רחוב יעד
#         ';99' \ מס' בית יעד
#         ';תל אביב' \ עיר יעד
#         ' ;בדיקה ;' \ שם חברה במוצא
#         'לקוח מקבל ;' \ שם חברה ביעד
#         'Testing comme;' \ הוראות למשלוח
#         '1;' \ דחיפות
#         '1;' \  מהיום למחר
#         '1;' \ סוג דיוור
#         '1;' \ מס' חבילות
#         '1;' \ האם כפול?
#         '0;' \  מספר קרטונים
#         'm23946;' \ מס’ הזמנה אצלכם
#         '2808;' \ קוד לקוח בCARGO
#         '0' \  ברקוד
#         ';בלהבלה' \ הערות נוספות אם יש
#         ' ;3' \ מס' משטחים
#         ';בדיקה ' \ עיר מוצא - לא חובה אם סופק מוצא עיר פרמטר 4
#         ';0521234567' \
#         ';ab@gmail.com' \
#         ';2022-07-05' \
#         ';0'  \ גוביינא

headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload.encode())

print(response.text)
