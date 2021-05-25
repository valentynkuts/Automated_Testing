from selenium import webdriver
import time


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

    # function waits for some time while the element is loaded
    # when it is found it immediately executes
    def clickLink(self, timeout=3):
        start = time.monotonic()
        end = start + timeout

        while end >= time.monotonic():
            try:
                res = self.driver.find_element_by_xpath('/html/body/div[2]/main/section[1]/div/div/div[4]/div/div/div['
                                                        '2]/div/div/div[1]/div/a/small')
                if res:
                    print(res)
                    res.click()
                    return 1

            except:
                print("An exception occurred")

    def fillForm(self):
        # switch to new opened tab
        self.driver.switch_to_window(self.driver.window_handles[1])
        r = self.driver.find_element_by_xpath("/html/body/div[2]/form[1]/div[1]/label[1]/input")
        r.clear()
        r.send_keys("supplier@phptravels.com")
        r = self.driver.find_element_by_xpath("/html/body/div[2]/form[1]/div[1]/label[2]/input")
        r.clear()
        r.send_keys("demosupplier")
        self.driver.find_element_by_xpath('/html/body/div[2]/form[1]/button').click()

    def close(self):
        self.driver.close()


# test
driver = webdriver.Chrome(executable_path='webdriver/chromedriver')
p = Phptravels(driver)
p.open()
p.clickLink(10)
p.fillForm()
