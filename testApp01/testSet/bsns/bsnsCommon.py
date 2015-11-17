
from testApp01.testSet.common.common import *


def open_app():
    """
    open the app,enter the index
    :return:
    """

    # skip
    if Element("GuideActivity", "Guide").is_exist():
        Element("GuideActivity", "skip").click()

    # welcome
    if Element("GuideActivity", "welcome").is_exist():

        while not Element("GuideActivity", "goShop").is_exist():

            # swip right
            my_swipe_to_right()
            sleep(1)
        else:
            Element("GuideActivity", "goShop").click()

    # loading
    wait_loading()

    # update
    if Element("Alert", "cancel").is_exist():
        Element("Alert", "cancel").click()


def wait_loading():
    """
    Waiting for the end of the page load
    :return:
    """
    # loading img
    while Element("Alert", "loading").is_exist():
        sleep(1)
    else:
        # time out
        if Element("Alert", "confirm").is_exist():
            Element("Alert", "confirm").click()
        else:
            pass


def get_login_cls():

    login_cls = get_xls("login")

    return login_cls