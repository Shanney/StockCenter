from jqdatasdk import *
import datetime
import xlwt
from excelutils import header
from selectstock.selections import analyze_enterprise

auth('13578992860', '1qaz2wsx')

book = xlwt.Workbook()
sheet = book.add_sheet('stocks')
header.init_excel_head(sheet)
# C15 酒、饮料和精制茶制造业
drink_list = get_industry_stocks('C15')
i = 1
for code in drink_list:
    security_info = get_security_info(code)
    if security_info.start_date <= datetime.date.fromisoformat('2015-01-01') and \
            security_info.end_date == datetime.date.fromisoformat('2200-01-01'):
        analyze_enterprise(security_info, sheet, i)
        i += 1
book.save(r"D:\stock.xls")


