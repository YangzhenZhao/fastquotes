import asyncio

import aiohttp

from . import async_quote
from .const import HEADERS, REQ_CODES_NUM_MAX, SINA_BASE_URL


class AsyncSinaQuote(async_quote.AsyncQuote):
    def __init__(self) -> None:
        pass

    async def price_dict(self, codes: list) -> dict:
        res = {}
        tasks = []
        session = aiohttp.ClientSession()

        async def fetch_data_str(codes: str) -> str:
            codes_str = ",".join(codes)
            response = await session.get(f"{SINA_BASE_URL}{codes_str}", headers=HEADERS)
            data_str = await response.text()
            response.close()
            return data_str

        async def small_price_dict(codes: list):
            data_str = await fetch_data_str(codes)
            data_list = data_str.strip().split("\n")
            for item in data_list:
                s = item.split(",")
                code, price = s[0].partition("=")[0][-6:], float(s[3])
                res[code] = price

        codes_len = len(codes)
        for i in range(0, codes_len, REQ_CODES_NUM_MAX):
            if i + REQ_CODES_NUM_MAX >= codes_len:
                small_codes = codes[i:]
            else:
                small_codes = codes[i : i + REQ_CODES_NUM_MAX]
            tasks.append(small_price_dict(small_codes))
        await asyncio.wait(tasks)
        await session.close()
        return res
