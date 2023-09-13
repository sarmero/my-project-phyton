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

    def back(self):
        return self.__end

    # Determinar si la fila esta vacía
    def empty(self):
        return True if self.__head == None else False

    def size(self):
        return self.__size

    # inserta un elemento al final de la fila
    def push_front(self, value):
        # se crea el nuevo nodo(libre)
        aux = Node(value)
        # si es el primer nodo en la fila
        if self.__head == None:
            # la cabecera enlaza a ese nodo
            self.__head = aux
            # el final enlaza al nuevo nodo
            self.__end = aux
        else:
            # el nuevo nodo enlaza a la cabecera actual
            aux.next = self.__head
            # la cabecera actual enlaza al nuevo nodo
            self.__head = aux

        self.__size += 1

    def push_back(self, value):
        # se crea el nuevo nodo(libre)
        aux = Node(value)
        # si es el primer nodo en la fila
        if self.__end == None:
            # la cabecera enlaza a ese nodo
            self.__end = aux
            # el final enlaza al nuevo nodo
            self.__head = aux
        else:
            # el nuevo nodo enlaza a la cabecera actual
            self.__end.next = aux
            # la cabecera actual enlaza al nuevo nodo
            self.__end = aux

        self.__size += 1
        pass

    def pop_front(self):
        value = None
        # verificar que la cabecera enlace a un nodo
        if (self.__head != None):
            # sacar el primer elemento
            aux = self.__head
            # guarda el valor
            value = aux.value
            # mover la cabecera al siguiente
            self.__head = self.__head.next

            # si se saca el ultimo elemento cabecera y final en nulo
            if self.__head == None:
                self.__end = None

            self.__size -= 1

        return value

    def pop_back(self):
        value = None

        if self.__end != None:
            value = self.__end
            # mientras actual (current) avanza y before es el anterior
            current = self.__head
            before = None
            print("current[", )
            while current != self.back():
                before = current
                current = current.next

            before.next = None  # si elimina el enlace del anterior
            self.__end = before  # se actualiza el final

            self.__size -= 1

        return value

    # insertar elementos en una posición
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
    # Modificar un valor en una posición

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

    # Eliminar un elemento en una posición

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
                before.next = current.next  # Enlace
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
            aux = aux.next
        return flag
    # limpiar toda la lista

    def clear(self):
        self.__head = None
        self.__end = None
        self.__size = 0
    # obtener el nodo a partir de una posición

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
