from abc import ABC, abstractmethod
from typing import Any

from src.domain.shared.collection import Collection


class List(Collection, ABC):

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def add(self, element: Any):
        pass

    @abstractmethod
    def remove(self, element: Any):
        pass

    @abstractmethod
    def __getitem__(self, item: int) -> Any:
        pass

    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __setitem__(self, key: int, value: Any):
        pass
