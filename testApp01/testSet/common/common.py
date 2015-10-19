__author__ = 'tongshan'
from selenium.common.exceptions import NoSuchElementException
from time import sleep
import readConfig
from selenium.webdriver.common.by import By
readConfigLocal = readConfig.ReadConfig


def openApp(driver):
    """
    open the app,enter the index
    :param driver:
    :return:
    """

    # skip
    if doesExitsElement(driver, By.ID, "guideLayout"):
        myClick(driver, By.ID, "skipBtn")

    # welcom
    if doesExitsElement(driver, By.ID, "ag_ll_dotlayout"):

        while not isExitsElement(driver, By.ID, "agi_bn_goshop"):

            # swip right
            mySwipeToRight(driver)
            sleep(1)
        else:
            myClick(driver, By.ID, "agi_bn_goshop")

    #loading
    waitLoading(driver)

    # update
    if doesExitsElement(driver, By.ID, "cancel_btn"):
        myClick(driver, By.ID, "cancel_btn")

def returnIndex(driver):
    """
    :return the index
    :param driver:
    :return:
    """
    pass

def doesExitsElement(driver, how, what):
    """
    To determine whether an element is exits
    :param driver:
    :param how:
    :param what:
    :return:True/False
    """
    i = 1
    while not isExitsElement(driver, how, what):
        sleep(1)
        i = i+1
        if i >= 10:
            return False
    else:
        return True

def isExitsElement( driver, how, what):
    """
     To determine whether an element is exits
    :param driver:
    :param how:
    :param what:
    :return:True/False
    """
    try:
        driver.find_element(by=how, value=what)
    except NoSuchElementException:
        return False
    return True

def getElement( driver, how, what):
    """
     get one element
    :param driver:
    :param how:
    :param what:
    :return:element/None
    """
    if doesExitsElement(driver, how, what):
        element = driver.find_element(by=how, value=what)
        return element
    else:
        return None

def getElements( driver, how, what,index):
    """
    get one element in Element List
    :param driver:
    :param how:
    :param what:
    :param index:
    :return:element/None
    """
    if doesExitsElement(driver, how, what):
        elements = driver.find_elements(by=how, value=what)
        return elements[index]
    else:
        return None

def getWindowSize( driver):
    """
    get current windows size mnn
    :param driver:
    :return:windowSize
    """
    global windowSize
    windowSize = driver.get_window_size()
    return windowSize

def mySwipeToUP(driver, during=None):
    """
    swipe UP
    :param driver:
    :param during:
    :return:
    """
    # if windowSize == None:
    windowSize = getWindowSize(driver)

    width = windowSize.get("width")
    height = windowSize.get("height")
    driver.swipe(width/2, height*3/4, width/2, height/4, during)

def mySwipeToDown(driver, during=None):
    """
    swipe down
    :param driver:
    :param during:
    :return:
    """
    windowSize = getWindowSize(driver)
    width = windowSize.get("width")
    height = windowSize.get("height")
    driver.swipe(width/2, height/4, width/2, height*3/4, during)

def mySwipeToLeft(driver, during=None):
    """
    swipe left
    :param driver:
    :param during:
    :return:
    """
    windowSize = getWindowSize(driver)
    width = windowSize.get("width")
    height = windowSize.get("height")
    driver.swipe(width/4, height/2, width*3/4, height/2, during)

def mySwipeToRight(driver, during=None):
    """
    swipe right
    :param driver:
    :param during:
    :return:
    """
    windowSize = getWindowSize(driver)
    width = windowSize.get("width")
    height = windowSize.get("height")
    driver.swipe(width*4/5, height/2, width/5, height/2, during)

def myClick(driver,how,what):
    """
    click element
    :param driver:
    :param how:
    :param what:
    :return:
    """
    try:
        el = getElement(driver, how, what)
        el.click()
    except AttributeError:
        raise

def myClicks(driver,how,what,index):
    """
    click element
    :param driver:
    :param how:
    :param what:
    :param index:
    :return:
    """
    try:
        el = getElements(driver, how, what, index)
        el.click()
    except AttributeError:
        raise

def mySendKey(driver, how, what, values):
    """
    sendKeys
    :param driver:
    :param how:
    :param what:
    :param values:
    :return:
    """
    try:
        el = getElement(driver, how, what)
        el.click()
        el.clear()
        el.send_keys(values)
    except AttributeError:
        raise

def mySendKeys(driver, how, what,index,values):
    """
    sendKeys
    :param driver:
    :param how:
    :param what:
    :param index:
    :param values:
    :return:
    """
    try:
        el = getElements(driver, how, what, index)
        el.click()
        el.clear()
        el.send_keys(values)
    except AttributeError:
        raise

def waitLoading(driver):
    """
    Waiting for the end of the page load
    :param driver:
    :return:
    """
    #loading img
    while isExitsElement(driver, By.CLASS_NAME, "android.widget.ProgressBar"):
        sleep(1)
    else:
        # time out
        if isExitsElement(driver, By.ID, "confirm_btn"):
            myClick(driver, By.ID, "confirm_btn")
        else:
            pass
