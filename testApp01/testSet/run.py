__author__ = 'tongshan'

import os
import readConfig
readConfigLocal = readConfig.ReadConfig()
import unittest
from testSet.common.DRIVER import myDriver
from testSet.common.AppiumServer import AppiumServer
import testSet.common.Log as Log

from time import sleep

import threading

mylock = threading.RLock()
log = Log.myLog.getLog()
logger = log.getMyLogger()
baseUrl = readConfigLocal.getConfigValue("baseUrl")

class Alltest():

    def __init__(self):
        global casePath, caseListLpath, caseList, suiteList, appiumPath
        self.caseListPath = os.path.join(readConfig.prjDir, "caseList.txt")
        self.casePath = os.path.join(readConfig.prjDir, "testSet\\")
        self.caseList = []
        self.suiteList = []
        self.appiumPath = readConfigLocal.getConfigValue("appiumPath")
        self.myServer = AppiumServer()

    def driverOn(self):
        """open the driver
        :return:
        """
        myDriver.GetDriver()

    def driverOff(self):
        """close the driver
        :return:
        """
        myDriver.GetDriver().quit()

    def setCaseList(self):
        """from the caseList get the caseName,set in caseList
        :return:
        """
        fp = open(self.caseListPath)

        for data in fp.readlines():

            sData = str(data)
            if sData != '' and not sData.startswith("#"):
                self.caseList.append(sData)
        fp.close()

    def createSuite(self):
        """from the caseList,get caseName,According to the caseName to search the testSuite
        :return:testSuite
        """
        self.setCaseList()
        testSuite = unittest.TestSuite()

        if len(self.caseList) > 0:

            for caseName in self.caseList:

                discover = unittest.defaultTestLoader.discover(self.casePath, pattern=caseName+'.py', top_level_dir=None)
                self.suiteList.append(discover)

        if len(self.suiteList) > 0:

            for test_suite in self.suiteList:
                for casename in test_suite:
                    testSuite.addTest(casename)
        else:
            return None

        return testSuite

    def run(self):
        """run test
        :return:
        """
        try:
            suit = self.createSuite()
            if suit != None:

                logger.info("begin to start Appium Server")

                self.myServer.startServer()

                while not self.myServer.isRunnnig():
                    sleep(1)

                else:
                    logger.info("end to start Appium Server")
                    logger.info("open Driver")
                    self.driverOn()
                    logger.info("Start to test")
                    # unittest.TextTestRunner(verbosity=2).run(suit)
                    logger.info("end to test")

            else:
                logger.info("Have no test to run")
        except Exception as ex:
            log.outputError(myDriver.GetDriver(), str(ex))
        finally:
             logger.info("close to Driver")
             self.driverOff()
             logger.info("begin stop Appium Server")
             self.myServer.stopServer()
             logger.info("end stop Appium Server")



if __name__ == '__main__':
    ojb = Alltest()
    ojb.run()







