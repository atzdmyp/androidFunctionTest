__author__ = 'tongshan'

from testApp01.testSet.common.common import *

def openApp():
    """
    open the app,enter the index
    :return:
    """

    # skip
    if element("GuideActivity", "Guide").isExist():
        element("GuideActivity", "skip").click()

    # welcome
    if element("GuideActivity", "welcome").isExist():

        while not element("GuideActivity", "goShop").isExist():

            # swip right
            mySwipeToRight()
            sleep(1)
        else:
            element("GuideActivity", "goShop").click()

    #loading
    waitLoading()

    # update
    if element("Alert", "cancel").isExist():
        element("Alert", "cancel").click()

def waitLoading():
    """
    Waiting for the end of the page load
    :return:
    """
    #loading img
    while element("Alert", "loading").isExist():
        sleep(1)
    else:
        # time out
        if element("Alert", "confirm").isExist():
            element("Alert", "confirm").click()
        else:
            pass


def getLoginCls():

    loginCls = getXLS("login")

    return loginCls


