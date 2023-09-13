from data.StoragePharmacy import StoragePharmacy
from structures.List import List


class ListPharmacy:
    __vector_medicine = List()
    __vector_buys = List()
    __vector_sale = List()
    __file_pharmacy = StoragePharmacy()

    def __init__(self):
        pass

    def add_medicine(self, medicine):
        self.__vector_medicine.push_front(medicine)

    def add_sale(self, sale):
        self.__vector_sale.push_front(sale)

    def add_buys(self, buys):
        self.__vector_buys.push_front(buys)

    def list_medicine_available(self):
        return None

    def list_medicine_sale(self, code):
        return None
    
    def list_medicine_buys(self, code):
        return None
    
