from color_printer import printRed
from selenium import webdriver

def setup_browser():
    try:
        # option = webdriver.ChromeOptions()
        # option.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
        # option.binary_location = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'

        # from selenium.webdriver.support import ui

        # user_field = "idanb"
        chrome_ver = "89"  # 86/87/88
        # global chrome_ver
        # options = webdriver.ChromeOptions()  # פיתחת כרום דרך משתמש רגיל
        # options.add_argument(f"user-data-dir=C:\\Users\\{user_field.get()}\\AppData\\Local\\Google\\Chrome\\User Data")
        # browser = webdriver.Chrome(executable_path=fr"C:\Program Files (x86)\\chromedriver{chrome_ver}.exe", options=options)

        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=550,1080")
        args = ["hide_console", ]
        _browser = webdriver.Chrome(executable_path=fr"C:\Program Files (x86)\chromedriver.exe",
                                    service_args=args,
                                    options=options)

        # browser = webdriver.Chrome(options=options)
        ChromeVer = _browser.capabilities['browserVersion']
        ChromeDriverVer = _browser.capabilities['chrome']['chromedriverVersion'].split(' ')[0]
        # print(ChromeVer)
        # print(ChromeDriverVer)
        print("ChromeVer " + ChromeVer[0:2])
        print("ChromeDriverVer " + ChromeDriverVer[0:2])
        # and if it doesn't exist, download it automatically,
        # then add chromedriver to path

        # chrome_ver = radioVar.get()  # 86/87/88
        # browser = webdriver.Chrome(executable_path=fr"C:\Program Files (x86)\chromedriver{chrome_ver}.exe")
        return _browser
    except Exception as e:
        printRed(str(e))
        # # messagebox.showerror("שגיאה", f"{e}")
        # messagebox.showerror("ChromeDriver error", f"""יש לעדכן גרסת דרייבר כרום, אנא הכנס לאתר
        # chromedriver.chromium.org
        # והעתק את גרסת כרום 89 המלאה (לדוגמא 89.0.4389.23)""")            # e = str(e)
        # # print("ValueError:")
        # # print(f"{bcolors.Red}e:{bcolors.Normal}")
        # # print(e)