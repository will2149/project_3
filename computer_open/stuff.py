import time
import unittest

from selenium.webdriver.support.select import Select

from computer_open.stuff_3 import BrowserDriver
from computer_open.stuff_2 import Browsing


class PrintData(unittest.TestCase, Browsing, BrowserDriver):
    pass

    unittest.skip('test')
    def test_01_hypaship(self):
        driver = self.homepage()

        
        self.postal(driver)
        '''
        self.carrier(driver)

        self.three_pl(driver)

        self.ecommerce(driver)
        '''

    def test_02_test(self):

        for x in range(6):
            if x != 1 and x != 0:
                print(x)
            else:
                print(' ')



if __name__ == "__main__":
    unittest.main()
