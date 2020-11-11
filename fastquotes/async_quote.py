import abc
from abc import abstractmethod


class AsyncQuote(metaclass=abc.ABCMeta):
    @abstractmethod
    async def price_dict(self, codes: list) -> dict:
        pass
