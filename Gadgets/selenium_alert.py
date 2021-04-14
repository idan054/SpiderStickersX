from time import sleep

from selenium import webdriver
from Gadgets.setup_browser import setup_browser

browser = setup_browser()

browser.get("https://google.com")

browser.execute_script('window.print();')
# alert_obj = browser.switch_to_alert()
# print(alert_obj)

# alert_obj.accept() – used to accept the Alert
# alert_obj.dismiss() – used to cancel the Alert
# alert.send_keys() – used to enter a value in the Alert text box.
# alert.text() – used to retrieve the message included in the Alert pop-up.
sleep(1)
print("1")
# alert_obj.accept()  # – used to accept the Alert



