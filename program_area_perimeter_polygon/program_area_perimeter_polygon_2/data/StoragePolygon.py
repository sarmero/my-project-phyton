

import pickle


class StoragePolygon:
    __file_name = ""

    def __init__(self):
        pass

    def set_file_name(self, file_name):
        self.__file_name = file_name

    def get_fileName(self):
        return self.__file_name

    def save(self, polygon):

        try:
            output = open(self.__file_name, 'wb')
            pickle.dump(polygon, output, pickle.HIGHEST_PROTOCOL)
        except:
            pass

    def open_file(self):
    
        try:
            input = open(self.__file_name, 'rb')
            try:
                polygon = pickle.load(input)
                return polygon 
            except:
                pass
        except:
            pass

        return None
