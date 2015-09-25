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
        global resultPath, step, checkPointNo
        resultPath = readConfig.logDir+"//result"
        step = 0
        checkPointNo = 0

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
        self.writeLog(startLine)

# =================================================================
# Function Name   : writeLog
# Function        : write output.log
# Input Parameters: logInfo
# Return Value    : -
# =================================================================
    def writeLog(self,logInfo):

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
# Function Name   : outputLogFile
# Function        : output info write to output.log
# Input Parameters: logInfo
# Return Value    : -
# =================================================================
    def outputLogFile(self, logInfo):

        step += 1
        print("Step:"+step+" "+logInfo)

        self.writeLog("Step:"+step+" "+logInfo)


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
        self.writeLog(endLine)

# =================================================================
# Function Name   : resultOK
# Function        : write the result(OK)
# Input Parameters:caseNo
# Return Value    :
# =================================================================
    def resultOK(self, caseNo):
        self.writeLog("TEST: "+caseNo+" :OK")

# =================================================================
# Function Name   : resultNG
# Function        : write the result(NG)
# Input Parameters:caseNo
# Return Value    :
# =================================================================
    def resultNG(self, caseNo):
        self.writeLog("TEST: "+caseNo+" :NG")

# =================================================================
# Function Name   : checkPointOK
# Function        : write the checkPoint(OK)
# Input Parameters:checkPoint
# Return Value    :
# =================================================================
    def checkPointOK(self, checkPoint):
        checkPointNo += 1

        self.writeLog("[CheckPoint "+checkPointNo+"] "+checkPoint+": OK")


# =================================================================
# Function Name   : checkPointNG
# Function        : write the checkPoint(NG)
# Input Parameters:checkPoint
# Return Value    :
# =================================================================
    def checkPointNG(self, checkPoint):
        checkPointNo += 1

        self.writeLog("[CheckPoint "+checkPointNo+"] "+checkPoint+": NG")

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
        #driver.save_screenshot(screenshotDir + "/" + screenshotName)