def consecutive_five_year_roe(indicators):
    # 返回连续五年ROE
    roe_positive_flag = True
    roe = []
    for indicator in indicators:
        print(indicator.loc[0].statDate+'    ' + str(indicator.loc[0].roe))
        roe.append(indicator.loc[0].roe)
        if indicator.loc[0].roe <= 0:
            roe_positive_flag = False
            break
    return roe_positive_flag


def ent_mode(income, cash_flow, balance):
    """
     roe可以看成是三个部分乘积组成
     1.产品净利润率（净利润/销售收入）
     2.总资产周转率（销售收入/平均总资产）
     3.杠杆系数（平均总资产/净资产）
    :param income: 利润表
    :return:
    """
    ind_one = income.loc[0].net_profit / cash_flow.loc[0].goods_sale_and_service_render_cash
    ind_two = cash_flow.loc[0].goods_sale_and_service_render_cash


