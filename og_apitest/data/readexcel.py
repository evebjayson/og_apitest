import xlrd
import os

class ExcelUtil():
    def __init__(self,sheetname):
        self.data = xlrd.open_workbook(os.path.join(os.path.dirname(__file__) + "\\api_data.xlsx"))
        self.table = self.data.sheet_by_name(sheetname)
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.allrow = self.table.nrows
        # 获取总列数
        self.allcol = self.table.ncols

    def dict_data(self):
        if self.allrow <= 1:
            print("总行数小于1")
        else:
            r = []
            j=1
            for i in range(self.allrow-1):
                s = {}
                # 从第二行取对应values值
                values = self.table.row_values(j)
                for x in range(self.allcol):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j+=1
            return r



