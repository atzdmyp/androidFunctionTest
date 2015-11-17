
import os
import testApp01.readConfig as readConfig
import unittest
from testApp01.testSet.common.DRIVER import MyDriver
from testApp01.testSet.common.AppiumServer import AppiumServer
import testApp01.testSet.common.Log as Log
from time import sleep
import HTMLTestRunner

readConfigLocal = readConfig.ReadConfig()

baseUrl = readConfigLocal.getConfigValue("baseUrl")


class Alltest():

    def __init__(self):
        global log, logger, resultPath
        self.caseListPath = os.path.join(readConfig.prjDir, "caseList.txt")
        self.casePath = os.path.join(readConfig.prjDir, "testSet\\")
        self.caseList = []
        self.suiteList = []
        self.appiumPath = readConfigLocal.getConfigValue("appiumPath")
        self.myServer = AppiumServer()
        log = Log.MyLog.get_log()
        logger = log.getMyLogger()
        resultPath = log.getResultPath()

    def driver_on(self):
        """open the driver
        :return:
        """
        MyDriver.get_driver()

    def driver_off(self):
        """close the driver
        :return:
        """
        MyDriver.get_driver().quit()

    def set_case_list(self):
        """from the caseList get the caseName,set in caseList
        :return:
        """
        fp = open(self.caseListPath)

        for data in fp.readlines():

            s_data = str(data)
            if s_data != '' and not s_data.startswith("#"):
                self.caseList.append(s_data)
        fp.close()

    def create_suite(self):
        """from the caseList,get caseName,According to the caseName to search the testSuite
        :return:test_suite
        """
        self.set_case_list()
        test_suite = unittest.TestSuite()

        if len(self.caseList) > 0:

            for caseName in self.caseList:

                discover = unittest.defaultTestLoader.discover(self.casePath, pattern=caseName+'.py', top_level_dir=None)
                self.suiteList.append(discover)

        if len(self.suiteList) > 0:

            for test_suite in self.suiteList:
                for case_name in test_suite:
                    test_suite.addTest(case_name)
        else:
            return None

        return test_suite

    def run(self):
        """run test
        :return:
        """
        try:
            suit = self.create_suite()
            if suit is not None:

                logger.info("begin to start Appium Server")

                self.myServer.start_server()

                while not self.myServer.is_runnnig():
                    sleep(1)

                else:
                    logger.info("end to start Appium Server")
                    # logger.info("open Driver")
                    # self.driverOn()
                    logger.info("Start to test")
                    fp = open(resultPath, 'wb')
                    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='testReport', description='Report_description')
                    runner.run(suit)
                    # unittest.TextTestRunner(verbosity=2).run(suit)
                    logger.info("end to test")

            else:
                logger.info("Have no test to run")
        except Exception as ex:
            log.outputError(MyDriver.get_driver(), str(ex))
        finally:
             logger.info("close to Driver")
             self.driver_off()
             logger.info("begin stop Appium Server")
             self.myServer.stop_server()
             logger.info("end stop Appium Server")

if __name__ == '__main__':
    ojb = Alltest()
    ojb.run()
