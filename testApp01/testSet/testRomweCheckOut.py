import unittest
import paramunittest
import testSet.common.Log as Log
from testSet.common.DRIVER import MyDriver
from testSet.common.common import Element
from testSet.bsns import bsnsCommon
from testSet.common import common

loginGls = bsnsCommon.get_login_cls()
addressGls = bsnsCommon.get_address_cls()
checkGls = bsnsCommon.get_checkout_cls()


@paramunittest.parametrized(*checkGls)
class TestCheckOut(unittest.TestCase):

    def setParameters(self, case_name, shipping_method, payment_method, coupon_code, freebie, card_number, cvv):
        """
        get parameters for checkout
        :param case_name:
        :param shipping_method:
        :param payment_method:
        :param coupon_code:
        :param freebie:
        :param card_number:
        :param cvv:
        :return:
        """
        self.caseName = case_name
        self.shipping_method = shipping_method
        self.payment_method = str(payment_method)
        self.coupon_code = coupon_code
        self.freebie = freebie
        self.card_number = card_number
        self.cvv = cvv
        self.code_coupon = 0
        self.code_freebie = 0
        self.result = 1

    def description(self):
        return self.caseName

    def setUp(self):
        self.Begin = "../../result/image/1.png"
        self.CheckPoint = "../../result/image/1.png"
        self.End = "../../result/image/1.png"

        # get driver
        self.driver = MyDriver.get_driver()
        self.caseNo = self.caseName

        # get log
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_my_logger()

        # start test
        self.log.build_start_line(self.caseName)
        self.begin = self.log.take_shot(self.driver, self.caseNo)
        self.logger.info("Take a shot, the picture path is:" + self.begin)

        # open app
        self.logger.info("Open App")

    def testCheckOut(self):
        try:
            email = loginGls[0][1]
            password = loginGls[0][2]
            bsnsCommon.login(email, password)
            bsnsCommon.wait_loading()
            bsnsCommon.cancel_update()

            bsnsCommon.add_goods_in_cart(1)
            # enter shopping bag
            Element("title", "right_shopping_bag").click()
            bsnsCommon.wait_loading()
            # get total price in shopping car
            self.total_price = bsnsCommon.get_total_price_in_cart()
            Element("shopping_bag", "checkout").click()

            # add address
            bsnsCommon.add_address_in_checkout(addressGls[0][1], addressGls[0][2], addressGls[0][3], addressGls[0][4], addressGls[0][5], addressGls[0][6], addressGls[0][7], addressGls[0][8], addressGls[0][9])
            bsnsCommon.wait_loading()

            # choose shipping and payment method
            bsnsCommon.choose_shipping_payment_methods_in_checkout(self.shipping_method, self.payment_method)

            # input coupon code
            self.code_coupon = bsnsCommon.input_coupon_code(self.coupon_code)
            # input freebie
            self.code_freebie = bsnsCommon.input_freebie(self.freebie)

            # check price
            if self.check_price():
                # enter payment page
                Element("checkout", "place_order").click()
                bsnsCommon.wait_loading()
                if bsnsCommon.input_card_paypal_message_in_payment(self.payment_method, self.card_number, self.cvv):
                    self.result = 0

            # check result
            self.check_result()

        except Exception as ex:
            self.logger.error(str(ex))

    def tearDown(self):
        self.end = self.log.take_shot(self.driver, self.caseNo)
        self.logger.info("Take a shot, the picture path is:" + self.end)
        self.log.build_end_line(self.caseName)

    def check_price(self):
        result = True
        # get total price in checkout
        last_total_price = bsnsCommon.get_total_price_in_checkout()
        # get shipping price in checkout
        shipping_price = bsnsCommon.get_shipping_price_in_checkout()
        # get subtotal price in checkout
        subtotal_price = bsnsCommon.get_subtotal_price_in_checkout()

        if not Element("checkout", "place_order").is_exist():
            common.my_swipe_to_up()
        else:
            if self.code_coupon == 0 and self.code_freebie == 0:
                if subtotal_price != self.total_price:
                    self.logger.info("Subtotal_price is not equal to total_price of shopping car, price is wrong.")
                    result = False
                else:
                    if (subtotal_price + shipping_price) != last_total_price:
                        self.logger.info("Subtotal_price plus shipping_price equals is not last_total_price, price is wrong.")
                        result = False
            elif self.code_coupon == 1 and self.code_freebie == 0:
                if Element("checkout", "coupon_code_price").is_exist():
                    # get coupon code price in checkout
                    coupon_code_price = bsnsCommon.get_coupon_code_price_in_checkout()
                    if self.total_price >= coupon_code_price:
                        if subtotal_price != (self.total_price - coupon_code_price):
                            self.logger.info("The total_price minus coupon_code_price is not subtotal_price, subtotal price is wrong.")
                            result = False
                    else:
                        if int(subtotal_price) != 0:
                            self.logger.info("The subtotal price is wrong.")
                            result = False
                        else:
                            if last_total_price != shipping_price:
                                self.logger.info("The total price in checkout is wrong.")
                                result = False
                else:
                    self.logger.info("Used coupon code but it is not be shown in price list, price list is wrong.")
                    result = False
            elif self.code_coupon == 0 and self.code_freebie == 1:
                if Element("checkout", "freebie_price").is_exist():
                    # get freebie price in checkout
                    freebie_price = bsnsCommon.get_freebie_price_in_checkout()
                    if self.total_price >= freebie_price:
                        if subtotal_price != (self.total_price - freebie_price):
                            self.logger.info("The total_price minus freebie_price is not subtotal_price, subtotal price is wrong.")
                            result = False
                    else:
                        if int(subtotal_price) != 0:
                            self.logger.info("The subtotal price is wrong.")
                            result = False
                        else:
                            if last_total_price != shipping_price:
                                self.logger.info("The total price in checkout is wrong.")
                                result = False
                else:
                    self.logger.info("Used shein points but it is not be shown in price list, price list is wrong.")
                    result = False
            elif self.code_coupon == 1 and self.code_freebie == 1:
                if Element("checkout", "coupon_code_price").is_exist() and Element("checkout", "freebie_price").is_exist():
                    # get coupon code price in checkout
                    coupon_code_price = bsnsCommon.get_coupon_code_price_in_checkout()
                    # get freebie price in checkout
                    freebie_price = bsnsCommon.get_freebie_price_in_checkout()
                    if self.total_price > coupon_code_price:
                        subtotal_price_text = self.total_price - coupon_code_price
                        subtotal_price_text2 = subtotal_price_text - freebie_price
                        if subtotal_price_text2 >= float(0):
                            if subtotal_price != subtotal_price_text2:
                                self.logger.info("Used coupon code and freebie but subtotal price is wrong.")
                                result = False
                        else:
                            if int(subtotal_price) != 0:
                                self.logger.info("The subtotal price is wrong.")
                                result = False
                    else:
                        if int(subtotal_price) != 0 or int(freebie_price) != 0:
                            self.logger.info("The subtotal price and freebie price are wrong.")
                            result = False
                else:
                    self.logger.info("Used coupon code and shein points but they are not be shown in price list, price list is wrong.")
                    result = False
        return result

    def check_result(self):
        self.assertEqual(self.result, 0)
