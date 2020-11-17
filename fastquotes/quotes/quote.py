import abc
from abc import abstractmethod


class Quote(metaclass=abc.ABCMeta):
    @abstractmethod
    def price(self, code: str) -> float:
        pass

    @abstractmethod
    def tick_dict(self, codes: list) -> dict:
        pass
