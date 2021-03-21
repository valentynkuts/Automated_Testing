from practiceselenium import Practiceselenium
from selenium import webdriver
import time

driver = webdriver.Opera(executable_path='../../webdriver/operadriver')
p = Practiceselenium(driver)
p.open()
p.clickOurletTalkTea()
p.fillFormLetTalkTea()
time.sleep(3)
p.clickSubmitLetTalkTea()

p.close()



