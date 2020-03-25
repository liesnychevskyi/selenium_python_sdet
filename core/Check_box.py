from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC  # EC - it is variable
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path='C:\\Users\\User\\PycharmProjects\\selenium_sdet\\drivers\\chromedriver.exe')

driver.get("http://newtours.demoaut.com/")  # opening URL takes some time

# waiting some time (5 second to wait all the elements on the page)
# driver.implicitly_wait(5)
# maximize browser
driver.maximize_window()
# take url
print(driver.current_url)
# take title
# print(driver.title)
# time.sleep(5)
#  ------------------------------------------------------------------------//
driver.find_element(By.XPATH, "/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/table/tbody/tr/td[1]/a").click()
time.sleep(5)
driver.find_element_by_name("userName").send_keys("mercury")
time.sleep(5)
driver.find_element_by_name("password").send_keys("mercury")
time.sleep(5)
driver.find_element_by_name("login").click()
time.sleep(5)
#  ------------------------------------------------------------------------//
roundTrip = driver.find_element_by_xpath("//input[@value='roundtrip']")
oneWey = driver.find_element_by_xpath("//input[@value='oneway']")
#  -----------------------------------------------------------------------//
if roundTrip.is_selected():
    print("Round trip is selected already")
else:
    roundTrip.click()
#  ------------------------------------------------------------------------//
if oneWey.is_selected():
    print("One way is selected already")
else:
    oneWey.click()
#  ------------------------------------------------------------------------//
# close the session
time.sleep(10)
driver.close()
driver.quit()