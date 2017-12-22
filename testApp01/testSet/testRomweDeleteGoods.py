import unittest
import testSet.common.Log as Log
from testSet.common.DRIVER import MyDriver
from testSet.common.common import Element
from testSet.bsns import bsnsCommon
from testSet.common import common

loginGls = bsnsCommon.get_login_cls()


class TestDeleteGoods(unittest.TestCase):

    def setUp(self):
        self.Begin = "../../result/image/1.png"
        self.CheckPoint = "../../result/image/1.png"
        self.End = "../../result/image/1.png"

        # get driver
        self.driver = MyDriver.get_driver()
        self.case_name = "testRomweDeleteGoods"

        # get log
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_my_logger()

        # start test
        self.log.build_start_line(self.case_name)
        self.begin = self.log.take_shot(self.driver, self.case_name)
        self.logger.info("Take a shot, the picture path is:" + self.begin)

        # open app
        self.logger.info("Open App")

    def testDeleteGoods(self):
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
            while Element("daily_new", "new_guide").is_exist():
                Element("daily_new", "new_guide").click()
            else:
                pass

            self.deleteGoods()

            self.check_result()

        except Exception as ex:
            self.logger.error(str(ex))

    def deleteGoods(self):
        # add goods to shopping bag
        # click add to bag
        while not Element("add_shopping_bag", "add_bag").is_exist():
            common.my_swipe_to_up()
        else:
            Element("add_shopping_bag", "add_bag").click()
        # choose size
        if Element("add_shopping_bag", "size").is_exist():
            Element("add_shopping_bag", "size").clicks(0)
        # click done
        if not Element("add_shopping_bag", "add_done").is_exist():
            common.my_swipe_to_up()
        else:
            Element("add_shopping_bag", "add_done").click()
        bsnsCommon.wait_loading()

        # go to shopping bag
        Element("add_shopping_bag", "shop_bag").click()
        bsnsCommon.wait_loading()
        # click new guide
        if Element("shopping_bag", "new_guide").is_exist():
            Element("shopping_bag", "new_guide").click()
        else:
            pass

        goods = Element("shopping_bag", "name").get_element_list()
        self.length = len(goods)

        # delete a goods
        if len(goods) == 1:
            common.my_swipe_to_right_2()
            if Element("shopping_bag", "delete").is_exist():
                Element("shopping_bag", "delete").click()
        elif len(goods) >= 2:
            while not Element("shopping_bag", "shopping").does_exist():
                common.my_swipe_to_up()
            else:
                common.my_swipe_to_right()
                if Element("shopping_bag", "delete").is_exist():
                    Element("shopping_bag", "delete").click()

    def tearDown(self):
        self.end = self.log.take_shot(self.driver, self.case_name)
        self.logger.info("Take a shot, the picture path is:" + self.end)
        self.log.build_end_line(self.case_name)

    def check_result(self):
        goods_list = Element("shopping_bag", "name").get_element_list()
        length2 = len(goods_list)
        self.logger.info("length : " + str(self.length) + "\n" + "length2 : " + str(length2))

        if self.length == length2 + 1:
            self.assertEqual(1, 1)
        else:
            self.assertEqual(0, 1)

        while not Element("BottomNavigation", "BottomNavigation").is_exist():
            common.back()
        else:
            pass
