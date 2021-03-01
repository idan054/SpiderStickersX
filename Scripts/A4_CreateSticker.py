from Gadgets.goToTab import goToTab


def create_sticker(browser):

    # כפתור יצירת משלוח סופי
    createDelivery_button = browser.find_element_by_class_name("ladda-label")
    createDelivery_button.click()

    # זיהוי מס' מעקב למשלוח
    butikTrackNumber = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div[1]/div/div/div/div[1]/div[1]/span[1]").text
    butikTrackNumber = int(''.join(l for l in butikTrackNumber if l.isdigit()))
    print("butikTrackNumber is ", butikTrackNumber)

    stickerLink = f"https://members.lionwheel.com/tasks/{butikTrackNumber}/print_label.pdf"
    goToTab(tabURL=stickerLink, browser=browser)

    return butikTrackNumber