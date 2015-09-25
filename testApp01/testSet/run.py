
import testSet.common.common as common
import readConfig as readConfig
import unittest
import testSet.test01 as test01
from selenium import webdriver

class run(unittest.TestCase):

    def __init__(self):
        global cases,casesPath
        cases =common.caseList

    def test(self):
        pass

def suite():
    suite01 = test01.suite()
    suite03 = test01.suite()
    SUITE = unittest.TestSuite([suite01, suite03])
    return SUITE

if __name__ == '__main__':
   runner = unittest.TextTestRunner()
   runner.run(suite())
