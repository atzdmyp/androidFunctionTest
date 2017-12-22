# -*- coding: UTF-8 -*-
import unittest
import paramunittest
import testSet.common.Log as Log
from testSet.common.DRIVER import MyDriver
from testSet.common.common import Element
from testSet.bsns import bsnsCommon
from time import sleep

loginCls = bsnsCommon.get_login_cls()


@paramunittest.parametrized(*loginCls)
class TestLogin(unittest.TestCase):
    """
    case_name
    """

    def setParameters(self, case_name, email, password, results, message):
        """
        get parameters of login
        :param case_name:
        :param email:
        :param password:
        :param results:
        :param message:
        :return:
        """
        self.case_name = str(case_name)
        self.email = str(email)
        self.password = str(password)
        self.results = str(results)
        self.message = str(message)

    def description(self):
        return self.case_name

    def setUp(self):
        self.Begin = "../../result/image/1.png"
        self.CheckPoint = "../../result/image/1.png"
        self.End = "../../result/image/1.png"

        # get driver
        self.driver = MyDriver.get_driver()
        self.caseNo = self.case_name

        # get log
        self.log = Log.MyLog().get_log()
        self.logger = self.log.get_my_logger()

        # start test
        self.log.build_start_line(self.caseNo)
        self.begin = self.log.take_shot(self.driver, self.case_name)
        self.logger.info("Take shot, the picture path is" + self.begin)

        # open app
        # bsnsCommon.open_app()
        self.logger.info("Open App")

    def testLogin(self):
        """
        Test Login
        :return:
        """
        try:
            # login the app
            bsnsCommon.login(self.email, self.password)
            if Element("Alert", "update_title").is_exist():
                Element("Alert", "cancel").click()
            else:
                pass

            self.check_result()

        except Exception as ex:
            self.logger.err(str(ex))

    def tearDown(self):
        self.End = self.log.take_shot(self.driver, self.case_name)
        self.logger.info("Take shot, the picture path is" + self.End)

        # test end
        self.log.build_end_line(self.caseNo)

    def check_result(self):
        """
        check result
        :return:
        """
        self.checkPoint = self.log.take_shot(self.driver, self.case_name)
        self.logger.info("Take shot, the picture path is:" + self.checkPoint)

        # login successfully
        if self.results == '1':
            bsnsCommon.wait_loading()
            if not Element("Alert", "layout").dose_exist():
                self.message = ""

                if Element("BottomNavigation", "BottomNavigation").dose_exist():
                    value = ""
                    self.assertEqual(value, self.message)
                    bsnsCommon.logout()

        # login fail
        if self.results == '0':

            sleep(1)

            if Element("Alert", "layout").does_exist():
                value = Element("Alert", "message").get_attribute("text")

                self.assertEqual(value, self.message)

                sleep(1)
                Element("Alert", "confirm").click()
            else:
                pass
