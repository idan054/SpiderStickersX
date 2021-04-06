from selenium import webdriver

try:
    webdriver.Chrome()
except Exception as e:
    e = str(e)
    e = e.split(" ")
    print(e[16])