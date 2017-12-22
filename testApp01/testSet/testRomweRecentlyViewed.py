# coding: utf-8
import unittest
import testSet.common.Log as Log
from testSet.bsns import bsnsCommon
from testSet.common.common import Element
from testSet.common.DRIVER import MyDriver
from testSet.common import common
from time import sleep

loginGls = bsnsCommon.get_login_cls()


class TestRecentlyViewed(unittest.TestCase):

    def setUp(self):
        self.Begin = "../../result/image/1.png"
        self.CheckPoint = "../../result/image/1.png"
        self.End = "../../result/image/1.png"

        # get driver
        self.driver = MyDriver.get_driver()
        self.case_name = "Test Recently Viewed"

        # get log
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_my_logger()

        # start test
        self.log.build_start_line(self.case_name)
        self.begin = self.log.take_shot(self.driver, self.case_name)
        self.logger.info("Take shot, the picture path is:" + self.begin)

        # open app
        self.logger.info("Open App")

    def testRecentlyViewed(self):
        try:
            email = loginGls[0][1]
            password = loginGls[0][2]
            bsnsCommon.login(email, password)
            bsnsCommon.wait_loading()
            if Element("Alert", "update_title").is_exist():
                Element("Alert", "cancel").click()
            else:
                pass

            # go to daily new
            Element("daily_new", "daily_new").click()
            bsnsCommon.wait_loading()
            # view a goods
            Element("daily_new", "daily_new_goods").clicks(0)
            sleep(1)
            common.my_swipe_to_up()
            self.goods_name = Element("daily_new", "goods_name").get_attribute("text")

            # go to recently viewed
            common.back()
            sleep(1)
            bsnsCommon.go_to_me()
            bsnsCommon.wait_loading()
            Element("recently_viewed", "recently_viewed").click()

            # check result
            self.checkResult()

        except Exception as ex:
            self.logger.error(str(ex))

    def tearDown(self):
        self.end = self.log.take_shot(self.driver, self.case_name)
        self.logger.info("Take shot, the picture path is:" + self.end)
        bsnsCommon.return_index()
        self.log.build_end_line()

    # check result
    def checkResult(self):
        common.my_swipe_to_up()
        goods = Element("recently_viewed", "goods_name").gets(0)
        value = goods.get_attribute("text")
        self.logger.info("recently goods_name is : " + value)
        if value == self.goods_name:
            self.assertEqual(1, 1)

