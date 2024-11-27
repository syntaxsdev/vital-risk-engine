from abc import ABC, abstractmethod
from typing import TypeVar

T = TypeVar("T")

class BrokerBase(ABC):

    @abstractmethod
    def get_orders(self) -> list:
        ...

    @abstractmethod
    def get_positions(self) -> list:
        ...