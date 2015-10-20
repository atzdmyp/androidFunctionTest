__author__ = 'tongshan'

from testSet.common.common import *
from selenium.webdriver.common.by import By


def openApp():
    """
    open the app,enter the index
    :return:
    """

    # skip
    if element("GuideActivity", "Guide").doesExist():
        element("GuideActivity", "skip").click()

    # # welcom
    # if doesExitsElement(By.ID, "ag_ll_dotlayout"):
    #
    #     while not isExitsElement(By.ID, "agi_bn_goshop"):
    #
    #         # swip right
    #         mySwipeToRight()
    #         sleep(1)
    #     else:
    #         myClick(By.ID, "agi_bn_goshop")
    #
    # #loading
    # waitLoading()

    # update
    if doesExitsElement(By.ID, "cancel_btn"):
        myClick(By.ID, "cancel_btn")

def waitLoading():
    """
    Waiting for the end of the page load
    :return:
    """
    #loading img
    while isExitsElement(By.CLASS_NAME, "android.widget.ProgressBar"):
        sleep(1)
    else:
        # time out
        if isExitsElement(By.ID, "confirm_btn"):
            myClick(By.ID, "confirm_btn")
        else:
            pass