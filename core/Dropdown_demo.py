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
#  ------------------------------------------------------------------------//
list_of_elements = driver.find_elements_by_xpath("//select[@name='passCount']/option")
time.sleep(5)
for each in list_of_elements:
    status = each.is_displayed()
    print(status)
    if status:
        print(each.text)
        each.click()
        time.sleep(5)
    else:
        print("Status Error !!! <<False>>")
# driver.find_element_by_id("").send_keys("")
#  ------------------------------------------------------------------------//

#  ------------------------------------------------------------------------//
# close the session
driver.close()
driver.quit()
