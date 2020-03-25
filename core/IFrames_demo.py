from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC  # EC - it is variable
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path='C:\\Users\\User\\PycharmProjects\\selenium_sdet\\drivers\\chromedriver.exe')

driver.get("http://seleniumhq.github.io/selenium/docs/api/java/index.html")  # opening URL takes some time

# waiting some time (5 second to wait all the elements on the page)
# driver.implicitly_wait(5)
# maximize browser
driver.maximize_window()
# take url
print(driver.current_url)
# take title
print(driver.title)
time.sleep(5)
#  ------------------------------------------------------------------------// Switch to frame
driver.switch_to.frame("packageListFrame")
driver.find_element_by_link_text("org.openqa.selenium.firefox").click()
time.sleep(3)
#  ------------------------------------------------------------------------// Switch to main page
driver.switch_to.default_content()
driver.back()
time.sleep(3)
#  -----------------------------------------------------------------------// Switch to other frame
driver.switch_to.frame("packageFrame")
driver.find_element_by_link_text("Action").click()
time.sleep(3)
#  ------------------------------------------------------------------------//
driver.switch_to.default_content()
time.sleep(3)
#  ------------------------------------------------------------------------//
driver.switch_to.frame("classFrame")
driver.find_element_by_xpath("/html/body/div[1]/ul/li[5]/a").click()
time.sleep(3)
#  ------------------------------------------------------------------------//
# close the session
time.sleep(10)
driver.close()
driver.quit()
