from practiceselenium import Practiceselenium
from selenium import webdriver
import time


driver = webdriver.Chrome(executable_path='../../webdriver/chromedriver')
p = Practiceselenium(driver)
p.open()
p.clickOurcheckOut()
p.fillFormCheckOut()
time.sleep(3)
p.clickSubmitCheckOut()
# p.clickCancel()

p.close()

