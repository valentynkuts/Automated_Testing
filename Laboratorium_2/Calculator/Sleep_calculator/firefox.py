from sleepcalculator import Sleepcalc
from selenium import webdriver

driver = webdriver.Chrome(executable_path='../../webdriver/chromedriver')
s = Sleepcalc(driver)
s.open()
s.search('Sleep Calculator')
