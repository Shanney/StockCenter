from jqdatasdk import *
from judgements.judgecow import *
from judgements.cashflow import *
from judgements.indicator import *


def analyze_enterprise(security_info, sheet, rowIndex):
    '''
    根据传入的股票代码，查询相关的指标，2015-2019年
    :param rowIndex: 当前行号
    :param sheet: 操作excel对象
    :param code: 股票代码
    :return:
    '''
    query_cash = query(cash_flow).filter(cash_flow.code == security_info.code)
    query_income = query(income).filter(income.code == security_info.code)
    query_indicator = query(indicator).filter(indicator.code == security_info.code)
    report_cash_flow = get_fundamentals(query_cash, statDate='2018')
    report_income = get_fundamentals(query_income, statDate='2018')
    indicators = [get_fundamentals(query_indicator, statDate=str(year)) for year in range(2014, 2019)]

    sheet.write(rowIndex, 0, security_info.code)
    sheet.write(rowIndex, 1, security_info.display_name)

    # 计算了上面行业里的第一支股票，经营活动现金流净额/净利润的值
    sheet.write(rowIndex, 2, net_profit_into_account(report_cash_flow.loc[0], report_income.loc[0]))

    # 销售商品、提供劳务收到的现金与营业收入对比
    # 理想的数字是1.17，通常，只要比值大于1就问题不大
    sheet.write(rowIndex, 3, sale_income_situation(report_cash_flow.loc[0], report_income.loc[0]))

    # 企业现金流肖像
    # 经营活动现金流净额，投资活动现金流净额，筹资活动现金流净额
    # cash_flow.net_operate_cash_flow,
    #          cash_flow.net_invest_cash_flow,
    #          cash_flow.net_finance_cash_flow
    if judge_cow(report_cash_flow.loc[0]):
        sheet.write(rowIndex, 4, '奶牛型企业')

    # 查询连续五年roe情况
    if consecutive_five_year_roe(indicators):
        sheet.write(rowIndex, 5, '连续五年ROE大于15%')

    query_balance = query(balance).filter(balance.code == security_info.code)
    report_balance_two = [get_fundamentals(query_balance, statDate=str(year)) for year in range(2017, 2019)]

    # 企业三个指标，查看企业模式，茅台模式，沃尔玛模式，银行模式
    enterprise_mode = ent_mode(report_income.loc[0], report_cash_flow.loc[0], report_balance_two, indicators[4].loc[0])
    sheet.write(rowIndex, 6, enterprise_mode['ind_one'])
    sheet.write(rowIndex, 7, enterprise_mode['ind_two'])
    sheet.write(rowIndex, 8, enterprise_mode['ind_three'])