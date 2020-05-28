from src.domain.list.linked_list import LinkedList


class Stack:

    def __init__(self):
        self.__stack = LinkedList()

    def push(self, element: object):
        self.__stack.add_first(element)