import unittest
from time import sleep
import testSet.common.Log as Log
from testSet.common.common import Element
from testSet.bsns import bsnsCommon
from testSet.common.DRIVER import MyDriver
import os


class TestQty(unittest.TestCase):

    def setUp(self):
        self.Begin = "../../result/image/1.png"
        self.CheckPoint = "../../result/image/1.png"
        self.End = "../../result/image/1.png"

        self.message_max = "Please be noted the maxium number is 999"
        self.message_min = "Please enter a correct amount"

        # get Driver
        self.driver = MyDriver.get_driver()
        self.case_name = "test the qty in shopping cart"

        # get Log
        self.log = Log.MyLog().get_log()
        self.logger = self.log.get_my_logger()

        # test Start
        self.log.build_start_line(self.case_name)

        self.Begin = self.log.take_shot(self.driver, self.case_name)

        self.logger.info("Take shot, the picture path is " + self.Begin)

        # open app
        bsnsCommon.open_app()

        self.logger.info("Open app")

    def testQty_plus(self):

        try:
            # add goods to cart
            self.logger.info("Add 1 goods to cart")
            self.goods_name_list = bsnsCommon.add_goods_in_cart(1)

            # Enter to the shopping cart
            self.logger.info("Enter to the shopping cart")
            Element("Shopping_cart", "shopping_cart").click()

            bsnsCommon.wait_loading()

            Element("Shopping_cart", "goods_num").send_keys(0, "999")

            os.popen("adb shell input keyevent 61")
            sleep(1)
            os.popen("adb shell input keyevent 66")

            # change qty_add
            Element("Shopping_cart", "plus_qty").clicks(0)

            if Element("Alert", "layout").does_exist():

                value = Element("Alert", "message").get_attribute("text")

                self.assertEqual(value, self.message_max)

                sleep(1)
                Element("Alert", "confirm").click()

            # return the index
            bsnsCommon.return_index()

        except Exception as ex:
            self.logger.error(str(ex))

    def testQty_minus(self):
        try:

            # Enter to the shopping cart
            self.logger.info("Enter to the shopping cart")
            Element("Shopping_cart", "shopping_cart").click()

            bsnsCommon.wait_loading()
            Element("Shopping_cart", "goods_num").send_keys(0, "0")

            # change qty_minus
            os.popen("adb shell input keyevent 61")
            sleep(1)
            os.popen("adb shell input keyevent 66")

            if Element("Alert", "layout").does_exist():

                value = Element("Alert", "message").get_attribute("text")

                self.assertEqual(value, self.message_min)

                sleep(1)
                Element("Alert", "confirm").click()
            # return the index
            bsnsCommon.return_index()

        except Exception as ex:
            self.logger.error(str(ex))

    def tearDown(self):

        for good_name in self.goods_name_list:
            bsnsCommon.delete_goods_in_cart(good_name)

        self.End = self.log.take_shot(self.driver, self.case_name)

        self.logger.info("Take shot, the picture path is " + self.End)

        # return the index
        bsnsCommon.return_index()

        # test Start
        self.log.build_end_line(self.case_name)