from selenium import webdriver
import time
from selenium.webdriver import ActionChains


class Phptravels:
    url = 'https://phptravels.com/demo/'
    driver = webdriver

    def __init__(self, webdriver):
        self.driver = webdriver

    def open(self):
        self.driver.maximize_window()
        self.driver.get(self.url)

    def clickLink1(self):
        res = self.driver.find_element_by_xpath('/html/body/div[2]/main/section[1]/div/div/div[4]/div/div/div['
                                                '2]/div/div/div[1]/div/a/small')
        res.click()

    def waitUntilLoaded(self, timeout, xpath):
        start = time.monotonic()
        end = start + timeout

        while end >= time.monotonic():
            try:
                res = self.driver.find_element_by_xpath(xpath)
                if res:
                    res.click()
                    return res

            except:
                print("Exception waitUntilLoaded")

    def waitUntilLoadedDropDownList(self, timeout, xpath):
        start = time.monotonic()
        end = start + timeout

        while end >= time.monotonic():
            try:
                res = self.driver.find_element_by_xpath(xpath)
                if res:
                    action = ActionChains(self.driver)
                    action.move_to_element(res).perform()
                    res.click()
                    return res

            except:
                print("Exception waitUntilLoadedDropDownList")

    # function waits for some time while the element is loaded
    # when it is found it immediately executes
    def clickLink(self, timeout=3):
        self.waitUntilLoaded(timeout, '/html/body/div[2]/main/section[1]/div/div/div[4]/div/div/div[2]/div/div/div['
                                      '1]/div/a/small')

    def fillForm(self):
        # switch to new opened tab
        # self.driver.switch_to_window(self.driver.window_handles[1])
        self.driver.switch_to.window(self.driver.window_handles[1])
        r = self.driver.find_element_by_xpath("/html/body/div[2]/form[1]/div[1]/label[1]/input")
        r.clear()
        r.send_keys("supplier@phptravels.com")
        r = self.driver.find_element_by_xpath("/html/body/div[2]/form[1]/div[1]/label[2]/input")
        r.clear()
        r.send_keys("demosupplier")
        self.driver.find_element_by_xpath('/html/body/div[2]/form[1]/button').click()

    # HOTELS
    def findLinkHotels(self, timeout=10):
        self.waitUntilLoaded(timeout, '/html/body/div[3]/nav/div[2]/ul/li[2]/a')

    def clickAddRoom(self, timeout=10):
        self.waitUntilLoadedDropDownList(timeout, '/html/body/div[3]/nav/div[2]/ul/li[2]/ul/li[3]/a')

    def close(self):
        self.driver.close()

    def findLinkLocation(self, timeout=10):
        self.waitUntilLoaded(timeout, '//*[@id="social-sidebar-menu"]/li[3]/a')

    def clickLocation(self, timeout=10):
        self.waitUntilLoadedDropDownList(timeout, '//*[@id="Locations"]/li/a')

    def add(self, timeout=10):
        self.waitUntilLoaded(timeout, '//*[@id="content"]/div[2]/div[2]/a')

    def addInfo(self):
        status = self.waitUntilLoaded(10, '/html/body/div[3]/div/form/div[2]/div/div[2]/div[1]/div/select')
        self.waitUntilLoadedDropDownList(5, '/html/body/div[3]/div/form/div[2]/div/div[2]/div[1]/div/select/option[1]')
        price = self.waitUntilLoaded(10, '//*[@id="content"]/form/div[2]/div/div[2]/div[2]/div/strong/input')
        # price = self.driver.find_element_by_xpath('//*[@id="content"]/form/div[2]/div/div[2]/div[2]/div/strong/input')
        price.clear()
        price.send_keys("88")

    def getPrice(self):
        # /html/body/div[3]/div/form/div[2]/div/div[2]/div[2]/div/strong/input
        info = self.driver.find_element_by_xpath('/html/body/div[3]/div/form/div[2]/div/div[2]/div[2]/div/strong/input')
        return info.text


# test
driver = webdriver.Chrome(executable_path='webdriver/chromedriver')
p = Phptravels(driver)
p.open()
p.clickLink(10)
p.fillForm()
p.findLinkHotels()
# time.sleep(4)
p.clickAddRoom()
p.addInfo()

# price = p.getPrice()
# time.sleep(4)
# assert price == '88', 'Something wrong'
# p.findLinkLocation()
# p.clickLocation()
# p.add()

# p.close()


#
