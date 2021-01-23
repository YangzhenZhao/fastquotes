# 基金

### 基金介绍

```py
import fastquotes

intro = fastquotes.fund_intro_dict()
print(intro["110011"])
```

输出结果:

```
{'基金代码': '110011', '基金简称': '易方达中小盘混合', '基金类型': '混合型'}
```

### 获取基金实时净值收益信息

```py
import fastquotes

ans_dic = fastquotes.fund_real_time_dict()
print(ans_dic["481010"])
```

输出结果:

```
{'code': '481010', 'name': '工银中小盘混合', 'update_date': '2021-01-22', 'pre_update_date': '2021-01-21', '单位净值': '3.9530', '累计净值': '3.9530', '上个交易日单位净值': '3.8910', '上个交易日累计净值': '3.8910', '日涨幅': '1.59', '手续费': '0.15%', '申购状态': '开放申购', '赎回状态': '开放赎回'}
```

### etf 列表

```py
import fastquotes

etf_l = fastquotes.etf_list()
print(len(etf_l), etf_l[:10])
```

输出结果:

```
383 ['sz159999', 'sz159998', 'sz159997', 'sz159996', 'sz159995', 'sz159994', 'sz159993', 'sz159992', 'sz159991', 'sz159990']
```
