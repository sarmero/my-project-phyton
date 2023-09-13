
from structures.List import List
import pickle


class StoragePharmacy:
    __file_name = ""

    def __init__(self):
        pass

    def set_file_name(self, file_name):
        self.__file_name = file_name

    def get_fileName(self):
        return self.__file_name

    def save(self, list):

        try:
            output = open(self.__file_name, 'wb')
            i = list.front()
            while i != None:
                pharmacy = i.value
                pickle.dump(pharmacy, output, pickle.HIGHEST_PROTOCOL)
                i = i.next
        except:
            pass

    def open_file(self):
        list = List()
    
        try:
            input = open(self.__file_name, 'rb')
            while True:
                try:
                    date = pickle.load(input)
                    list.push_front(date)
                except:
                    break
        except:
            pass
    
        return list
