from structures.Node import Node


class Stack:
    __top = None
    __base = None
    __size = 0

    def __init__(self):
        self.__top = None
        self.__base = None
        self.__size = 0

    # Inserta un elemento a final de la fila
    def push(self, value):
        # Se crea el nuevo nodo(libre)
        aux = Node(value)

        # Si es el primer nodo en la fila
        if self.__top == None:
            # la cabecera enlaza a ese nodo
            self.__top = aux
            # El final enlaza a ese nodo
            self.__base = aux
        else:
            # El nuevo nodo enlaza a la cabecera actual
            aux.next = self.__top
            # El final se enlaza al nuevo nodo
            self.__top = aux
        self.__size += 1

    def pop(self):
        value = None

        if self.__size != None:
            # Sacar el primer elemento
            aux = self.__top
            # Obtener el valor del primer elemento
            value = aux.value
            # Mover la cabecera al siguiente
            self.__top = self.__top.next

            # Si se saca el ultimo elemento
            # cabecera y final en nulo
            if self.__top == None:
                self.__base = None

            self.__size -= 1

        return value

    # Determinar si la fila esta vacía
    def empty(self):
        return True if self.__top == None else False

    def front(self):
        return self.__top

    def back(self):
        return self.__base

    def size(self):
        return self.__size
