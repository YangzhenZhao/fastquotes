import abc
import asyncio
from typing import Optional

import aiohttp

from fastquotes.const import HEADERS, REQ_CODES_NUM_MAX
from fastquotes.utils import format_stock_codes


class AsyncQuote(metaclass=abc.ABCMeta):
    def __init__(self) -> None:
        pass

    @property
    @abc.abstractmethod
    def base_url(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def split_char(self) -> str:
        pass

    @abc.abstractmethod
    def parse_out_tick_dict(self, msg: str) -> Optional[dict]:
        pass

    async def tick_dict(self, codes: list) -> dict:
        format_codes = format_stock_codes(codes)
        res = {}
        tasks = []

        async with aiohttp.ClientSession() as session:

            async def small_price_dict(small_codes: list):
                data_str = await self._fetch_data_str(session, small_codes)
                data_list = data_str.strip().split("\n")
                for item in data_list:
                    tick_dict = self.parse_out_tick_dict(item)
                    if tick_dict is None:
                        return
                    res[tick_dict["code"]] = tick_dict

            codes_len = len(format_codes)
            for i in range(0, codes_len, REQ_CODES_NUM_MAX):
                if i + REQ_CODES_NUM_MAX >= codes_len:
                    small_codes = format_codes[i:]
                else:
                    small_codes = format_codes[i : i + REQ_CODES_NUM_MAX]
                tasks.append(small_price_dict(small_codes))
            await asyncio.wait(tasks)
        return res

    async def price_dict(self, codes: list) -> dict:
        tick_dict = await self.tick_dict(codes)
        res_dict = {}
        for code, tick in tick_dict.items():
            if "current_price" in tick:
                res_dict[code] = tick["current_price"]
        return res_dict

    async def pre_close_dict(self, codes: list) -> dict:
        tick_dict = await self.tick_dict(codes)
        res_dict = {}
        for code, tick in tick_dict.items():
            if "pre_close" in tick:
                res_dict[code] = tick["pre_close"]
        return res_dict

    async def open_dict(self, codes: list) -> dict:
        tick_dict = await self.tick_dict(codes)
        res_dict = {}
        for code, tick in tick_dict.items():
            if "open" in tick:
                res_dict[code] = tick["open"]
        return res_dict

    async def total_vol_dict(self, codes: list) -> dict:
        tick_dict = await self.tick_dict(codes)
        res_dict = {}
        for code, tick in tick_dict.items():
            if "total_vol" in tick:
                res_dict[code] = tick["total_vol"]
        return res_dict

    async def _fetch_data_str(self, session, codes: list) -> str:
        codes_str = ",".join(codes)
        async with await session.get(
            f"{self.base_url}{codes_str}", headers=HEADERS
        ) as response:
            return await response.text()
