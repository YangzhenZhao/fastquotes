from typing import Optional

from fastquotes.const import SINA_BASE_URL
from fastquotes.utils import parse_out_sina_tick_dict

from . import quote


class SinaQuote(quote.Quote):
    @property
    def base_url(self) -> str:
        return SINA_BASE_URL

    def parse_out_tick_dict(self, msg: str) -> Optional[dict]:
        return parse_out_sina_tick_dict(msg)

    @property
    def split_char(self) -> str:
        return ","

    @property
    def pclose_field_id(self) -> int:
        return 2
