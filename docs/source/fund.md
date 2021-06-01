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

### 基金规模


```py
import fastquotes
print(fastquotes.fund.daily.fund_size("110011"))
```

输出结果:   

```
314.64
```

```py
import asyncio
from datetime import datetime

from fastquotes.fund.daily import fund_size_dict

from all_codes import all_codes


async def run():
    dic = await fund_size_dict(all_codes)
    return dic


print(datetime.now(), len(all_codes))
loop = asyncio.get_event_loop()
ans = loop.run_until_complete(run())
print(datetime.now(), len(ans), ans["110011"])
print(list(ans.items())[:10])
```

输出结果:  

```
2021-05-31 14:56:17.709765 5557
2021-05-31 14:56:36.597977 5350 314.64
[('008051', 0.12), ('519002', 18.69), ('008038', 0.3), ('900011', 5.45), ('900099', 130.05), ('160212', 12.2), ('000043', 9.41), ('008037', 0.48), ('007643', 14.31), ('900089', 49.98)]
```

因为是从网页爬取的，不是很稳定，可以使用如下方式或取尽可能多的信息:

```py
from fastquotes import fund

size_dict = {}
leave_codes = set(all_codes)
while True:
    print(len(leave_codes))
    size_dict_tmp = await fund.daily.fund_size_dict(list(leave_codes))
    if not size_dict_tmp:
        break
    for code, value in size_dict_tmp.items():
        size_dict[code] = value
        leave_codes.remove(code)
    await asyncio.sleep(5)
```

### 基金公司  


```py
from fastquotes import fund

company_dict = {}
leave_codes = set(all_codes)
while True:
    print(len(leave_codes))
    company_dict_tmp = await fund.daily.fund_company_dict(list(leave_codes))
    if not company_dict_tmp:
        break
    for code, value in company_dict_tmp.items():
        company_dict[code] = value
        leave_codes.remove(code)
    await asyncio.sleep(5)
```
