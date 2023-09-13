

import pickle


class StoragePolygon:
    __file_name = ""

    def __init__(self):
        pass

    def set_file_name(self, file_name):
        self.__file_name = file_name

    def get_fileName(self):
        return self.__file_name

    def save(self, array_list):

        try:
            output = open(self.__file_name, 'wb')
            for i in range(len(array_list)):
                polygon = array_list[i]
                pickle.dump(polygon, output, pickle.HIGHEST_PROTOCOL)

        except:
            pass

    def open_file(self):
        array_polygon = []
        try:
            input = open(self.__file_name, 'rb')
            while True:
                try:
                    polygon = pickle.load(input)
                    array_polygon .append(polygon)
                except:
                    break
        except:
            pass

        return array_polygon
