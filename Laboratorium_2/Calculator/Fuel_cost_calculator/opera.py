from fueltest import FuelTest
from selenium import webdriver

driver = webdriver.Opera(executable_path='../../webdriver/operadriver')
f = FuelTest(driver)
f.open()
f.CalculateCost()
message = f.getMessage()
assert message == "This trip will require 22.5 liters of fuel, which amounts to a fuel cost of $63."

if message == "This trip will require 22.5 liters of fuel, which amounts to a fuel cost of $63.":
    print("OK")

# f.close()