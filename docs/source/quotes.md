# 直接获取行情

### SinaQuote/TencentQuote

```py
import fastquotes

# quote = fastquotes.TencentQuote()
quote = fastquotes.SinaQuote()
codes = fastquotes.exchange_stock_list()

tick_dict = quote.tick_dict(codes)
print(len(tick_dict))
print(tick_dict["000001"])
```

输出结果:

```
4072
{'time': '150003', 'name': '平安银行', 'code': '000001', 'current_price': 17.83, 'pre_close': 17.37, 'open': 17.38, 'high': 17.93, 'low': 17.25, 'total_amount': 1509511577.97, 'total_vol': 85293051.0, 'bid1_vol': 2100, 'bid1': 17.82, 'bid2_vol': 18900, 'bid2': 17.81, 'bid3_vol': 1400, 'bid3': 17.8, 'bid4_vol': 38000, 'bid4': 17.79, 'bid5_vol': 130900, 'bid5': 17.78, 'ask1_vol': 11153, 'ask1': 17.83, 'ask2_vol': 146800, 'ask2': 17.84, 'ask3_vol': 1400, 'ask3': 17.85, 'ask4_vol': 38000, 'ask4': 17.86, 'ask5_vol': 80400, 'ask5': 17.87}
```
