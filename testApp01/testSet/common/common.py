# ========================================================
# Summary        :common
# Author         :tong shan
# Create Date    :2015-09-16
# Amend History  :
# Amended by     :
# ========================================================

from selenium.common.exceptions import NoSuchElementException
from time import sleep
import readConfig
from selenium.webdriver.common.by import By
readConfigLocal = readConfig.ReadConfig


# =================================================================
# Function Name   : openApp
# Function        : open the SheIn ,enter then index
# Input Parameters: driver
# Return Value    : -
# =================================================================
def openApp(driver):

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


# =================================================================
# Function Name   : doesExitsElement
# Function        : To determine whether an element is exits
# Input Parameters: driver, how, what
# Return Value    : True/False
# =================================================================
def doesExitsElement(driver, how, what):
    i = 1
    while not isExitsElement(driver, how, what):
        sleep(1)
        i = i+1
        if i >= 10:
            return False
    else:
        return True


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
# Function        : get one element
# Input Parameters: driver, how, what
# Return Value    : element/None
# =================================================================
def getElement( driver, how, what):

    if doesExitsElement(driver, how, what):
        element = driver.find_element(by=how, value=what)
        return element
    else:
        return None

# =================================================================
# Function Name   : getElement
# Function        : get one element in Element List
# Input Parameters: driver, how, what
# Return Value    : element/None
# =================================================================
def getElements( driver, how, what,index):

    if doesExitsElement(driver, how, what):
        elements = driver.find_elements(by=how, value=what)
        return elements[index]
    else:
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

# =================================================================
# Function Name   : myClick
# Function        : click element
# Input Parameters: driver, how , what
# Return Value    : -
# =================================================================
def myClick(driver,how,what):

    if doesExitsElement(driver, how, what):
        el = getElement(driver, how, what)
        el.click()
    else:
        raise Exception("can't click the element:"+str(how)+"="+what)

# =================================================================
# Function Name   : myClicks
# Function        : click element
# Input Parameters: driver, how , what
# Return Value    : -
# =================================================================
def myClicks(driver,how,what,index):

    if doesExitsElement(driver, how, what):
        el = getElements(driver, how, what, index)
        el.click()
    else:
        raise Exception("can't click the element:"+str(how)+"="+what)

# =================================================================
# Function Name   : mySendKey
# Function        : sendKeys
# Input Parameters: driver, how , what
# Return Value    : -
# =================================================================
def mySendKey(driver, how, what, values):

    if doesExitsElement(driver, how, what):
        el = getElement(driver, how, what)
        el.click()
        el.clear()
        el.send_keys(values)
    else:
        pass
        # raise Exception("can't click the element:"+str(how)+"="+what)

# =================================================================
# Function Name   : mySendKey
# Function        : sendKeys
# Input Parameters: driver, how , what
# Return Value    : -
# =================================================================
def mySendKeys(driver, how, what,index,values):

    if doesExitsElement(driver, how, what):
        el = getElements(driver, how, what, index)
        el.click()
        el.clear()
        el.send_keys(values)
    else:
        pass
        # raise Exception("can't click the element:"+str(how)+"="+what)



# =================================================================
# Function Name   : waitLoading
# Function        : sendKeys
# Input Parameters: wait Loading
# Return Value    : -
# =================================================================
def waitLoading(driver):

    #loading img
    while isExitsElement(driver, By.CLASS_NAME, "android.widget.ProgressBar"):
        sleep(1)
    else:
        # time out
        if isExitsElement(driver, By.ID, "confirm_btn"):
            myClick(driver, By.ID, "confirm_btn")
        else:
            pass
