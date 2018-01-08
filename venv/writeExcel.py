import xlrd
class readExcel:
    def readExcel(self,nameFileExcel):
        try:
            rb = xlrd.open_workbook(nameFileExcel)
        except FileNotFoundError:
            print('Ошибка-'+FileNotFoundError)
        sheet = rb.sheet_by_index(0)
        for rownum in range(sheet.nrows):
            row = sheet.row_values(rownum)
            print(row)
    def createFile(self,nameFile):
        try:
            my_file = open(nameFile,'w')
        except FileExistsError:
           print('Ошибка-'+FileExistsError)
obj1 = readExcel()
obj1.readExcel('1.xls')
obj1.createFile('some.txt')