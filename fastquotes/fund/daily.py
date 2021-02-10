from datetime import datetime
from typing import Optional

import demjson
import requests

from ..const import CUSTOM_HEADER
from ..trade_calendar import TradeCalendar


def fund_real_time_dict() -> dict:
    url = "http://fund.eastmoney.com/Data/Fund_JJJZ_Data.aspx"
    params = {
        "t": "1",
        "lx": "1",
        "letter": "",
        "gsid": "",
        "text": "",
        "sort": "zdf,desc",
        "page": "1,20000",
        "dt": "1580914040623",
        "atfc": "",
        "onlySale": "0",
    }
    res = requests.get(url, params=params, headers=CUSTOM_HEADER)
    text = res.text.strip("var db=")
    data_dict = demjson.decode(text)
    day, pre_day = data_dict["showday"]
    res_dic = {}
    for item in data_dict["datas"]:
        code = item[0]
        res_dic[code] = {
            "code": code,
            "name": item[1],
            "update_date": day,
            "pre_update_date": pre_day,
            "单位净值": item[3],
            "累计净值": item[4],
            "上个交易日单位净值": item[5],
            "上个交易日累计净值": item[6],
            "日涨幅": item[8],
            "手续费": item[17],
            "申购状态": item[9],
            "赎回状态": item[10],
        }
    return res_dic


def fund_latest_profit_dict(codes: list = None) -> Optional[dict]:
    real_time_dict = fund_real_time_dict()
    if codes is None:
        real_time_list = list(real_time_dict.items())
    else:
        real_time_list = [(code, real_time_dict[code]) for code in codes]
    calendar = TradeCalendar()
    is_trade_date = calendar.is_trade_date()
    today_str = datetime.now().strftime("%Y-%m-%d")
    profit_dict = {}
    for code, msg in real_time_list:
        if _is_valid_profit(msg, is_trade_date, today_str):
            profit: Optional[float] = float(msg["单位净值"]) / float(msg["上个交易日单位净值"]) - 1
        else:
            profit = None
        profit_dict[code] = profit
    return profit_dict


def _is_valid_profit(
    item: dict,
    is_trade_date: bool,
    today_str: str,
) -> bool:
    if item["单位净值"] == "":
        return False
    if is_trade_date and today_str != item["update_date"]:
        return False
    return True
