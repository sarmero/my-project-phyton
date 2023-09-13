

from data.StorageInputOutput import StorageInputOutput
from structures.List import List


class ListControlInputOutput():
    __list_output = List()
    __file_report_parking = StorageInputOutput()

    def __init__(self):
        pass

    def add_vehicle(self, output):
        self.__list_output.push_front(output)

    def get_list(self):
        return self.__list_output

    def search_by_code(self, code):
        # algoritmo de búsqueda secuencial
        control = None

        i = self.__list_output.front()
        while i != None:
            if code == i.value.get_code():
                control = i.value
                break
            i = i.next
        return control

    def list_report_service(self):
        list = List()
        i = self.__list_output.front()
        while i is not None:
            if i.value.is_service() is True:
                list.push_front(i.value)
            i = i.next

        return list

    def list_report_service_date(self, date):
        list = List()
        i = self.__list_output.front()
        while i is not None:
            if i.value.get_date_input() == date:
                list.push_front(i.value)
            i = i.next

        return list

    def list_report_service_tuition(self, tuition):
        vehicle = None
        i = self.__list_output.front()
        while i is not None:
            if i.value.get_tuition() == tuition:
                vehicle = i.value
            i = i.next

        return vehicle

    def register_output(self, vehicle):
        i = self.__list_output.front()
        while i is not None:
            if vehicle.get_tuition() == i.value.get_tuition():
                i.value = vehicle
                i.value.set_service(False)
            i = i.next

    def save_file(self, route):
        self.__file_report_parking.set_file_name(route)
        self.__file_report_parking.save(self.__list_output)

    def load_file(self, route):
        self.__file_report_parking.set_file_name(route)
        self.__list_output = self.__file_report_parking.open()
