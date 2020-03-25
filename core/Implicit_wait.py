
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path='C:\\Users\\User\\PycharmProjects\\selenium_sdet\\drivers\\chromedriver.exe')

driver.get("http://newtours.demoaut.com/")  # opening URL takes some time

# waiting some time (implicit)
driver.implicitly_wait(10)
# maximize browser
driver.maximize_window()
# take url
print(driver.current_url)
# take title
print(driver.title)
# assertion
assert "Welcome: Mercury Tours" in driver.title
# execution
driver.find_element_by_name("userName").send_keys("mercury")
driver.find_element_by_name("password").send_keys("mercury")
driver.find_element_by_name("login").click()
# close the session
driver.close()
driver.quit()
