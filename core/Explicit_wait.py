
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC  # EC - it is variable
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path='C:\\Users\\User\\PycharmProjects\\selenium_sdet\\drivers\\chromedriver.exe')

driver.get("https://www.expedia.com/")  # opening URL takes some time

# waiting some time (5 second to wait all the elements on the page)
driver.implicitly_wait(5)

# maximize browser
driver.maximize_window()

# take url
print(driver.current_url)

# take title
print(driver.title)
time.sleep(5)
# assertion
# assert "" in driver.title
# execution
driver.find_element(By.ID, "tab-flight-tab-hp").click()
# driver.find_element_by_id("tab-flight-tab-hp").click()

# driver.find_element_by_id("flight-origin-hp-flight").clear()
driver.find_element_by_id("flight-origin-hp-flight").send_keys("Israel")
time.sleep(5)
#  ------------------------------------------------------------------------//
driver.find_element_by_id("flight-destination-hp-flight").clear()
time.sleep(5)
driver.find_element_by_id("flight-destination-hp-flight").send_keys("NYC")
#  ------------------------------------------------------------------------//
driver.find_element_by_id("flight-returning-hp-flight").clear()
time.sleep(5)
driver.find_element_by_id("flight-returning-hp-flight").send_keys("07/07/2020")
#  ------------------------------------------------------------------------//
driver.find_element_by_id("flight-departing-hp-flight").clear()
time.sleep(5)
driver.find_element_by_id("flight-departing-hp-flight").send_keys("03/01/2020")
#  ------------------------------------------------------------------------//
driver.find_element_by_xpath('//*[@id="traveler-selector-hp-flight"]/div/ul/li/button').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="traveler-selector-hp-flight"]/div/ul/li/button').click()
#  ------------------------------------------------------------------------//
time.sleep(5)
driver.find_element_by_xpath('//*[@id="gcw-flights-form-hp-flight"]/div[8]/label/button').click()
#  ------------------------------------------------------------------------//
wait = WebDriverWait(driver, 10)  # object wait driver for condition
element = wait.until(EC.element_to_be_clickable((By.ID, "stopFilter_stops-0")))
element.click()
#  ------------------------------------------------------------------------//
# close the session
driver.close()
driver.quit()
