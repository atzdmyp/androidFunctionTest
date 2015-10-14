__author__ = 'tongshan'

import os
import readConfig
readConfigLocal = readConfig.ReadConfig()

class init:

    def __init__(self):
        global startServer,closeServer, checkPhone, logDir
        self.startServer = readConfigLocal.getcmdValue("startServer")
        self.closeServer = readConfigLocal.getcmdValue("closeServer")
        self.checkPhone = readConfigLocal.getcmdValue("checkPhone")
        self.prjDir = readConfig.prjDir


    def connectPhone(self):
        """
        check the phone is connect
        """
        value = os.popen(self.checkPhone)

        for data in value.readline():
            sDate = str(data)
            if sDate.find("device"):
                return True
        return False

    def stratServer(self):

        os.system(self.startServer)

    def closeServer(self):

        os.system(self.closeServer)

    def install(self):

        pass

    def getApk(self):
        apks = os.listdir(self.prjDir)

        if len(apks) >0:
            for apk in apks:
                pass

    def GetFileFromThisRootDir(self, dir, ext = None):
        allfiles = []
        needExtFilter = (ext != None)
        for root, dirs, files in os.walk(dir):
            for filespath in files:
                filepath = os.path.join(root, filespath)
                extension = os.path.splitext(filepath)[1][1:]
                if needExtFilter and extension in ext:
                    allfiles.append(filepath)
                elif not needExtFilter:
                        allfiles.append(filepath)
        return allfiles


if __name__ == '__main__':
    ojb = init()
    while not  ojb.connectPhone():
        pass

