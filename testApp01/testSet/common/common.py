# ========================================================
# Summary        :common
# Author         :tong shan
# Create Date    :2015-09-16
# Amend History  :
# Amended by     :
# ========================================================

from selenium.common.exceptions import NoSuchElementException
import readConfig
from selenium.webdriver.common.by import By
readConfigLocal = readConfig.ReadConfig

from time import sleep




# =================================================================
# Function Name   : openApp
# Function        : open the SheIn ,enter then index
# Input Parameters: driver
# Return Value    : -
# =================================================================
def openApp(driver):

    # skip
    if isExitsElement(driver, By.ID, "guideLayout"):
        el = driver.find_element_by_id("skipBtn")
        el.click()
        sleep(3)
    # welcom
    if isExitsElement(driver, By.ID, "ag_ll_dotlayout"):

        while not isExitsElement(driver, By.ID, "agi_bn_goshop"):
            mySwipeToRight(driver)
            sleep(3)
        else:
            el = driver.find_element_by_id("agi_bn_goshop")
            sleep(3)
            el.click()
            sleep(3)
    # update
    if isExitsElement(driver, By.ID, "cancel_btn"):
        el = driver.find_element_by_id("cancel_btn")
        sleep(3)
        el.click()

# =================================================================
# Function Name   : isExitsElement
# Function        : To determine whether an element is exits
# Input Parameters: driver, how, what
# Return Value    : True/False
# =================================================================
def isExitsElement( driver, how, what):
    try:
        driver.find_element(by=how, value=what)
    except NoSuchElementException:
        return False
    return True

# =================================================================
# Function Name   : getElement
# Function        : To determine whether an element is exits
# Input Parameters: driver, how, what
# Return Value    : element/None
# =================================================================
def getElement( driver, how, what):
    i = 1
    while True:
        if isExitsElement(driver, how, what):
            element = driver.find_element(by=how, value=what)
            return element
        i += 1
        if i >= 10:
            return None

# =================================================================
# Function Name   : getWindowSize
# Function        : get current windows size
# Input Parameters: driver
# Return Value    : windowSize
# =================================================================
def getWindowSize( driver):
    global windowSize
    windowSize = driver.get_window_size()
    return windowSize

# =================================================================
# Function Name   : mySwipeToUP
# Function        : swipe UP
# Input Parameters: driver, during
# Return Value    : -
# =================================================================
def mySwipeToUP(driver, during=None):

    # if windowSize == None:
    windowSize = getWindowSize(driver)

    width = windowSize.get("width")
    height = windowSize.get("height")
    driver.swipe(width/2, height*3/4, width/2, height/4, during)

# =================================================================
# Function Name   : mySwipeToDown
# Function        : swipe UP
# Input Parameters: driver, during
# Return Value    : -
# =================================================================
def mySwipeToDown(driver, during=None):

    windowSize = getWindowSize(driver)
    width = windowSize.get("width")
    height = windowSize.get("height")
    driver.swipe(width/2, height/4, width/2, height*3/4, during)

# =================================================================
# Function Name   : mySwipeToLeft
# Function        : swipe UP
# Input Parameters: driver, during
# Return Value    : -
# =================================================================
def mySwipeToLeft(driver, during=None):

    windowSize = getWindowSize(driver)
    width = windowSize.get("width")
    height = windowSize.get("height")
    driver.swipe(width/4, height/2, width*3/4, height/2, during)

# =================================================================
# Function Name   : mySwipeToRight
# Function        : swipe UP
# Input Parameters: driver, during
# Return Value    : -
# =================================================================
def mySwipeToRight(driver, during=None):

    windowSize = getWindowSize(driver)
    width = windowSize.get("width")
    height = windowSize.get("height")
    driver.swipe(width*4/5, height/2, width/5, height/2, during)












