import requests

from fastquotes.const import HEADERS, TENCENT_BASE_URL

from . import quote


class TencentQuote(quote.Quote):
    def __init__(self) -> None:
        self._session = requests.session()

    def price(self, code: str) -> float:
        detail_list = self._fetch_data_str(code).split("~")
        return float(detail_list[3])

    async def tick_dict(self, codes: list) -> dict:
        pass

    def _fetch_data_str(self, code) -> str:
        response = self._session.get(f"{TENCENT_BASE_URL}{code}", headers=HEADERS)
        return response.text
