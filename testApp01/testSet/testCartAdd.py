import unittest
import paramunittest

from time import sleep
import testSet.common.Log as Log
import testSet.common.common as myCommon
from testSet.common.common import Element
from testSet.bsns import bsnsCommon
from testSet.common.DRIVER import MyDriver

add_cart_cls = bsnsCommon.get_add_cart_cls()


@paramunittest.parametrized(*add_cart_cls)
class TestAddCart(unittest.TestCase):

    def setParameters(self, case_name, size, qty, results, message):
        self.case_name = case_name
        self.size = size
        self.qty = qty
        self.results = results
        self.message = message

    def setUp(self):
        self.Begin = "../../result/image/1.png"
        self.CheckPoint = "../../result/image/1.png"
        self.End = "../../result/image/1.png"

        # get Driver
        self.driver = MyDriver.get_driver()
        self.caseNo = self.case_name

        # get Log
        self.log = Log.MyLog().get_log()
        self.logger = self.log.get_my_logger()

        # test Start
        self.log.build_start_line(self.caseNo)

        self.Begin = self.log.take_shot(self.driver, self.case_name)

        self.logger.info("Take shot, the picture path is " + self.Begin)

        # open app
        bsnsCommon.open_app()

        self.logger.info("Open app")

    def testAddCart(self):
        try:
            self.logger.info("Enter the goods details")

            while not Element("Shop", "goods").is_exist():
                myCommon.my_swipe_to_up()
            else:
                myCommon.my_swipe_to_up()
                Element("Shop", "goods").clicks(0)

            bsnsCommon.wait_loading()

            self.logger.info("Get the goods's name")

            self.goods_name = Element("title", "title").get_attribute("text")

            self.logger.info("Enter the shopping cart")

            Element("Shopping_cart", "shopping_cart").click()

            bsnsCommon.wait_loading()

            bsnsCommon.delete_goods_in_cart(self.goods_name)

            myCommon.back()

            bsnsCommon.wait_loading()

            goods_num = Element("Shopping_cart", "shopping_cart").get_attribute("text")

            self.logger.info("Add goods to cart")

            self.add_cart()

            self.check_result(goods_num)

        except Exception as ex:
            self.logger.error(str(ex))

    def tearDown(self):
        self.End = self.log.take_shot(self.driver, self.case_name)

        self.logger.info("Take shot, the picture path is " + self.End)

        self.logger.info("Enter the shopping cart")

        Element("Shopping_cart", "shopping_cart").click()

        bsnsCommon.wait_loading()

        # delete the goods which we add to shopping cart
        bsnsCommon.delete_goods_in_cart(self.goods_name)

        # return the index
        bsnsCommon.return_index()

        # test Start
        self.log.build_end_line(self.caseNo)

    def add_cart(self):
        """
        add goods to shopping cart
        :return:
        """

        self.logger.info("Enter add cart page")
        Element("Good_details", "add").click()

        if Element("add_cart", "add_cart").does_exist():

            if self.size == "1":
                self.logger.info("Select size")
                Element("add_cart", "size").clicks(0)

            if self.qty == "0":
                self.logger.info("Input qty")
                Element("add_cart", "qty").get().clear()

            Element("add_cart", "buy").click()

    def check_result(self, num):
        """
        check the result
        :return:
        """

        self.CheckPoint = self.log.take_shot(self.driver, self.case_name)
        self.logger.info("Take shot, the picture path is " + self.CheckPoint)

        if self.results == '1':

            goods_num = Element("Shopping_cart", "shopping_cart").get_attribute("text")

            self.assertEqual(int(num)+1, int(goods_num))

        if self.results == '0':

            sleep(1)

            if Element("Alert", "layout").does_exist():

                value = Element("Alert", "message").get_attribute("text")

                self.assertEqual(value, self.message)

                sleep(1)
                Element("Alert", "confirm").click()

                Element("add_cart", "cancel").click()