from jqdatasdk import *
import datetime
import xlwt
from excelutils import header
from selectstock.selections import analyze_enterprise
import os


def generate_stock_info(industry_code, concept_flag):
    """
    生成行业股票筛选后的excel表格
    :param industry_code: 行业代码, conecpt_flag: 是否概念行业
    :return:
    """
    book = xlwt.Workbook()
    sheet = book.add_sheet('stocks')
    header.init_excel_head(sheet)
    # C15 酒、饮料和精制茶制造业
    # C27 药
    if concept_flag:
        drink_list = get_concept_stocks(industry_code)
    else:
        drink_list = get_industry_stocks(industry_code)
    i = 1
    for code in drink_list:
        security_info = get_security_info(code)
        if security_info.start_date <= datetime.date.fromisoformat('2015-01-01') and \
                security_info.end_date == datetime.date.fromisoformat('2200-01-01'):
            print(security_info.display_name + '   ' + security_info.code)
            analyze_enterprise(security_info, sheet, i)
            i += 1
    # book.save(r"D:\stock_" + industry_code + ".xls")
    directory = r'C:\workingFolder\stocks'
    if not os.path.exists(directory):
        os.makedirs(directory)

    book.save(r"C:\workingFolder\stocks\stock_" + industry_code + ".xls")
