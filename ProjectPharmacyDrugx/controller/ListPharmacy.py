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
        list = List()
        i = self.__vector_medicine.front()
        while i != None:
            if i.value.get_code() > 0:
                list.push_front(i.value)
            i = i.next

        return list


    def list_medicine_sale(self, code):
        sale = self.__vector_sale
        list = self.__list_description(sale,code)
        return list
    
    def list_medicine_buys(self, code):
        buys = self.__vector_buys
        list = self.__list_description(buys,code)
        return list
    
    def __list_description(self,vector,code):
        list = List()
        i = vector.front()
        while i != None:
            if code == i.value.get_code_medicine():
                list.push_front(i.value)
            i = i.next

        return list


    def save_list(self):
        self.__file_pharmacy.set_file_name('medicine.eps')
        self.__file_pharmacy.save(self.__vector_medicine)
        self.__file_pharmacy.set_file_name('buys.eps')
        self.__file_pharmacy.save(self.__vector_buys)
        self.__file_pharmacy.set_file_name('sale.eps')
        self.__file_pharmacy.save(self.__vector_sale)

    def load_list(self):
        self.__file_pharmacy.set_file_name('medicine.eps')
        self.__vector_medicine = self.__file_pharmacy.open_file()
        self.__file_pharmacy.set_file_name('buys.eps')
        self.__vector_buys= self.__file_pharmacy.open_file()
        self.__file_pharmacy.set_file_name('sale.eps')
        self.__vector_sale= self.__file_pharmacy.open_file()