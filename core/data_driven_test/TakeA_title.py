import time
from selenium import webdriver
#  ------------------------------------------------------------------------------//
driver = webdriver.Chrome(executable_path='C:\\Users\\User\\PycharmProjects\\selenium_sdet\\drivers\\chromedriver.exe')
#  driver.get("http://newtours.demoaut.com/")
driver.get("http://newtours.demoaut.com/mercuryreservation.php")
#  ------------------------------------------------------------------------------//
# waiting some time (5 second to wait all the elements on the page)
driver.implicitly_wait(5)

# maximize browser
driver.maximize_window()

# take url
print(driver.current_url)

# take title
title_landing_page = driver.title
print(title_landing_page)
time.sleep(5)

driver.close()