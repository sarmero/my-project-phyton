import random

import classes.Polygon
from data.StoragePolygon import StoragePolygon


class ListPolygon:
    array_polygon = []
    __file_polygon = StoragePolygon()
    code_save = ""
    __code_original = ""
    

    def __init__(self):
        pass

    def add_polygon(self, polygon):
        self.array_polygon.append(polygon)

    def show_polygon(self, cod):
        for i in range(self.get_size()):
            if self.array_polygon[i].code == cod:
                return self.array_polygon[i]

        return None

    def get_size(self):
        return len(self.array_polygon)

    def get_polygon(self, index):
        return self.array_polygon[index]

    def save_as_polygon(self,route):
        self.__file_polygon.set_file_name(route)
        self.__file_polygon.save(self.array_polygon)

    def save_polygon(self,route):
        self.__file_polygon.set_file_name(route)
        polygon = self.search_polygon_code(self.code_save)
        polygon.code = self.__code_original
        self.__file_polygon.save(polygon)

    def load_polygon(self,route):
        self.__file_polygon.set_file_name(route)
        polygon = self.__file_polygon.open_file()
        cod = polygon.code
        self.__code_original = polygon.code

        while  self.search_code(cod) == True:
            cod = cod + str(random.randint(0, 9))

        polygon.code = cod
        self.code_save = polygon.code
        self.array_polygon.append(polygon)

    def update_polygon(self, polygon):
        for i in range(self.get_size()):
            if self.array_polygon[i].code == polygon.code:
                self.array_polygon[i].code = polygon.code
                self.array_polygon[i].point_x = polygon.point_x
                self.array_polygon[i].point_y = polygon.point_y
                self.array_polygon[i].quantity_point = polygon.quantity_point

    def delete_polygon(self, code):
        for i in range(self.get_size()):
            if self.array_polygon[i].code == code:
                self.array_polygon.remove(self.get_polygon(i))
                if code == self.code_save:
                    self.code_save = ""
                break

    def search_polygon_point(self, quantity_point):
        array = []
        for i in range(self.get_size()):
            if self.array_polygon[i].quantity_point == quantity_point:
                array.append(self.array_polygon[i])

        return array

    def search_polygon_code(self, code):
        for i in range(self.get_size()):
            if self.array_polygon[i].code == code:
                return self.array_polygon[i]

        return None
    
    def search_code(self, code):
        for i in range(self.get_size()):
            if self.array_polygon[i].code == code:
                return True
        return False
