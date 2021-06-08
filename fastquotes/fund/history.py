import json
from datetime import datetime
from typing import Optional

import requests

from ..const import CUSTOM_HEADER


def get_dividend(msg: str) -> Optional[float]:
    if not msg:
        return None
    left, right = 0, len(msg) - 1
    while not msg[left].isdigit() or not msg[right].isdigit():
        if not msg[left].isdigit():
            left += 1
        if not msg[right].isdigit():
            right -= 1
    return float(msg[left : right + 1])


def fund_history_data(fund_code: str) -> list:
    url = f"http://fund.eastmoney.com/pingzhongdata/{fund_code}.js"
    text = requests.get(url, headers=CUSTOM_HEADER).text
    text = text[
        text.find("Data_netWorthTrend") + 21 : text.find("Data_ACWorthTrend") - 15
    ]
    res_list = []
    dividend_sum = 0.0
    growth_rate_factor = 1.0
    for item in json.loads(text):
        dividend = get_dividend(item["unitMoney"])
        unit_nv = item["y"]
        if dividend is not None:
            dividend_sum += dividend
            growth_rate_factor *= (unit_nv + dividend) / unit_nv
        res_list.append(
            {
                "日期": datetime.fromtimestamp(item["x"] // 1000).strftime("%Y%m%d"),
                "单位净值": unit_nv,
                "累计净值": unit_nv + dividend_sum,
                "复权净值": unit_nv * growth_rate_factor,
                "日涨幅": item["equityReturn"],
                "分红送配": dividend,
            }
        )
    return res_list


def fund_history_profit_dict(fund_code: str) -> dict:
    fund_history_list = fund_history_data(fund_code)
    res_dic = {}
    for i in range(1, len(fund_history_list)):
        item = fund_history_list[i]
        last_item = fund_history_list[i - 1]
        res_dic[item["日期"]] = item["复权净值"] / last_item["复权净值"] - 1
    return res_dic
