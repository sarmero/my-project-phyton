
from structures.Node import Node


class Stack:
    __top = None
    __base = None
    __size = 0

    def __init__(self):
        self.__top = None
        self.__base = None
        self.__size = 0

    # inserta un elemento al final de la fila
    def push(self, value):
        # se crea el nuevo nodo(libre)
        aux = Node(value)

        # si es el primer nodo en la fila
        if self.__top == None:
            # la cabecera enlaza a ese nodo
            self.__top = aux
            # la final enlaza a ese nodo
            self.__base = aux
        else:
            # el siguiente del final enlaza al nuevo nodo
            aux.next = self.__top
            # el final enlaza al nuevo nodo
            self.__top = aux

        self.__size += 1

    # sacar el primer elemento de la lista
    def pop(self):
        value = None

        if self.__top != None:
            # sacar el primer elemento
            aux = self.__top
            # obtener el valor del primer elemento
            value = aux.value
            # mover la cabecera al siguiente
            self.__top = self.__top.next

            if self.__top == None:
                self.__base = None

        self.__size -= 1

        return value

    def empty(self):
        return True if self.__top == None else False

    def front(self):
        return self.__top

    def back(self):
        return self.__base

    def size(self):
        return self.__size
