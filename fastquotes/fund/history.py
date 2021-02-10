import json
from datetime import datetime

import requests

from ..const import CUSTOM_HEADER


def fund_history_data(fund_code: str) -> list:
    url = f"http://fund.eastmoney.com/pingzhongdata/{fund_code}.js"
    text = requests.get(url, headers=CUSTOM_HEADER).text
    text = text[
        text.find("Data_netWorthTrend") + 21 : text.find("Data_ACWorthTrend") - 15
    ]
    res_list = []
    for item in json.loads(text):
        res_list.append(
            {
                "日期": datetime.fromtimestamp(item["x"] // 1000).strftime("%Y-%m-%d"),
                "单位净值": item["y"],
                "日涨幅": item["equityReturn"],
            }
        )
    return res_list
