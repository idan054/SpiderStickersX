import winsound

from Scripts.A2_goToTab import goToTab


def send_track_mail(browser, finalOrderLink,
                    buyer_name, butikTrackNumber):
    winsound.Beep(2000, 110)
    winsound.Beep(1000, 100)
    goToTab(browser=browser, tabURL=finalOrderLink)
    print(finalOrderLink)
    print(butikTrackNumber)
    print("Please Wait!")

    mailValue = """
        היי """ + buyer_name + """, 
    המשלוח שלך נאסף ממחסנינו ע"י חברת המשלוחים 
    וצפוי להגיע אליך תוך 2-3 ימי עסקים. 
    **במידה ובחרת במשלוח מהיר, המשלוח יגיע אליך תוך יום עסקים 1**
    מס' המשלוח שלך הינו """ + butikTrackNumber + """
    במקרה הצורך ניתן ליצור קשר עם חברת המשלוחים ב- 03-5109114
    תודה לך, צוות ספיידר תלת מימד
        """

    order_note_field = browser.find_element_by_id("add_order_note")
    order_note_field.send_keys(mailValue)
    dropDown_note_mode = browser.find_element_by_id("order_note_type")
    # dropDown_note_mode = browser.find_element_by_xpath("//*[@id=\"order_note_type\"]/option[2]")
    dropDown_note_mode.click()
    publicMode = browser.find_element_by_xpath('//*[@id="order_note_type"]/option[2]')
    publicMode.click()
    #     browser.click(כפתור שליחה)
    sendMailButton = browser.find_element_by_xpath(
        '//*[@id="woocommerce-order-notes"]/div[2]/div/p[2]/button')
    sendMailButton.click()

    winsound.Beep(2000, 150)
    winsound.Beep(1500, 150)
    winsound.Beep(1500, 150)
    winsound.Beep(2000, 150)
    browser.quit()  # סוגר את הכרום