from abc import ABC, abstractmethod


class BrokerBase(ABC):

    @abstractmethod
    def get_orders(self) -> list:
        ...

    @abstractmethod
    def get_positions(self) -> list:
        ...