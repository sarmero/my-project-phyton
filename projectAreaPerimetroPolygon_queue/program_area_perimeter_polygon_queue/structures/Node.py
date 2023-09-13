

from multiprocessing import Value


class Node:

    _value: None
    _next: None

    def __init__(self, value):
        self._value = value
        self._next = Node

    @property
    def value(self):
        return self._value

    @Value.setter
    def value(self, value):
        self._value = value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next):
        self._next = next
