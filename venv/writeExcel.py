import xlrd
rb = xlrd.open_workbook('1.xls')
sheet = rb.sheet_by_index(0)
for rownum in range(sheet.nrows):
    row = sheet.row_values(rownum)
    print(row)