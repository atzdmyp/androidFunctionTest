__author__ = 'Administrator'

import os
import threading
import readConfig
readConfigLocal = readConfig.ReadConfig()
mylock = threading.RLock()
num = 0

class myServer(threading.Thread):

    def __init__(self, name):
        global appiumPath
        threading.Thread.__init__(self)
        self.t_name = name
        self.appiumPath = readConfigLocal.getConfigValue("appiumPath")

    def run(self):
        rootDirectory = self.appiumPath[:2]
        startCMD = "node node_modules\\appium\\bin\\appium.js"

        #cd root directory ;cd appiuu path; start server
        os.system(rootDirectory+"&"+"cd "+self.appiumPath+"&"+startCMD)

        print("---------------------------------------------------")

class myTest(threading.Thread):

    def __init__(self, name):
        global appiumPath
        threading.Thread.__init__(self)
        self.t_name = name

    def run(self):
        print(self.t_name)


if __name__ == '__main__':

    thread1 = myServer("A")
    thread2 = myTest("B")

    thread1.start()

    thread2.start()