from sleepcalculator import Sleepcalc
from selenium import webdriver

driver = webdriver.Firefox(executable_path='../../webdriver/geckodriver')
s = Sleepcalc(driver)
s.open()
s.search('Sleep Calculator')
