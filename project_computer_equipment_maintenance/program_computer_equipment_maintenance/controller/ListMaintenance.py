from structures.List import List


class ListMaintenance:
    list_maintenance = List()

    def __init__(self):
        pass

    def add_maintenance(self, maintenance):
        self.list_maintenance.push_front(maintenance)

    def search_by_code(self, code):
        # algoritmo de búsqueda secuencial
        # mantenimiento queda nulo cuando no se encuentra
        maintenance = None

        i = self.list_maintenance.front()
        while i != None:
            if code == i.value.code:
                maintenance = i.value
                break
            i = i.next
        return maintenance

    # Mostrar todos los mantenimiento
    def show_maintenance(self):
        text = ""
        i = self.list_maintenance.front()
        while i != None:
            text += i.value.show_maintenance() + "\n"
            i = i.next
        return text

    def get_size(self):
        return self.list_maintenance.size

    # Obtener el total de mantenimiento

    def get_maintenance(self):
        return self.list_maintenance
