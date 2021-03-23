from zalando import Zalando
from selenium import webdriver
import time

name = 'John'
lastname = 'Hilton'
email = 'jhilton@gmail.com'
password = '12345678'

driver = webdriver.Opera(executable_path='../../webdriver/operadriver')
z = Zalando(driver)
z.open()

z.ToRegister()
z.FillRegisterForm(name, lastname, email, password)
# z.clickSubmitRegisterForm()

