import xlrd

path = r'C:\Users\Utkarsh\Desktop\Leadzen_assignment\files\saucedemo_locators.xlsx'

workbook = xlrd.open_workbook(path)     ## book obj
worksheet = workbook.sheet_by_name('Sheet1')        ## sheet obj
rows_ = worksheet.get_rows()        ## generator object
header = next(rows_)


def demo_locators():
    d = {}
    for ele in rows_:
        d[ele[0].value] =  (ele[1].value, ele[2].value)

    return d






















