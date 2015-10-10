# ========================================================
# Summary        :run
# Author         :tong shan
# Create Date    :2015-10-09
# Amend History  :
# Amended by     :
# ========================================================

import readConfig
readConfigLocal = readConfig.ReadConfig()
import unittest
from testSet.common.DRIVER import myDriver
import os
from time import sleep

import win32com.client
import threading

mylock = threading.RLock()
class myServer(threading.Thread):

    def __init__(self):
        global appiumPath
        threading.Thread.__init__(self)
        self.appiumPath = readConfigLocal.getConfigValue("appiumPath")

    def run(self):
        rootDirectory = self.appiumPath[:2]
        startCMD = "node node_modules\\appium\\bin\\appium.js"

        #cd root directory ;cd appiuu path; start server
        os.system(rootDirectory+"&"+"cd "+self.appiumPath+"&"+startCMD)

        print("---------------------------------------------------")

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
# Function Name   : stratAppiumServer
# Function        : start the appium Server
# Input Parameters: -
# Return Value    : -
# =================================================================
    def stratAppiumServer(self):

        rootDirectory = self.appiumPath[:2]
        startCMD = "node node_modules\\appium\\bin\\appium.js"

        #cd root directory ;cd appiuu path; start server
        os.popen(rootDirectory+"&"+"cd "+self.appiumPath+"&"+startCMD)

        sleep(30)
        print("sleep 30s ")


# =================================================================
# Function Name   : stopAppiumServer
# Function        : stop the appium Server
# Input Parameters: -
# Return Value    : -
# =================================================================
    def stopAppiumServer(self):
        pass

# =================================================================
# Function Name   : driverOn
# Function        : open the driver
# Input Parameters: -
# Return Value    : -
# =================================================================
    def driverOn(self):

        myDriver.GetDriver()

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



        mylock.acquire()

        print("locked")

        print("sleep20")
        sleep(20)
        # else:

        print("release")
        mylock.release()
        suit = self.createSuite()
        if suit != None:

            # self.stratAppiumServer()
            print("stratAppiumServer")
            # self.driverOn()
            print("driverOn")
            unittest.TextTestRunner(verbosity=2).run(suit)
            self.driverOff()
            self.stopAppiumServer()

        else:
            print("Have no test to run")


    # def isStartServer(self):
    #
    #     WMI = win32com.client.GetObject('winmgmts:')
    #     processCodeCov = WMI.ExecQuery('select * from Win32_Process where Name='')
    #     if len(processCodeCov) > 0:
    #         print('%s is exists' % process_name)
    #     else:
    #         print('%s is not exists' % process_name)




if __name__ == '__main__':

    thread1 = myServer()
    thread2 = Alltest()

    thread2.start()
    thread1.start()



