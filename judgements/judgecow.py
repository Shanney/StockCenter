def judge_cow(record):
    # 企业现金流肖像
    # 经营活动现金流净额，投资活动现金流净额，筹资活动现金流净额
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
        net_tmp_value = record.subtotal_operate_cash_inflow \
                        - record.subtotal_invest_cash_outflow \
                        - record.subtotal_finance_cash_outflow + record.proceeds_from_sub_to_mino_s

        if net_tmp_value > 0:
            return True

    return False

