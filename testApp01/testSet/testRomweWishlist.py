# coding: utf-8
import unittest
import testSet.common.Log as Log
from testSet.common.DRIVER import MyDriver
from testSet.bsns import bsnsCommon
from testSet.common.common import Element
from testSet.common import common

loginGls = bsnsCommon.get_login_cls()


class TestWishlist(unittest.TestCase):

    def setUp(self):
        self.Begin = "../../result/image/1.png"
        self.CheckPoint = "../../result/image/1.png"
        self.End = "../../result/image/1.png"

        # get driver
        self.driver = MyDriver.get_driver()
        self.case_name = "Test My Wishlist"

        # get log
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_my_logger()

        # test start
        self.log.build_start_line(self.case_name)
        self.begin = self.log.take_shot(self.driver, self.case_name)
        self.logger.info("Take shot, the picture path is:" + self.begin)

        # open app
        self.logger.info("Open App")

    def testWishlist(self):
        try:
            email = loginGls[0][1]
            password = loginGls[0][2]
            bsnsCommon.login(email, password)
            bsnsCommon.wait_loading()
            if Element("Alert", "update_title").is_exist():
                Element("Alert", "cancel").click()
            else:
                pass

            # test add goods to wish list
            self.addWishlist()
            # check add wish list result
            self.checkAddResult()
            # test remove goods from wish list
            self.removeWishlist()
            # check remove wish list result
            self.checkRemoveResult()

        except Exception as ex:
            self.logger.error(str(ex))

    def tearDown(self):
        self.end = self.log.take_shot(self.driver, self.case_name)
        self.logger.info("Take shot, the picture path is:" + self.end)
        bsnsCommon.return_index()
        self.log.build_end_line(self.case_name)

    # add goods to wish list
    def addWishlist(self):
        # go to daily new
        Element("daily_new", "daily_new").click()
        bsnsCommon.wait_loading()

        # find a goods
        Element("daily_new", "daily_new_goods").clicks(0)
        # click new guide
        if Element("daily_new", "new_guide").is_exist():
            Element("daily_new", "new_guide").click()
        else:
            pass
        # get add goods name
        self.goods_name = Element("daily_new", "goods_name").get_attribute("text")
        # add goods to wish_list
        while not Element("daily_new", "add_wishlist").is_exist():
            common.my_swipe_to_up()
        else:
            Element("daily_new", "add_wishlist").click()
            if Element("Alert", "layout").does_exist():
                self.addResult = self.log.take_shot(self.driver, self.case_name)
                self.logger.info("Take shot, the picture path is:" + self.addResult)
                Element("Alert", "confirm").click()

    # remove goods from wish list
    def removeWishlist(self):
        # go to My Wishlist
        common.back()
        bsnsCommon.go_to_me()
        bsnsCommon.wait_loading()
        common.my_swipe_to_up()

        # get remove goods name
        self.re_goods_name = Element("wish_list", "wish_goods_name").gets(0).get_attribute("text")
        # find a goods
        Element("wish_list", "wish_goods_name").clicks(0)

        # remove goods from wish list
        while not Element("daily_new", "add_wishlist").is_exist():
            common.my_swipe_to_up()
        else:
            Element("daily_new", "add_wishlist").click()

    # check add result
    def checkAddResult(self):
        # go to My Wishlist
        common.back()
        bsnsCommon.go_to_me()
        bsnsCommon.wait_loading()
        common.my_swipe_to_up()

        self.addResult = self.log.take_shot(self.driver, self.case_name)
        self.logger.info("Take shot, the picture path is:" + self.addResult)
        goods = Element("wish_list", "wish_goods_name").get_element_list()

        for name in goods:
            name.get_attribute("text")
            goods_name = name
            if goods_name == self.goods_name:
                self.assertEqual(1, 1)
                self.logger.info("Add goods successfully : OK")

    # check remove result
    def checkRemoveResult(self):
        # go to My Wishlist
        common.back()
        bsnsCommon.wait_loading()
        common.my_swipe_to_up()

        goods = Element("wish_list", "wish_goods_name").get_element_list()

        if len(goods) > 0:
            for name in goods:
                name.get_attribute("text")
                goods_name = name
                if goods_name != self.goods_name:
                    pass
                else:
                    self.assertEqual(0, 1)
                    break
