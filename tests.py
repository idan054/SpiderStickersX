from time import sleep
from Gadgets.bcolors import bcolors

whileIndex = 0
while whileIndex < 3:  # infinite until break
    try:
        origin_location = browser.find_element_by_xpath('//*[@id="new_task"]/div[1]/div[6]/div[1]/span/span[1]/span')
        # origin_location = browser.find_element_by_class('select2-selection select2-selection--single')
        origin_location.click()
        havakuk_origin = browser.find_element_by_xpath("//*[@id=\"select2-task_source_location-results\"]/li")
        havakuk_origin.click()
        break
    except:  # When error...
        whileIndex += 1
        print(f"{bcolors.Red}except {whileIndex}...{bcolors.Normal}")
        sleep(1.5)  # (Error fix) Must have to make sure page is up