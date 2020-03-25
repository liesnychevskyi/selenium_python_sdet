from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC  # EC - it is variable
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path='C:\\Users\\User\\PycharmProjects\\selenium_sdet\\drivers\\chromedriver.exe')

driver.get("http://automationtesting.in/")  # opening URL takes some time

# waiting some time (5 second to wait all the elements on the page)
# driver.implicitly_wait(5)
# maximize browser
driver.maximize_window()
# take url
print(driver.current_url)
# take title
print(driver.title)
time.sleep(5)
#  ------------------------------------------------------------------------//
more = driver.find_element_by_xpath("//a[text()='More…']")
sikuli = driver.find_element_by_xpath("//a[text()='Sikuli']")
#  ------------------------------------------------------------------------//
actions = ActionChains(driver)
actions.move_to_element(more).move_to_element(sikuli).click().perform()
time.sleep(5)
#  ------------------------------------------------------------------------//

#  ------------------------------------------------------------------------//

#  ------------------------------------------------------------------------//

#  ------------------------------------------------------------------------//
time.sleep(10)
driver.close()  # it is close just parent window
driver.quit()  # it is close all active windows
