import unittest
import testSet.common.Log as Log
from testSet.common.DRIVER import MyDriver
from testSet.common.common import Element
from testSet.bsns import bsnsCommon
from testSet.common import common

loginGls = bsnsCommon.get_login_cls()


class TestAboutUs(unittest.TestCase):

    def setUp(self):
        self.Begin = "../../result/image/1.png"
        self.CheckPoint = "../../result/image/1.png"
        self.End = "../../result/image/1.png"

        # get driver
        self.driver = MyDriver.get_driver()
        self.case_name = "testReturnPolicy"

        # get log
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_my_logger()

        # start test
        self.log.build_start_line(self.case_name)
        self.begin = self.log.take_shot(self.driver, self.case_name)
        self.logger.info("Take a shot, the picture path is:" + self.begin)

        # open app
        self.logger.info("Open App")

    def testAboutUs(self):
        try:
            email = loginGls[0][1]
            password = loginGls[0][2]
            bsnsCommon.login(email, password)
            bsnsCommon.wait_loading()
            if Element("Alert", "update_title").is_exist():
                Element("Alert", "cancel").click()
            else:
                pass

            # go to account setting
            bsnsCommon.go_to_setting()

            Element("account_setting", "return_policy").click()
            bsnsCommon.wait_loading()
            self.checkpoint = self.log.take_shot(self.driver, self.case_name)
            self.logger.info("Take a shot, the picture path is:" + self.checkpoint)
            self.check_result()

        except Exception as ex:
            self.logger.error(str(ex))

    def tearDown(self):
        self.end = self.log.take_shot(self.driver, self.case_name)
        self.logger.info("Take a shot, the picture path is:" + self.end)
        self.log.build_end_line(self.case_name)

    def check_result(self):
        if Element("returnpolicy", "return_policy_title").is_exist():
            value = Element("returnpolicy", "return_policy_title").get_attribute("text")
            self.logger.info("The title of 'Return Policy' is:" + value)
            if value == "Return Policy":
                self.assertEqual(1, 1)
            else:
                self.assertEqual(0, 1)
        while not Element("BottomNavigation", "BottomNavigation").is_exist():
            common.back()
        else:
            pass

