# coding: utf-8
import unittest
import paramunittest
import testSet.common.Log as Log
from testSet.common.DRIVER import MyDriver
from testSet.bsns import bsnsCommon
from testSet.common.common import Element
from time import sleep

loginGls = bsnsCommon.get_login_cls()
addressGls = bsnsCommon.get_address_cls()


class TestDeleteAddress(unittest.TestCase):
    """
    case name
    """
    def setUp(self):
        self.Begin = "../../result/image/1.png"
        self.CheckPoint = "../../result/image/1.png"
        self.End = "../../result/image/1.png"

        # get driver
        self.driver = MyDriver.get_driver()
        self.case_no = "Test delete address"

        # get log
        self.Log = Log.MyLog.get_log()
        self.logger = self.Log.get_my_logger()

        # start test
        self.Log.build_start_line(self.case_no)
        self.begin = self.Log.take_shot(self.driver, self.case_no)
        self.logger.info("Take shot, the picture is:" + self.begin)

        # open app
        self.logger.info("Open App")

    def testDeleteAddress(self):
        try:
            email = loginGls[0][1]
            password = loginGls[0][2]
            # login app
            bsnsCommon.login(email, password)
            bsnsCommon.wait_loading()
            if Element("Alert", "update_title").is_exist():
                Element("Alert", "cancel").click()
            else:
                pass

            # go to 'ME'
            bsnsCommon.go_to_me()
            sleep(1)
            # go to add address page
            Element("address_management", "address_book").click()

            if Element("Address", "delete_address").is_exist():
                # delete address
                Element("Address", "delete_address").clicks(0)
                if Element("Alert", "layout").does_exist():
                    Element("Alert", "confirm").click()
            else:
                self.addAddress()
                # delete address
                Element("Address", "delete_address").clicks(0)
                if Element("Alert", "layout").does_exist():
                    Element("Alert", "confirm").click()

        except Exception as ex:
            self.logger.error(str(ex))

    def tearDown(self):

        self.end = self.Log.take_shot(self.driver, self.case_no)

        self.logger.info("Take shot, the picture path is:" + self.end)

        self.log.build_end_line(self.case_no)

    def addAddress(self):
        # enter given name
        Element("Address", "edit_elements").send_keys(0, addressGls[0][1])
        # enter surname
        Element("Address", "edit_elements").send_keys(1, addressGls[0][2])
        # enter phone
        Element("Address", "edit_elements").send_keys(2, addressGls[0][3])
        # enter zip code
        Element("Address", "edit_elements").send_keys(3, addressGls[0][4])
        # enter address line1
        Element("Address", "edit_elements").send_keys(4, addressGls[0][5])
        # enter address line2
        Element("Address", "edit_elements").send_keys(5, addressGls[0][6])
        # enter city
        Element("Address", "edit_elements").send_keys(6, addressGls[0][7])
        # enter country
        if addressGls[0][8] != "":
            Element("Address", "edit_elements").clicks(7)
            sleep(1)
            i = int(addressGls[0][8])
            Element("Address", "country_list").clicks(i)
        # enter state/province
        if addressGls[0][8] == "0" and addressGls[0][8] == "7" and addressGls[0][8] == "8":
            j = int(addressGls[0][9])
            Element("Address", "country_list").clicks(j)
        else:
            Element("Address", "edit_elements").send_keys(8, addressGls[0][9])
        # click done button
        Element("Address", "done_btn").click()
