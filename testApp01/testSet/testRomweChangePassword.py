# -*- coding: utf-8 -*-

import unittest
import paramunittest
import threading
import testSet.common.Log as Log
from testSet.common.common import Element
from testSet.common.DRIVER import MyDriver
from testSet.bsns import bsnsCommon
from time import sleep

changePasswordCls = bsnsCommon.get_change_password_cls()
loginCls = bsnsCommon.get_login_cls()


@paramunittest.parametrized(*changePasswordCls)
class TestChangePassword(unittest.TestCase):
    """
        case name
    """

    def setParameters(self, case_name, old_password, new_password, confirm_password, result, message):
        """
        get parameters of changePassword
        :param case_name:
        :param old_password:
        :param new_password:
        :param confirm_password:
        :param result:
        :param message:
        :return:
        """
        self.caseName = case_name
        self.oldPassword = old_password
        self.newPassword = new_password
        self.confirmPassword = confirm_password
        self.result = result
        self.message = message

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
        self.log.build_start_line(self.caseNo)
        self.begin = self.log.take_shot(self.driver, self.caseName)
        self.logger.info("Take shot, the picture path is:" + self.begin)

        # open app
        self.logger.info("Open App")

        # login app

    def testChangePassword(self):

        try:
            email = loginCls[0][1]
            password = loginCls[0][2]
            bsnsCommon.login(email, password)
            bsnsCommon.wait_loading()
            if Element("Alert", "update_title").is_exist():
                Element("Alert", "cancel").click()
            else:
                pass

            bsnsCommon.go_to_setting()

            Element("account_setting", "change_password").click()

            self.input_password(self.oldPassword, self.newPassword, self.confirmPassword)

            self.check_result()

        except Exception as ex:
            self.logger.error(str(ex))

    def tearDown(self):
        self.End = self.log.take_shot(self.driver, self.caseName)

        self.logger.info("Take shot, the picture path is:" + self.End)

        bsnsCommon.return_index()

        self.log.build_end_line(self.caseNo)

    def input_password(self, old_password, new_password, confirm_password):
        # input old password
        Element("change_password", "old_pass").send_key(old_password)
        # input new password
        Element("change_password", "new_pass").send_key(new_password)
        # input confirm password
        Element("change_password", "confirm_pass").send_key(confirm_password)
        # click submit button
        Element("change_password", "change_password").click()

    def check_result(self):
        sleep(1)

        if Element("Alert", "layout").does_exist():
            value = Element("Alert", "message").get_attribute("text")

            self.assertEqual(value, self.message)
            sleep(1)
            Element("Alert", "confirm").click()
            sleep(1)

        if self.result == "1":
            Element("account_setting", "change_password").click()
            bsnsCommon.wait_loading()

            self.input_password(self.newPassword, self.oldPassword, self.oldPassword)
            sleep(1)
            Element("Alert", "confirm").click()
