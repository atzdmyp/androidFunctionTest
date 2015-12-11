import unittest
import paramunittest

from time import sleep
import testSet.common.common as myCommon
import testSet.common.Log as Log
from testSet.common.common import Element
from testSet.bsns import bsnsCommon
from testSet.common.DRIVER import MyDriver

feed_back_cls = bsnsCommon.get_feed_back_cls()


@paramunittest.parametrized(*feed_back_cls)
class TestSettingFeedBack(unittest.TestCase):

    def setParameters(self, case_name, email, advice, message):
        self.case_name = case_name
        self.email = email
        self.advice = advice
        self.message = message

    def setUp(self):
        self.Begin = "../../result/image/1.png"
        self.CheckPoint = "../../result/image/1.png"
        self.End = "../../result/image/1.png"

        # get Driver
        self.driver = MyDriver.get_driver()
        self.caseNo = "Test recently viewed"

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

    def testSettingFeedBack(self):
        try:
            self.logger.info("Enter the profile")

            # find the bottom Navigation bar
            while not Element("BottomNavigation", "BottomNavigation").is_exist():
                sleep(1)
            else:
                # enter the profile
                Element("BottomNavigation", "profile").click()

            bsnsCommon.wait_loading()

            myCommon.my_swipe_to_up()

            # enter my address
            self.logger.info("Enter the setting")

            element_list = Element("profile", "profile_tv").get_element_list()

            for i in range(len(element_list)):

                element_name = element_list[i]

                if element_name == "Setting":

                    element_list[i].click()

                    break

            bsnsCommon.wait_loading()

            Element("setting", "feed_back").click()

            bsnsCommon.wait_loading()

            Element("feed_back", "email").send_key(self.email)

            Element("feed_back", "advice").send_key(self.advice)

            Element("title","rightButton").click()

        except Exception as ex:
            self.logger.error(str(ex))

    def tearDown(self):
        self.End = self.log.take_shot(self.driver, self.caseNo)

        self.logger.info("Take shot, the picture path is " + self.End)

        # return the index
        bsnsCommon.return_index()

        # test Start
        self.log.build_end_line(self.caseNo)

    def check_result(self):

        sleep(1)

        if Element("Alert", "layout").does_exist():

            value = Element("Alert", "message").get_attribute("text")

            self.assertEqual(value, self.message)

            sleep(1)
            Element("Alert", "confirm").click()

