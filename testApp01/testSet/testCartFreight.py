import unittest
import testSet.common.Log as Log
from testSet.common.common import Element
from testSet.bsns import bsnsCommon
from testSet.common.DRIVER import MyDriver


class TestFreight(unittest.TestCase):

    def setUp(self):

        self.Begin = "../../result/image/1.png"
        self.CheckPoint = "../../result/image/1.png"
        self.End = "../../result/image/1.png"

        # get Driver
        self.driver = MyDriver.get_driver()
        self.case_name = "Test Freight"

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

    def testFreight(self):

        try:
            # Enter to the shopping cart
            self.logger.info("Enter to the shopping cart")
            Element("Shopping_cart", "shopping_cart").click()

            # clear the shopping cart
            bsnsCommon.clear_cart()

            # add goods to shopping cart
            self.logger.info("Add 1 goods to cart")
            self.goods_name_list = bsnsCommon.add_goods_in_cart("1")

            # enter the shopping cart
            self.logger.info("Enter to the shopping cart")
            Element("Shopping_cart", "shopping_cart").click()

            bsnsCommon.wait_loading()

            self.check_result()

        except Exception as ex:
            self.logger.error(str(ex))

    def tearDown(self):

        self.logger.info("Enter the shopping cart")

        Element("Shopping_cart", "shopping_cart").click()

        bsnsCommon.wait_loading()

        for good_name in self.goods_name_list:
            bsnsCommon.delete_goods_in_cart(good_name)

        self.End = self.log.take_shot(self.driver, self.case_name)

        self.logger.info("Take shot, the picture path is " + self.End)

        # return the index
        bsnsCommon.return_index()

        # test Start
        self.log.build_end_line(self.case_name)

    def check_result(self):

        result = Element("Shopping_cart", "total_price").get_attribute("text")

        total_price = result[result.find("$"):]

        while float(total_price) < 100:
            # change qty_add
            Element("Shopping_cart", "plus_qty").clicks(0)
        else:
            if Element("Shopping_cart", "shipping").is_exist():
                self.assertEqual("1", "1")
            else:
                self.assertEqual("1", "")
