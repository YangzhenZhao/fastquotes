import abc
import concurrent.futures
from typing import Optional

import requests

from fastquotes.const import HEADERS, REQ_CODES_NUM_MAX
from fastquotes.utils import format_stock_code, format_stock_codes


class Quote(metaclass=abc.ABCMeta):
    def __init__(self):
        self._session = requests.session()

    @property
    @abc.abstractmethod
    def base_url(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def split_char(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def pclose_field_id(self) -> int:
        pass

    @abc.abstractmethod
    def parse_out_tick_dict(self, msg: str) -> Optional[dict]:
        pass

    def current_price(self, code: str) -> float:
        return float(self._detail_list(code)[3])

    def pre_close(self, code: str) -> float:
        return float(self._detail_list(code)[self.pclose_field_id])

    def tick(self, code: str) -> Optional[dict]:
        code = format_stock_code(code)
        tick_dict = self.tick_dict([code])
        tick_list = list(tick_dict.items())
        if not tick_list or not tick_list[0][1]:
            return None
        return tick_list[0][1]

    def price_dict(self, codes: list) -> dict:
        tick_dict = self.tick_dict(codes)
        res_dict = {}
        for code, tick in tick_dict.items():
            if "current_price" in tick:
                res_dict[code] = tick["current_price"]
        return res_dict

    def pre_close_dict(self, codes: list) -> dict:
        tick_dict = self.tick_dict(codes)
        res_dict = {}
        for code, tick in tick_dict.items():
            if "pre_close" in tick:
                res_dict[code] = tick["pre_close"]
        return res_dict

    def open_dict(self, codes: list) -> dict:
        tick_dict = self.tick_dict(codes)
        res_dict = {}
        for code, tick in tick_dict.items():
            if "open" in tick:
                res_dict[code] = tick["open"]
        return res_dict

    def total_vol_dict(self, codes: list) -> dict:
        tick_dict = self.tick_dict(codes)
        res_dict = {}
        for code, tick in tick_dict.items():
            if "total_vol" in tick:
                res_dict[code] = tick["total_vol"]
        return res_dict

    def tick_dict(self, codes: list) -> dict:
        format_codes = format_stock_codes(codes)
        res = {}

        def small_price_dict(small_codes: list):
            data_str = self._fetch_codes_data_str(small_codes)
            data_list = data_str.strip().split("\n")
            for item in data_list:
                tick_dict = self.parse_out_tick_dict(item)
                if tick_dict is None:
                    return
                res[tick_dict["code"]] = tick_dict

        codes_len = len(format_codes)
        workers = codes_len // REQ_CODES_NUM_MAX + codes_len % REQ_CODES_NUM_MAX
        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
            for i in range(0, codes_len, REQ_CODES_NUM_MAX):
                if i + REQ_CODES_NUM_MAX >= codes_len:
                    small_codes = format_codes[i:]
                else:
                    small_codes = format_codes[i : i + REQ_CODES_NUM_MAX]
                executor.submit(small_price_dict, small_codes)
        return res

    def _detail_list(self, code: str) -> list:
        format_code = format_stock_code(code)
        return self._fetch_data_str(format_code).split(self.split_char)

    def _fetch_data_str(self, code: str) -> str:
        response = self._session.get(self.base_url + code, headers=HEADERS)
        return response.text

    def _fetch_codes_data_str(self, codes: list) -> str:
        codes_str = ",".join(codes)
        response = self._session.get(self.base_url + codes_str, headers=HEADERS)
        return response.text
