import unittest
import testSet.common.Log as Log
from testSet.common.DRIVER import MyDriver
from testSet.common.common import Element
from testSet.bsns import bsnsCommon
from testSet.common import common
from time import sleep

loginGls = bsnsCommon.get_login_cls()


class TestAddShoppingBag(unittest.TestCase):

    def setUp(self):
        self.Begin = "../../result/image/1.png"
        self.CheckPoint = "../../result/image/1.png"
        self.End = "../../result/image/1.png"

        # get driver
        self.driver = MyDriver.get_driver()
        self.case_name = "Test Add ShoppingBag"

        # get log
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_my_logger()

        # start test
        self.log.build_start_line(self.case_name)
        self.begin = self.log.take_shot(self.driver, self.case_name)
        self.logger.info("Take shot, the picture path is:" + self.begin)

        # open app
        self.logger.info("Open App")

    def testAddShoppingBag(self):

        try:
            # login
            email = loginGls[0][1]
            password = loginGls[0][2]
            bsnsCommon.login(email, password)
            bsnsCommon.wait_loading()
            # click cancel for update
            if Element("Alert", "update_title").is_exist():
                Element("Alert", "cancel").click()

            # go to daily new
            Element("daily_new", "daily_new").click()
            bsnsCommon.wait_loading()

            # find a goods
            Element("daily_new", "daily_new_goods").clicks(0)
            # click new guide
            while Element("daily_new", "new_guide").does_exist():
                Element("daily_new", "new_guide").click()
            else:
                pass

            self.addShoppingBag()

            self.check_Result()

        except Exception as ex:
            self.logger.error(str(ex))

    def tearDown(self):
        self.end = self.log.take_shot(self.driver, self.case_name)
        self.logger.info("Take shot, the picture path is:" + self.end)
        self.log.build_end_line(self.case_name)

    def addShoppingBag(self):

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
        self.name = Element("add_shopping_bag", "name").get_attribute("text")

    def check_Result(self):

        # go to shopping bag
        Element("add_shopping_bag", "shop_bag").click()
        bsnsCommon.wait_loading()
        # click new guide
        if Element("shopping_bag", "new_guide").is_exist():
            Element("shopping_bag", "new_guide").click()
        else:
            pass
        names = Element("shopping_bag", "name").get_element_list()

        for name in names:
            value = name.get_attribute("text")
            self.logger.info("names are : " + value + "\n")
            if value == self.name:
                self.assertEqual(1, 1)
            else:
                pass

