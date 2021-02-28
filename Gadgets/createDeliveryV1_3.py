from Scripts.A2_goToTab import goToTab

#note Not in use since v1.3
def create_deliveryV1_3(browser):

    # createDelivery_button = browser.find_element_by_class_name("ladda-label")
    # createDelivery_button.click()
    #
    # # הגדרת מס' מעקב (משלוח)
    # _butikTrackNumber = browser.find_element_by_xpath(
    #     "/html/body/div[1]/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div[2]/a").text
    # print(_butikTrackNumber)
    #
    # printButton = browser.find_element_by_xpath(
    #     "/html/body/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div[2]/a")
    # printButton.click()
    # stickerButton = browser.find_element_by_link_text("מדבקה")
    # stickerButton.click()
    # browser.switch_to.window(browser.window_handles[0])  # עובר לטאב פעיל כדי למנוע שגיאה במקרה שהטאב הפעיל נסגר

    # Fixed version 1.4
    _new_butikTrackNumber = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div[1]/div/div/div/div[1]/div[1]/span[1]").text
    _new_butikTrackNumber = int(''.join(l for l in _new_butikTrackNumber if l.isdigit()))
    print(_new_butikTrackNumber)

    stickerLink = f"https://www.spider3d.co.il/wp-admin/post.php?post={_new_butikTrackNumber}&action=edit"
    goToTab(tabURL=stickerLink, browser=browser)



    return _new_butikTrackNumber

def goToSticker(browser):
    for window in browser.window_handles:  # עבור החלונות שברשימת החלונות
        # print(browser.title) # הדפס את שם הדף
        # time.sleep(0.05)  # המתן 2 שניות ואז עבור לחלון שברשימה
        browser.switch_to.window(window)
        # browser.switch_to.window(browser.window_handles[1])/html/body/div[3]/div[2]/div[1]/div/div/div/div[2]/div/div/div[1]/div[8]/div/d
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