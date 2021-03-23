from practiceselenium import Practiceselenium
from selenium import webdriver

driver = webdriver.Chrome(executable_path='../../webdriver/chromedriver')
p = Practiceselenium(driver)
p.open()
p.clickWelcome()

p.close()
