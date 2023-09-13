
import pickle

from structures.Stack import Stack


class StoragePolygon:
    __file_name = ""

    def __init__(self):
        pass

    def set_file_name(self, file_name):
        self.__file_name = file_name

    def get_fileName(self):
        return self.__file_name

    def save(self, queue_polygon):

        try:
            output = open(self.__file_name, 'wb')
            i = queue_polygon.front()
            while i != None:
                polygon = i.value
                pickle.dump(polygon, output, pickle.HIGHEST_PROTOCOL)
                i = i.next

        except:
            pass

    def open_file(self):
        queue_polygon = Stack()
        try:
            input = open(self.__file_name, 'rb')
            while True:
                try:
                    polygon = pickle.load(input)
                    queue_polygon.push(polygon)
                except:
                    break
        except:
            pass

        return queue_polygon
