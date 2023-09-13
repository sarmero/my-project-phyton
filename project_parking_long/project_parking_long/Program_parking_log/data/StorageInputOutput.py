
import pickle

from structures.List import List


class StorageInputOutput():
    __file_name = ""

    def __init_(self):
        pass

    def set_file_name(self, file_name):
        self.__file_name = file_name

    def get_file_name(self):
        return self.__file_name

    # llevar de la memoria el disco duro (salida de datos en la memoria _ output)
    def save(self, list):
        # al manejar archivos se debe trabajar  con excepciones
        try:
            output = open(self.__file_name, 'wb')
            i = list.front()
            while i != None:
                vehículo = i.value
                pickle.dump(vehículo, output, pickle.HIGHEST_PROTOCOL)
                i = i.next

        except Exception as e:
            print(e)

    # traer del disco duro a la memoria ( entrada de datos en la memoria - input)

    def open(self):
        list = List()
        try:
            # r (read - leer) b: binario (bytes)
            input = open(self.__file_name, 'rb')
            while True:
                try:
                    vehicle = pickle.load(input)
                    list.push_front(vehicle)
                except:
                    break
        except :
            pass

        return list
