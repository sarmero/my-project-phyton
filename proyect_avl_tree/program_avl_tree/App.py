import os
from structures.AVLTree import AVLTree
from structures.BinaryTree import BinaryTree


def print_list(title, list):
    print(title)
    aux = list.front()
    while aux is not None:
        print(aux.value)
        aux = aux.next


os.system("cls")
tree = AVLTree()
numbers = [30, 40, 20, 10, 15]

for number in numbers:
    tree.insert(number)

# list = tree.pre_order()
# print_list("pre-orden", list)

# list = tree.in_order()
# print_list("in-orden", list)

list = tree.post_order()
print_list("post-orden", list)

""""
aux = tree.search(48)
if aux is None:
    print("no existe", aux)
else:
    print("existe", aux)
"""

height = tree.height()
print("La altura es: ", height)
