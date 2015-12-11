import unittest
import paramunittest

from time import sleep
import testSet.common.Log as Log
import testSet.common.common as myCommon
from testSet.common.common import Element
from testSet.bsns import bsnsCommon
from testSet.common.DRIVER import MyDriver

write_review_cls = bsnsCommon.get_write_review_cls()


@paramunittest.parametrized(*write_review_cls)
class TestReview(unittest.TestCase):

    def setParameters(self, case_name, user_name, star, content, result, message):
        self.case_name = case_name
        self.user_name = user_name
        self.star = star
        self.content = content
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

    def testReview(self):
        try:
            self.logger.info("Enter the goods details")

            while not Element("Shop", "goods").is_exist():
                myCommon.my_swipe_to_up()
            else:
                myCommon.my_swipe_to_up()
                Element("Shop", "goods").clicks(0)

            bsnsCommon.wait_loading()

            self.logger.info("Enter the write review")
            while not Element("Good_details", "write_review").is_exist():
                myCommon.my_swipe_to_up()
            else:
                Element("Good_details", "write_review").click()

            bsnsCommon.wait_loading()

            self.logger.info("Write review")

            self.write_reviews()

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

    def write_reviews(self):

        if self.user_name != "default":
            Element("Review", "user_name").send_key(self.user_name)

        Element("Review", "content").send_key(self.content)

        Element("Review", "submit").click()

    def check_result(self):

        if Element("Alert", "layout").does_exist():

                value = Element("Alert", "message").get_attribute("text")

                self.assertEqual(value, self.message)

                sleep(1)
                Element("Alert", "confirm").click()

