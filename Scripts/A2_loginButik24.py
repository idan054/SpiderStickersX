from time import sleep



def loginButik24(browser):
    browser.switch_to.window(browser.window_handles[0])  # עובר לטאב פעיל כדי למנוע שגיאה במקרה שהטאב הפעיל נסגר
    browser.get("https://members.lionwheel.com/?locale=he") #התחברות
    print("x")

    pass_field = browser.find_element_by_id("user_password")
    pass_field.send_keys("575968")

    user_wordpress_field = browser.find_element_by_id("user_username")
    user_wordpress_field.send_keys("ספיידר-3d")

    sleep(0.3)
    # try:
    #     browser.find_element_by_xpath("/html/body/div[2]/form/div[5]/button").click()
    # except:
    #     print("Xpath A Error!")
    try:
        browser.find_element_by_xpath('//*[@id="new_user"]/div[4]/button').click()
    except:
        print("Xpath B Error!")
    # try:
    #     user_wordpress_field.send_keys("ספיידר-3d").send_keys(Keys.ENTER)
    # except:
    #     print("send Keys (C) Error!")