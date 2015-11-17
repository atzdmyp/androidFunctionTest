
import logging
import testApp01.readConfig as readConfig
import time
import os
from time import sleep
import threading


class Log:

    def __init__(self):

        global logger, resultPath, logPath
        resultPath = os.path.join(readConfig.prjDir, "result")
        logPath = os.path.join(resultPath, (time.strftime('%Y%m%d%H%M%S', time.localtime())))
        if os.path.exists(logPath) is False:
            os.makedirs(logPath)
        self.checkNo = 0
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        # create handler,write log
        fh = logging.FileHandler(os.path.join(logPath, "outPut.log"))
        # Define the output format of formatter handler
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)

        self.logger.addHandler(fh)

    def get_result_path(self):
        """get the reultPath
        :return:report_path
        """
        report_path = os.path.join(logPath, "report.html")
        return report_path

    def get_my_logger(self):
        """get the logger
        :return:logger
        """
        return self.logger

    def build_start_line(self, case_no):
        """build the start log
        :param case_no:
        :return:
        """

        start_line = "----  " + case_no + "   START     ----"
        self.logger.info(start_line)

    def build_end_line(self, case_no):
        """build the end log
        :param case_no:
        :return:
        """
        end_line = "----  " + case_no + "   END     ----"
        self.logger.info(end_line)
        self.checkNo = 0

    def write_result(self, result):
        """write the case result(OK or NG)
        :param result:
        :return:
        """
        report_path = os.path.join(logPath, "report.txt")
        flogging = open(report_path, "a")
        try:
            flogging.write(result+"\n")
        finally:
            flogging.close()
        pass

    def result_OK(self, case_no):
        self.write_result(case_no+": OK")

    def result_NG(self, case_no):
        self.write_result(case_no+": NG")

    def check_point_OK(self, driver, case_name, check_point):
        """write the case's checkPoint(OK)
        :param driver:
        :param case_name:
        :param check_point:
        :return:
        """
        self.checkNo += 1

        self.logger.info("[CheckPoint_"+str(self.checkNo)+"]: "+check_point+": OK")

        # take shot
        self.screenshot_OK(driver, case_name)

    def checkPoint_NG(self, driver, case_name, check_point):
        """write the case's checkPoint(NG)
        :param driver:
        :param case_name:
        :param check_point:
        :return:
        """
        self.checkNo += 1

        self.logger.info("[CheckPoint_"+str(self.checkNo)+"]: "+check_point+": NG")

        # take shot
        self.screenshot_NG(driver, case_name)

    def screenshot_OK(self, driver, case_name):
        """screen shot
        :param driver:
        :param case_name:
        :return:
        """
        screenshot_path = os.path.join(logPath, case_name)
        screenshot_name = "CheckPoint_"+str(self.checkNo)+"_OK.png"

        # wait for animations to complete before taking screenshot
        sleep(1)
        driver.get_screenshot_as_file(os.path.join(screenshot_path, screenshot_name))

    def screenshot_NG(self, driver, case_name):
        """screen shot
        :param driver:
        :param case_name:
        :return:
        """
        screenshot_path = os.path.join(logPath, case_name)
        screenshot_name = "CheckPoint_"+str(self.checkNo)+"_NG.png"

        # wait for animations to complete before taking screenshot
        sleep(1)
        driver.get_screenshot_as_file(os.path.join(screenshot_path, screenshot_name))

    def screenshot_ERROR(self, driver, case_name):
        """screen shot
        :param driver:
        :param case_name:
        :return:
        """
        screenshot_path = os.path.join(logPath, case_name)
        screenshot_name = "ERROR.png"

        # wait for animations to complete before taking screenshot
        sleep(1)
        driver.get_screenshot_as_file(os.path.join(screenshot_path, screenshot_name))


class MyLog:
    """
    This class is used to get log
    """

    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_log():

        if MyLog.log is None:

            MyLog.mutex.acquire()
            MyLog.log = Log()
            MyLog.mutex.release()

        return MyLog.log

if __name__ == "__main__":
    logTest = MyLog.get_log()
    logger = logTest.getMyLogger()
    logger.debug("1111")
    logTest.buildStartLine("test")






