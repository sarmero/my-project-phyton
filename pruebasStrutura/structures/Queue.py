
from structures.Node import Node


class Queue:
    __head = None
    __end = None
    __size = 0

    def __init__(self):
        self.__head = None
        self.__end = None
        self.__size = 0

    # inserta un elemento al final de la fila
    def push(self, value):
        # se crea el nuevo nodo(libre)
        aux = Node(value)

        # si es el primer nodo en la fila
        if self.__head == None:
            # la cabecera enlaza a ese nodo
            self.__head = aux
            # la final enlaza a ese nodo
            self.__end = aux
        else:
            # el siguiente del final enlaza al nuevo nodo
            self.__end.next = aux
            # el final enlaza al nuevo nodo
            self.__end = aux

        self.__size += 1

    # sacar el primer elemento de la lista
    def pop(self):
        value = None

        if self.__head != None:
            # sacar el primer elemento
            aux = self.__head
            # obtener el valor del primer elemento
            value = aux.value
            # mover la cabecera al siguiente
            self.__head = self.__head.next

            if self.__head == None:
                self.__end = None

        self.__size -= 1

        return value

    def empty(self):
        return True if self.__head == None else False

    def front(self):
        return self.__head

    def back(self):
        return self.__end

    def size(self):
        return self.__size
    

    def delete(self, index):
        flag = False
        if index >= 0 and index < self.__size:
            i = self.__head
            j = 0
            before = None
            while i != self.back() and j < index:
                before = i
                i = i.next
                j += 1

            if before == None:
                self.pop()
            else:
                before.next = i.next
                flag = True
                self.__size -= 1
        else:
            if index > 0:
                print("   * error: ( size: ", self.__size, " index: ", index, " )")
            else:
                print("   * error index (", index, ")")

        return flag
    
    def update(self, index, new_value):
        flag = False
        if index >= 0 and index < self.__size:
            i = self.__head
            j = 0

            while i != self.back() and j < self.__size:
                if j == index:
                    i.value = new_value
                    break
                i = i.next
                j += 1

            flag = True
        else:
            if index > 0:
                print("   * error: ( size: ", self.__size, " index: ", index, " )")
            else:
                print("   * error index (", index, ")")

        return flag
    

    def insert(self, index, value):
        flag = False
        if index >= 0 and index < self.__size:
            i = self.__head
            j = 0
            before = None
            while i != self.back() and j < index:
                before = i
                i = i.next
                j += 1

            if before == None:
                self.push(value)
            else:
                aux = Node(value)
                aux.next = before.next
                before.next = aux
                flag = True
                self.__size += 1
        else:
            if index > 0:
                print("   * error: ( size: ", self.__size, " index: ", index, " )")
            else:
                print("   * error index (", index, ")")
