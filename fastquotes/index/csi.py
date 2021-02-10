import codecs
import json

import requests

from ..const import CUSTOM_HEADER


def latest_one_year_data(code: str) -> list:
    url = (
        f"http://www.csindex.com.cn/zh-CN/indices/index-detail/{code}?"
        "earnings_performance=1%E5%B9%B4&data_type=json"
    )
    text = requests.get(url, headers=CUSTOM_HEADER).text
    res_list = []
    text = codecs.decode(text.encode(), "utf-8-sig")

    for item in json.loads(text):
        res_list.append(
            {
                "date": item["tradedate"][:10],
                "close": item["tclose"],
            }
        )
    return res_list
