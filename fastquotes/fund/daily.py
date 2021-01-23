import demjson
import requests


def fund_real_time_dict() -> dict:
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            " (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
        )
    }
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
    res = requests.get(url, params=params, headers=headers)
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
