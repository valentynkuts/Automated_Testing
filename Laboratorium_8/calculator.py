from selenium import webdriver


class FuelTest:
    url = 'https://www.calculator.net/fuel-cost-calculator.html'
    driver = webdriver

    def __init__(self, webdriver):
        self.driver = webdriver

    def open(self):
        self.driver.maximize_window()
        self.driver.get(self.url)

    def CalculateCost(self):
        distance = self.driver.find_element_by_xpath('//*[@id ="content"]/table/tbody/tr[1]/td[2]/input')
        distance.clear()
        distance.send_keys("300")
        efficiency = self.driver.find_element_by_xpath(' //*[@id ="content"]/table/tbody/tr[2]/td[2]/input')
        efficiency.clear()
        efficiency.send_keys("7.5")
        price = self.driver.find_element_by_xpath('//*[@id ="content"]/table/tbody/tr[3]/td[2]/input')
        price.clear()
        price.send_keys("2.8")
        calculate = self.driver.find_element_by_xpath('//*[@id="content"]/table/tbody/tr[4]/td/input')
        calculate.click()

    def getMessage(self):
        info = self.driver.find_element_by_xpath('//*[@id="content"]/p[2]')
        message = info.text
        return message

    def close(self):
        self.driver.close()


# test
driver = webdriver.Chrome(executable_path='webdriver/chromedriver')
f = FuelTest(driver)
f.open()
f.CalculateCost()
message = f.getMessage()
assert message == "This trip will require 22.5 liters of fuel, which amounts to a fuel cost of $63."
# f.close()
