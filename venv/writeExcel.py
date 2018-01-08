import xlrd
class readExcel:

    def writeInfromToFile(self):
        obj1.writeFile('some.txt','База знаний.')
        obj1.writeFile('some.txt','\n')
        obj1.writeFile('some.txt','Автор: Ожогин Юрий.')
        obj1.writeFile('some.txt', '\n')
        obj1.writeFile('some.txt', '\n')

    def writeExcelQuestions(self,nameFileExcel):
        try:
            rb = xlrd.open_workbook(nameFileExcel)
        except FileNotFoundError:
            print('Ошибка файл не найден')
        sheet = rb.sheet_by_index(0)
        i = 1
        obj1.writeFile('some.txt', 'Вопросы:')
        obj1.writeFile('some.txt', '\n')
        while i<len(sheet.row_values(1)):
            row = sheet.row_values(1)[i]
            stringRow = str(row)
            stringRow = stringRow.replace('[','')
            stringRow = stringRow.replace(']','')
            stringRow = stringRow.replace("'","")
            obj1.writeFile('some.txt',stringRow+'?')
            obj1.writeFile('some.txt', '\n')
            i = i + 2

    def writeFile(self,nameFile,write):
        try:
            my_file = open(nameFile,'a')
        except FileNotFoundError:
           print('Ошибка файл не найден')
        try:
            my_file.write(write)
        except IOError:
            print('Ошибка записи в файл')

    def writeOtherInf(self,nameFileExcel):
        try:
            rb = xlrd.open_workbook(nameFileExcel)
        except FileNotFoundError:
            print('Ошибка файл не найден')
        sheet = rb.sheet_by_index(0)
        obj1.writeFile('some.txt', '\n')
        for rownum in range(sheet.nrows):
            row = sheet.row_values(rownum)
            stringRow = str(row)
            stringRow = stringRow.replace('[', '')
            stringRow = stringRow.replace(']', '')
            stringRow = stringRow.replace("'", "")
            if rownum!=0 and rownum !=1 and rownum !=2 and rownum!=23:
                obj1.writeFile('some.txt', stringRow)
                obj1.writeFile('some.txt', '\n')
                print(stringRow)

obj1 = readExcel()
obj1.writeInfromToFile()
obj1.writeExcelQuestions('1.xls')
obj1.writeOtherInf('1.xls')
