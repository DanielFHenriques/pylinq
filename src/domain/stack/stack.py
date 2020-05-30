from src.domain.list.singly_linked_list import SinglyLinkedList


class Stack:

    def __init__(self):
        self.__stack = SinglyLinkedList()

    def push(self, element: object):
        self.__stack.add_first(element)

    def pop(self):
        self.__stack.remove_first()

    def top(self) -> object:
        return self.__stack.get(0)

    def top_and_pop(self) -> object:
        return self.__stack.remove_first()

    def is_empty(self) -> bool:
        return self.__stack.is_empty()

    def make_empty(self):
        self.__stack = SinglyLinkedList()

    def __len__(self):
        return len(self.__stack)
