

# packNum = packNum.get()
from time import sleep


global clean_address_String
def embed_details(browser, buyer_city, buyer_street
                  ,buyer_street_number, buyer_name,
                  clean_address ,buyer_phone, buyer_email,
                  buyer_notes, orderNum, packNum):
    # Embed pre-set Spider3D details

    global clean_address_String
    while True: # infinite until break
        try:
            origin_location = browser.find_element_by_xpath("//*[@id=\"new_task\"]/div[1]/div[6]/div[1]/span/span[1]/span")
            origin_location.click()
            havakuk_origin = browser.find_element_by_xpath("//*[@id=\"select2-task_source_location-results\"]/li")
            havakuk_origin.click()
            break
        except: # When error...
            print("except...")
            sleep(1.5)  # (Error fix) Must have to make sure page is up

    try:
        clean_address_String = ' '.join([str(x) for x in clean_address])
        print(clean_address_String)
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
        streetField.send_keys(clean_address_String)
    except:
        print("Error while add street")
        pass

    try:
        streetNumField = browser.find_element_by_id("task_destination_number")
        streetNumField.send_keys(buyer_street_number)
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