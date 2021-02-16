from time import sleep



def loginWordpress(browser):
    browser.switch_to.window(browser.window_handles[0])  # עובר לטאב פעיל כדי למנוע שגיאה במקרה שהטאב הפעיל נסגר
    browser.get("https://www.spider3d.co.il/s3d-login") #התחברות
    # print("x")
    # Eyal@kivi.co.il
    # S)8gm$WAyQuoHP#8#E)KvztH

    pass_field = browser.find_element_by_id("user_pass")
    pass_field.send_keys("S)8gm$WAyQuoHP#8#E)KvztH")
    sleep(0.3)

    user_wordpress_field = browser.find_element_by_id("user_login")
    user_wordpress_field.send_keys("Eyal@kivi.co.il")

    sleep(0.3)
    browser.find_element_by_id("wp-submit").click()