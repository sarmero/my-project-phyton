from structures.Node import Node


class Queue:
    __head = None
    __end = None
    __size = 0

    def __init__(self):
        self.__head = None
        self.__end = None
        self.__size = 0

    # Inserta un elemento a final de la fila
    def push(self, value):
        # Se crea el nuevo nodo(libre)
        aux = Node(value)

        # Si es el primer nodo en la fila
        if self.__head == None:
            # la cabecera enlaza a ese nodo
            self.__head = aux
            # El final enlaza a ese nodo
            self.__end = aux
        else:
            # El siguiente del final se enlaza al nuevo nodo
            self.__end.next = aux
            # El final se enlaza al nuevo nodo
            self.__end = aux
        self.__size += 1

    def pop(self):
        value = None

        if self.__size != None:
            # Sacar el primer elemento
            aux = self.__head
            # Obtener el valor del primer elemento
            value = aux.value
            # Mover la cabecera al siguiente
            self.__head = self.__head.next

            # Si se saca el ultimo elemento
            # cabecera y final en nulo
            if self.__head == None:
                self.__end = None

            self.__size -= 1

        return value

    # Determinar si la fila esta vacía
    def empty(self):
        return True if self.__head == None else False

    def front(self):
        return self.__head

    def back(self):
        return self.__end

    def size(self):
        return self.__size
