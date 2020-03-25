from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path='C:\\Users\\User\\PycharmProjects\\selenium_sdet\\drivers\\chromedriver.exe')

driver.get("http://newtours.demoaut.com/")
time.sleep(5)

user_ele = driver.find_element_by_name("userName")
print("Element is displayed: ", user_ele.is_displayed())  # Return true/false
print("Element is enable: ", user_ele.is_enabled())  # Return true/false

password_ele = driver.find_element_by_name("password")
print("Element is displayed: ", password_ele.is_displayed())  # Return true/false
print("Element is enable: ", password_ele.is_enabled())  # Return true/false

button_ele = driver.find_element_by_name("login")
print("Element is displayed: ", button_ele.is_displayed())  # Return true/false
print("Element is enable: ", button_ele.is_enabled())  # Return true/false

user_ele.send_keys("mercury")
password_ele.send_keys("mercury")
time.sleep(3)
button_ele.click()

time.sleep(3)
roundTrip_radio = driver.find_element_by_css_selector("input[value=roundtrip]")
print("Element is selected: ", roundTrip_radio.is_selected())

oneWay_radio = driver.find_element_by_css_selector("input[value=oneway]")
print("Element is selected: ", oneWay_radio.is_selected())

print(driver.current_url)
print(driver.title)

driver.close()
driver.quit()
