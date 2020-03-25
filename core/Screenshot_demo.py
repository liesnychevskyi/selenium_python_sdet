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
#  Take a screen shot
driver.save_screenshot("C:\\Users\\User\\PycharmProjects\\selenium_sdet\\screenshots\\amazon_home_page_1.png")
#  ------------------------------------------------------------------------------//
#  Take a screen shot as a file
driver.get_screenshot_as_file("C:\\Users\\User\\PycharmProjects\\selenium_sdet\\screenshots\\amazon_home_page_2.png")
#  ------------------------------------------------------------------------------//
#  Take a screen shot as PNJ file
#  driver.get_screenshot_as_png("C:\\Users\\User\\PycharmProjects\\selenium_sdet\\screenshots\\amazon_home_page_3")
#  ------------------------------------------------------------------------------//

#  ------------------------------------------------------------------------------//

#  ------------------------------------------------------------------------------//
driver.close()
driver.quit()
#  ------------------------------------------------------------------------------//
