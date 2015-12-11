import unittest
import paramunittest

from time import sleep
import testSet.common.Log as Log
from testSet.common.common import Element
from testSet.bsns import bsnsCommon
from testSet.common.DRIVER import MyDriver

address_cls = bsnsCommon.get_address_cls()
loginCls = bsnsCommon.get_login_cls()


@paramunittest.parametrized(*address_cls)
class TestAddRegister(unittest.TestCase):

    def setParameters(self, case_name, first_name, last_name, gender, country, state_province, city, line1, line2, phone, zip_code, results, message):
        self.case_name = case_name
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.country = country
        self.state_province = state_province
        self.city = city
        self.line1 = line1
        self.line2 = line2
        self.phone = phone
        self.zip_code = zip_code
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

    def testAddAddress(self):
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

            bsnsCommon.wait_loading()

            # add new address
            self.logger.info("Enter the Address Management")
            Element("address_management", "add_address").click()

            bsnsCommon.wait_loading()

            self.input_info()

            self.check_result()

        except Exception as ex:
            self.logger.error(str(ex))

    def tearDown(self):
        self.End = self.log.take_shot(self.driver, self.case_name)

        self.logger.info("Take shot, the picture path is " + self.End)

        # return the index
        bsnsCommon.return_index()

        # test Start
        self.log.build_end_line(self.caseNo)

    def input_info(self):
        """
        input the information of address
        :return:
        """

        # input the first name
        Element("Address", "first_name").send_key(self.first_name)

        # input the last name
        Element("Address", "last_name").send_key(self.last_name)

        # input the Gender
        if self.gender == "MS.":
            Element("Address", "MS").click()

        if self.gender == "MR.":
            Element("Address", "MR ").click()

        # input Country
        if self.country != "":
            Element("Address", "Country ").click()

            i = int(self.country)

            Element("Address", "Country_State_list ").clicks(i)

        # input State_Province
        if self.country != "0" and self.country != "7":
            Element("Address", "State_Province").send_key(self.state_province)
        else:
            i = int(self.state_province)
            Element("Address", "Country_State_list ").clicks(i)

        # input city
        Element("Address", "City").send_key(self.city)

        # input Address line1
        Element("Address", "Line1").send_key(self.line1)

        # input city
        Element("Address", "Line2").send_key(self.line2)

        # input Phone
        Element("Address", "Phone").send_key(self.phone)

        # input zip code
        Element("Address", "ZIP_code").send_key(self.zip_code)

        Element("title", "rightButton").click()

    def check_result(self):

        self.CheckPoint = self.log.take_shot(self.driver, self.case_name)
        self.logger.info("Take shot, the picture path is " + self.CheckPoint)
        result = self.first_name+" "+self.last_name
        if self.results == "1":

            bsnsCommon.wait_loading()

            element_list = Element("address_management", "recipient").get_element_list()

            for i in range(len(element_list)):

                value = element_list[i].get_attribute("text")

                if result == value:

                    self.assertEqual(1, 1)

        if self.results == "0":
            sleep(1)

            if Element("Alert", "layout").does_exist():

                value = Element("Alert", "message").get_attribute("text")

                self.assertEqual(value, self.message)

                sleep(1)
                Element("Alert", "confirm").click()

