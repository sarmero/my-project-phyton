import classes.Polygon
from data.StoragePolygon import StoragePolygon
from structures.Queue import Queue


class ListPolygon:
    array_polygons = Queue()
    __file_polygon = StoragePolygon()

    def __init__(self):
        pass

    def add_polygon(self, polygon):
        self.array_polygons.push(polygon)

    def search_by_code(self, code):
        polygon = None
        i = self.array_polygons.front()
        while i != None:
            if code == i.value.code:
                polygon = i.value
            break
        i = i.next

        return polygon

    def show_polygon(self, cod):
        for i in range(self.get_size()):
            if self.array_polygons[i].code == cod:
                return self.array_polygons[i]

        return None

    def get_size(self):
        return self.array_polygons.size()

    def get_polygon(self, index):
        return self.array_polygons[index]

    def save_polygon(self):
        self.__file_polygon.set_file_name('polygon.plg')
        self.__file_polygon.save(self.array_polygons)

    def load_polygon(self):
        self.__file_polygon.set_file_name('polygon.plg')
        self.array_polygons = self.__file_polygon.open_file()

    def list_code_polygon(self, com):
        polygon = None
        i = self.array_polygons.front()
        while i != None:
            com.addItem(str(i.value.code))
        i = i.next

        return polygon
