# 概览

使用 fastquotes 快速获取基本的行情数据(多线程或者异步)

## 安装

`pip install fastquotes`     

安装最新版: `pip install fastquotes==最新版本号`

验证安装:

```py
In [1]: import fastquotes

In [2]: fastquotes.__version__
Out[2]: 'x.y.z'
```

## 示例

```py
In [1]: import fastquotes

In [2]: q = fastquotes.SinaQuote()

In [3]: q.price("sz000001")
Out[3]: 17.18
```
