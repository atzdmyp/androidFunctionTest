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
# import sys

class Log:

    def __init__(self, caseNo):

        self.caseNo = caseNo
        global resultPath, logPah, step, checkPointNo
        self.resultPath = readConfig.logDir+"\\result\\"
        self.logPath = self.resultPath+(time.strftime('%Y%m%d%H%M', time.localtime()))+"\\"+self.caseNo+"\\"
        self.step = 0
        self.checkPointNo = 0

# =================================================================
# Function Name   : buildStartLine
# Function        : create start line
# Input Parameters: caseNo
# Return Value    :
# =================================================================
    def buildStartLine(self):
        timePart = time.strftime('%Y-%m-%d %H:%M', time.localtime())
        startLine = "----  " + self.caseNo + "   " + "START" + "   " + timePart +\
        "  ----"
        self.writeLog(startLine)

# =================================================================
# Function Name   : writeLog
# Function        : write output.log
# Input Parameters: logInfo
# Return Value    : -
# =================================================================
    def writeLog(self,logInfo):

        print(logInfo)

        if os.path.exists(self.logPath) == False:
            os.makedirs(self.logPath)
        flogging = open(self.logPath + "outPut.log", "a")
        # s_utf8 = logInfo.encode('UTF-8')
        try:
            flogging.write(logInfo+"\n")
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

        self.step += 1

        self.writeLog("Step"+str(self.step)+": "+logInfo)


# =================================================================
# Function Name   : buildEndLine
# Function        : create end line
# Input Parameters: caseNo
# Return Value    : endLine
# =================================================================
    def buildEndLine(self):
        timePart = time.strftime('%Y-%m-%d %H:%M', time.localtime())
        endLine = "----  " + self.caseNo + "    " + "END" + "    " + timePart +\
        "  ----"+ "\n"
        self.writeLog(endLine)

# =================================================================
# Function Name   : resultOK
# Function        : write the result(OK)
# Input Parameters:caseNo
# Return Value    :
# =================================================================
    def resultOK(self):
        self.writeLog("TEST: "+self.caseNo+" :OK")

# =================================================================
# Function Name   : resultNG
# Function        : write the result(NG)
# Input Parameters:caseNo
# Return Value    :
# =================================================================
    def resultNG(self):
        self.writeLog("TEST: "+self.caseNo+" :NG")

# =================================================================
# Function Name   : checkPointOK
# Function        : write the checkPoint(OK)
# Input Parameters:checkPoint
# Return Value    :
# =================================================================
    def checkPointOK(self, driver, checkPoint):
        self.checkPointNo += 1

        self.writeLog("[CheckPoint "+str(self.checkPointNo)+"] "+checkPoint+": OK")

        # take shot
        self.screenshotOK(driver, checkPoint)


# =================================================================
# Function Name   : checkPointNG
# Function        : write the checkPoint(NG)
# Input Parameters:checkPoint
# Return Value    :
# =================================================================
    def checkPointNG(self, driver, checkPoint):
        self.checkPointNo += 1

        self.writeLog("[CheckPoint_"+str(self.checkPointNo)+"] "+checkPoint+": NG")

        #take shot
        self.screenshotNG(driver, checkPoint)

# =================================================================
# Function Name   : screenshotOK
# Function        : take shot
# Input Parameters:driver,checkPoint
# Return Value    : -
# =================================================================
    def screenshotOK(self, driver,checkPoint):


        screenshotName = "[CheckPoint_"+str(self.checkPointNo) +  "_OK.png"

        # wait for animations to complete before taking screenshot
        sleep(1)
        driver.get_screenshot_as_file(self.logPath+screenshotName)

# =================================================================
# Function Name   : screenshotNG
# Function        : take shot
# Input Parameters:driver,checkPoint
# Return Value    : -
# =================================================================
    def screenshotNG(self, driver,checkPoint):

        screenshotName = "[CheckPoint_"+str(self.checkPointNo) + "_NG.png"

        # wait for animations to complete before taking screenshot
        sleep(1)
        driver.get_screenshot_as_file(self.logPath+screenshotName)

# =================================================================
# Function Name   : screenshotException
# Function        : take shot
# Input Parameters:driver,checkPoint
# Return Value    : -
# =================================================================
    def screenshotException(self, driver,checkPoint):

        screenshotName = "[CheckPoint_"+str(self.checkPointNo) + "_NG.png"

        # wait for animations to complete before taking screenshot
        sleep(1)
        driver.get_screenshot_as_file(self.logPath+screenshotName)