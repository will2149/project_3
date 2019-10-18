import time
from selenium import webdriver


class BrowserDriver(object):

    def browserdriver(self) -> object:
        self.driver = webdriver.Chrome(executable_path='/Users/Guest/PycharmProjects/first_proj/driver1/chromedriver')
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()


        return self.driver





def find_element_by_xpath(param):
    return None


def find_element_by_id(param):
    return None


def find_elements_by_xpath(param):
    return None


def find_elements_by_id():
    return None