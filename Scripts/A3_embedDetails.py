

# packNum = packNum.get()
from time import sleep

 ## A3 Embed details to Butik 24 based selenium
from Gadgets.multi_usage.bcolors import bcolors


def embed_details(browser, buyer_city, buyer_street
                  ,buyer_street_number, buyer_name,
                  clean_address ,buyer_phone, buyer_email,
                  buyer_notes, orderNum, packNum):

    def embed_spider_details():
        s = browser.find_element_by_xpath('//*[@id="task_source_name"]')
        s.send_keys("ספיידר תלת מימד")

        sleep(0.2)
        s = browser.find_element_by_xpath('//*[@id="source-city-other-button"]')
        s.click()

        sleep(0.2)
        s = browser.find_element_by_xpath('//*[@id="task_source_city_other"]')
        s.send_keys("גדרה")

        sleep(0.2)
        s = browser.find_element_by_xpath('//*[@id="source-street-other-button"]')
        s.click()

        sleep(0.2)
        s = browser.find_element_by_xpath('//*[@id="task_source_street_other"]')
        s.send_keys("חבקוק")

        sleep(0.2)
        s = browser.find_element_by_xpath('//*[@id="task_source_number"]')
        s.send_keys("114")

        sleep(0.2)
        s = browser.find_element_by_xpath('//*[@id="task_source_notes"]')
        s.send_keys("אייל - 058-5551234")

        sleep(0.2)
        s = browser.find_element_by_xpath('//*[@id="task_source_phone"]')
        s.send_keys("0522509900")

        sleep(0.2)
        s = browser.find_element_by_xpath('//*[@id="task_source_email"]')
        s.send_keys("info@spider3d.co.il")
    ## embed_spider_details
    whileIndex = 0
    while whileIndex < 3: # infinite until break
        try:
            sleep(1.5)  # (Error fix) Must have to make sure page is up
            origin_location = browser.find_element_by_xpath('//*[@id="new_task"]/div[1]/div[6]/div[1]/span/span[1]/span')
            # origin_location = browser.find_element_by_class('select2-selection select2-selection--single')
            origin_location.click()
            havakuk_origin = browser.find_element_by_xpath("//*[@id=\"select2-task_source_location-results\"]/li")
            havakuk_origin.click()
            print(f"{bcolors.Green}Success adding spider details automatically{whileIndex}...{bcolors.Normal}")
            break
        except: # When error...
            print(f"{bcolors.Red}except. adding spider details manually {whileIndex}...{bcolors.Normal}")
            embed_spider_details()
            whileIndex += 1
            sleep(1.5)  # (Error fix) Must have to make sure page is up

    try:
        print("Try adding Note!")
        print("clean_address:")
        print(clean_address)

        destinationNotes = browser.find_element_by_id("task_destination_notes")
        # destinationNotes.send_keys(clean_address_String + f". מס' הזמנה: #{orderNum} " + "\n" + buyer_notes)
        destinationNotes.send_keys(f". מס' הזמנה: #{orderNum} " + "\n" + buyer_notes)
    except:
        print("Error while add Notes")
        pass

    # Embed dynamic buyer details
    try:
        nameField = browser.find_element_by_id("task_destination_name")
        nameField.send_keys(buyer_name)
    except:
        print("Error while add name at text field 1")
        pass

    # לחיצה על כפתור אחר (עיר)
    browser.find_element_by_id("destination-city-other-button").click()
    try:
        cityNameField = browser.find_element_by_name("task[destination_city_other]")
        cityNameField.send_keys(buyer_city)
    except:
        print("Error while add city")
        pass

    # לחיצה על כפתור אחר (רחוב)
    browser.find_element_by_id("destination-street-other-button").click()
    try:
        streetField = browser.find_element_by_name("task[destination_street_other]")
        # streetField.send_keys(buyer_street)
        streetField.send_keys(clean_address)
    except:
        print("Error while add street")
        pass

    try:
        streetNumField = browser.find_element_by_id("task_destination_number")
        # No needed because full clean_address
        # streetNumField.send_keys(buyer_street_number)
    except:
        print("Error while add street Number")
        pass

    try:
        nameField2 = browser.find_element_by_id("task_destination_recipient_name")
        nameField2.send_keys(buyer_name)
    except:
        print("Error while add Name TextField 2")
        pass

    try:
        phoneField = browser.find_element_by_id("task_destination_phone")
        phoneField.send_keys(buyer_phone)
    except:
        print("Error while add phone")
        pass


    # try:
    #     mailField = browser.find_element_by_id("task_destination_email")
    #     mailField.send_keys(buyer_email)
    # except:
    #     print("Error while add mail")
    #     pass

    # packNum = input("Before print, How many packs?")
    packNumFeild = browser.find_element_by_id("task_packages_quantity")
    packNumFeild.clear()
    packNumFeild.send_keys(f"{packNum}")

    # if packNum == "y":  # יצירת ברירת מחדל 1
    #     packNumFeild = browser.find_element_by_id("task_packages_quantity")
    #     packNumFeild.clear()
    #     packNumFeild.send_keys("2")
    # else:
    #     pass