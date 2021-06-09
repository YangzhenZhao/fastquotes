from datetime import datetime

import requests


def stock_exit_right(date: str = None) -> list:
    """
    :param date: 每年的 12.31 或者 6.30, 例: 20201231, 20200630, 20191231, 20190630
    """
    if date is None:
        now = datetime.now()
        if (now.month, now.day) >= (6, 30):
            date = f"{now.year}0630"
        else:
            date = f"{now.year - 1}1231"
    params = {
        "st": "YAGGR",
        "sr": "-1",
        "ps": "5000",
        "p": "1",
        "type": "DCSOBS",
        "js": '{"data":(x),"pages":(tp)}',
        "token": "894050c76af8597a853f5b408b759f5d",
        "filter": f'(ReportingPeriod=^{"-".join([date[:4], date[4:6], date[6:]])}^)',
    }
    data_list = requests.get(_url, params=params).json()["data"]
    res_list = []
    for old_item in data_list:
        new_item = {}
        for new_key, old_key in _field_map.items():
            value = old_item[old_key]
            if new_key in _date_fields:
                value = _format_date(value)
            new_item[new_key] = value
        res_list.append(new_item)
    return res_list


_field_map = {
    "code": "Code",
    "name": "Name",
    "送转总比例": "SZZBL",
    "送股比例": "SGBL",
    "转股比例": "ZGBL",
    "现金分红比例": "XJFH",
    "股息率": "GXL",
    "预案公告日": "YAGGR",
    "股权登记日": "GQDJR",
    "除权除息日": "CQCXR",
    "总股本(元)": "TotalEquity",
    "每股收益(元)": "EarningsPerShare",
    "每股净资产(元)": "NetAssetsPerShare",
    "每股公积金(元)": "MGGJJ",
    "每股未分配利润(元)": "MGWFPLY",
    "净利润同比增长(%)": "JLYTBZZ",
    "分红配送报告期": "ReportingPeriod",
    "方案进度": "ProjectProgress",
    "配送方案": "AllocationPlan",
    "最新公告日期": "NOTICEDATE",
}
_date_fields = {"预案公告日", "股权登记日", "分红配送报告期", "除权除息日", "最新公告日期"}
_url = "http://dcfm.eastmoney.com/EM_MutiSvcExpandInterface/api/js/get"


def _format_date(date: str) -> str:
    return date[:10].replace("-", "")[:8]
