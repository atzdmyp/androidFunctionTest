import unittest
import testSet.common.Log as Log
from testSet.common.DRIVER import MyDriver
from testSet.common.common import Element
from testSet.bsns import bsnsCommon
from testSet.common import common
from time import sleep

loginGls = bsnsCommon.get_login_cls()


class TestChangeCurrency(unittest.TestCase):

    def setUp(self):
        self.Begin = "../../result/image/1.png"
        self.CheckPoint = "../../result/image/1.png"
        self.End = "../../result/image/1.png"

        # get driver
        self.driver = MyDriver.get_driver()
        self.case_name = "testChangeCurrency"

        # get log
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_my_logger()

        # start test
        self.log.build_start_line(self.case_name)
        self.begin = self.log.take_shot(self.driver, self.case_name)
        self.logger.info("Take a shot, the picture path is:" + self.begin)

        # oppen app
        self.logger.info("Open App")

    def testChangeCurrency(self):
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

            self.changeCurrency()
            self.check_result()

        except Exception as ex:
            self.logger.error(str(ex))

    def tearDown(self):
        self.end = self.log.take_shot(self.driver, self.case_name)
        self.logger.info("Take a shot, the picture path is:" + self.end)
        self.log.build_end_line(self.case_name)

    def changeCurrency(self):
        # change currency
        Element("account_setting", "change_currency").click()
        sleep(1)
        Element("change_currency", "currency").clicks(1)
        self.value = Element("change_currency", "currency").gets(1).get_attribute("text")
        self.logger.info("Currency is:" + self.value)

    def check_result(self):

        # go to daily new
        while not Element("BottomNavigation", "BottomNavigation").is_exist():
            common.back()
        else:
            Element("BottomNavigation", "SHOP").click()
            sleep(1)
        Element("daily_new", "daily_new").click()
        bsnsCommon.wait_loading()
        # find a goods
        Element("daily_new", "daily_new_goods").clicks(0)
        while Element("daily_new", "new_guide").does_exist():
            Element("daily_new", "new_guide").click()
        else:
            pass
        # get goods currency
        value2 = Element("daily_new", "goods_currency").get_attribute("text")
        self.logger.info("Changed currency is:" + value2[0:3])

        if value2[0:3] == self.value:
            self.assertEqual(1, 1)
        else:
            self.assertEqual(0, 1)

        while not Element("BottomNavigation", "BottomNavigation").is_exist():
            common.back()
