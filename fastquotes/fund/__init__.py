import json

import requests


def fund_list() -> list:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    }
    url = "http://fund.eastmoney.com/js/fundcode_search.js"
    res = requests.get(url, headers=headers)
    text_data = res.text
    res_list = json.loads(text_data.strip("var r = ")[:-1])
    for i, item in enumerate(res_list):
        res_list[i] = {"基金代码": item[0], "基金简称": item[2], "基金类型": item[3]}
    return res_list
