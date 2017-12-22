import unittest
import paramunittest
import testSet.common.Log as Log
from testSet.common.DRIVER import MyDriver
from testSet.common.common import Element
from testSet.bsns import bsnsCommon
from testSet.common import common
from time import sleep

loginGls = bsnsCommon.get_login_cls()
feedbackGls = bsnsCommon.get_feed_back_cls()


@paramunittest.parametrized(*feedbackGls)
class TestFeedback(unittest.TestCase):
    def setParameters(self, case_name, fb_email, fb_content, fb_result, fb_message):
        """
        get parameters of feedback
        :param case_name:
        :param fb_email:
        :param fb_content:
        :param fb_result:
        :param fb_message:
        :return:
        """
        self.case_name = case_name
        self.fb_email = fb_email
        self.fb_content = fb_content
        self.fb_result = fb_result
        self.fb_message = fb_message

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
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_my_logger()

        # start test
        self.log.build_start_line(self.caseNo)
        self.begin = self.log.take_shot(self.driver, self.case_name)
        self.logger.info("Take a shot, the picture path is:" + self.begin)

        # open app
        self.logger.info("Open App")

    def testFeedback(self):
        try:
            email = loginGls[0][1]
            password = loginGls[0][2]
            bsnsCommon.login(email, password)
            bsnsCommon.wait_loading()

            if Element("Alert", "update_title").is_exist():
                Element("Alert", "cancel").click()
            else:
                pass

            # go to account setting
            bsnsCommon.go_to_setting()
            self.feedback(self.fb_email, self.fb_content)
            self.check_result()

        except Exception as ex:
            self.logger.error(str(ex))

    def tearDown(self):
        self.end = self.log.take_shot(self.driver, self.case_name)
        self.logger.info("Take a shot, the picture path is:" + self.end)
        self.log.build_end_line(self.caseNo)

    def feedback(self, email, content):
        # go to feedback
        Element("account_setting", "feedback").click()
        sleep(1)
        # input feedback email
        Element("feedback", "feedback_email").send_key(email)
        # input feedback content
        Element("feedback", "feedback_message").send_key(content)

        if not Element("feedback", "submit").is_exist():
            common.back()
        else:
            pass
        Element("feedback", "submit").click()
        while not Element("BottomNavigation", "BottomNavigation").is_exist():
            common.back()
        else:
            pass

    def check_result(self):
        # feedback successfully
        if self.fb_result == '1':
            value = Element("Alert", "feed_successfully").get_attribute("text")
            self.logger.info("Feedback successfully message is :" + value)
            self.assertEqual(value, self.fb_message)

        # feedback fail
        if self.fb_result == '0':
            value = Element("Alert", "message").get_attribute("text")
            self.assertEqual(value, self.fb_message)
            sleep(1)
            Element("Alert", "confirm").click()
        else:
            pass


