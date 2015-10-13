# ========================================================
# Summary        :Log
# Author         :tong shan
# Create Date    :2015-09-16
# Amend History  :
# Amended by     :
# ========================================================

import readConfig as readConfig
import os
import time
from time import sleep
import threading

class Log:

    def __init__(self):

        global resultPath, logPah, checkNo
        self.resultPath = readConfig.logDir+"\\result\\"
        self.logPath = self.resultPath+(time.strftime('%Y%m%d%H%M%S', time.localtime()))+"\\"
        self.checkNo = 0

# =================================================================
# Function Name   : buildStartLine
# Function        : create start line
# Input Parameters: caseNo
# Return Value    :
# =================================================================
    def buildStartLine(self, caseNo):

        startLine = "----  " + caseNo + "   " + "START" + "   " +\
        "  ----"
        self.writeLog(startLine)

# =================================================================
# Function Name   : writeLog
# Function        : write output.log
# Input Parameters: logInfo
# Return Value    : -
# =================================================================
    def writeLog(self,logInfo):

        if os.path.exists(self.logPath) == False:
            os.makedirs(self.logPath)
        flogging = open(self.logPath + "outPut.log", "a")
        try:
            flogging.write(logInfo+"\n")
        finally:
            flogging.close()
        pass

# =================================================================
# Function Name   : writeResult
# Function        : write result.txt
# Input Parameters: result
# Return Value    : -
# =================================================================
    def writeResult(self,result):

        if os.path.exists(self.logPath) == False:
            os.makedirs(self.logPath)
        flogging = open(self.logPath + "result.txt", "a")
        try:
            flogging.write(result+"\n")
        finally:
            flogging.close()
        pass


# =================================================================
# Function Name   : outputLogFile
# Function        : output info write to output.log
# Input Parameters: logInfo
# Return Value    : -
# =================================================================
    def outputLogFile(self, logInfo):

        timePart = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.writeLog("["+timePart+"}"+": "+logInfo)

# =================================================================
# Function Name   : outputError
# Function        : output Error to output.log
# Input Parameters: logInfo
# Return Value    : -
# =================================================================
    def outputError(self, driver,errorInfo):

        self.screenshotError(driver)
        self.writeLog("[Error]"+errorInfo)

# =================================================================
# Function Name   : buildEndLine
# Function        : create end line
# Input Parameters: caseNo
# Return Value    : endLine
# =================================================================
    def buildEndLine(self, caseNo):

        endLine = "----  " + caseNo + "    " + "END" + "    " +\
        "  ----"+ "\n"
        self.writeLog(endLine)
        self.checkNo = 0

# =================================================================
# Function Name   : resultOK
# Function        : write the result(OK)
# Input Parameters:caseNo
# Return Value    :
# =================================================================
    def resultOK(self, caseNo):
        self.writeResult("TEST: "+caseNo+" :OK")

# =================================================================
# Function Name   : resultNG
# Function        : write the result(NG)
# Input Parameters:caseNo
# Return Value    :
# =================================================================
    def resultNG(self, caseNo):
        self.writeResult("TEST: "+caseNo+" :NG")

# =================================================================
# Function Name   : checkPointOK
# Function        : write the checkPoint(OK)
# Input Parameters:checkPoint
# Return Value    :
# =================================================================
    def checkPointOK(self, driver,caseName, checkPoint):

        self.checkNo += 1

        self.writeLog("[CheckPoint_"+str(self.checkNo)+"]: "+checkPoint+": OK")

        # take shot
        self.screenshotOK(driver, caseName)


# =================================================================
# Function Name   : checkPointNG
# Function        : write the checkPoint(NG)
# Input Parameters:checkPoint
# Return Value    :
# =================================================================
    def checkPointNG(self, driver, caseName,checkPoint):

        self.checkNo += 1

        self.writeLog("[CheckPoint_"+str(self.checkNo)+"]: "+checkPoint+": NG")

        #take shot
        self.screenshotNG(driver, caseName)

# =================================================================
# Function Name   : screenshotOK
# Function        : take shot
# Input Parameters:driver,checkPoint
# Return Value    : -
# =================================================================
    def screenshotOK(self, driver, caseName):

        screenshotPath = self.logPath+caseName+"\\"
        screenshotName = "CheckPoint_"+str(self.checkNo)+"_OK.png"

        # wait for animations to complete before taking screenshot
        sleep(1)
        driver.get_screenshot_as_file(screenshotPath+screenshotName)

# =================================================================
# Function Name   : screenshotNG
# Function        : take shot
# Input Parameters:driver,checkPoint
# Return Value    : -
# =================================================================
    def screenshotNG(self, driver, caseName):

        screenshotPath = self.logPath+caseName+"\\"
        screenshotName = "CheckPoint_"+str(self.checkNo)+"_NG.png"

        # wait for animations to complete before taking screenshot
        sleep(1)
        driver.get_screenshot_as_file(screenshotPath+screenshotName)

# =================================================================
# Function Name   : screenshotError
# Function        : take shot
# Input Parameters:driver
# Return Value    : -
# =================================================================
    def screenshotError(self, driver):

        screenshotName = "Error.png"

        # wait for animations to complete before taking screenshot
        sleep(1)
        driver.get_screenshot_as_file(self.logPath+screenshotName)


class myLog:

    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def getLog():

        if myLog.log == None:

            myLog.mutex.acquire()
            myLog.log = Log()
            myLog.mutex.release()

        return myLog.log