

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

    def empty(self):
        return True if self.__head == None else False

    def size(self):
        return self.__size

    def push_front(self, value):
        aux = Node(value)

        if self.__head == None:
            self.__head = aux
            self.__end = aux
        else:
            aux.next = self.__head
            self.__head = aux

        self.__size += 1

    def push_back(self, value):
        aux = Node(value)

        if self.__head == None:
            self.__head = aux
            self.__end = aux
        else:
            self.__end.next = aux
            self.__end = aux

        self.__size += 1

    def pop_front(self):
        value = None

        if self.__head != None:
            aux = self.__head
            self.__head = self.__head.next
            value = aux.value
            aux.next = None
            if self.__head == None:
                self.__end = None

            self.__size -= 1

        return value

    def pop_back(self):
        value = None

        if self.__head != None:
            i = self.__head
            before = None
            while i != self.back():
                before = i
                i = i.next

            before.next = None
            self.__end = before

            self.__size -= 1

        return value

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
                self.push_front(value)
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
                self.pop_front()
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

    def get_value(self, index):
        if index >= 0 and index < self.__size:
            j = 0
            i = self.__head
            value = None
            while i != None and j <= index:
                value = i.value
                i = i.next
                j += 1

            return value
        else:
            return None

    def search_value(self, value):
        list = List()
        i = self.__head
        j = 0
        while i != self.back():
            if i.value == value:
                list.push_front("index :"+str(j))
            i = i.next
            j += 1

        return list

    def clear(self):
        self.__head = None
        self.__end = None
        self.__size = 0

    def search_by_index(self, value):
        i = self.__head
        j = 0
        while i != self.back():
            if i.value == value:
                return j
            i = i.next
            j += 1

        return -1
