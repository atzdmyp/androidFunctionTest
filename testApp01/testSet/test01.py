import unittest

import testApp01.testSet.common.Log as Log
from testApp01.testSet.bsns.bsnsCommon import *
from testApp01.testSet.common.DRIVER import MyDriver


class Test01(unittest.TestCase):

    def setUp(self):
        self.driver = MyDriver.get_driver()
        self.caseNo = "test01"
        self.flag = False

        # get Log
        self.log = Log.MyLog().get_log()
        self.logger = self.log.getMyLogger()

        # get caseNo
        # filename = sys.argv[0][sys.argv[0].rfind(os.sep)+1:]
        # length = len(filename.split("/"))

        # test Start
        self.log.buildStartLine(self.caseNo)

    def test_case01(self):

        try:
            open_app()

            self.logger.info("Open app : OK")

            # find the bottom Navigation bar
            if Element("BottomNavigation", "BottomNavigation").does_exist():
                Element("BottomNavigation", "profile").click()
            else:
                pass

            self.logger.info("Open profile : OK")

            if Element("profile", "title").does_exist():
                Element("profile", "SignIn").click()
                wait_loading()
            else:
                pass

            self.logger.info("click sign in Button : OK")

            if Element("login", "title").does_exist():
                # input email
                Element("login", "mailAndPass").send_keys(0, "123456@11.com")

                # input password
                Element("login", "mailAndPass").send_keys(1, "123456")

                # click sign in button
                Element("login", "signIn").click()

                wait_loading()
            else:
                pass

            # checkPoint:show the email and sheIn points
            if Element("profile", "user").does_exist():

                value = Element("profile", "user").get_attribute("text")
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

        # write result
        if self.flag:
            self.log.resultOK(self.caseNo)
        else:
            self.log.resultNG(self.caseNo)

        # test End
        self.log.buildEndLine(self.caseNo)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Test01)
    unittest.TextTestRunner(verbosity=2).run(suite)



