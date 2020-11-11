from datetime import datetime

from .utils import read_trade_days


class TradeCalendar:
    def __init__(self) -> None:
        self._trade_days = read_trade_days()
        self._trade_days_set = set(self._trade_days)
        self._trade_days_len = len(self._trade_days)
        self._pre_trade_date = {}
        for i in range(1, self._trade_days_len):
            self._pre_trade_date[self._trade_days[i]] = self._trade_days[i - 1]

    def is_trade_date(self, date=None) -> bool:
        return self._format_date(date) in self._trade_days_set

    def pre_trade_date(self, date=None) -> str:
        date = self._format_date(date)
        if date in self._pre_trade_date:
            return self._pre_trade_date[date]
        return None

    def _format_date(self, date) -> str:
        if date is None:
            return datetime.now().strftime("%Y%m%d")
        if isinstance(date, datetime):
            date = date.strftime("%Y%m%d")
        elif isinstance(date, int):
            date = str(date)
        return date
