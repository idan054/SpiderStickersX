from Gadgets.multi_usage.goToTab import goToTab

# 1 Click the final create button
# 2 Get butikTrackNumber, butikBarCode
# 3 Redirect to Sticker tab
## A4 Create sticker & Get details from sticker page
def create_sticker(browser):
    # כפתור יצירת משלוח סופי
    createDelivery_button = browser.find_element_by_class_name("ladda-label")
    createDelivery_button.click()

    # זיהוי מס' מעקב למשלוח
    butikTrackNumber = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div[1]/div/div/div/div[1]/div[1]/span[1]").text
    butikTrackNumber = int(''.join(l for l in butikTrackNumber if l.isdigit()))
    print("butikTrackNumber is ", butikTrackNumber)

    # butikBarCode = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/div[1]/div/div/div/div[2]/div/div/div[1]/div[6]/div/span[2]").text
    butikBarCode = butikTrackNumber
    print("butikBarCode = butikTrackNumber")
    print("butikBarCode is ", butikBarCode)

    # stickerLink = f"https://members.lionwheel.com/tasks/{butikTrackNumber}/print_label.pdf"
    stickerLink = f"https://members.lionwheel.com/tasks/{butikTrackNumber}/print_labels"
    goToTab(tabURL=stickerLink, browser=browser)

    return butikTrackNumber, butikBarCode