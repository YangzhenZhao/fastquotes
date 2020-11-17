import requests
import concurrent.futures

from fastquotes.const import HEADERS, TENCENT_BASE_URL, REQ_CODES_NUM_MAX

from . import quote
from fastquotes.utils import parse_out_tencent_tick_dict


class TencentQuote(quote.Quote):
    def __init__(self) -> None:
        self._session = requests.session()

    def price(self, code: str) -> float:
        detail_list = self._fetch_data_str(code).split("~")
        return float(detail_list[3])

    def tick_dict(self, codes: list) -> dict:
        res = {}
        def small_price_dict(codes: list):
            data_str = self._fetch_codes_data_str(codes)
            data_list = data_str.strip().split("\n")
            for item in data_list:
                tick_dict = parse_out_tencent_tick_dict(item)
                if tick_dict is None:
                    return
                res[tick_dict["code"]] = tick_dict
        codes_len = len(codes)
        workers = codes_len // REQ_CODES_NUM_MAX + codes_len % REQ_CODES_NUM_MAX
        with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
            for i in range(0, codes_len, REQ_CODES_NUM_MAX):
                if i + REQ_CODES_NUM_MAX >= codes_len:
                    small_codes = codes[i:]
                else:
                    small_codes = codes[i : i + REQ_CODES_NUM_MAX]
                executor.submit(small_price_dict, small_codes)
        return res

    def _fetch_data_str(self, code) -> str:
        response = self._session.get(f"{TENCENT_BASE_URL}{code}", headers=HEADERS)
        return response.text

    def _fetch_codes_data_str(self, codes: list) -> str:
        codes_str = ",".join(codes)
        response = self._session.get(f"{TENCENT_BASE_URL}{codes_str}", headers=HEADERS)
        return response.text
