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

            self.logger.info("Open app : OK")

            #find the bottom Navigation bar
            if element("BottomNavigation", "BottomNavigation").doesExist():
                element("BottomNavigation", "profile").click()
            else:
                pass

            self.logger.info("Open profile : OK")

            if element("profile", "title").doesExist():
                element("profile", "SignIn").click()
                waitLoading()
            else:
                pass

            self.logger.info("click sign in Button : OK")

            if element("login", "title").doesExist():
                #input email
                element("login", "mailAndPass").sendKeys(0, "123456@11.com")

                #input password
                element("login", "mailAndPass").sendKeys(1, "123456")

                #click sign in button
                element("login", "signIn").click()

                waitLoading()
            else:
                pass

            #checkPoint:show the email and sheIn points
            if element("profile", "user").doesExist():

                value = element("profile", "user").getAttribute("text")
                if value == "Hello,123456":
                    self.flag = True
                    self.log.checkPointOK(self.driver, self.caseNo, "show the email and sheIn points")
                else:
                    self.log.checkPointNG(self.driver, self.caseNo, "show the email and sheIn points")
            else:
                self.log.checkPointNG(self.driver, self.caseNo, "show the email and sheIn points")

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



