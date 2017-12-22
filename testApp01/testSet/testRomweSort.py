import unittest
import testSet.common.Log as Log
from testSet.common.DRIVER import MyDriver
from testSet.common.common import Element
from testSet.bsns import bsnsCommon
from testSet.common import common

loginGls = bsnsCommon.get_login_cls()


class TestGoodsSort(unittest.TestCase):

    def setUp(self):
        self.Begin = "../../result/image/1.png"
        self.CheckPoint = "../../result/image/1.png"
        self.End = "../../result/image/1.png"

        # get driver
        self.driver = MyDriver.get_driver()
        self.case_name = "testSort"

        # get log
        self.log = Log.MyLog.get_log()
        self.logger = self.log.get_my_logger()
        self.logger.info("Get log.")

        # start test
        self.log.build_start_line(self.case_name)
        self.begin = self.log.take_shot(self.driver, self.case_name)
        self.logger.info("Take a shot, the picture path is:" + self.begin)

        # open app
        self.logger.info("Open App")

    def testSort(self):
        try:
            email = loginGls[0][1]
            password = loginGls[0][2]
            bsnsCommon.login(email, password)
            bsnsCommon.wait_loading()
            self.logger.info("login.")
            if Element("Alert", "update_title").is_exist():
                Element("Alert", "cancel").click()
            else:
                pass

            Element("daily_new", "daily_new").click()
            bsnsCommon.wait_loading()
            self.logger.info("daily new.")

            for i in range(1, 3):
                while not bsnsCommon.wait_loading():
                    common.my_swipe_to_up()
                else:
                    break
            else:
                break

            goods_name = Element("wish_list", "wish_goods_name").get_element_list()

            if len(goods_name) != 0:
                for i in len(goods_name):
                    self.names = goods_name[i].get_attribute("text")

                else:
                    break
                self.logger.info("names are:" + self.names)
            else:
                self.logger.info("No find elements.")

            # self.sort_left = Element("category", "sort_left").get_element_list()
            # self.sort_right = Element("category", "sort_right").get_element_list()
            # left_category = []
            # right_category = []
            # if len(self.sort_left) != 0:
            #     for i in len(self.sort_left):
            #         left_category[i] = self.sort_left[i].get_attribute("text")
            #         self.logger.info("Left category are:" + left_category[i] + "  ")
            # else:
            #     self.logger.info("Don't get the left category!")
            #     return False
            # if len(self.sort_right) != 0:
            #     for j in len(self.sort_right):
            #         right_category[j] = self.sort_left[j].get_attribute("text")
            #         self.logger.info("Right category are:" + right_category[j] + "  ")
            # else:
            #     self.logger.info("Don't get the right category!")
            #     return False
            # category_name = []
            # for n in range(1, 60):
            #     if n % 2 != 0:
            #         category_name[n] = left_category[(n+1)/2]
            #     else:
            #         category_name[n] = right_category[n/2]
            #     pass

        except Exception as ex:
            self.logger.error(str(ex))

    def tearDown(self):
        self.end = self.log.take_shot(self.driver, self.case_name)
        self.logger.info("Take a shot, the picture path is:" + self.end)
        self.log.build_end_line(self.case_name)

    def check_result(self):
        pass
