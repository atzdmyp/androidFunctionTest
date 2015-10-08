# ========================================================
# Summary        :myPhone
# Author         :tong shan
# Create Date    :2015-10-08
# Amend History  :
# Amended by     :
# ========================================================

import os
import readConfig
readConfigLocal = readConfig.ReadConfig()

class myPhone:


    def __init__(self):
        global viewPhone,vievAndroid, openPhone, installSoftware, uninstallSoftware
        self.viewPhone = readConfigLocal.getAdbValue("viewPhone")
        self.viewAndroid = readConfigLocal.getAdbValue("viewAndroid")
        self.openCmd = readConfigLocal.getAdbValue("openPhone")
        self.installSoftware = readConfigLocal.getAdbValue("installSoftware")
        self.uninstallSoftware = readConfigLocal.getAdbValue("uninstallSoftware")

# =================================================================
# Function Name   : getDeviceName
# Function        : get the devices name
# Input Parameters: -
# Return Value    : devicesName
# =================================================================
    def getDeviceName(self):

        deviceList = []

        returnValue = os.popen(self.viewPhone)
        for value in returnValue.readlines():
            sValue = str(value)
            if sValue.rfind('device'):
                if not sValue.startswith("List"):
                    deviceList.append(sValue[:sValue.find('device')].strip())
        if len(deviceList) != 0:
            return deviceList[0]
        else:
            return None

# =================================================================
# Function Name   : getAndroidVersion
# Function        : get the Android Version
# Input Parameters: -
# Return Value    : devicesName
# =================================================================
    def getAndroidVersion(self):
        returnValue = str(os.popen(self.viewAndroid).read())

        if returnValue != None:
            pop = returnValue.rfind(str('='))
            return returnValue[pop+1:]
        else:
            return None



# =================================================================
# Function Name   : openPhone
# Function        : open and unlock the phone
# Input Parameters: driver
# Return Value    : -
# =================================================================
    def openPhone(self):
        value = os.system(self.openCmd)

# =================================================================
# Function Name   : install
# Function        : install software in the phone
# Input Parameters: driver
# Return Value    : -
# =================================================================
    def install(self):
        pass

# =================================================================
# Function Name   : uninstall
# Function        : uninstall software in the phone
# Input Parameters: driver
# Return Value    : -
# =================================================================
    def uninstall(self):
        pass


if __name__ == '__main__':

    obj = myPhone()

    #obj.openPhone()
    obj.getDeviceName()


