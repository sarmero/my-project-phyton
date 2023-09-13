from structures.BinaryTree import BinaryTree
from structures.List import List
from structures.Node2 import Node2


class AVLTree(BinaryTree):
    __root: Node2 = None

    def __init__(self):
        self.__root = None

    def insert(self, value):
        if self.__root is None:
            self.__root = Node2(value)
        else:
            self.__root = self.__insert(self.__root, value)

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

        balance_parent = self.__get_balance(aux)
        if balance_parent == 2:
            balance_son = self.__get_balance(aux.left)
            # RSI Rotación Simple a la Izquierda
            if balance_son == 1:
                self.__connect_right(aux)
            # RDI RotaciónDoble a la Izquierda
            elif balance_son == -1:
                pass
        elif balance_parent == -2:
            balance_son = self.__get_balance(aux.right)
            # RDD Rotación Doble a la Derecha
            if balance_son == 1:
                pass
            # RSD Rotación Simple a la Derecha
            elif balance_son == -1:
                aux = self.__connect_left(aux)

        return aux
    """"
    # sobre-escritura
    def insert(self, value):
        super().insert()
        pass
    """

    def __connect_left(self, x):
        y = x.right
        z = y.left
        y.left = x
        x.right = z
        return y

    def __connect_right(self, x):
        y = x.left
        z = y.right

        y.right = x
        x.left = z
        return y

    def __move_left(self):
        pass

    def __move_right(self):
        pass

    def __get_balance(self, aux):
        level_left = self.__height(aux.left)
        level_right = self.__height(aux.right)
        print("left:[", level_left, "] right: [", level_right, "]")
        print("balance", "[", level_left, level_right, "]")
        return level_left - level_right

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
            return -1
        left = 1 + self.__height(aux.left)
        right = 1 + self.__height(aux.right)
        if left > right:
            return left
        else:
            return right
