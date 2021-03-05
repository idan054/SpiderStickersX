import json

# Todo לבדוק ולעדכן בהתאם, מה קורה אם יש (') בתיאור המקורי של הפוסט
from Gadgets.multi_usage.bcolors import bcolors


def json_printer(the_dict):
    print(f"{bcolors.Blue}{bcolors.BOLD}"
          f"Json view:"
          f"{bcolors.Normal}")
    # JSON VIEW -  Replace (') to (") for good Json file
    the_dist_as_json = str(the_dict).replace("\'", "\"")

    try:
        print("Try method A...")
        the_dist_as_json = json.loads(the_dist_as_json)
        the_dist_as_json = json.dumps(the_dist_as_json, indent=2)
        print(the_dist_as_json)

    except ValueError as e:
        e = str(e)

        try:
            print("Try method B...")
            the_dist_as_json = json.dumps(the_dict, indent=2)
            print(the_dist_as_json)
        except:
            if "Expecting" in e:
                print(f"{bcolors.Red}json_printer Error. Make sure (') not character in the_dict{bcolors.Normal}")
                print("Show normal view:")
                print(the_dict)
                return
