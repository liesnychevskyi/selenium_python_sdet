from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC  # EC - it is variable
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path='C:\\Users\\User\\PycharmProjects\\selenium_sdet\\drivers\\chromedriver.exe')

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")  # opening URL takes some time

# waiting some time (5 second to wait all the elements on the page)
# driver.implicitly_wait(5)
# maximize browser
driver.maximize_window()
# take url
print(driver.current_url)
# take title
print(driver.title)
time.sleep(5)
#  ------------------------------------------------------------------------// 1. Scroll down by pixel
#  driver.execute_script("window.scrollBy(0,1000,"")")
#  time.sleep(5)
#  ------------------------------------------------------------------------// 2. Scroll down till element is found
# flag_german = driver.find_element_by_xpath("//img[@alt='Flag of Germany']")
# driver.execute_script("arguments[0].scrollIntoView();", flag_german)
# time.sleep(5)
#  ------------------------------------------------------------------------// 3. Scroll to the end of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(5)
#  ------------------------------------------------------------------------//
time.sleep(5)
#  ------------------------------------------------------------------------//

#  ------------------------------------------------------------------------//
time.sleep(10)
driver.close()  # it is close just parent window
driver.quit()  # it is close all active windows
