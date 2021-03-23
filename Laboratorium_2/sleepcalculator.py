from selenium import webdriver


class Sleepcalc:
    url = 'https://www.calculator.net'
    driver = webdriver

    def __init__(self, webdriver):
        self.driver = webdriver

    def open(self):
        self.driver.maximize_window()
        self.driver.get(self.url)

    def search(self, info):
        input = self.driver.find_element_by_id('calcSearchTerm')
        input.send_keys(info)
        # button_search = self.driver.find_element_by_id('bluebtn')
        # button_search.click()
        link = self.driver.find_element_by_link_text(info)
        link.click()

    def close(self):
        self.driver.close()




