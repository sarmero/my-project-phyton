from data.StorageEps import StorageEps
from structures.List import List


class ListEPS:
    __list = List()
    __file_eps = StorageEps()
    file_name = ""

    def __init__(self):
        self.file_name = ""

    def add_object(self, object):
        self.__list.push_front(object)

    def get_list(self):
        return self.__list
    
    def save_list(self):
        self.__file_eps.set_file_name(self.file_name)
        self.__file_eps.save(self.__list)
        

    def load_list(self):
        self.__file_eps.set_file_name(self.file_name)
        self.__list = self.__file_eps.open_file()
        