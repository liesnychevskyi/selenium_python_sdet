from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path='C:\\Users\\User\\PycharmProjects\\selenium_sdet\\drivers\\chromedriver.exe')

driver.get("http://demo.automationtesting.in/Windows.html")
driver.maximize_window()
print(driver.current_url)  # return current URL
print(driver.title)  # title of page
driver.find_element_by_xpath('//*[@id="Tabbed"]/a/button').click()
time.sleep(5)

driver.close()
driver.quit()
