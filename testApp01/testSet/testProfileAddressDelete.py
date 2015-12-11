import unittest
import paramunittest

from time import sleep
import testSet.common.Log as Log
from testSet.common.common import Element
from testSet.bsns import bsnsCommon
from testSet.common.DRIVER import MyDriver

loginCls = bsnsCommon.get_login_cls()
address_cls = bsnsCommon.get_address_cls()


class TestProfileAddressAdd(unittest.TestCase):

    def setUp(self):
        self.Begin = "../../result/image/1.png"
        self.CheckPoint = "../../result/image/1.png"
        self.End = "../../result/image/1.png"

        # get Driver
        self.driver = MyDriver.get_driver()
        self.caseNo = "Test delete Address"

        # get Log
        self.log = Log.MyLog().get_log()
        self.logger = self.log.get_my_logger()

        # test Start
        self.log.build_start_line(self.caseNo)

        self.Begin = self.log.take_shot(self.driver, self.caseNo)

        self.logger.info("Take shot, the picture path is " + self.Begin)

        # open app
        bsnsCommon.open_app()

        self.logger.info("Open app")

    def testProfileAddressDelete(self):
        try:
            self.logger.info("Enter the profile")

            # find the bottom Navigation bar
            while not Element("BottomNavigation", "BottomNavigation").is_exist():
                sleep(1)
            else:
                # enter the profile
                Element("BottomNavigation", "profile").click()

            bsnsCommon.wait_loading()

            # first login
            user_name = loginCls[0][1]
            password = loginCls[0][2]

            bsnsCommon.login(user_name, password)

            bsnsCommon.wait_loading()

            # enter my address
            self.logger.info("Enter the my address")

            Element("profile", "profile_tv").clicks(3)

            self.addAddress()

            # delete address

            bsnsCommon.wait_loading()
        except Exception as ex:
            self.logger.error(str(ex))

    def tearDown(self):
        self.End = self.log.take_shot(self.driver, self.caseNo)

        self.logger.info("Take shot, the picture path is " + self.End)

        # return the index
        bsnsCommon.return_index()

        # test Start
        self.log.build_end_line(self.caseNo)

    def addAddress(self):
        # add new address
        self.logger.info("Enter the Address Management")
        Element("address_management", "add_address").click()

        bsnsCommon.wait_loading()

        # input the first name
        Element("Address", "first_name").send_key(address_cls[0][1])

        # input the last name
        Element("Address", "last_name").send_key(address_cls[0][2])

        # input the Gender
        if address_cls[0][3] == "MS.":
            Element("Address", "MS").click()

        if address_cls[0][3] == "MR.":
            Element("Address", "MR ").click()

        # input Country
        if address_cls[0][4] != "":
            Element("Address", "Country ").click()

            i = int(address_cls[0][4])

            Element("Address", "Country_State_list ").clicks(i)

        # input State_Province
        if address_cls[0][4] != "0" and address_cls[0][4] != "7":
            Element("Address", "State_Province").send_key(address_cls[0][5])
        else:
            i = int(address_cls[0][5])
            Element("Address", "Country_State_list ").clicks(i)

        # input city
        Element("Address", "City").send_key(address_cls[0][6])

        # input Address line1
        Element("Address", "Line1").send_key(address_cls[0][7])

        # input city
        Element("Address", "Line2").send_key(address_cls[0][8])

        # input Phone
        Element("Address", "Phone").send_key(address_cls[0][9])

        # input zip code
        Element("Address", "ZIP_code").send_key(address_cls[0][10])

        Element("title", "rightButton").click()



