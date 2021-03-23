from msedge.selenium_tools.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

# Practiceselenium
class Practiceselenium:
    url = 'http://www.practiceselenium.com/'
    driver = webdriver

    def __init__(self, webdriver):
        self.driver = webdriver

    def open(self):
        self.driver.maximize_window()
        self.driver.get(self.url)

    def clickOurPassion(self):
        self.driver.find_element_by_link_text("Our Passion").click();

    def clickmenu(self):
        self.driver.find_element_by_link_text("Menu").click();

    def clickOurcheckOut(self):
        self.driver.find_element_by_link_text("Check Out").click();

    def clickWelcome(self):
        self.driver.find_element_by_link_text("Welcome").click();

    def clickOurletTalkTea(self):
        self.driver.find_element_by_link_text("Let's Talk Tea").click();

    def fillFormLetTalkTea(self):
        self.driver.find_element_by_name("name").send_keys("Test")
        self.driver.find_element_by_name("email").send_keys("test@gmail.com")
        self.driver.find_element_by_name("subject").send_keys("Tea")
        self.driver.find_element_by_name("message").send_keys("Let's talk")

    def clickSubmitLetTalkTea(self):
        self.driver.find_element_by_xpath('//*[@id="form_78ea690540a24bd8b9dcfbf99e999fea"]/div[1]/div[5]/input').click()


    def fillFormCheckOut(self):
        self.driver.find_element_by_id("email").send_keys("test@gmail.com")
        self.driver.find_element_by_id("name").send_keys("Test")
        self.driver.find_element_by_id("address").send_keys("Poland")
        Select(self.driver.find_element_by_id("card_type")).select_by_visible_text("Visa")
        self.driver.find_element_by_id("card_number").send_keys("card_number")
        self.driver.find_element_by_id("cardholder_name").send_keys("cardholder_name")
        self.driver.find_element_by_id("verification_code").send_keys("verification_code")

    def clickSubmitCheckOut(self):
        self.driver.find_element_by_xpath('//*[@id="wsb-element-00000000-0000-0000-0000-000452010925"]/div/div/form/div/button').click()

    def clickCancel(self):
        self.driver.find_element_by_link_text("Cancel").click();

    def close(self):
        self.driver.close()
