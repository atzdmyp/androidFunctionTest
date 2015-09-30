
import unittest
from selenium.webdriver.common.by import By
import testSet.common.Log as Log
import testSet.common.common as myCommon
from testSet.common.DRIVER import myDriver

class test01(unittest.TestCase):


    def setUp(self):
        global driver, log, caseNo
        self.driver = myDriver.GetDriver()
        self.caseNo = "test01"

        #get Log
        self.log = Log.Log(self.caseNo)

        #get caseNo
        # filename = sys.argv[0][sys.argv[0].rfind(os.sep)+1:]
        # length = len(filename.split("/"))


        #test Start
        self.log.buildStartLine()


    def testCase01(self):

        try:

            myCommon.openApp(self.driver)

            self.log.outputLogFile("Open app : OK")

            #find the bottom Navigation bar
            if myCommon.doesExitsElement(self.driver, By.ID, "fmc_ll_tab"):
                myCommon.myClick(self.driver, By.ID, "fmc_bn_profiletest")
            else:
                pass

            self.log.outputLogFile("Open profile : OK")

            if myCommon.doesExitsElement(self.driver, By.ID, "profile_head"):
                myCommon.myClick(self.driver, By.ID, "profile_sign_in")
                myCommon.waitLoading(self.driver)
            else:
                pass

            self.log.outputLogFile("click sign in Button : OK")

            if myCommon.isExitsElement(self.driver, By.ID, "we_et_input"):
                #input email
                myCommon.mySendKeys(self.driver, By.CLASS_NAME, "android.widget.EditText", 0, "123456@11.com")

                #input password
                myCommon.mySendKeys(self.driver, By.CLASS_NAME, "android.widget.EditText", 1, "123456")

                #click sign in button
                myCommon.myClick(self.driver, By.ID, "al_bn_sign")

                myCommon.waitLoading(self.driver)
            else:
                pass

            #checkPoint:show the email and sheIn points
            if myCommon.doesExitsElement(self.driver, By.ID, "profile_user"):

                el = myCommon.getElement(self.driver, By.ID, "profile_user")
                if el.get_attribute("text") == "Hello,123456":
                    self.log.checkPointOK(self.driver, "show the email and sheIn points")
                else:
                    self.log.checkPointNG(self.driver, "show the email and sheIn points")
            else:
                pass

        except Exception as ex:

            self.log.outputError(self.driver, str(ex))


    def tearDown(self):

        #return the index

        self.driver.quit()

        #test End
        self.log.buildEndLine()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test01)
    unittest.TextTestRunner(verbosity=2).run(suite)



