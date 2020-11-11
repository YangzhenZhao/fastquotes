import requests

from . import quote
from .const import HEADERS, SINA_BASE_URL


class SinaQuote(quote.Quote):
    def __init__(self) -> None:
        self._session = requests.session()

    def price(self, code: str) -> float:
        detail_list = self._fetch_data_str(code).split(",")
        return float(detail_list[3])

    def _fetch_data_str(self, code) -> str:
        response = self._session.get(f"{SINA_BASE_URL}{code}", headers=HEADERS)
        return response.text
