from sleepcalculator import Sleepcalc
from selenium import webdriver

driver = webdriver.Opera(executable_path='../../webdriver/operadriver')
s = Sleepcalc(driver)
s.open()
s.search('Sleep Calculator')
