import time
from selenium import webdriver

#  ------------------------------------------------------------------------------//
driver = webdriver.Chrome(executable_path='C:\\Users\\User\\PycharmProjects\\selenium_sdet\\drivers\\chromedriver.exe')
driver.get("http://www.amazon.com")
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
#  ------------------------------------------------------------------------------//
#  Capture all the COOkIES from the browser
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)
#  ------------------------------------------------------------------------------//
#  Add new cookies to the browser
cookie = {'name': 'Mycookie', 'value': '1234567890'}
driver.add_cookie(cookie)  # add cookie
#  ------------------------------------------------------------------------------//
#  Checking one more time all cookies after adding new cookie
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)
#  ------------------------------------------------------------------------------//
#  Deleting the cookie
driver.delete_cookie('Mycookie')
#  ------------------------------------------------------------------------------//
#  Checking one more time all cookies after deleting new cookie
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)
#  ------------------------------------------------------------------------------//
driver.close()
driver.quit()
#  ------------------------------------------------------------------------------//
