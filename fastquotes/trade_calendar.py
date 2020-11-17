from bisect import bisect_left
from datetime import datetime
from typing import Optional

from .utils import read_trade_days


class TradeCalendar:
    def __init__(self) -> None:
        self._trade_days: list = read_trade_days()
        self._trade_days_set: set = set(self._trade_days)
        self._trade_days_len: int = len(self._trade_days)

    def is_trade_date(self, date=None) -> bool:
        return self._format_date(date) in self._trade_days_set

    def trade_date_list(self) -> list:
        return self._trade_days

    def pre_trade_date(self, date=None) -> Optional[str]:
        date = self._format_date(date)
        idx = bisect_left(self._trade_days, date) - 1
        if idx == -1:
            return None
        return self._trade_days[idx]

    def _format_date(self, date) -> str:
        if date is None:
            return datetime.now().strftime("%Y%m%d")
        if isinstance(date, datetime):
            date = date.strftime("%Y%m%d")
        elif isinstance(date, int):
            date = str(date)
        return date
