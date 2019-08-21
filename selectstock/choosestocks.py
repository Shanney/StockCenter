from jqdatasdk import *
import pandas as pd

auth('13578992860', '1qaz2wsx')

# C15 酒、饮料和精制茶制造业
# 计算了上面行业里的第一支股票，经营活动现金流净额/净利润的值
drink_list = get_industry_stocks('C15')
q = query(cash_flow.net_operate_cash_flow,
          income.net_profit).filter(
    income.code == drink_list[0],
    cash_flow.code == income.code
)
rets = get_fundamentals(q, statDate='2018')
print(rets)
print(rets.loc[0].net_operate_cash_flow / rets.loc[0].net_profit)

# 销售商品、提供劳务收到的现金与营业收入对比
# 理想的数字是1.17，通常，只要比值大于1就问题不大
q = query(cash_flow.goods_sale_and_service_render_cash,
          income.total_operating_revenue).filter(
    income.code == drink_list[0],
    cash_flow.code == income.code
)
rets = get_fundamentals(q, statDate='2018')
print(rets)
print(rets.loc[0].goods_sale_and_service_render_cash / rets.loc[0].total_operating_revenue)

# 企业现金流肖像
# 经营活动现金流净额，投资活动现金流净额，筹资活动现金流净额
q = query(cash_flow.net_operate_cash_flow,
          cash_flow.net_invest_cash_flow,
          cash_flow.net_finance_cash_flow
          ).filter(
    cash_flow.code == drink_list[0]
)
rets = get_fundamentals(q, statDate='2018')


def ent_cash_snapshot(net_operate_cash_flow, net_invest_cash_flow, net_finance_cash_flow):
    ret = ''
    if net_operate_cash_flow > 0:
        ret += '+'
    else:
        ret += '-'
    if net_invest_cash_flow > 0:
        ret += '+'
    else:
        ret += '-'
    if net_finance_cash_flow > 0:
        ret += '+'
    else:
        ret += '-'
    print(ret)


ent_cash_snapshot(rets.loc[0].net_operate_cash_flow,
                  rets.loc[0].net_invest_cash_flow,
                  rets.loc[0].net_finance_cash_flow)
