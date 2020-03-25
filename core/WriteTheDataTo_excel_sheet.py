import openpyxl
#  ------------------------------------------------------------------------/ Work book
#  path_to_excel_file = "C:/Users/User/PycharmProjects/selenium_sdet/test_data/Test.xlsx"
path_to_excel_file = "C:/Users/User/PycharmProjects/selenium_sdet/test_data/Test_0.xlsx"
workBook = openpyxl.load_workbook(path_to_excel_file)  # load the workbook (object)
#  sheet = workBook.active  # if you have only 1 sheet in particular workbook
#  sheet_to_write = workBook.get_sheet_by_name("list")  # If we have more than 1 active sheets
sheet_to_write = workBook["list"]  # new instead deprecated method
#  ------------------------------------------------------------------------/
#  ------------------------------------------------------------------------/ Reading data from ecxel file
for r in range(1, 6):  # If you set 5 it will creating just 4 rows ...  (1, 5 -1)=4 or (1, 6 -1)=5
    for c in range(1, 4):
        sheet_to_write.cell(row=r, column=c).value = "Stas very reach"
    workBook.save(path_to_excel_file)  # save the writen data
#  ------------------------------------------------------------------------/
#  ------------------------------------------------------------------------/
#  ------------------------------------------------------------------------//
#  ------------------------------------------------------------------------//
#  ------------------------------------------------------------------------//
#  ------------------------------------------------------------------------//
#  ------------------------------------------------------------------------//
#  ------------------------------------------------------------------------//

