import xlrd
class readExcel:

    def readExcel(self,nameFileExcel):
        try:
            rb = xlrd.open_workbook(nameFileExcel)
        except FileNotFoundError:
            print('Ошибка файл не найден')
        sheet = rb.sheet_by_index(0)
        for rownum in range(sheet.nrows):
            row = sheet.row_values(rownum)
            stringRow = str(row)
            obj1.writeFile('some.txt',stringRow)
            print(stringRow)

    def writeFile(self,nameFile,write):
        try:
            my_file = open(nameFile,'a')
        except FileNotFoundError:
           print('Ошибка файл не найден')
        try:
            my_file.write(write)
        except IOError:
            print('Ошибка записи в файл')

obj1 = readExcel()
obj1.readExcel('1.xls')