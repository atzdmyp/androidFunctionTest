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

    def __init__(self):
        global resultPath
        resultPath = readConfig.logDir+"//result"

# =================================================================
# Function Name   : buildStartLine
# Function        : create start line
# Input Parameters: caseNo
# Return Value    :
# =================================================================
    def buildStartLine(self,caseNo):
        timePart = time.strftime('%Y-%m-%d %H:%M', time.localtime())
        startLine = "----  " + caseNo + "   " + "START" + "   " + timePart +\
        "  ----"
        self.outputLogFile(startLine)

# =================================================================
# Function Name   : outputLogFile
# Function        : output info write to output.log
# Input Parameters: logInfo
# Return Value    : -
# =================================================================
    def outputLogFile(self, logInfo):

        print(logInfo)

        if os.path.exists(resultPath) == False:
            os.makedirs(resultPath)
        flogging = open(resultPath + "//log.log", "a")
        # s_utf8 = logInfo.encode('UTF-8')
        try:
            flogging.write(logInfo+"\n")
        finally:
            flogging.close()
        pass


# =================================================================
# Function Name   : buildEndLine
# Function        : create end line
# Input Parameters: caseNo
# Return Value    : endLine
# =================================================================
    def buildEndLine(self, caseNo):
        timePart = time.strftime('%Y-%m-%d %H:%M', time.localtime())
        endLine = "----  " + caseNo + "    " + "END" + "    " + timePart +\
        "  ----"+ "\n"
        self.outputLogFile(endLine)

# =================================================================
# Function Name   : resultOK
# Function        : write the result(OK)
# Input Parameters:caseNo
# Return Value    :
# =================================================================
    def resultOK(self, caseNo):
        self.outputLogFile(caseNo+" :OK")

# =================================================================
# Function Name   : resultNG
# Function        : write the result(NG)
# Input Parameters:caseNo
# Return Value    :
# =================================================================
    def resultNG(self, caseNo):
        self.outputLogFile(caseNo+" :NG")

# =================================================================
# Function Name   : checkPointOK
# Function        : write the checkPoint(OK)
# Input Parameters:checkPoint
# Return Value    :
# =================================================================
    def checkPointOK(self, checkPoint):
        pass

# =================================================================
# Function Name   : checkPointNG
# Function        : write the checkPoint(NG)
# Input Parameters:checkPoint
# Return Value    :
# =================================================================
    def checkPointNG(self, checkPoint):
        pass

# =================================================================
# Function Name   : checkPointNG
# Function        : write the checkPoint(NG)
# Input Parameters:checkPoint
# Return Value    :
# =================================================================
    def screenshot(self, driver,checkPoint):
        global screenShotCount
        screenshotName = str(screenShotCount) + "_" + checkPoint + ".png"

        # wait for animations to complete before taking screenshot
        sleep(1)
        # driver.save_screenshot(screenshotDir + "/" + screenshotName)