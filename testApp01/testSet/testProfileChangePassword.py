import unittest
import paramunittest

from time import sleep
import testSet.common.Log as Log
from testSet.common.common import Element
from testSet.bsns import bsnsCommon
from testSet.common.DRIVER import MyDriver

change_password_cls = bsnsCommon.get_change_password_cls()
loginCls = bsnsCommon.get_login_cls()


@paramunittest.parametrized(*change_password_cls)
class TestChangePassword(unittest.TestCase):

    def setParameters(self,case_name, old_password, new_password, confirm_password, result, message):
        self.case_name = case_name
        self.new_password = new_password
        self.old_password = old_password
        self.confirm_password = confirm_password
        self.result = result
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

    def testChangePassword(self):
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

            # enter the account setting
            Element("profile", "profile_tv").clicks(0)
            bsnsCommon.wait_loading()

            # enter the change password
            Element("account_setting", "change_password").click()
            bsnsCommon.wait_loading()

            self.input_password(self.old_password, self.new_password, self.confirm_password)

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

    def input_password(self, old_password, new_password, confirm_password):

        # input old_password
        Element("change_password", "pass_input").send_keys(0, old_password)

        # input new_password
        Element("change_password", "pass_input").send_keys(1, new_password)

        # input confirm_password
        Element("change_password", "pass_input").send_keys(1, confirm_password)

        Element("change_password", "change_password").click()

    def check_result(self):
        sleep(1)

        if Element("Alert", "layout").does_exist():

            value = Element("Alert", "message").get_attribute("text")

            self.assertEqual(value, self.message)

            sleep(1)
            Element("Alert", "confirm").click()

        if self.result == "1":

            # enter the change password
            Element("account_setting", "change_password").click()
            bsnsCommon.wait_loading()

            self.input_password(self.new_password, self.old_password, self.old_password)

            sleep(1)
            Element("Alert", "confirm").click()



