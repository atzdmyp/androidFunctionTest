# ========================================================
# Summary        :DRIVER
# Author         :tongshan
# Create Date    :2015-09-16
# Amend History  :
# Amended by     :
# ========================================================

from selenium.common.exceptions import WebDriverException

import testApp01.readConfig as readConfig

readConfigLocal = readConfig.ReadConfig()
from testApp01.testSet.common import init

import threading
from appium import webdriver
from urllib.error import URLError

class myDriver():

    driver = None
    mutex = threading.Lock()
    myInit = init.init()
    platformName = readConfigLocal.getConfigValue("platformName")
    platformVersion = myInit.getAndroidVersion()
    appPackage = readConfigLocal.getConfigValue("appPackage")
    appActivity = readConfigLocal.getConfigValue("appActivity")
    deviceName = myInit.getDeviceName()
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


