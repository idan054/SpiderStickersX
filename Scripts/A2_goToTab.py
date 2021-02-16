import time



def goToTab(tabURL, browser):
    browser.switch_to.window(browser.window_handles[0])  # עובר לטאב פעיל כדי למנוע שגיאה במקרה שהטאב הפעיל נסגר
    print("Successfully redirect active available tab")

    print(browser.current_window_handle)
    print(browser.current_url)  # הדפס את קישור הדף

    # בודק אם הטאב קיים ופתוח כרגע
    def TabURLChecker():  # בודק האם הטאב המבוקש פתוח
        for window in browser.window_handles:  # עבור החלונות שברשימת החלונות
            # print(browser.title) # הדפס את שם הדף
            time.sleep(0.05)  # המתן 2 שניות ואז עבור לחלון שברשימה
            browser.switch_to.window(window)
            # browser.switch_to.window(browser.window_handles[1])
            # print(window)  # AKA Cdwindow-Ef75Db87501C77D30E44297374C1600B # חלון לדוגמא
            # print(browser.current_url)  # הדפס את קישור הדף
            print(browser.title)  # הדפס את שם הדף
            # if browser.current_url == tabURL:
            if browser.current_url == tabURL:
                browser.switch_to.window(browser.current_window_handle)  # עובר לטאב שפתוח מבחינת המחשב
                # browser.refresh()
                break  # אם דף משלוח חדש פתוח, עצור בו
            else:
                print(tabURL + " != " + browser.current_url)

    TabURLChecker()

    # אם לאחר הלופ בוטיק 24 לא נמצא, פתח אותו והפעל את לופ החיפוש מחדש
    if browser.current_url != tabURL:
        print("Butik 24 Not Found, try OPEN Butik24 Tab")
        browser.execute_script(f'''window.open("{tabURL}","_blank");''')
        TabURLChecker()
        print(browser.current_url)  # הדפס את קישור הדף
        # browser.execute_script(window.open(tabURL))
        # pass