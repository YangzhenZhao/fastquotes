# 交易日历

### 判断是否为交易日

```py
import fastquotes

calendar = fastquotes.TradeCalendar()
print(calendar.is_trade_date("20201115"))
print(calendar.is_trade_date("20201113"))
```

输出结果:

```
False
True
```



### 查询前一个交易日   

```py
import fastquotes

calendar = fastquotes.TradeCalendar()
print(calendar.pre_trade_date("20201115"))
print(calendar.pre_trade_date("19901214"))
```

输出结果:

```
20201113
None
```

### 查询下一个交易日

```py
import fastquotes

calendar = fastquotes.TradeCalendar()
print(calendar.next_trade_date("20201115"))
print(calendar.next_trade_date("19960301"))
```

输出结果:

```
20201116
19960304
```

### 交易日列表   


```py
import fastquotes

calendar = fastquotes.TradeCalendar()
l = calendar.trade_date_list()
print(len(l))
print(l[-5:])
```

输出结果:

```
7343
['20201225', '20201228', '20201229', '20201230', '20201231']
```
