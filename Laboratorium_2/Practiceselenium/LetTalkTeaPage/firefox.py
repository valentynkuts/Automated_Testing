from practiceselenium import Practiceselenium
from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path='../../webdriver/geckodriver')
p = Practiceselenium(driver)
p.open()
p.clickOurletTalkTea()
p.fillFormLetTalkTea()
time.sleep(3)
p.clickSubmitLetTalkTea()

p.close()


