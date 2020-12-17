import asyncio
import concurrent.futures
import json
from io import BytesIO

import aiohttp
import requests
import xlrd

from fastquotes.utils import exchange_prefix

url_sh = "http://query.sse.com.cn/security/stock/getStockListData.do"
headers_sh = {
    "Host": "query.sse.com.cn",
    "Pragma": "no-cache",
    "Referer": "http://www.sse.com.cn/assortment/stock/list/share/",
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        " (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
    ),
}
params_sh = {
    "jsonCallBack": "jsonpCallback66942",
    "isPagination": "true",
    "stockCode": "",
    "csrcCode": "",
    "areaName": "",
    "stockType": 1,  # 1表示主板A股,8表示科创板
    "pageHelp.cacheSize": "1",
    "pageHelp.beginPage": "1",
    "pageHelp.pageSize": "2000",
    "pageHelp.pageNo": "1",
    "pageHelp.endPage": "11",
    "_": "1589881387934",
}
url_sz = "http://www.szse.cn/api/report/ShowReport"
params_sz = {
    "SHOWTYPE": "xlsx",
    "CATALOGID": "1110",
    "TABKEY": "tab1",
    "random": "0.6935816432433362",
}


async def async_exchange_stock_list():
    res_list = await async_stock_list()
    return [f"{exchange_prefix(code)}{code}" for code in res_list]


async def async_stock_list():
    res_list = []
    async with aiohttp.ClientSession() as session:

        async def req_sh_list(stock_type):
            params_sh["stockType"] = stock_type
            async with session.get(
                url_sh, params=params_sh, headers=headers_sh
            ) as response:
                text = await response.text()
            loads_data = json.loads(text[text.find("{") : -1])
            res_list.extend([data["SECURITY_CODE_A"] for data in loads_data["result"]])

        async def req_sz_list():

            async with session.get(url_sz, params=params_sz) as r:
                sheet = xlrd.open_workbook(file_contents=(await r.read())).sheet_by_index(0)
                res_list.extend([c.value for c in sheet.col(4)[1:]])

        await asyncio.wait([req_sh_list(1), req_sh_list(8), req_sz_list()])

        return res_list


def exchange_stock_list() -> list:
    res_list = stock_list()
    return [f"{exchange_prefix(code)}{code}" for code in res_list]


def stock_list() -> list:
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        fut1 = executor.submit(stock_list_sz)
        fut2 = executor.submit(stock_list_sh)
    return fut1.result() + fut2.result()


def stock_list_sz() -> list:
    r = requests.get(url_sz, params=params_sz)
    sheet = xlrd.open_workbook(file_contents=r.content).sheet_by_index(0)
    return [c.value for c in sheet.col(4)[1:]]


def stock_list_sh() -> list:
    def req_list(stock_type):
        params_sh["stockType"] = stock_type
        response = requests.get(url_sh, params=params_sh, headers=headers_sh)
        text = response.text
        loads_data = json.loads(text[text.find("{") : -1])
        res_list = [data["SECURITY_CODE_A"] for data in loads_data["result"]]
        return res_list

    return req_list(1) + req_list(8)
