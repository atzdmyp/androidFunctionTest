# ========================================================
# Summary        :DRIVER
# Author         :tongshan
# Create Date    :2015-09-16
# Amend History  :
# Amended by     :
# ========================================================

import readConfig
readConfigLocal = readConfig.ReadConfig()

import threading
from appium import webdriver

class myDriver():
    driver = None
    mutex = threading.Lock()
    platformName = readConfigLocal.getConfigValue("platformName")
    platformVersion = readConfigLocal.getConfigValue("platformVersion")
    appPackage = readConfigLocal.getConfigValue("appPackage")
    deviceName = readConfigLocal.getConfigValue("deviceName")
    baseUrl = readConfigLocal.getConfigValue("baseUrl")
    desired_caps = {"platformName": platformName, "platformVersion": platformVersion, "appPackage": appPackage, "deviceName": deviceName}
    def _init__(self):
        pass


    @staticmethod
    def GetDriver():
        if myDriver.driver == None :
            myDriver.mutex.acquire()
            if myDriver.driver==None :

                myDriver.driver = webdriver.Remote(myDriver.baseUrl, myDriver.desired_caps)
                # myDriver.driver = myDriver()
            # else:
            #     print('shi li hua')
            myDriver.mutex.release()
        # else:
        #     print('shi li hua')
        return myDriver.driver

if __name__ == '__main__':
    myDriver.GetDriver()


