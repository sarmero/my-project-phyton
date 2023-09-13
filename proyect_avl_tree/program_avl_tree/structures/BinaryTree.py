
from structures.List import List
from structures.Node2 import Node2


class BinaryTree:
    __root: Node2 = None

    def __init__(self):
        self.__root = None

    def insert(self, value):
        if self.__root is None:
            self.__root = Node2(value)
        else:
            self.__insert(self.__root, value)

    def __insert(self, aux, value):
        # print(value, " < ", aux.value)
        if value < aux.value:
            # print("left:", aux.left.value if aux.left is not None else "none")
            if aux.left is None:
                aux.left = Node2(value)
            else:
                self.__insert(aux.left, value)
        else:
            # print("right", aux.right.value if aux.right is not None else "none")
            if aux.right is None:
                aux.right = Node2(value)
            else:
                self.__insert(aux.right, value)

    def search(self, value):
        self.__search(self.__root, value)

    def __search(self, aux, value):
        if aux is not None:
            if aux.value == value:
                return aux
            if aux.value > value:
                return self.__search(aux.left, value)
            else:
                return self.__search(aux.right, value)

    # PID

    def pre_order(self):
        list = List()
        self.__pre_order(self.__root, list)
        return list
    # Recorrido pre_order recursivo

    def __pre_order(self, aux, list: List):
        if aux is not None:
            # print(aux.value)  # mostrar padre
            list.push_back(aux.value)
            self.__pre_order(aux.left, list)  # Avance por la izquierda
            self.__pre_order(aux.right, list)  # Avance por la derecha

    # IPD
    def in_order(self):
        list = List()
        self.__in_order(self.__root, list)
        return list

    def __in_order(self, aux, list: List):
        if aux is not None:
            self.__in_order(aux.left, list)
            list.push_back(aux.value)
            self.__in_order(aux.right, list)

    # IDP
    def post_order(self):
        list = List()
        self.__post_order(self.__root, list)
        return list

    def __post_order(self, aux, list: List):
        if aux is not None:
            self.__post_order(aux.left, list)
            self.__post_order(aux.right, list)
            list.push_back(aux.value)

    def height(self):
        return self.__height(self.__root)

    def __height(self, aux):
        if aux is None:
            return 0
        left = 1 + self.__height(aux.left)
        right = 1 + self.__height(aux.right)
        if left > right:
            return left
        else:
            return right
