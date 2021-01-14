# tick字段说明

## 新浪

```py
{
    'time': '150003',
    'name': '平安银行',
    'code': '000001',
    'current_price': 17.83,         # 当前价格(单位:元)     类型:float
    'pre_close': 17.37,             # 昨收价格(单位:元)     类型:float
    'open': 17.38,                  # 今日开盘价格(单位:元)  类型:float
    'high': 17.93,                  # 最高价格(单位:元)     类型:float
    'low': 17.25,                   # 最低价格(单位:元)     类型:float
    'total_amount': 1509511577.97,  # 成交总金额(单位:元)   类型:float
    'total_vol': 85293051.0,        # 成交总量(单位:股)     类型:float
    'bid1_vol': 2100,               # 买一量(单位:股)       类型:int
    'bid1': 17.82,                  # 买一价格(单位:元)     类型:float
    'bid2_vol': 18900,        
    'bid2': 17.81, 
    'bid3_vol': 1400, 
    'bid3': 17.8, 
    'bid4_vol': 38000, 
    'bid4': 17.79, 
    'bid5_vol': 130900, 
    'bid5': 17.78, 
    'ask1_vol': 11153,             # 卖一量(单位:股)        类型:int
    'ask1': 17.83,                 # 卖一价格(单位:元)      类型:float
    'ask2_vol': 146800, 
    'ask2': 17.84, 
    'ask3_vol': 1400, 
    'ask3': 17.85, 
    'ask4_vol': 38000, 
    'ask4': 17.86, 
    'ask5_vol': 80400, 
    'ask5': 17.87
}
```

## 腾讯

```py
{
    'time': '161503', 
    'name': '平安银行', 
    'code': '000001', 
    'current_price': 20.03,        # 当前价格(单位:元)      类型:float
    'pre_close': 20.7,            # 昨收价格(单位:元)      类型:float
    'open': 17.38,                 # 今日开盘价格(单位:元)   类型:float
    'high': 20.89,                 # 最高价格(单位:元)      类型:float
    'low': 19.95,                  # 最低价格(单位:元)      类型:float
    'total_amount': 1509510000.0,  # 成交总金额(单位:元)    类型:float
    'total_vol': 85293100.0,       # 成交总量(单位:股)      类型:float
    'bid1': 17.82,                 # 买一价格(单位:元)      类型:float
    'bid1_vol': 2100,              # 买一量(单位:股)        类型:int
    'bid2': 17.81, 
    'bid2_vol': 18900, 
    'bid3': 17.8, 
    'bid3_vol': 1400, 
    'bid4': 17.79, 
    'bid4_vol': 38000, 
    'bid5': 17.78, 
    'bid5_vol': 130900, 
    'ask1': 17.83,                 # 卖一价格(单位:元)      类型:float
    'ask1_vol': 11200,             # 卖一量(单位:股)        类型:int
    'ask2': 17.84, 
    'ask2_vol': 146800, 
    'ask3': 17.85, 
    'ask3_vol': 250100, 
    'ask4': 17.86, 
    'ask4_vol': 57000, 
    'ask5': 17.87, 
    'ask5_vol': 80400
    'up_limit': 22.77,             # 涨停价(单位:元)        类型:float
    'down_limit': 18.63,           # 跌停价(单位:元)        类型:float
    'price_change': -0.67,         # 价格改变(单位:元)       类型:float
    'pct_change': -3.24,           # 涨跌幅(单位:%)         类型:float
    'flow_market_value': 3886.97,  # 流通市值(单位:亿元)     类型:float
    'total_market_value': 3887.01  # 总市值(单位:亿元)       类型:float
}
```
