import math


class Polygon:
    code = ""
    point_x = []
    point_y = []
    quantity_point = 0

    def __init__(self, code, quantity_point, point_y, point_x):
        self.code = code
        self.point_x = point_x
        self.point_y = point_y
        self.quantity_point = quantity_point
        self.__close_polygon()

    def __close_polygon(self):
        self.point_x.append(self.point_x[0])
        self.point_y.append(self.point_y[0])

    def __calculate_distance(self, x1, y1, x2, y2):
        distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
        return distance

    def calculate_perimeter(self):
        perimeter = 0

        for i in range(self.quantity_point):
            distance = self.__calculate_distance(
                self.point_x[i], self.point_y[i],
                self.point_x[i+1], self.point_y[i+1]
            )
            perimeter += distance

        return perimeter

    def calculate_area(self):
        value_a = 0
        value_b = 0
        for i in range(self.quantity_point):
            value_a += (self.point_x[i] * self.point_y[i+1])
            value_b += (self.point_y[i] * self.point_x[i+1])

        area = math.fabs(value_a - value_b)/2
        return area

    def points_count(self):
        return self.quantity_point
