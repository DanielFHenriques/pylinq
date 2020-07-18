from typing import Any

from src.domain.iterator.singly_linked_list_iterator import SinglyLinkedListIterator
from src.domain.list.list import List
from src.domain.shared.node import Node


class SinglyLinkedList(List):

    def __init__(self):
        self.__head: 'Node' or None = None
        self.__tail: 'Node' or None = None
        self.__current_items = 0

    def is_empty(self) -> bool:
        return self.__current_items == 0

    def add(self, element: Any):
        new_node = Node(element, None)

        if self.__head is None:
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.next_node = new_node
            self.__tail = new_node

        self.__current_items += 1

    def remove(self, element: Any) -> bool:
        if self.__head is None:
            return False

        current: 'Node' = self.__head

        if current.element == element:
            if self.__head == self.__tail:
                self.__head = None
                self.__tail = None
            else:
                self.__head = self.__head.next_node

        while current.next_node is not None and current.element != element:
            current = current.next_node

        if current.next_node is not None:
            if current.next_node == self.__tail:
                self.__tail = current

            current.next_node = current.next_node.next_node
            self.__current_items -= 1
            return True

        return False

    def __getitem__(self, item: int) -> Any:
        if item >= self.__current_items:
            raise ValueError(f"Cannot access index {item} of list with {self.__current_items} elements")

        index = 0
        current = self.__head

        while index < item:
            current = current.next_node
            index += 1

        return current.element

    def __iter__(self):
        iterator = SinglyLinkedListIterator(self)

        while iterator.has_next():
            yield iterator.next()

    def __len__(self):
        return self.__current_items

    def __setitem__(self, key: int, value: Any):
        node = self[key]
        node.element = value
