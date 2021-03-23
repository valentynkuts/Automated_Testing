from practiceselenium import Practiceselenium
from selenium import webdriver
import time

driver = webdriver.Opera(executable_path='../../webdriver/operadriver')
p = Practiceselenium(driver)
p.open()
p.clickOurcheckOut()
p.fillFormCheckOut()
time.sleep(3)
p.clickSubmitCheckOut()
# p.clickCancel()

p.close()


