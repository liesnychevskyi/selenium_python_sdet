from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path='C:\\Users\\User\\PycharmProjects\\selenium_sdet\\drivers\\chromedriver.exe')

driver.get("http://newtours.demoaut.com/")

print(driver.current_url)
print(driver.title)

driver.get("http://pavantestingtools.blog.spot.in/")

driver.maximize_window()

print(driver.current_url)  # return current URL
print(driver.title)  # title of page
# driver.find_element_by_xpath('').click()
time.sleep(5)

driver.back()  # driver step back

time.sleep(5)

print(driver.current_url)
print(driver.title)
driver.forward()  # step forward

print(driver.current_url)
print(driver.title)

driver.close()
driver.quit()
