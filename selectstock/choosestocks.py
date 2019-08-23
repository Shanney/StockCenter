from jqdatasdk import *
from judgements.judgecow import *
from judgements.cashflow import *
from judgements.indicator import *

auth('13578992860', '1qaz2wsx')

# C15 酒、饮料和精制茶制造业
drink_list = get_industry_stocks('C15')
query_cash = query(cash_flow).filter(cash_flow.code == drink_list[0])
query_income = query(income).filter(income.code == drink_list[0])
query_indicator = query(indicator).filter(indicator.code == drink_list[0])
report_cash_flow = get_fundamentals(query_cash, statDate='2018')
report_income = get_fundamentals(query_income, statDate='2018')
indicators = [get_fundamentals(query_indicator, statDate=str(year)) for year in range(2014, 2019)]

# 计算了上面行业里的第一支股票，经营活动现金流净额/净利润的值
print(net_profit_into_account(report_cash_flow.loc[0], report_income.loc[0]))

# 销售商品、提供劳务收到的现金与营业收入对比
# 理想的数字是1.17，通常，只要比值大于1就问题不大
print(sale_income_situation(report_cash_flow.loc[0], report_income.loc[0]))

# 企业现金流肖像
# 经营活动现金流净额，投资活动现金流净额，筹资活动现金流净额
# cash_flow.net_operate_cash_flow,
#          cash_flow.net_invest_cash_flow,
#          cash_flow.net_finance_cash_flow
if judge_cow(report_cash_flow.loc[0]):
    print('奶牛型企业')

# 查询连续五年roe情况
consecutive_five_year_roe(indicators)

query_balance = query(balance).filter(balance.code == drink_list[0])
report_balance_two = [get_fundamentals(query_balance, statDate=str(year)) for year in range(2017, 2019)]

# 企业三个指标，查看企业模式，茅台模式，沃尔玛模式，银行模式
ent_mode(report_income.loc[0], report_cash_flow.loc[0], report_balance_two, indicators[4].loc[0])
