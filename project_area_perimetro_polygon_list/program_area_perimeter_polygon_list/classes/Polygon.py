import math

from structures.Queue import Queue


class Polygon:
    code = ""
    points = Queue()
    quantity_point = 0

    def __init__(self, code, quantity_point, points):
        self.code = code
        self.points = points
        self.quantity_point = quantity_point
        self.__close_polygon()

    def __close_polygon(self):
        self.points.push(self.points.front().value)

    def __calculate_distance(self, x1, y1, x2, y2):
        distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
        return distance

    def calculate_perimeter(self):
        perimeter = 0
        i = self.points.front()

        while i != self.points.back():
            point_a = i.value
            point_b = i.next.value

            distance = self.__calculate_distance(
                point_a.x, point_a.y,
                point_b.x, point_b.y
            )
            perimeter += distance
            i = i.next

        return perimeter

    def calculate_area(self):
        value_a: float
        value_b: float

        value_a = 0
        value_b = 0

        i = self.points.front()
        while i != self.points.back():
            point_a = i.value
            point_b = i.next.value

            value_a += point_a.x * point_b.y
            value_b += point_a.y * point_b.x
            i = i.next

        area = math.fabs(value_a - value_b)/2
        return area

    def points_count(self):
        return self.quantity_point
