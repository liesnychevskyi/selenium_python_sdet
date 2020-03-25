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
links = driver.find_elements(By.TAG_NAME, "a")
print(len(links))
for each in links:
    print(each.text)
#  ------------------------------------------------------------------------//
#  ------------------------------------------------------------------------//
# close the session
driver.close()
driver.quit()
