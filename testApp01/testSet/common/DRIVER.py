# ========================================================
# Summary        :DRIVER
# Author         :tongshan
# Create Date    :2015-09-16
# Amend History  :
# Amended by     :
# ========================================================

from selenium.common.exceptions import WebDriverException
from testApp01 import readConfig
readConfigLocal = readConfig.ReadConfig()
import testApp01.testSet.common.myPhone as myPhone

import threading
from appium import webdriver
from urllib.error import URLError

class myDriver():

    driver = None
    mutex = threading.Lock()
    myPhone = myPhone.myPhone()
    platformName = readConfigLocal.getConfigValue("platformName")
    platformVersion = myPhone.getAndroidVersion()
    appPackage = readConfigLocal.getConfigValue("appPackage")
    appActivity = readConfigLocal.getConfigValue("appActivity")
    deviceName = myPhone.getDeviceName()
    baseUrl = readConfigLocal.getConfigValue("baseUrl")
    desired_caps = {"platformName": platformName, "platformVersion": platformVersion, "appPackage": appPackage,
                    "appActivity": appActivity, "deviceName": deviceName}

    def _init__(self):
        pass

    @staticmethod
    def GetDriver():

        try:
            if myDriver.driver == None :
                myDriver.mutex.acquire()
                if myDriver.driver==None :

                    try:
                        myDriver.driver = webdriver.Remote(myDriver.baseUrl, myDriver.desired_caps)
                    except URLError:
                        myDriver.driver = None

                myDriver.mutex.release()

            return myDriver.driver
        except WebDriverException:
            raise


