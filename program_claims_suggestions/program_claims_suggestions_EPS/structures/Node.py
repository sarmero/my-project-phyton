

from multiprocessing import Value


class Node:

    __value: None
    __next: None

    def __init__(self, value):
        self.__value = value
        self.__next = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, next):
        self.__next = next
