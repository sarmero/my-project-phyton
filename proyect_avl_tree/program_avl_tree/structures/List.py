from structures.Node import Node


class List:
    __head = None
    __end = None
    __size = 0

    def __init__(self):
        self.__head = None
        self.__end = None
        self.__size = 0

    def front(self):
        return self.__head

    def empty(self):
        return True if self.__head == None else False

    def back(self):
        return self.__end

    def size(self):
        return self.__size

    # Adicionar un elemento al principio
    def push_front(self, value):
        aux = Node(value)
        if self.__head == None:
            self.__head = aux
            self.__end = aux
        else:
            aux.next = self.__head
            self.__head = aux
        self.__size += 1

    # Adicionar un elemento al final
    def push_back(self, value):
        aux = Node(value)
        if self.__head == None:
            self.__end = aux
            self.__head = aux
        else:
            self.__end.next = aux
            self.__end = aux
        self.__size += 1

    # quitar primer elemento
    def pop_front(self):
        value = None
        if self.__size != None:
            aux = self.__head
            self.__head = self.__head.next
            value = aux.value
            aux.next = None

            if self.__head == None:
                self.__end == None
            self.__size -= 1
        return value

    # quitar ultimo elemento
    def pop_back(self):
        value = None
        if self.__head != None:
            value = self.__end

            # mientras el Actual avanza (current) avanza y before es el anterior
            current = self.__head
            before = None
            while current != self.back():
                before = current
                current = current.next

            before.next = None  # se elimina el enlace anterior
            self.__end = before  # se actualiza el final

            self.__size -= 1

        return value

    # Insertar elemento en una posición
    def insert(self, index, value):
        flag = False
        if index >= 0 and index < self.__size:

            current = self.__head
            before = None
            i = 0
            while current != self.back() and i < index:  # self.back()
                before = current
                current = current.next
                i += 1

            if before is None:  # Verificar inserción al inicio
                self.push_front(value)
            else:
                aux = Node(value)
                aux.next = before.next
                before.next = aux
                self.__size += 1
            flag = True
        return flag

    # Actualizar el valor de un elemento en una posición
    def update(self, index, new_value):
        flag = False
        if index >= 0 and index < self.__size:
            current = self.__head
            i = 0
            while current != None and i < index:
                current = current.next
                i += 1
            current.value = new_value
            flag = True
        return flag

    # eliminar elemento en un posición
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
                before.next = current.next  # El enlace entre las tablas
                self.__size -= 1
            flag = True
        return flag

    # Obtener el elemento de una posición
    def get_value(self, index):
        value = None
        if index >= 0 and index < self.__size:
            aux = self.__head
            i = 0
            while aux != None and i <= index:
                if i == index:
                    value = aux.value
                    break
                aux = aux.next
                i += 1
        return value

    # Verificar si un valor existe en la lista

    def search_value(self, value):
        flag = False
        aux = self.__head
        while aux != None:
            if aux.value == value:
                flag = True
                break
            aux = aux.next
        return flag

    # Limpiar toda la lista
    def clear(self):
        self.__head = None
        self.__end = None
        self.__size = 0

    # Obtener el nodo a partir de un posición
    def search_by_index(self, value):
        index = -1
        aux = self.__head
        i = 0
        while aux != None:
            if aux.value == value:
                index = i
                break
            aux = aux.next
            i += 1
        return index
