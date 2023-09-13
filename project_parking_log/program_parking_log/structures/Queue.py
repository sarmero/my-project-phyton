

from structures.Node import Node


class Queue:
    __head = None
    __end = None
    __size = None

    def __init__(self):
        self.__head = None
        self.__end = None
        self.__size = 0

    # inserta un elemento al final de la fila
    def push(self, value):
        # se crea el nuevo nodo (libre)
        aux = Node(value)

        # si es el primer nodo de la fila
        if self.__head == None:
            # la cabeceara enlaza al nuevo nodo
            self.__head = aux
            # el final enlaza al nuevo nodo
            self.__end = aux
        else:
            # el siguiente del final se enlaza al nuevo nodo
            self.__end.next = aux
            # el final se enlaza al nuevo nodo
            self.__end = aux

        self.__size += 1

    # sacar el primer elemento de la fila
    def pop(self):
        value = None

        # verificar que la cabecera enlace al nudo
        if self.__head != Node:
            # sacra el primer elemento
            aux = self.__head
            # obtener el valor del primer elemento
            value = aux.value
            # mover la cabecera al siguiente
            self.__head = self.__head.next

            # si se saca el ultimo elemento
            # cabecera y final en nulo
            if self.__head == None:
                self.__end = None

            self.__size -= 1

        return value

    # determinar si la fila esta vacía
    def empty(self):

        return True if self.__head == None else False

    def front(self):
        return self.__head

    def back(self):
        return self.__end

    def size(self):
        return self.__size
