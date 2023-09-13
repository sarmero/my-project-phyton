import classes.Polygon
from data.StoragePolygon import StoragePolygon
from structures.Stack import Stack


class ListPolygon:
    __queue_polygons = Stack()
    __file_polygon = StoragePolygon()

    def __init__(self):
        pass

    def add_polygon(self, polygon):
        self.__queue_polygons.push(polygon)

    def search_by_code(self, code):
        polygon = None
        i = self.__queue_polygons.front()
        while i != None:
            if code == i.value.code:
                polygon = i.value
                break
            i = i.next

        return polygon

    def get_size(self):
        return self.__queue_polygons.size()

    def save_polygon(self):
        self.__file_polygon.set_file_name('polygon.plg')
        self.__file_polygon.save(self.__queue_polygons)

    def load_polygon(self):
        self.__file_polygon.set_file_name('polygon.plg')
        self.__queue_polygons = self.__file_polygon.open_file()

    def list_code_polygon(self, com):
        i = self.__queue_polygons.front()
        while i != None:
            com.addItem(i.value.code)
            i = i.next

    def get_queue(self):
        return self. __queue_polygons
