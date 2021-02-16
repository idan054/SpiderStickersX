from time import sleep
from selenium import webdriver
from guiDesign import orderLinkField


# function currently not in use...
def setup_order_link():
    if "spider3d.co.il" in orderLinkField.get():
        _finalOrderLink = orderLinkField.get()
        print("if finalOrderLink" + _finalOrderLink)
    else:
        _finalOrderLink = f"https://www.spider3d.co.il/wp-admin/post.php?post={orderLinkField.get()}&action=edit"
        print("else finalOrderLink" + _finalOrderLink)
        return _finalOrderLink