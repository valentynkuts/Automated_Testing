from zalando import Zalando
from selenium import webdriver


name = 'John'
lastname = 'Hilton'
email = 'jhilton@gmail.com'
password = '12345678'

driver = webdriver.Chrome(executable_path='../../webdriver/chromedriver')
z = Zalando(driver)
z.open()

z.ToRegister()
z.FillRegisterForm(name, lastname, email, password)
# z.clickRadio()
# z.clickSubmitRegisterForm()



