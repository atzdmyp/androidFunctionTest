import unittest

import testSet.common.Log as Log
from testSet.bsns.bsnsCommon import *
from testSet.common.DRIVER import myDriver


class test01(unittest.TestCase):


    def setUp(self):
        global driver, log, caseNo, flag
        self.driver = myDriver.GetDriver()
        self.caseNo = "test01"
        self.flag = False

        #get Log
        self.log = Log.myLog().getLog()
        self.logger = self.log.getMyLogger()

        #get caseNo
        # filename = sys.argv[0][sys.argv[0].rfind(os.sep)+1:]
        # length = len(filename.split("/"))


        #test Start
        self.log.buildStartLine(self.caseNo)


    def testCase01(self):

        try:
            openApp()

            self.logger.debug("Open app : OK")

            #find the bottom Navigation bar
            if doesExitsElement(By.ID, "fmc_ll_tab"):
                myClick(By.ID, "fmc_bn_profile")
            else:
                pass

            self.logger.debug("Open profile : OK")

            if doesExitsElement(By.ID, "profile_head"):
                myClick(By.ID, "profile_sign_in")
                waitLoading()
            else:
                pass

            self.logger.debug("click sign in Button : OK")

            if isExitsElement(By.ID, "we_et_input"):
                #input email
                mySendKeys(By.CLASS_NAME, "android.widget.EditText", 0, "123456@11.com")

                #input password
                mySendKeys(By.CLASS_NAME, "android.widget.EditText", 1, "123456")

                #click sign in button
                myClick(By.ID, "al_bn_sign")

                waitLoading()
            else:
                pass

            #checkPoint:show the email and sheIn points
            if doesExitsElement(By.ID, "profile_user"):

                el = getElement(By.ID, "profile_user")
                if el.get_attribute("text") == "Hello,123456":
                    self.flag = True
                    self.log.checkPointOK(self.driver, self.caseNo, "show the email and sheIn points")
                else:
                    self.log.checkPointNG(self.driver, self.caseNo, "show the email and sheIn points")
            else:
                pass



        except Exception as ex:

            self.logger.error(self.driver, str(ex))


    def tearDown(self):

        #write result
        if self.flag:
            self.log.resultOK(self.caseNo)
        else:
            self.log.resultNG(self.caseNo)

        #test End
        self.log.buildEndLine(self.caseNo)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(test01)
    unittest.TextTestRunner(verbosity=2).run(suite)



