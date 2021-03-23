from practiceselenium import Practiceselenium
from selenium import webdriver

driver = webdriver.Firefox(executable_path='../../webdriver/geckodriver')
p = Practiceselenium(driver)
p.open()
p.clickWelcome()

p.close()


