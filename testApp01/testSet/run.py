# ========================================================
# Summary        :run
# Author         :tong shan
# Create Date    :2015-10-09
# Amend History  :
# Amended by     :
# ========================================================

import readConfig as readConfig
import unittest
from testSet.common.DRIVER import myDriver


class run():

    def __init__(self):
        global casePath, caseListLpath, caseList, suiteList
        self.caseListPath = readConfig.logDir+"\\caseList.txt"
        self.casePath = readConfig.logDir+"\\testSet\\"
        self.caseList = []
        self.suiteList = []

# =================================================================
# Function Name   : stratAppiumServer
# Function        : start the appium Server
# Input Parameters: -
# Return Value    : -
# =================================================================
    def stratAppiumServer(self):
        pass

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
    def runTest(self):

        suit = self.createSuite()

        if suit != None:

            self.stratAppiumServer()
            self.driverOn()
            unittest.TextTestRunner(verbosity=2).run(suit)
            self.driverOff()
            self.stopAppiumServer()

        else:
            print("Have no test to run")


if __name__ == '__main__':

    obj = run()

    obj.runTest()
