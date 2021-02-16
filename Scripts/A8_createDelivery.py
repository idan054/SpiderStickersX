
def create_delivery(browser):
    createDelivery_button = browser.find_element_by_class_name("ladda-label")
    createDelivery_button.click()

    # הגדרת מס' מעקב (משלוח)
    _butikTrackNumber = browser.find_element_by_xpath(
        "/html/body/div[3]/div[2]/div[1]/div/div/div/div[2]/div/div/div[1]/div[8]/div/div/span[1]").text
    print(_butikTrackNumber)

    printButton = browser.find_element_by_xpath(
        "/html/body/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div[2]/a")
    printButton.click()
    stickerButton = browser.find_element_by_link_text("מדבקה")
    stickerButton.click()

    browser.switch_to.window(browser.window_handles[0])  # עובר לטאב פעיל כדי למנוע שגיאה במקרה שהטאב הפעיל נסגר

    return _butikTrackNumber

def goToSticker(browser):
    for window in browser.window_handles:  # עבור החלונות שברשימת החלונות
        # print(browser.title) # הדפס את שם הדף
        # time.sleep(0.05)  # המתן 2 שניות ואז עבור לחלון שברשימה
        browser.switch_to.window(window)
        # browser.switch_to.window(browser.window_handles[1])
        print(window)  # AKA Cdwindow-Ef75Db87501C77D30E44297374C1600B #חלון לדוגמא
        print(browser.current_url)  # הדפס את קישור הדף
        print(browser.title)  # הדפס את שם הדף
        # if browser.current_url == tabURL:
        if "print_label.pdf" in browser.current_url:
            browser.switch_to.window(browser.current_window_handle)  # עובר לטאב שפתוח מבחינת המחשב
            break  # אם דף משלוח חדש פתוח, עצור בו
        else:
            print("Wrong Tab," + " != " + browser.current_url)
        print(browser.current_url)