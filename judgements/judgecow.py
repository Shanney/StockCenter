import numpy as np


def judge_cow(record):
    """
    企业现金流肖像

    :param record:现金流量表数据
    :return:
    """

    # 经营活动现金流净额，投资活动现金流净额，筹资活动现金流净额
    result = {'cow_flag': False, 'health_flag': False}
    ent_type = ''
    if record.net_operate_cash_flow > 0:
        ent_type += '+'
    else:
        ent_type += '-'
    if record.net_invest_cash_flow > 0:
        ent_type += '+'
    else:
        ent_type += '-'
    if record.net_finance_cash_flow > 0:
        ent_type += '+'
    else:
        ent_type += '-'
    if ent_type == '+--':
        # ﻿经营现金流入要大于投资现金流出和筹资现金流出的总和
        # 经营现金流净值，减去投资活动、筹资活动的净流出（不包括分红），
        net_tmp_value = np.nan_to_num(record.net_operate_cash_flow) +\
                        np.nan_to_num(record.net_invest_cash_flow) +\
                        np.nan_to_num(record.net_finance_cash_flow) +\
                        np.nan_to_num(record.dividend_interest_payment)
        # 要看流出值是正还是负

        if net_tmp_value > 0:
            result['cow_flag'] = True
    elif ent_type == '++-':
        # 老母鸡型企业，成长已是过去式，只要售价不高（低市盈率），产蛋率不错（高股息率），则值得拥有
        # ﻿如果投资现金不是变卖家当所得，且经营现金流入和投资现金流入足以覆盖筹资现金流出，投资者可以初步认定这是一家健康发展的企业
        net_tmp_value = record.net_operate_cash_flow + record.net_invest_cash_flow \
            + record.net_finance_cash_flow
        if net_tmp_value > 0:
            result['health_flag'] = True

    result['ent_type'] = ent_type
    return result

