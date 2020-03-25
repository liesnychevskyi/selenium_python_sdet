from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC  # EC - it is variable
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path='C:\\Users\\User\\PycharmProjects\\selenium_sdet\\drivers\\chromedriver.exe')

driver.get("http://demo.automationtesting.in/Windows.html")  # opening URL takes some time

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
driver.find_element_by_xpath('//*[@id="Tabbed"]/a/button').click()
time.sleep(5)
#  ------------------------------------------------------------------------// Parent window ID
print("Windows number 1 is: ", driver.current_window_handle)
#  -----------------------------------------------------------------------// Returns all the open browsers windows
handles = driver.window_handles
for window in handles:
    print("ID is:", window)
    driver.switch_to.window(window)
    print(driver.title)
    if driver.title == "Frames & windows":
        driver.close()
#  ------------------------------------------------------------------------//

#  ------------------------------------------------------------------------//

#  ------------------------------------------------------------------------// Close the session
time.sleep(10)
#  driver.close() #  it is close just parent window
driver.quit()  # it is close all active windows
