# 工具方法

### 获取股票的交易所前缀

接口: `exchange_prefix`

```py
In [1]: import fastquotes
In [2]: fastquotes.exchange_prefix("000001")
Out[2]: 'sz'
```

### 计算某一天是星期几

```py
In [12]: from fastquotes.utils import get_day_of_week

In [13]: get_day_of_week(2021, 5, 16)
Out[13]: 0

In [14]: get_day_of_week(2021, 5, 17)
Out[14]: 1
```

