
from classes.ControlInOut import ControlInOut
from data.StorageControlInOut import StorageControlInOut
from structures.List import List


class ListControlInOut:
    __list_control_in_out = List()
    __control_in_out = StorageControlInOut()
    def __init__(self):
        pass 

    def list_control_in_out(self):
        self.__list_control_in_out

    def add_control_in_out(self, control: ControlInOut):
        self.__list_control_in_out.push_front(control)

    def list_in_service(self):
        list_in_parking = List()
        i = self.__list_control_in_out.front()
        while i is not None:
            if i.value.service is True:
                list_in_parking.push_front(i.value)
            i = i.next

        return list_in_parking

    def search_by_code(self, code: int): 
        car = None
        i = self.__list_control_in_out.front()
        while i is not None:
            if i.value.code == code and i.value.service is True:
                car = i.value
                break
            i = i.next

        return car

    def calculate_total(self): 
        cost_total = 0
        i = self.__list_control_in_out.front()
        while i is not None:
            cost_total += i.value.cost
            i = i.next

        return cost_total

    def search_by_registration_number(self, registration: str):
        car = None
        i = self.__list_control_in_out.front()
        while i is not None:
            if i.value.registration_number == registration:
                car = i.value
                break
            i = i.next

        return car
    
    def search_by_registration_number_service(self, registration: str):
        car = None
        i = self.__list_control_in_out.front()
        while i is not None:
            if i.value.registration_number == registration and i.value.service is True:
                car = i.value
                break
            i = i.next

        return car

    def search_by_date_in(self, date_in: str): 
        list_date = List()
        i = self.__list_control_in_out.front()
        while i is not None:
            if i.value.date_in == date_in :
                list_date.push_front(i.value)
            i = i.next

        return list_date
    
    def register_input(self, car: ControlInOut):
        i = self.__list_control_in_out.front()
        while i is not None:
            if i.value.code is car.code:
                i.value.date_in = car.date_in
                i.value.time_in = car.time_in
                i.value.minutes = car.minutes
                i.value.cost = car.cost
                i.value.service = False
            i = i.next

    def search_code_validate(self, code):
        valid:bool = False
        i = self.__list_control_in_out.front()
        while i is not None:
            if i.value.code == code:
                valid = True
                break
            i = i.next

        return valid
    
    def search_number_validate(self, number):
        valid:bool = False
        i = self.__list_control_in_out.front()
        while i is not None:
            if i.value.registration_number == number and i.value.service is True:
                valid = True
                break
            i = i.next

        return valid
    
    def save_control(self, route):
        self.__control_in_out.set_file_name(route)
        self.__control_in_out.save(self.__list_control_in_out)

    def load_control(self, route):
        self.__control_in_out.set_file_name(route)
        self.__list_control_in_out = self.__control_in_out.open()