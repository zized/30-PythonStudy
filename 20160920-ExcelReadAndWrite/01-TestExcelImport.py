import xlrd

#import  xlwt3

'''
http://www.cnblogs.com/ArtsCrafts/p/xlrd.html
�ǳ���, ��Ҫ�õ� xlrd �ĸ����� open_workbook , wb.sheets(), s.nrows-(����),s.ncols -(����),  s.cell(row, col).value- (��ȡָ����λ����ֵ)��
'''

from openpyxl import workbook

from openpyxl import load_workbook
from blaze.expr.core import path


def showexcel(file ='test1.xlsx', colnameindex = 1):
    workbook =xlrd.open_workbook(file)
    
    sheets = workbook.sheet_names()
    print(sheets)
    table = workbook.sheet_by_name('testtab1')
    nrows = table.nrows
    colnames = table.row_values(colnameindex)
    list = []
    for rownum in range(1,nrows):
        row = table.row_values(rownum)
        print(type(row))
        if row:
            app = {}
            for i in range(len(colnames)):
                app[colnames[i]] = row[i]
            list.append(app)
    print(list)
    return list
    
showexcel()
    
    
    