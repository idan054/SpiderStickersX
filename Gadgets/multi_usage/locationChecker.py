# To choose delivery company
from difflib import SequenceMatcher
from pathlib import Path
import os

# האתר שלנו - mahirli.com
# והנה היעדים שאנו מגיעים אליהם כל יום :
# באיזור המרכז
# תל אביב, יפו, רמת גן, גבעתיים, פתח תקווה, גני תקווה, קרית אונו, בני ברק, יהוד, אור יהודה, גבעת שמואל ,בת  ים ,ראשון לציון, חולון, רמלה, לוד, גבעת שמואל,
#
# באיזור השרון
# כפר סבא, רעננה, הוד השרון, רמת השרון, הרצליה, ראש העין, סביון, הרצליה פיתוח, כפר שמריהו.
# והיישובים הגדולים בסביבה
#
# דרום והשפלה
# אשקלון, אשדוד, גן יבנה, יבנה, רחובות, נס ציונה, גדרה, באר יעקב, מזכרת בתיה, קריית עקרון והיישובים הגדולים בסביבה
#
# הוד השרון מורחב
# נתניה, כפר יונה, עמק חפר, אבן יהודה, תל מונד, אודים, תל מונד, געש, שפיים, רשפון והיישובים הגדולים בסביבה
# בברכה,

global similar_level, location
def location_checker(string):
    global similar_level, location

    def similar(a, b):
        return SequenceMatcher(None, a, b).ratio()

    # a = similar("רמת השרון","הוד שרון")
    # print(a)

    # loactions_file = open("C:\\Users\\idanb\\Desktop\\pyton Projects\\SpiderStickersX\\loactions.txt", "r", encoding="utf8")
    loactions_file = open("loactions.txt", "r", encoding="utf8")
    # locations = loactions_file.read().split(",")
    locations = loactions_file.read().splitlines()
    # print(*locations)

    for location in locations:
        similar_level = similar(string, location)
        if similar_level == 1:
            print(string, "=", location)
            print(f"{string} נמצאת ברשימה! המשלוח הועבר למהיר לי")
            break

        elif similar_level > 0.7:
            print(string, "~", location, "|",
                  float("{:.2f}".format(similar_level)))
            print(f"""
            מקום המגורים של הלקוח: {string}, בעוד מהיר לי עובדים ב{location}
            .האם להעביר את המשלוח אליהם? {similar_level} 
            """)
            break
    print(similar_level)
    return similar_level, location

# location_checker("תל אביב")
