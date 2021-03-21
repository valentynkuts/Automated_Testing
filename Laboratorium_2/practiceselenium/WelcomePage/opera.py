from practiceselenium import Practiceselenium
from selenium import webdriver

driver = webdriver.Opera(executable_path='../../webdriver/operadriver')
p = Practiceselenium(driver)
p.open()
p.clickWelcome()

p.close()
