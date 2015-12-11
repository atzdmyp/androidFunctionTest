import unittest
import paramunittest

from time import sleep
import testSet.common.Log as Log
from testSet.common.common import Element
from testSet.bsns import bsnsCommon
from testSet.common.DRIVER import MyDriver

register_cls = bsnsCommon.get_register_cls()


@paramunittest.parametrized(*register_cls)
class TestRegister(unittest.TestCase):

    def setParameters(self, case_name, email, password, confirm_password, results, message):
        """
        get the parameter for register
        :param case_name:
        :param email:
        :param password:
        :param confirm_password:
        :param results:
        :param message:
        :return:
        """
        self.case_name = case_name
        self.email = email
        self.password = password
        self.confirm_password = confirm_password
        self.results = results
        self.message = message

    def setUp(self):

        # get Driver
        self.driver = MyDriver.get_driver()
        self.caseNo = self.case_name

        # get Log
        self.log = Log.MyLog().get_log()
        self.logger = self.log.get_my_logger()

        # test Start
        self.log.build_start_line(self.case_name)

        # open app
        bsnsCommon.open_app()

        self.logger.info("Open app")

    def testRegister(self):
        """
        test register
        :return:
        """
        try:

            self.logger.info("Enter the profile page")
            # find the bottom Navigation bar
            while not Element("BottomNavigation", "BottomNavigation").is_exist():
                sleep(1)
            else:
                # enter the profile
                Element("BottomNavigation", "profile").click()

            bsnsCommon.wait_loading()

            self.logger.info("Enter the sign in page")

            if not Element("profile", "SignIn").is_exist():

                self.logger.debug("Current is already login, first logout")

                bsnsCommon.logout()

            Element("profile", "SignIn").click()

            bsnsCommon.wait_loading()

            self.logger.info("Enter the register page")

            Element("login", "register").click()

            bsnsCommon.wait_loading()

            self.logger.info("input email,password,confirm_password")
            self.register()

            bsnsCommon.wait_loading()

            self.logger.info("check the %s result"%(self.case_name))
            self.check_result()

        except Exception as ex:
            self.logger.error(str(ex))

    def tearDown(self):
        # return the index
        bsnsCommon.return_index()

        # test Start
        self.log.build_end_line(self.case_name)

    def register(self):
        """
        register
        :return:
        """
        Element("register", "input").send_keys(0, self.email)
        Element("register", "input").send_keys(1, self.password)
        Element("register", "input").send_keys(2, self.confirm_password)

        Element("register", "register").click()

    def check_result(self):
        """
        check the result
        :return:
        """

        # register success
        if self.results == "1":
            value = Element("profile", "user").get_attribute("text")

            self.assertEqual(value, self.message)

        # register fail
        if self.results == "0":
            if Element("Alert", "layout").does_exist():

                value = Element("Alert", "message").get_attribute("text")

                self.assertEqual(value, self.message)

                Element("Alert", "confirm").click()
