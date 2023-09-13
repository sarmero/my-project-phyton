from structures.List import List
from data.StorageEquipment import StorageEquipment


class ListEquipment:
    __list_equipment = List()
    __file_equipment = StorageEquipment()

    def __init__(self):
        pass

    def add_equipment(self, equipment):
        self.__list_equipment.push_front(equipment)

    def search_by_code(self, code):
        # algoritmo de búsqueda secuencial
        # equipos queda nulo cuando no se encuentra
        equipment = None

        i = self.__list_equipment.front()
        while i != None:
            if code == i.value.code:
                equipment = i.value
                break
            i = i.next
        return equipment

    # Mostrar todos los equipos
    def show_equipment(self):
        text = ""
        i = self.__list_equipment.front()
        while i != None:
            text += i.value.show_equipment() + "\n"
            i = i.next
        return text

    def get_size(self):
        return self.__list_equipment.size

    # Obtener el total de equipos

    def get_equipment(self):
        return self.__list_equipment

    def save_equipment(self):
        self.__file_equipment.set_file_name('equipment.plg')
        self.__file_equipment.save(self.__list_equipment)

    def open_equipment(self):
        self.__file_equipment.set_file_name('equipment.plg')
        self.__list_equipment = self.__file_equipment.open()
