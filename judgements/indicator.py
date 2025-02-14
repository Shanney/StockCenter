import numpy as np

def consecutive_five_year_roe(indicators):
    # 返回连续五年ROE，应该只关注roe大于15%的企业
    result = {}
    roe_positive_flag = True
    consecutive_detail = ''
    for indicator in indicators:
        # print(indicator.loc[0].statDate + '    ' + str(indicator.loc[0].roe))
        if indicator.loc[0].roe < 15:
            roe_positive_flag = False
        consecutive_detail += str(indicator.loc[0].roe) + '   '
    result['roe_positive_flag'] = roe_positive_flag
    result['consecutive_detail'] = consecutive_detail
    return result


def ent_mode(income, cash_flow, balance_two, indicator):
    """
     roe可以看成是三个部分乘积组成
     1.产品净利润率（净利润/销售收入）
     2.总资产周转率（销售收入/平均总资产）
     3.杠杆系数（平均总资产/净资产）
     即查看企业模式，茅台模式，沃尔玛模式，银行模式
     但是净资产没法算啊。。。。如果用净利润/ROE呢？是平均净资产
    :param indicator: 财务指标表
    :param balance_two: 连续两年的资产负债表，为了使用期初和期末数据
    :param cash_flow: 现金流量表
    :param income: 利润表
    :return:
    """
    ind_one = np.nan_to_num(income.net_profit) / np.nan_to_num(cash_flow.goods_sale_and_service_render_cash)

    # 平均总资产=（期初+期末)/2
    ave_asset = (np.nan_to_num(balance_two[0].loc[0].total_sheet_owner_equities) + np.nan_to_num(
        balance_two[1].loc[0].total_sheet_owner_equities)) / 2
    ind_two = np.nan_to_num(cash_flow.goods_sale_and_service_render_cash) / np.nan_to_num(ave_asset)

    ave_net_asset = np.nan_to_num(income.net_profit) / np.nan_to_num(indicator.roe)
    ind_three = np.nan_to_num(ave_asset) / np.nan_to_num(ave_net_asset)

    return {'ind_one': str(ind_one), 'ind_two': str(ind_two), 'ind_three': str(ind_three)}
    # print('产品利润率：' + str(ind_one))
    # print('总资产周转率' + str(ind_two))
    # print('杠杆系数' + str(ind_three))
