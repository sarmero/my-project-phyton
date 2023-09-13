

from structures.Node import Node


class Stack:
    __top = None
    __base = None
    __size = None

    def __init__(self):
        self.__top = None
        self.__base = None
        self.__size = 0

    # inserta un elemento al final de la fila
    def push(self, value):
        # se crea el nuevo nodo (libre)
        aux = Node(value)

        # si es el primer nodo de la fila
        if self.__top == None:
            # la cabeceara enlaza al nuevo nodo
            self.__top = aux
            # el final enlaza al nuevo nodo
            self.__base = aux
        else:
            # el siguiente del final se enlaza al nuevo nodo
            aux.next = self.__top
            # el final se enlaza al nuevo nodo
            self.__top = aux

        self.__size += 1

    # sacar el primer elemento de la fila
    def pop(self):
        value = None

        # verificar que la cabecera enlace al nudo
        if self.__top != Node:
            # sacra el primer elemento
            aux = self.__top
            # obtener el valor del primer elemento
            value = aux.value
            # mover la cabecera al siguiente
            self.__top = self.__top.next

            # si se saca el ultimo elemento
            # cabecera y final en nulo
            if self.__top == None:
                self.__base = None

            self.__size -= 1

        return value

    # determinar si la fila esta vacía
    def empty(self):

        return True if self.__top == None else False

    def front(self):
        return self.__top

    def back(self):
        return self.__base

    def size(self):
        return self.__size
