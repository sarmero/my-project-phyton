import math


class Polygon:
    __point_x = []
    __point_y = []
    __quantity_point = 0

    def __init__(self, quantity_point, point_y, point_x):
        self.__point_x = point_x
        self.__point_y = point_y
        self.__quantity_point = quantity_point
        self.__close_polygon()

    def __close_polygon(self):
        self.__point_x.append(self.__point_x[0])
        self.__point_y.append(self.__point_y[0])

    def __calculate_distance(self, x1, y1, x2, y2):
        distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
        return distance
        pass

    def calculate_perimeter(self):
        perimeter = 0

        for i in range(self.__quantity_point):
            distance = self.__calculate_distance(
                self.__point_x[i], self.__point_y[i],
                self.__point_x[i+1], self.__point_y[i+1]
            )
            perimeter += distance

        return perimeter

    def calculate_area(self):
        value_a = 0
        value_b = 0
        for i in range(self.__quantity_point):
            value_a += (self.__point_x[i]*self.__point_y[i+1])
            value_b += (self.__point_y[i]*self.__point_x[i+1])

        area = math.fabs(value_a - value_b)/2
        return area

    def show_polygon(self):
        text = f"{'':-<23s}\n"
        text += f"| {'x':^10s}|{'y':^10s}|\n"
        text += f"{'':-<62s}\n"
        for i in range(self.__quantity_point):
            text += f"| {self.__point_x[i]:^10.1f}|{self.__point_y[i]:^10.1f}|\n"
        text += f"{'':-<23s}\n"

        perimeter = self.calculate_perimeter()
        area = self.calculate_area()

        text += f"| {'perímetro: ':^10s}|{perimeter:^10.5f}|\n"
        text += f"| {'Area: ':^10s}|{area:^10.5f}|\n"
        text += f"{'':-<23s}\n"
        return text
