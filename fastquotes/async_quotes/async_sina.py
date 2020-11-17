import asyncio

import aiohttp

from fastquotes.const import HEADERS, REQ_CODES_NUM_MAX, SINA_BASE_URL
from fastquotes.utils import parse_out_sina_tick_dict

from . import async_quote


class AsyncSinaQuote(async_quote.AsyncQuote):
    def __init__(self) -> None:
        pass

    async def tick_dict(self, codes: list) -> dict:
        res = {}
        tasks = []

        async with aiohttp.ClientSession() as session:

            async def small_price_dict(codes: list):
                data_str = await self._fetch_data_str(session, codes)
                data_list = data_str.strip().split("\n")
                for item in data_list:
                    tick_dict = parse_out_sina_tick_dict(item)
                    if tick_dict is None:
                        continue
                    res[tick_dict["code"]] = tick_dict

            codes_len = len(codes)
            for i in range(0, codes_len, REQ_CODES_NUM_MAX):
                if i + REQ_CODES_NUM_MAX >= codes_len:
                    small_codes = codes[i:]
                else:
                    small_codes = codes[i : i + REQ_CODES_NUM_MAX]
                tasks.append(small_price_dict(small_codes))
            await asyncio.wait(tasks)

        return res

    async def price_dict(self, codes: list) -> dict:
        res = {}
        tasks = []

        async with aiohttp.ClientSession() as session:

            async def small_price_dict(codes: list):
                data_str = await self._fetch_data_str(session, codes)
                data_list = data_str.strip().split("\n")
                for item in data_list:
                    s = item.split(",")
                    try:
                        code, price = s[0].partition("=")[0][-6:], float(s[3])
                    except IndexError:
                        continue
                    res[code] = price

            codes_len = len(codes)
            for i in range(0, codes_len, REQ_CODES_NUM_MAX):
                if i + REQ_CODES_NUM_MAX >= codes_len:
                    small_codes = codes[i:]
                else:
                    small_codes = codes[i : i + REQ_CODES_NUM_MAX]
                tasks.append(small_price_dict(small_codes))
            await asyncio.wait(tasks)

        return res

    async def _fetch_data_str(self, session, codes: list) -> str:
        codes_str = ",".join(codes)
        async with session.get(
            f"{SINA_BASE_URL}{codes_str}", headers=HEADERS
        ) as response:
            return await response.text()
