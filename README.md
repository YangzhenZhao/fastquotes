[![PyPI](https://img.shields.io/pypi/v/fastquotes.svg)](https://pypi.org/project/fastquotes/)  [![Documentation Status](https://readthedocs.org/projects/fastquotes/badge/?version=latest)](https://fastquotes.readthedocs.io/zh/latest/?badge=latest)

### FastQuotes

通过多线程或者异步的方法来获取行情

<a href="https://fastquotes.readthedocs.io/zh/latest/" target="_blank">中文文档</a>

**注意**:   
获取股票列表的接口容易**被封 IP**，请提前做好应对措施!!

### Installation

直接安装: `pip install quotes`       
安装最新版本(推荐): `pip install quotes==最新版本`

卸载: `pip uninstall fastquotes -y`

### Examples

```py
import fastquotes

# quote = fastquotes.TencentQuote()
quote = fastquotes.SinaQuote()
codes = fastquotes.stock_list()

tick_dict = quote.tick_dict(codes)
print(len(tick_dict))
print(tick_dict["000001"])
```

Output:

```
4074
{'time': '150003', 'name': '平安银行', 'code': '000001', 'current_price': 18.46, 'pre_close': 17.83, 'open': 17.78, 'high': 18.5, 'low': 17.75, 'total_amount': 2508632642.49, 'total_vol': 137340072.0, 'bid1_vol': 125782, 'bid1': 18.45, 'bid2_vol': 42000, 'bid2': 18.44, 'bid3_vol': 15240, 'bid3': 18.43, 'bid4_vol': 31100, 'bid4': 18.42, 'bid5_vol': 21200, 'bid5': 18.41, 'ask1_vol': 404680, 'ask1': 18.46, 'ask2_vol': 285665, 'ask2': 18.47, 'ask3_vol': 15240, 'ask3': 18.48, 'ask4_vol': 31100, 'ask4': 18.49, 'ask5_vol': 2538805, 'ask5': 18.5}
```

### Requirements

Python 3.6+

### References

- <a href="https://github.com/jindaxiang/akshare" target="_blank">https://github.com/jindaxiang/akshare</a>   
- <a href="https://github.com/shidenggui/easyquotation" target="_blank">https://github.com/shidenggui/easyquotation</a>   
