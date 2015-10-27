__author__ = 'tongshan'

import os
import urllib.request
from urllib.error import URLError
from multiprocessing import Process
import testApp01.readConfig as readConfig
readConfigLocal = readConfig.ReadConfig()

class AppiumServer:

    def __init__(self):
        global appiumPath, baseUrl
        appiumPath = readConfigLocal.getConfigValue("appiumPath")
        baseUrl = readConfigLocal.getConfigValue("baseUrl")

    def startServer(self):
        """start the appium server
        :return:
        """
        cmd = self.getCmd()
        t1 = runServer(cmd)
        p = Process(target=t1.start())
        p.start()

    def stopServer(self):
        """stop the appium server
        :return:
        """
        #kill myServer
        os.system('taskkill /f /im node.exe')

    def reStartServer(self):
        """reStart the appium server
        :arg:
        :return:
        """
        self.stopServer()
        self.startServer()

    def isRunnnig(self):
        """Determine whether server is running
        :return:True or False
        """
        response = None
        url = baseUrl+"/status"
        try:
            response = urllib.request.urlopen(url, timeout=5)

            if str(response.getcode()).startswith("2"):
                return True
            else:
                return False
        except URLError:
            return False
        finally:
            if response:
                response.close()

    def getCmd(self):
        """get the cmd of start appium server
        :return:cmd
        """
        rootDirectory = appiumPath[:2]
        startCMD = "node node_modules\\appium\\bin\\appium.js"

        cmd =rootDirectory+"&"+"cd "+appiumPath+"&"+startCMD

        return cmd

import threading


class runServer(threading.Thread):

    def __init__(self, cmd):
        threading.Thread.__init__(self)
        self.cmd = cmd

    def run(self):
        os.system(self.cmd)

if __name__ == "__main__":
    oo = AppiumServer()
    oo.startServer()
