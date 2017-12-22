# coding:utf-8

import unittest
import paramunittest
import testSet.common.Log as Log
from testSet.common.DRIVER import MyDriver
from testSet.common.common import Element
from testSet.bsns import bsnsCommon
from time import sleep

addressGls = bsnsCommon.get_address_cls()
loginGls = bsnsCommon.get_login_cls()


@paramunittest.parametrized(*addressGls)
class TestAddAddress(unittest.TestCase):
    """
        case name
    """
    def setParameters(self, case_name, first_name, last_name, country, state, city, address_1, address_2, phone, zip_code, results, message):
        """
        get parameters of add address
        :param case_name:
        :param first_name:
        :param last_name:
        :param country:
        :param state:
        :param city:
        :param address_1:
        :param address_2:
        :param phone:
        :param zip_code:
        :param results:
        :param message:
        :return:
        """
        self.case_name = case_name
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.state = state
        self.city = city
        self.address_1 = address_1
        self.address_2 = address_2
        self.phone = phone
        self.zip_code = zip_code
        self.results = results
        self.message = message

    def setDescription(self):
        self.case_name

    def setUp(self):
        self.Begin = "../../result/image/1.png"
        self.check_point = "../../result/image/1.png"
        self.End = "../../result/image/1.png"

        # get driver
        self.driver = MyDriver.get_driver()
        self.case_no = self.case_name

        # get log
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_my_logger()

        # start test
        self.log.build_start_line(self.case_no)
        self.begin = self.log.take_shot(self.driver, self.case_name)
        self.logger.info("Take picture, the path is:" + self.begin)

        # open app
        self.logger.info("Open App")

    def testAddress(self):
        try:
            email = loginGls[0][1]
            password = loginGls[0][2]
            bsnsCommon.login(email, password)
            bsnsCommon.wait_loading()

            if Element("Alert", "update_title").is_exist():
                Element("Alert", "cancel").click()
            else:
                pass

            # go to 'ME'
            bsnsCommon.go_to_me()
            # go to address_book
            Element("address_management", "address_book").click()

            # add address
            Element("address_management", "add_address").click()
            bsnsCommon.input_address(self.first_name, self.last_name, self.phone, self.zip_code, self.address_1, self.address_2, self.city, self.country, self.state)

            # check result
            self.check_result()

        except Exception as ex:
            self.logger.error(str(ex))

    def tearDown(self):
        self.end = self.log.take_shot(self.driver, self.case_name)

        self.logger.info("Take picture, the path is:" + self.end)

        bsnsCommon.return_index()

        self.log.build_end_line(self.case_no)

    def check_result(self):

        sleep(1)

        # add address fail
        if Element("Alert", "layout").does_exist():
            value = Element("Alert", "message").get_attribute("text")
            self.assertEqual(value, self.message)
            Element("Alert", "confirm").click()
            sleep(1)

        # add address successfully
        if self.results == "1":
            value = Element("Address", "name_text").get_attribute("text")
            result = self.first_name + " " + self.last_name
            if value == result:
                self.assertEqual(1, 1)
                # delete address
                Element("Address", "delete_address").click()
                if Element("Alert", "layout").does_exist():
                    Element("Alert", "confirm").click()

