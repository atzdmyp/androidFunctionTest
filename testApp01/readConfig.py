import sys,os
import configparser
import codecs
global configfile_path

logDir = os.path.abspath('..')
# cwd = os.path.realpath(sys.argv[0])
# cwd = os.path.abspath(cwd)
# if os.path.isfile(cwd):
#     logDir = os.path.dirname(os.path.dirname(os.path.dirname(cwd)))
# else:
#     logDir = os.path.dirname(os.path.dirname(cwd))
configfile_path = logDir +"\\config.ini"


class ReadConfig:
    def __init__(self):

        fd = open(configfile_path)
        data = fd.read()
        #remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configfile_path,"w")
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configfile_path)

    def getConfigValue(self, name):
        value = self.cf.get("config", name)
        return value