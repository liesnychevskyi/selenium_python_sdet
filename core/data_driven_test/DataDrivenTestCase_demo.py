import time
from selenium import webdriver
from core.data_driven_test import EXCEL_utiles  # import methods


path_excel = "C:\\Users\\User\\PycharmProjects\\selenium_sdet\\test_data\\Test.xlsx"
sheet_name = "dataDrivenTest"
#  ------------------------------------------------------------------------------//
driver = webdriver.Chrome(executable_path='C:\\Users\\User\\PycharmProjects\\selenium_sdet\\drivers\\chromedriver.exe')
driver.get("http://newtours.demoaut.com/")
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
rows = EXCEL_utiles.getRowCount(path_excel, sheet_name)
for r in range(2, rows+1):
    user_name = EXCEL_utiles.readData(path_excel, sheet_name, r, 1)
    password = EXCEL_utiles.readData(path_excel, sheet_name, r, 2)
    time.sleep(5)
    driver.find_element_by_name("userName").send_keys(user_name)
    time.sleep(5)
    driver.find_element_by_name("password").send_keys(password)
    time.sleep(5)
    driver.find_element_by_name("login").click()
    time.sleep(5)
    if driver.title == "Find a Flight: Mercury Tours:":
        print("Test is Passed...")
        EXCEL_utiles.writeData(path_excel, sheet_name, r, 3, "test pass")
    else:
        print("Test Failed...")
        EXCEL_utiles.writeData(path_excel, sheet_name, r, 3, "test fail")

    driver.find_element_by_link_text("Home").click()
#  ------------------------------------------------------------------------//
# close the session

#  ------------------------------------------------------------------------//

