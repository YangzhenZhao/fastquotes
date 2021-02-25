# 数字货币

### 从coinmarketcap获取比特币历史某天收盘价

```py
In [1]: from fastquotes import coin

In [2]: coin.get_btc_pclose_by_date(2021, 2, 22)
Out[2]: 54207.31906543
```

### 从coinmarketcap获取比特币最近价格

```py
In [1]: from fastquotes import coin

In [2]: coin.get_btc_latest_price()
Out[2]: 49845.46501508884
```
