
import os
from structures.List import List


def print_list(list):
    aux = list.front()
    i = 0
    print("Lista")
    while aux is not None:
        print("[", i, "]", aux.value)
        aux = aux.next
        i += 1

    print("total ", list.size())
    os.system("pause")


list = List()

os.system("cls")
print("Insertar 15 al inicio")
list.push_front(15)
# print_list(list)
print("Insertar 40 al inicio")
list.push_front(40)
# print_list(list)
print("Insertar 108 al inicio")
list.push_back(108)
# print_list(list)
print("Insertar 77 a la posición 4")
list.insert(4, 77)
# print_list(list)
print("Insertar 77 a la posición 2")
list.insert(2, 77)
# print_list(list)
print("Insertar 77 a la posición 0")
list.insert(0, 77)
# print_list(list)
'''
print("Insertar 77 a la posición -1")
list.insert(-1, 77)
print_list(list)
'''
print("Modificar 2000 a la posición 0")
list.update(0, 2000)
# print_list(list)
print("Modificar 2000 a la posición 2")
list.update(2, 2000)
# print_list(list)
# print("Modificar 2000 a la posición 10")
list.update(10, 2000)
print_list(list)
'''
print("Modificar 2000 a la posición -7")
list.update(-7, 2000)
print_list(list)

print("Eliminar la posición 0")
list.delete(0)
print_list(list)
print("Eliminar la posición 3")
list.delete(3)
print_list(list)
print("Eliminar la posición 15")
list.delete(15)
print_list(list)
print("Eliminar la posición -7")
list.delete(-7)
print_list(list)
'''
print("Buscar valores con 2000")
list.search_value(2000)
print("*** búsqueda *****")
print_list(list.search_value(2000))
print("*******************")
print_list(list)

print("\n buscar el la posición  3")
value = list.get_value(3)
if value != None:
    print("el valor en la posición 3 es ", value, "\n")
else:
    print("el index no existe\n")


print("Quitar el primero")
list.pop_front()
print_list(list)
print("Quitar el ultimo")
list.pop_back()
print_list(list)
