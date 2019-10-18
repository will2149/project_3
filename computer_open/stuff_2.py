import time
from lib2to3.pgen2 import driver

from selenium.webdriver.support.select import Select

from computer_open.stuff_3 import BrowserDriver

'''
class Select(object):
    pass
'''


class Browsing(BrowserDriver):
    pass

    def homepage(self):
        driver = self.browserdriver()
        driver.get('https://www.hypaship.com/')
        return driver

    def postal(self, driver):
        for x in range(6):
            if x != 1 and x != 0:
                print(x)
                driver.find_element_by_xpath('(//a[@class="nav-link"])['+str(x)+']').click()
                title = driver.find_elements_by_xpath('//div[@class="row justify-content-center"]/div/div/div[2]/h5')
                data = driver.find_elements_by_xpath('//div[@class="row justify-content-center"]/div/div/div[2]/p')
                for y in range(len(title)):
                    file1 = open("/Users/Guest/PycharmProjects/long_hypaship_project/computer_open/data.txt", "a")
                    file1.write(title[y].text + ': \n')
                    file1.write('\t' + data[y].text + '\n' + '\n')
                    file1.close()
                time.sleep(5)


'''
    def postal(self, driver):

        driver.find_element_by_xpath('(//a[@class="nav-link"])[2]').click()
        time.sleep(1)
        title = driver.find_elements_by_xpath('//div[@class="row justify-content-center"]/div/div/div[2]/h5')
        data = driver.find_elements_by_xpath('//div[@class="row justify-content-center"]/div/div/div[2]/p')
        for x in range(len(title)):
            file1 = open("/Users/Guest/PycharmProjects/long_hypaship_project/computer_open/data.txt", "a")
            file1.write(title[x].text + ': \n')
            file1.write('\t' + data[x].text + '\n' + '\n')
            file1.close()
        time.sleep(5)

    def carrier(self, driver):
        time.sleep(5)
        driver.find_element_by_xpath('(//a[@class="nav-link"])[3]').click()
        time.sleep(1)
        title = driver.find_elements_by_xpath('//div[@class="row justify-content-center"]/div/div/div[2]/h5')
        data = driver.find_elements_by_xpath('//div[@class="row justify-content-center"]/div/div/div[2]/p')
        for x in range(len(title)):
            file1 = open("/Users/Guest/PycharmProjects/long_hypaship_project/computer_open/data.txt", "a")
            file1.write(title[x].text + ': \n')
            file1.write('\t' + data[x].text + '\n' + '\n')
            file1.close()
        time.sleep(10)




    def three_pl(self, driver):
        driver.find_element_by_xpath('(//a[@class="nav-link"])[4]').click()
        time.sleep(1)
        title = driver.find_elements_by_xpath('//div[@class="row justify-content-center"]/div/div/div[2]/h5')
        data = driver.find_elements_by_xpath('//div[@class="row justify-content-center"]/div/div/div[2]/p')
        for x in range(len(title)):
            file1 = open("/Users/Guest/PycharmProjects/long_hypaship_project/computer_open/data.txt", "a")
            file1.write(title[x].text + ': \n')
            file1.write('\t' + data[x].text + '\n' + '\n')
            file1.close()
        time.sleep(10)



    def ecommerce(self, driver):
        time.sleep(10)
        driver.find_element_by_xpath('(//a[@class="nav-link"])[5]').click()
        time.sleep(1)
        title = driver.find_elements_by_xpath('//div[@class="row justify-content-center"]/div/div/div[2]/h5')
        data = driver.find_elements_by_xpath('//div[@class="row justify-content-center"]/div/div/div[2]/p')
        for x in range(len(title)):
            file1 = open("/Users/Guest/PycharmProjects/long_hypaship_project/computer_open/data.txt", "a")
            file1.write(title[x].text + ': \t')
            file1.write('\t' + data[x].text + '\n' + '\n')
            file1.close()
        time.sleep(10)
'''
