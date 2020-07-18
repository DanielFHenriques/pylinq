from abc import ABC, abstractmethod

from src.domain.shared.node import Node


class Iterator(ABC):

    @abstractmethod
    def has_next(self) -> bool:
        pass

    @abstractmethod
    def next(self) -> 'Node':
        pass
