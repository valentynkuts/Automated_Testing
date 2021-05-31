from selenium import webdriver
from loguru import logger
import time

logger.add("debug.log", format="{time} {level} {message}", level="DEBUG",
           rotation="20 KB", compression="zip")


class Phptravels:
    url = 'https://phptravels.com/demo/'
    driver = webdriver

    def __init__(self, webdriver):
        self.driver = webdriver

    def open(self):
        self.driver.maximize_window()
        self.driver.get(self.url)

    # this function raise Exception because does not find the element
    @logger.catch
    def clickLink1(self):
        res = self.driver.find_element_by_xpath('/html/body/div[2]/main/section[1]/div/div/div[4]/div/div/div['
                                                '2]/div/div/div[1]/div/a/small')
        res.click()

    # function waits for some time while the element is loaded
    # when it is found it immediately executes
    @logger.catch
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
                    logger.info('click')
                    return 1

            except Exception as e:
                # print("An exception occurred")
                # logger.exception("An exception occurred")
                logger.exception(e)

    def fillForm(self):
        # switch to new opened tab
        # self.driver.switch_to_window(self.driver.window_handles[1])
        self.driver.switch_to.window(self.driver.window_handles[1])
        logger.info('Swith to https://www.phptravels.net/supplier')
        r = self.driver.find_element_by_xpath("/html/body/div[2]/form[1]/div[1]/label[1]/input")
        r.clear()
        r.send_keys("supplier@phptravels.com")
        logger.info('Enter email supplier@phptravels.com')
        r = self.driver.find_element_by_xpath("/html/body/div[2]/form[1]/div[1]/label[2]/input")
        r.clear()
        r.send_keys("demosupplier")
        logger.info('Enter password demosupplier')
        self.driver.find_element_by_xpath('/html/body/div[2]/form[1]/button').click()

    def close(self):
        self.driver.close()


# test
driver = webdriver.Chrome(executable_path='webdriver/chromedriver')
p = Phptravels(driver)
p.open()
logger.info("Open https://phptravels.com/demo/")
# p.clickLink1() # raise Exception
p.clickLink(10)
p.fillForm()
# p.close()
logger.info("Close")
