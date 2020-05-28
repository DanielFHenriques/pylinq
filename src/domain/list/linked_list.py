from src.domain.list.list import List
from src.domain.shared.node import Node


class LinkedList(List):

    def __init__(self):
        self.__head: 'Node' or None = None
        self.__tail: 'Node' or None = None
        self.__current_items = 0

    def get(self, idx: int) -> object:
        current_idx = 0
        current = self.__head

        while current_idx < idx and current is not None:
            current = current.next_node

        return current.element if current is not None else None

    def set(self, idx: int, value: object) -> object:
        if self.is_empty():
            return None

        current_idx = 0
        current = self.__head

        while current_idx < idx and current is not None:
            current = current.next_node

        if current is None:
            return None

        old_value = current.element

        current.element = value

        return old_value

    def is_empty(self) -> bool:
        return self.__current_items == 0

    def add(self, element: object) -> bool:
        new_node = Node(element, None)

        if self.is_empty():
            self.__head = new_node
            self.__tail = new_node
            self.__current_items += 1

            return True

        self.add_last(element)

        return True

    def remove(self, element: object) -> bool:
        if self.is_empty():
            return False

        previous = None
        current = self.__head

        while current is not None and current.element != element:
            previous = current
            current = current.next_node

        if current is None:
            return False

        if self.__current_items == 1:
            self.clear()
            return True

        previous.next_node = current.next_node
        self.__current_items -= 1

    def clear(self):
        self.__head = None
        self.__tail = None
        self.__current_items = 0

    def to_array(self) -> list:
        return [node.element for node in self]

    def add_last(self, element: object):
        new_node = Node(element, None)

        self.__tail.next_node = new_node
        self.__tail = new_node
        self.__current_items += 1

    def add_first(self, element: object):
        new_node = Node(element, self.__head)

        self.__head = new_node
        self.__current_items += 1

    def get_first(self):
        return self.get(0)

    def get_last(self):
        return self.get(len(self) - 1)

    def remove_first(self):
        old_head = self.__head
        self.__head = self.__head.next_node

        return old_head.element

    def remove_last(self):
        new_tail = self.__head
        idx = 0

        while idx < self.__current_items - 1:
            new_tail = new_tail.next_node

        new_tail.next_node = None
        self.__tail = new_tail

    def __iter__(self):
        current = self.__head

        while current is not None:
            yield current
            current = current.next_node

    def __len__(self) -> int:
        return self.__current_items
