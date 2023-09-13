
import os
from structures.Queue import Queue



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


queue = Queue()

list = [10,20,30,40,50,60,70,80,90,100]

for lists in list:
    queue.push(lists)

print_list(queue)

print("Eliminar en la posición 2")
queue.delete(2)
print_list(queue)

print("editar en la posición 4")
queue.update(4,5000)
print_list(queue)

print("Insert en la posición 7")
queue.insert(7,965)
print_list(queue)