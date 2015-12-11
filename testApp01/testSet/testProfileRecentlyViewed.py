import unittest

from time import sleep
import testSet.common.common as myCommon
import testSet.common.Log as Log
from testSet.common.common import Element
from testSet.bsns import bsnsCommon
from testSet.common.DRIVER import MyDriver


class TestRecentlyViewed(unittest.TestCase):

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

    def testRecentlyViewed(self):
        try:
            self.logger.info("Enter the goods details")

            while not Element("Shop", "goods").is_exist():
                myCommon.my_swipe_to_up()
            else:
                myCommon.my_swipe_to_up()
                Element("Shop", "goods").clicks(0)

            bsnsCommon.wait_loading()

            self.logger.info("Get the goods's name")

            self.goods_name = Element("title", "title").get_attribute("text")

            # return the index
            bsnsCommon.return_index()

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
            self.logger.info("Enter the recently viewed")

            element_list = Element("profile", "profile_tv").get_element_list()

            for i in range(len(element_list)):

                element_name = element_list[i]

                if element_name == "Recently Viewed":

                    element_list[i].click()

                    break

            bsnsCommon.wait_loading()

            self.check_result(self.goods_name)

        except Exception as ex:
            self.logger.error(str(ex))

    def tearDown(self):
        self.End = self.log.take_shot(self.driver, self.caseNo)

        self.logger.info("Take shot, the picture path is " + self.End)

        # return the index
        bsnsCommon.return_index()

        # test Start
        self.log.build_end_line(self.caseNo)

    def check_result(self, result):

        if Element("recently_viewed", "goods_name").is_exist():

            value = Element("recently_viewed", "goods_name").gets(0).get_attribute("text")

            if value == result:

                Element("title", "rightButton").click()

                if Element("recently_viewed", "no_data").is_exist():

                    self.assertEqual("1", "1")
                else:
                    self.assertEqual("1", "0")

            else:
                self.assertEqual("1", "0")




