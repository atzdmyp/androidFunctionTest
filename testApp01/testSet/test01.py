
import unittest
import sys
import os
import inspect
from time import sleep
from selenium.webdriver.common.by import By
import testSet.common.Log as Log
import testSet.common.common as myCommon
from testSet.common.DRIVER import myDriver

class test01(unittest.TestCase):


    def setUp(self):
        global driver, log, caseNo
        driver = myDriver.GetDriver()

        #get Log
        log = Log.Log()

        #get caseNo
        # filename = sys.argv[0][sys.argv[0].rfind(os.sep)+1:]
        # length = len(filename.split("/"))
        caseNo = inspect.stack()[1][3]

        #test Start
        log.buildStartLine(caseNo)


    def testCase01(self):

        myCommon.openApp(driver)

        log.outputLogFile("Open app : OK")

        #find the bottom Navigation bar
        while not myCommon.isExitsElement(driver, By.ID, "fmc_ll_tab"):
            sleep(1)
        else:
            el = myCommon.getElement(driver, By.ID, "fmc_bn_profile")
            el.click()

        log.outputLogFile("Open profile : OK")

        while not myCommon.isExitsElement(driver, By.ID, "profile_head"):
            sleep(1)
        else:
            el = myCommon.getElement(driver, By.ID, "profile_sign_in")
            el.click()
        log.outputLogFile("click sign in Button : OK")

        while not myCommon.isExitsElement(driver, By.ID, "we_et_input"):
            sleep(1)
        else:
            el = myCommon.getElements(driver, By.CLASS_NAME, "android.widget.EditText", 0)
            el.click()
            el.clear()
            el.send_keys("2ts@qq.com")
            el = myCommon.getElements(driver, By.CLASS_NAME, "android.widget.EditText", 1)
            el.send_keys("111111")
            el = myCommon.getElement(driver, By.ID, "al_bn_sign")
            el.click()





    def tearDown(self):
        driver.quit()

        #test End
        log.buildEndLine(caseNo)


if __name__ == '__main__':

    suite = unittest.TestLoader().loadTestsFromTestCase(test01)
    unittest.TextTestRunner(verbosity=2).run(suite)



