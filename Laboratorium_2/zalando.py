from msedge.selenium_tools.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select


class Zalando:
    url = 'https://www.zalando.pl'
    driver = webdriver

    def __init__(self, webdriver):
        self.driver = webdriver

    def open(self):
        self.driver.maximize_window()
        self.driver.get(self.url)

    def ToRegister(self):
        login = self.driver.find_element_by_class_name('z-navicat-header_navToolItemLink')
        action = ActionChains(self.driver)
        action.move_to_element(login).perform()
        linkToRegister = self.driver.find_element_by_class_name('z-navicat-header_userAccountRegister')
        linkToRegister.click()

    def FillRegisterForm(self, name='', lastname='', email='', password=''):
        input = self.driver.find_element_by_name('register.firstname')
        input.clear()
        input.send_keys(name)
        input = self.driver.find_element_by_name('register.lastname')
        input.clear()
        input.send_keys(lastname)
        input = self.driver.find_element_by_name('register.email')
        input.clear()
        input.send_keys(email)
        input = self.driver.find_element_by_name('register.password')
        input.clear()
        input.send_keys(password)

    def clickRadio(self):
        # self.driver.find_element_by_id("register.gender-zds_radio_mens_1").click()
        self.driver.find_element_by_xpath('//*[@id="register.gender-zds_radio_womens_0"]').click()


    def clickSubmitRegisterForm(self):
        # self.driver.find_element_by_class_name("btn btn-primary").click()
        self.driver.find_element_by_xpath('//*[@id="section-register"]/div/form/div[7]/button').click()

    def close(self):
        self.driver.close()




