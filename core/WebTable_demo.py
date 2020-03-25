from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC  # EC - it is variable
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path='C:\\Users\\User\\PycharmProjects\\selenium_sdet\\drivers\\chromedriver.exe')

driver.get("https://wet-boew.github.io/v4.0-ci/demos/tables/tables-en.html")  # opening URL takes some time

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
rows = len(driver.find_elements_by_xpath('//*[@id="wb-auto-1"]/tbody/tr'))
print(rows)
time.sleep(5)
#  ------------------------------------------------------------------------//
columns = len(driver.find_elements_by_xpath('//*[@id="wb-auto-1"]/tbody/tr[1]/td'))
print(columns)
time.sleep(5)
#  ------------------------------------------------------------------------// loop for incrementing rows
#  for r in rows(2, rows-1) # to avoid hadar row
print("Rendering engine" + "     " + "Browser" + "     " + "Platform" + "     " + "     " + "Engine version" + "    " + "CSS grade")
for r in range(1, rows+1):
    for c in range(1, columns+1):
        value = driver.find_element_by_xpath("//*[@id='wb-auto-1']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(value, end="           ")
    print()
#  ------------------------------------------------------------------------//

#  ------------------------------------------------------------------------//

#  ------------------------------------------------------------------------// Close the session
time.sleep(10)
#  driver.close() #  it is close just parent window
driver.quit()  # it is close all active windows
