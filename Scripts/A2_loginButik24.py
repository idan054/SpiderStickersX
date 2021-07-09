from time import sleep


## A2 Login butik from selenium
def loginDeliveryCompany24(browser, deliveryCompany):
    browser.switch_to.window(browser.window_handles[0])  # עובר לטאב פעיל כדי למנוע שגיאה במקרה שהטאב הפעיל נסגר
    browser.get("https://members.lionwheel.com/?locale=he") #התחברות
    print("x")

    user_wordpress_field = browser.find_element_by_id("user_username")
    pass_field = browser.find_element_by_id("user_password")

    if deliveryCompany == 23:
        # מהיר לי - 23
        user_wordpress_field.send_keys("ספיידר תלת מימד")
        pass_field.send_keys("0585551234")
    else:
        # בוטיק 24 - 24
        user_wordpress_field.send_keys("ספיידר-3d")
        pass_field.send_keys("575968")


    sleep(0.3)
    try:
        login_button = browser.find_element_by_xpath('/html/body/div[2]/form/div[4]/button')
        login_button.click()
    except:
        print("Xpath A Error!")
    try:
        login_button = browser.find_element_by_xpath('//*[@id="new_user"]/div[4]/button')
        login_button.click()
    except:
        print("Xpath B Error!")
    try:
       login_button = browser.find_element_by_link_text("התחבר")
       login_button.click()
    except:
        print("Xpath text C Error!")
    try:
        login_button = browser.find_elements_by_tag_name('button')[0]
        login_button.click()
    except:
        print("Xpath text D Error!")
