
from re import I
from xmlrpc.client import boolean
from structures.Node import Node


class List:

    __head = None
    __end = None
    __size = 0

    def __init__(self):
        self._head = None
        self.__end = None
        self.__size = 0

    def front(self):
        return self.__head

    def back(self):
        return self.__end

    def empty(self):
        return True if self.__head == None else False

    def size(self):
        return self.__size

        # adicionar un elemnto al inicio

    def push_front(self, value):
        # se crea el nuevo nodo (libre)
        aux = Node(value)
        if self.__head == None:
            self.__head = aux
            self.__end = aux
        else:
            aux.next = self.__head
            self.__head = aux
        self.__size += 1
        return

        # adicionar un elemnto al final

    def push_back(self, value):
        # se crea el nuevo nodo (libre)
        aux = Node(value)
        if self.__head == None:
            self.__head = aux
            self.__end = aux
        else:
            self.__end.next = aux
            self.__end = aux
        self.__size += 1
        return

        # quitar primer elemento

    def pop_front(self):
        value = None
        if (self.__head != None):
            aux = self.__head
            self.__head = self.__head.next
            value = aux.value
            aux.next = None
            if self.__head == None:
                self.__end = None
            self.__size -= 1
        return value

    def pop_back(self):
        # current es el actual
        # before es el anterior
        # Mientras actual(current) avanza y before es el anterior
        value = None
        if self.__end != None:
            current = self.__head
            before = None
            while current != self.back():
                before = current
                current = current.next

            before.next = None  # se elimina el enlace  anterior
            self.__end = before  # se actualiza el final
            self.__size -= 1

        return value

    # insertar elemento en una posicion
    def insert(self, index, value):
        flag = False
        if index >= 0 and index < self.__size:
            current = self.__head
            before = None
            i = 0
            while current != self.back() and i < index:
                before = current
                current = current.next
                i += 1

            if before is None:  # verificar inserción al inicio
                self.push_front(value)
            else:
                aux = Node(value)
                aux.next = before.next
                before.next = aux
                self.__size += 1
                flag = True
        return flag

    # actualizar elemento  en una posicion

    def update(self, index, new_value):
        flag = False
        if index <= 0 and index < self.__size:
            current = self.__head
            i = 0
            while current != self.back() and i < index:
                current = current.next
                i += 1

            current.value = new_value
            flag = True
        return flag

    # eliminar elemento  en una posicion

    def delete(self, index):
        flag = False
        if index >= 0 and index < self.__size:
            current = self.__head
            before = None
            i = 0
            while current != self.back() and i < index:
                before = current
                current = current.next
                i += 1

            if before is None:
                self.pop_front()
            else:
                before.next = current.next  # enlance
                self.__size += 1
            flag = True
        return flag

    # obtener el elemento de una posicion

    def get_value(self, index):
        value = None

        if index >= 0 and index < self.__size:
            aux = self.__head
            i = 0
            while aux != None:
                if i == index:
                    value = aux.value
                    break
                aux = aux.next
                i += 1

        return value

    # veriifcar si un valor existe en la lista

    def search_value(self, value):
        flag = False
        aux = self.__head
        while aux != None:
            if aux.value == value:
                flag = True
            aux = aux.next

        return flag

    # limpiar toda la lista

    def clear(self):
        self.__head = None
        self.__end = None
        self.__size = 0

    # obtener el nodo  a partir de una posicion
    def search_by_index(self, value):
        index = -1
        aux = self.__head
        i = 0
        while aux != None:
            if aux.value == value:
                index = I
                break
            aux = aux.next
            i += 1

        return index
