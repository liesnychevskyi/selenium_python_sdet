import time

from selenium import webdriver

#  ------------------------------------------------------------------------/Fire_f options for download to specified dir
fp = webdriver.FirefoxProfile()
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/plain,application/pdf")  # Mime type
fp.set_preference("browser.download.manager.showWhenStarting", False)
fp.set_preference("browser.download.dir", "C:\\SeleniumPythonDownload_folder")
fp.set_preference("browser.download.folderList", 2)
fp.set_preference("pdfjs.disabled", True)  # for PDF files disabling pop-up window

driver = webdriver.Firefox(firefox_profile=fp)
driver.get("http://demo.automationtesting.in/FileDownload.html")  # opening URL takes some time
#  ------------------------------------------------------------------------/
# waiting some time (5 second to wait all the elements on the page)
# driver.implicitly_wait(5)
# maximize browser
driver.maximize_window()
# take url
print(driver.current_url)
# take title
print(driver.title)
time.sleep(5)
#  ------------------------------------------------------------------------// Download text file
txt_box = driver.find_element_by_id("textbox")
button = driver.find_element_by_id("createTxt")
file_link = driver.find_element_by_id("link-to-download")

driver.execute_script("arguments[0].scrollIntoView();", txt_box)
time.sleep(5)
txt_box.send_keys("download_text_file")
time.sleep(5)
button.click()
time.sleep(5)
file_link.click()
time.sleep(5)
#  ------------------------------------------------------------------------// Download PDF file
txt_box_pdf = driver.find_element_by_id("pdfbox")
button_pdf = driver.find_element_by_id("createPdf")
file_link_pdf = driver.find_element_by_id("pdf-link-to-download")

driver.execute_script("arguments[0].scrollIntoView();", txt_box_pdf)
time.sleep(5)
txt_box_pdf.send_keys("download_pdf_file")
time.sleep(5)
button_pdf.click()
time.sleep(5)
file_link_pdf.click()
time.sleep(5)
#  ------------------------------------------------------------------------//

#  ------------------------------------------------------------------------//

#  ------------------------------------------------------------------------//

#  ------------------------------------------------------------------------//
time.sleep(10)
driver.close()  # it is close just parent window
driver.quit()  # it is close all active windows
