from typing import Any


class Node:

    def __init__(self,
                 element: Any,
                 next_node: 'Node' or None):
        self.__element = element
        self.__next_node = next_node

    @property
    def element(self) -> Any:
        return self.__element

    @element.setter
    def element(self, value: Any):
        self.__element = value

    @property
    def next_node(self) -> 'Node':
        return self.__next_node

    @next_node.setter
    def next_node(self, value: 'Node'):
        self.__next_node = value
