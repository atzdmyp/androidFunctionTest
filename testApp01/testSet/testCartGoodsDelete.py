import unittest
import testSet.common.Log as Log
from testSet.common.common import Element
from testSet.bsns import bsnsCommon
from testSet.common.DRIVER import MyDriver


class TestDeleteGoods(unittest.TestCase):

    def setUp(self):

        self.Begin = "../../result/image/1.png"
        self.CheckPoint = "../../result/image/1.png"
        self.End = "../../result/image/1.png"

        # get Driver
        self.driver = MyDriver.get_driver()
        self.case_name = "Test shopping cart"

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

    def testDeleteGoods(self):

        try:

            # add goods to cart
            self.logger.info("Add 2 goods to cart")
            self.goods_name_list = bsnsCommon.add_goods_in_cart(2)

            # Enter to the shopping cart
            self.logger.info("Enter to the shopping cart")
            Element("Shopping_cart", "shopping_cart").click()

            bsnsCommon.wait_loading()

            # delete one goods
            bsnsCommon.delete_goods_in_cart(self.goods_name_list[0])

            # get the total_price
            total_price = bsnsCommon.get_total_price_in_cart()

            # check result
            self.check_result(total_price)

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

    def check_result(self, price):

        self.CheckPoint = self.log.take_shot(self.driver, self.case_name)

        result = Element("Shopping_cart", "total_price").get_attribute("text")

        total_price = result[result.find("$")+1:]

        self.assertEqual(total_price, price)




