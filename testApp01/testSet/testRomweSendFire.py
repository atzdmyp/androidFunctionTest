import unittest
import testSet.common.Log as Log
from testSet.common.DRIVER import MyDriver
from testSet.common.common import Element
from testSet.bsns import bsnsCommon
from time import sleep

loginGls = bsnsCommon.get_login_cls()


class TestSendFire(unittest.TestCase):

    def setUp(self):
        self.Begin = "../../result/image/1.png"
        self.CheckPoint = "../../result/image/1.png"
        self.End = "../../result/image/1.png"

        # get driver
        self.driver = MyDriver.get_driver()
        self.case_name = "testRomweSendFire"

        # get log
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_my_logger()

        # start test
        self.log.build_start_line(self.case_name)
        self.begin = self.log.take_shot(self.driver, self.case_name)
        self.logger.info("Take a shot, the picture path is:" + self.begin)

        # open app
        self.logger.info("Open App")

    def testSendFire(self):
        try:
            email = loginGls[0][1]
            password = loginGls[0][2]
            bsnsCommon.login(email, password)
            bsnsCommon.wait_loading()
            if Element("Alert", "update_title").is_exist():
                Element("Alert", "cancel").click()

            # go to daily new
            Element("daily_new", "daily_new").click()
            bsnsCommon.wait_loading()

            # find a goods
            Element("daily_new", "daily_new_goods").clicks(0)
            while Element("daily_new", "new_guide").does_exist():
                Element("daily_new", "new_guide").click()
            else:
                pass
            self.sendFire()
            self.check_result()

        except Exception as ex:
            self.logger.error(str(ex))

    def tearDown(self):
        self.end = self.log.take_shot(self.driver, self.case_name)
        self.logger.info("Take a shot, the picture path is:" + self.end)
        self.log.build_end_line(self.case_name)

    def sendFire(self):
        Element("add_shopping_bag", "edit_fire").send_key("test fire!!!")
        sleep(1)
        Element("add_shopping_bag", "fire").click()

    def check_result(self):
        pass
