from abc import abstractmethod, ABC


class Collection(ABC):

    @abstractmethod
    def is_empty(self) -> bool:
        pass

    @abstractmethod
    def add(self, element: object) -> bool:
        pass

    @abstractmethod
    def remove(self, element: object) -> bool:
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def to_array(self) -> list:
        pass

    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def __len__(self) -> int:
        pass
