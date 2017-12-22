import unittest
import testSet.common.Log as Log
from testSet.common.DRIVER import MyDriver
from testSet.common.common import Element
from testSet.bsns import bsnsCommon
from testSet.common import common
from time import sleep

loginGls = bsnsCommon.get_login_cls()


class TestClearCache(unittest.TestCase):

    def setUp(self):
        self.Begin = "../../result/image/1.png"
        self.CheckPoint = "../../result/image/1.png"
        self.End = "../../result/image/1.png"

        # get driver
        self.driver = MyDriver.get_driver()
        self.case_name = "testClearCache"

        # get log
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_my_logger()

        # start test
        self.log.build_start_line(self.case_name)
        self.begin = self.log.take_shot(self.driver, self.case_name)
        self.logger.info("Take a shot, the picture path is:" + self.begin)

        # oppen app
        self.logger.info("Open App")

    def testClearCache(self):
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
            self.clearCache()
            self.check_result()

        except Exception as ex:
            self.logger.error(str(ex))

    def tearDown(self):
        self.end = self.log.take_shot(self.driver, self.case_name)
        self.logger.info("Take a shot, the picture path is:" + self.end)
        self.log.build_end_line(self.case_name)

    def clearCache(self):
        self.cache = Element("account_setting", "cache_size").get_attribute("text")
        self.logger.info("Cache size is:" + self.cache)
        Element("account_setting", "clear_cache").click()

        if Element("Alert", "clear_cache_sure").is_exist():
            Element("Alert", "clear_cache_sure").click()
        else:
            pass

    def check_result(self):
        sleep(1)
        # get cache size
        value = Element("account_setting", "cache_size").get_attribute("text")
        self.logger.info("After clear, cache size is:" + value)

        if value == "0.00M":
            self.assertEqual(1, 1)
        else:
            self.assertEqual(0, 1)
        while not Element("BottomNavigation", "BottomNavigation").is_exist():
            common.back()
        else:
            pass

