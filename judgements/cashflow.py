import numpy as np

def net_profit_into_account(cash_flow, income):
    # 经营活动产生的现金流量净额 > 净利润 > 0
    # 经营活动现金流净额/净利润的值
    # 用于确认净利润是否变成现金进入公司账户
    # 这个比值越大越好，持续大于1是优秀企业的重要特征
    # 房地产行业不适用与这个指标
    return np.nan_to_num(cash_flow.net_operate_cash_flow) / np.nan_to_num(income.net_profit)


def sale_income_situation(cash_flow, income):
    # 销售商品、提供劳务收到的现金与营业收入对比
    # 理想的数字是1.17，通常，只要比值大于1就问题不大
    return np.nan_to_num(cash_flow.goods_sale_and_service_render_cash) / np.nan_to_num(income.total_operating_revenue)
