# 直接获取行情

## SinaQuote/TencentQuote

### 直接获取股票的当前价格

```py
import fastquotes

quote = fastquotes.TencentQuote()
# quote = fastquotes.SinaQuote()
print(quote.current_price('000001'))
print(quote.current_price('sh000905'))
```

输出结果:

```
18.46
6341.01
```

### 直接获取股票的昨收

```py
import fastquotes

# quote = fastquotes.TencentQuote()
quote = fastquotes.SinaQuote()
print(quote.pre_close('000001'))
print(quote.pre_close('sh000905'))

```

输出结果:

```
17.83
6336.9406
```


### 获取多支股票的 tick 数据

```py
import fastquotes

# quote = fastquotes.TencentQuote()
quote = fastquotes.SinaQuote()
codes = fastquotes.stock_list()

tick_dict = quote.tick_dict(codes)
print(len(tick_dict))
print(tick_dict["000001"])
```

输出结果:

```
4074
{'time': '150003', 'name': '平安银行', 'code': '000001', 'current_price': 18.46, 'pre_close': 17.83, 'open': 17.78, 'high': 18.5, 'low': 17.75, 'total_amount': 2508632642.49, 'total_vol': 137340072.0, 'bid1_vol': 125782, 'bid1': 18.45, 'bid2_vol': 42000, 'bid2': 18.44, 'bid3_vol': 15240, 'bid3': 18.43, 'bid4_vol': 31100, 'bid4': 18.42, 'bid5_vol': 21200, 'bid5': 18.41, 'ask1_vol': 404680, 'ask1': 18.46, 'ask2_vol': 285665, 'ask2': 18.47, 'ask3_vol': 15240, 'ask3': 18.48, 'ask4_vol': 31100, 'ask4': 18.49, 'ask5_vol': 2538805, 'ask5': 18.5}
```
