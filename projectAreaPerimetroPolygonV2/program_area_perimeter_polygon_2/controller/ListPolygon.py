import classes.Polygon


class ListPolygon:
    __array_polygon = []

    def __init__(self):
        pass

    def add_polygon(self, polygon):
        self.__array_polygon.append(polygon)

    def show_polygons(self):
        text = ""
        for i in range(self.get_size()):
            text += self.__array_polygon[i].show_polygon()+"\n"
        return text

    def get_size(self):
        return len(self.__array_polygon)
