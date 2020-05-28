from abc import ABC, abstractmethod

from src.domain.shared.collection import Collection


class List(Collection, ABC):

    @abstractmethod
    def get(self, idx: int) -> object:
        pass

    @abstractmethod
    def set(self, idx: int, value: object) -> object:
        pass
