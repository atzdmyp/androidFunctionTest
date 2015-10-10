# ========================================================
# Summary        :run
# Author         :tong shan
# Create Date    :2015-10-09
# Amend History  :
# Amended by     :
# ========================================================

from testApp01 import readConfig
readConfigLocal = readConfig.ReadConfig()
import unittest
from testApp01.testSet.common.DRIVER import myDriver
import os
from time import sleep

from urllib.error import URLError
from selenium.common.exceptions import WebDriverException
import threading

mylock = threading.RLock()
num = 0
class myServer(threading.Thread):

    def __init__(self):
        global appiumPath
        threading.Thread.__init__(self)
        self.appiumPath = readConfigLocal.getConfigValue("appiumPath")
        self.stopped = False

    def run(self):
        rootDirectory = self.appiumPath[:2]
        startCMD = "node node_modules\\appium\\bin\\appium.js"

        #cd root directory ;cd appiuu path; start server
        os.system(rootDirectory+"&"+"cd "+self.appiumPath+"&"+startCMD)

    def stop(self):
        self.stopped = True

    def isStopped(self):
        return self.stopped

class Alltest(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        global casePath, caseListLpath, caseList, suiteList, appiumPath
        self.caseListPath = readConfig.logDir+"\\caseList.txt"
        self.casePath = readConfig.logDir+"\\testSet\\"
        self.caseList = []
        self.suiteList = []
        self.appiumPath = readConfigLocal.getConfigValue("appiumPath")


# =================================================================
# Function Name   : driverOff
# Function        : colse the driver
# Input Parameters: -
# Return Value    : -
# =================================================================
    def driverOff(self):
        myDriver.GetDriver().quit()

# =================================================================
# Function Name   : setCaseList
# Function        : read caseList.txt and set caseList
# Input Parameters: -
# Return Value    : -
# =================================================================
    def setCaseList(self):

        print(self.caseListPath)

        fp = open(self.caseListPath)

        for data in fp.readlines():

            sData = str(data)
            if sData != '' and not sData.startswith("#"):
                self.caseList.append(sData)

# =================================================================
# Function Name   : createSuite
# Function        : get testCase in caseList
# Input Parameters: -
# Return Value    : testSuite
# =================================================================
    def createSuite(self):

        self.setCaseList()

        testSuite = unittest.TestSuite()

        if len(self.caseList) > 0:

            for caseName in self.caseList:

                print("caseName="+caseName)

                discover = unittest.defaultTestLoader.discover(self.casePath, pattern=caseName+'.py', top_level_dir=None)

                self.suiteList.append(discover)

        if len(self.suiteList) > 0:

            for test_suite in self.suiteList:
                for casename in test_suite:
                    testSuite.addTest(casename)
        else:
            return None

        return testSuite

# =================================================================
# Function Name   : runTest
# Function        : run test
# Input Parameters: -
# Return Value    : testSuite
# =================================================================
    def run(self):

        global num
        while not isStartServer():
            mylock.acquire()
            print("sleep1")
            sleep(1)
            mylock.release()
        else:
            suit = self.createSuite()
            if suit != None:

                print("test========================")
                #unittest.TextTestRunner(verbosity=2).run(suit)

                # self.driverOff()
                # self.stopAppiumServer()
            else:
                print("Have no test to run")


def isStartServer():

    try:
        driver = myDriver.GetDriver()

        if driver == None:
            return False
        else:
            return True
    except WebDriverException:
        print("WebDriverException")
        pass
    return True



if __name__ == '__main__':

    thread1 = myServer()
    thread2 = Alltest()

    thread2.start()
    thread1.start()




