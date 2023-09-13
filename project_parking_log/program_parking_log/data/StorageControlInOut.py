import pickle
from structures.List import List


class StorageControlInOut:
    __file_name:str = ""

    def __init__(self):
        pass

    def set_file_name(self, file_name: str): 
        self.__file_name = file_name

    def get_file_name(self):
        return self.__file_name

    # llevar la memoria al disco duro (salida de datos de la memoria - output)

    def save(self, listControlInOut: List):
        # al manejar archivos se debe trabajar con excepciones
        try:
            # w: write (escribir) b: binario (bytes)
            output = open(self.__file_name, 'wb')
            i = listControlInOut.front()
            while i != None:
                controlInOut = i.value
                pickle.dump(controlInOut, output, pickle.HIGHEST_PROTOCOL)
                i = i.next
        except:
            pass

    # Traer del disco duro a la memoria ( entrada de datos a la memoria)

    def open(self):
        listControlInOut = List()
        try:
            # r (read - leer) b: binario (bytes)
            input = open(self.__file_name, 'rb')
            while True:
                try:
                    controlInOut = pickle.load(input)
                    listControlInOut.push_front(controlInOut)
                except:
                    break
        except :
            pass

        return listControlInOut