from zalando import Zalando
from selenium import webdriver
import  time

name = 'John'
lastname = 'Hilton'
email = 'jhilton@gmail.com'
password = '12345678'

driver = webdriver.Firefox(executable_path='../../webdriver/geckodriver')
z = Zalando(driver)
z.open()

z.ToRegister()
z.FillRegisterForm(name, lastname, email, password)
# z.clickSubmitRegisterForm()
