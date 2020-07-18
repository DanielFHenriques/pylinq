from typing import TYPE_CHECKING, Any

from src.domain.iterator.iterator import Iterator

if TYPE_CHECKING:
    from src.domain.list.singly_linked_list import SinglyLinkedList


class SinglyLinkedListIterator(Iterator):

    def __init__(self, linked_list: 'SinglyLinkedList'):
        self.__current_index = 0
        self.__linked_list = linked_list

    def has_next(self) -> bool:
        return self.__current_index < len(self.__linked_list)

    def next(self) -> 'Any':
        result = self.__linked_list[self.__current_index]
        self.__current_index += 1

        return result
