import unittest
from time import sleep
import testSet.common.Log as Log
import testSet.common.common as myCommon
from testSet.common.common import Element
from testSet.bsns import bsnsCommon
from testSet.common.DRIVER import MyDriver

loginCls = bsnsCommon.get_login_cls()


class TestSave(unittest.TestCase):

    def setUp(self):

        self.Begin = "../../result/image/1.png"
        self.CheckPoint = "../../result/image/1.png"
        self.End = "../../result/image/1.png"

        # get Driver
        self.driver = MyDriver.get_driver()
        self.case_name = "Test save the goods"

        # get Log
        self.log = Log.MyLog().get_log()
        self.logger = self.log.get_my_logger()

        # test Start
        self.log.build_start_line(self.case_name)

        self.Begin = self.log.take_shot(self.driver, self.case_name)

        self.logger.info("Take shot, the picture path is " + self.Begin)

        # open app
        bsnsCommon.open_app()

        self.logger.info("Open app")

    def testSave(self):

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

            bsnsCommon.return_index()

            self.logger.info("Enter the goods details")

            while not Element("Shop", "goods").is_exist():
                myCommon.my_swipe_to_up()
            else:
                myCommon.my_swipe_to_up()
                Element("Shop", "goods").clicks(0)

            bsnsCommon.wait_loading()

            self.logger.info("Get the goods's name")

            self.goods_name = Element("title", "title").get_attribute("text")

            Element("Good_details", "save").click()

            self.check_result(self.goods_name)

        except Element as ex:

            self.logger.error(str(ex))

    def tearDown(self):
        self.End = self.log.take_shot(self.driver, self.case_name)

        self.logger.info("Take shot, the picture path is " + self.End)

        # return the index
        bsnsCommon.return_index()

        # test Start
        self.log.build_end_line(self.case_name)

    def check_result(self, goods_name):

        value = Element("Good_details", "save").get_attribute("text")

        while value != "saved":
            sleep(1)
        else:
            bsnsCommon.return_index()

        self.logger.info("Enter the profile")

        # find the bottom Navigation bar
        while not Element("BottomNavigation", "BottomNavigation").is_exist():
            sleep(1)
        else:
            # enter the profile
            Element("BottomNavigation", "profile").click()

        bsnsCommon.wait_loading()

        self.logger.info("Enter the my wish list")

        Element("profile", "profile_tv").clicks(2)

        bsnsCommon.wait_loading()

        goods_list = []

        self.logger.info("Determine whether there is a goods")

        while Element("wish_list", "goods_name").is_exist():
            self.logger.info("Get the goods name")

            element_list = Element("Shopping_cart", "goods_name").get_element_list()

            if element_list is not None:

                self.logger.info("Get the last goods name")
                last_goods_name = element_list[-1].get_attribute("text")

                for i in range(len(element_list)):

                    value = element_list[i].get_attribute("text")

                    if value == goods_name:

                        self.assertEqual("1", "1")

                        Element("Shopping_cart", "delete_goods").clicks(i)

                        Element("Alert", "confirm").click()

                        bsnsCommon.wait_loading()

                        return

            if last_goods_name not in goods_list:

                self.logger.info("Goods is not end")

                self.logger.info("Swipe up, if not end")

                myCommon.my_swipe_to_up()

                goods_list.append(last_goods_name)
            else:
                self.logger.info("Goods is end")
                self.assertEqual("1", "0")
                return


