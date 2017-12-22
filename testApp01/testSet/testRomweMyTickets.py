import unittest
import paramunittest
import testSet.common.Log as Log
from testSet.common.DRIVER import MyDriver
from testSet.common.common import Element
from testSet.bsns import bsnsCommon
from time import sleep

loginGls = bsnsCommon.get_login_cls()
ticketsGls = bsnsCommon.get_tickets_cls()


@paramunittest.parametrized(*ticketsGls)
class TestMyTickets(unittest.TestCase):

    def setParameters(self, case_name, first_name, last_name, email, language, content, result, message):
        """
        get parameters for my_tickets
        :param case_name:
        :param first_name:
        :param last_name:
        :param email:
        :param language:
        :param content:
        :param result:
        :param message:
        :return:
        """
        self.case_name = case_name
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.language = language
        self.content = content
        self.result = result
        self.message = message

    def Description(self):
        return self.case_name

    def setUp(self):
        self.Begin = "../../result/image/1.png"
        self.CheckPoint = "../../result/image/1.png"
        self.End = "../../result/image/1.png"

        # get driver
        self.driver = MyDriver.get_driver()
        self.caseNo = self.case_name

        # get log
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_my_logger()

        # start test
        self.log.build_start_line(self.caseNo)
        self.begin = self.log.take_shot(self.driver, self.case_name)
        self.logger.info("Take a shot, the picture path is:" + self.begin)

        # open app
        self.logger.info("Open App")

    def testMyTickets(self):
        try:
            login_email = loginGls[0][1]
            login_pass = loginGls[0][2]
            bsnsCommon.login(login_email, login_pass)
            bsnsCommon.wait_loading()
            bsnsCommon.cancel_update()

            bsnsCommon.go_to_me()
            sleep(1)
            Element("my_tickets", "my_tickets").click()
            bsnsCommon.wait_loading()

            Element("my_tickets", "add_tickets").click()
            bsnsCommon.wait_loading()

            Element("my_tickets", "tickets_topic").click()
            bsnsCommon.wait_loading()

            self.inputTickets(self.first_name, self.last_name, self.email, self.language, self.content)
            self.checkResult()

        except Exception as ex:
            self.logger.error(str(ex))

    def tearDown(self):
        self.end = self.log.take_shot(self.driver, self.case_name)
        self.logger.info("Take a shot, the picture path is:" + self.end)
        self.log.build_start_end_line(self.caseNo)

    def inputTickets(self, firstName, lastName, email, language, content):
        # input first name
        Element("my_tickets", "first_name").send_key(firstName)
        # input last name
        Element("my_tickets", "last_name").send_key(lastName)
        # select language
        Element("my_tickets", "language").send_key(language)
        # input email
        Element("my_tickets", "email").send_key(email)
        # input question
        Element("my_tickets", "question").send_key(content)
        # click submit
        Element("my_tickets", "submit").click()

    def checkResult(self):
        # successfully
        if self.result == 1:
            value = Element("Alert", "message").get_attribute("text")
            self.assertEqual(value, self.message)

        # fail
        if self.result == 0:
            value = Element("Alert", "message").get_attribute("text")
            self.assertEqual(value, self.message)
