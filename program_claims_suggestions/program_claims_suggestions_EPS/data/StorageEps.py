
from structures.List import List
import pickle


class StorageEps:
    __file_name = ""

    def __init__(self):
        pass

    def set_file_name(self, file_name):
        self.__file_name = file_name

    def get_fileName(self):
        return self.__file_name

    def save(self, list_eps):

        try:
            output = open(self.__file_name, 'wb')
            i = list_eps.front()
            while i != None:
                eps = i.value
                pickle.dump(eps, output, pickle.HIGHEST_PROTOCOL)
                i = i.next
        except:
            pass

    def open_file(self,):
        list_eps = List()
    
        try:
            input = open(self.__file_name, 'rb')
            while True:
                try:
                    date = pickle.load(input)
                    list_eps.push_front(date)
                except:
                    break
        except:
            pass
    
        return list_eps
