# 概览

使用 fastquotes 快速获取基本的行情数据，支持异步    

## 安装

`pip install fastquotes`   


安装最新版本:   
假设最新版本为`0.0.2`, 则执行`pip install fastquotes==0.0.2`     


## 示例

```py
In [1]: import fastquotes

In [2]: q = fastquotes.SinaQuote()

In [3]: q.price("sz000001")
Out[3]: 17.18
```
