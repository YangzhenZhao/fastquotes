# 股票列表

### A股所有股票列表

接口: `stock_list`

```py
import fastquotes

codes = fastquotes.stock_list()
print(len(codes))
print(codes[:10])
```

输出结果:

```
4072
['000001', '000002', '000004', '000005', '000006', '000007', '000008', '000009', '000010', '000011']
```

异步接口: `async_stock_list`

```py
import fastquotes
import asyncio

async def run():
    codes = await fastquotes.async_stock_list()
    print(len(codes))
    print(codes[:10])

loop = asyncio.get_event_loop()
loop.run_until_complete(run())
```

输出结果:

```
4072
['688001', '688002', '688003', '688004', '688005', '688006', '688007', '688008', '688009', '688010']
```

### 沪市股票列表

接口：`stock_list_sh`


```py
codes = fastquotes.stock_list_sh()
print(len(codes))
print(codes[:10])
```

输出结果:

```
1755
['600000', '600004', '600006', '600007', '600008', '600009', '600010', '600011', '600012', '600015']
```

### 深市股票列表

接口: `stock_list_sz`

```py
codes = fastquotes.stock_list_sz()
print(len(codes))
print(codes[:10])
```

输出结果:

```
2317
['000001', '000002', '000004', '000005', '000006', '000007', '000008', '000009', '000010', '000011']
```
