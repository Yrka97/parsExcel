import xlrd
class readExcel:
    def readExcel(self,nameFileExcel):
        rb = xlrd.open_workbook(nameFile)
        sheet = rb.sheet_by_index(0)
        for rownum in range(sheet.nrows):
            row = sheet.row_values(rownum)
            print(row)
    def createFile(self,nameFile):
        my_file = open(nameFile,wr)
        my_file.fileno()
obj1 = readExcel()
obj1.readExcel('1.xls')