class Node:

    def __init__(self,
                 element: object,
                 next_node: 'Node' or None):
        self.__element = element
        self.__next_node = next_node

    @property
    def element(self) -> object:
        return self.__element

    @element.setter
    def element(self, value: object):
        self.__element = value

    @property
    def next_node(self) -> 'Node':
        return self.__next_node

    @next_node.setter
    def next_node(self, value: 'Node'):
        self.__next_node = value
