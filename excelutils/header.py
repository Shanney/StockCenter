def init_excel_head(sheet1):
    sheet1.write(0, 0, '股票代码')
    sheet1.write(0, 1, '股票名称')
    sheet1.write(0, 2, '经营活动现金流净额/净利润的值')
    sheet1.write(0, 3, '销售商品、提供劳务收到的现金与营业收入对比')
    sheet1.write(0, 4, '企业现金流肖像')
    sheet1.write(0, 5, '连续五年roe情况')
    sheet1.write(0, 6, '产品利润率')
    sheet1.write(0, 7, '总资产周转率')
    sheet1.write(0, 8, '杠杆系数')