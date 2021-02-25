import json
from datetime import datetime, timedelta

import requests

from ..const import CUSTOM_HEADER


def get_btc_pclose_by_date(year: int, month: int, day: int) -> float:
    """
    从coinmarketcap获取比特币历史某天收盘价
    """
    end = datetime(year, month, day, 8, 0)
    begin = end - timedelta(1)
    begin_timestamp = int(begin.timestamp())
    end_timestamp = int(end.timestamp())
    text = requests.get(
        f"https://web-api.coinmarketcap.com/v1/cryptocurrency/ohlcv/historical"
        f"?id=1&convert=USD&time_start={begin_timestamp}&time_end={end_timestamp}",
        headers=CUSTOM_HEADER,
    ).text
    return json.loads(text)["data"]["quotes"][0]["quote"]["USD"]["close"]


def get_btc_latest_price() -> float:
    """
    从coinmarketcap获取比特币最近价格
    """
    url = "https://web-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"
    parameters = {
        "start": "1",
        "limit": "1",
        "convert": "USD",
    }
    text = requests.get(url, headers=CUSTOM_HEADER, params=parameters).text
    return json.loads(text)["data"][0]["quote"]["USD"]["price"]
