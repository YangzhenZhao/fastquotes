import json

import requests


def fund_intro_dict() -> dict:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    }
    url = "http://fund.eastmoney.com/js/fundcode_search.js"
    res = requests.get(url, headers=headers)
    text_data = res.text
    res_list = json.loads(text_data.strip("var r = ")[:-1])
    res_dict = {}
    for item in res_list:
        res_dict[item[0]] = {"基金代码": item[0], "基金简称": item[2], "基金类型": item[3]}
    return res_dict


def etf_list() -> list:
    url = (
        "http://vip.stock.finance.sina.com.cn/quotes_service/api"
        "/jsonp.php/IO.XSRV2.CallbackList['da_yPT46_Ll7K6WD']:"
        "/Market_Center.getHQNodeDataSimple"
    )
    params = {
        "page": "1",
        "num": "1000",
        "sort": "symbol",
        "asc": "0",
        "node": "etf_hq_fund",
        "[object HTMLDivElement]": "qvvne",
    }
    r = requests.get(url, params=params)
    data_text = r.text
    data_list = json.loads(data_text[data_text.find("([") + 1 : -2])
    return [item["symbol"] for item in data_list]
