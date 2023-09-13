class Node2:
    __left: None
    __right: None
    __value: None

    def __init__(self, value):
        self.__left = None
        self.__right = None
        self.__value = value

    # getter

    @property
    def value(self):
        return self.__value

    # setter
    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        self.__left = left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        self.__right = right
