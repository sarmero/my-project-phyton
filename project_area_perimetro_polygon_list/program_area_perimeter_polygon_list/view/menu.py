
import os
from classes.Polygon import Polygon
from controller.ListPolygon import ListPolygon


class Menu:

    __vector_polygon = ListPolygon()

    def __init__(self):
        pass

    def __showTitle(self, title):
        os.system("cls")
        text = f"{'':-<62s}"+"\n"
        text += f"|{title:^60s}|\n"
        text += f"{'':-<62s}"+"\n"
        return text

    def showMenu(self):
        option = 0
        while (option != "3"):
            text = self.__showTitle(
                "MENU PARA OBTENER EL AREA Y EL PERÍMETRO DE UN POLÍGONO")
            text += f"| {'1. Registrar polígono':<59s}|\n"
            text += f"| {'2. listar polígono':<59s}|\n"
            text += f"| {'3. salir':<59s}|\n"
            text += f"{'':-<62s}"+"\n"
            print(text)
            option = int(input("Ingrese una opción: "))

            if option == 1:
                self.__registerPolygons()
            elif option == 2:
                self.__show_polygon()
            elif option == 3:
                self.__output()
            else:
                text = self.__showTitle("Error - Opción no valida")
                print(text)
            os.system("pause")

    def __registerPolygons(self):
        point_x = []
        point_y = []
        text = self.__showTitle("1. REGISTRAR POLÍGONO")
        print(text)
        print("polígono # "+str(self.__vector_polygon.get_size()+1)+"\n")
        quantity_points = int(input("ingrese la cantidad de puntos: "))
        for i in range(quantity_points):
            print("punto # "+str(i+1)+"->")
            x = float(input("valor de x: "))
            y = float(input("valor de y: "))
            point_x.append(x)
            point_y.append(y)

        polygon = Polygon(quantity_points, point_y, point_x)
        self.__vector_polygon.add_polygon(polygon)

    def __show_polygon(self):
        text = self.__showTitle("2 MOSTRAR POLÍGONO")
        text += self.__vector_polygon.show_polygons()
        print(text)

    def __output(self):
        text = self.__showTitle("3. SALIR")
        text += f"| {'Hecho por: Sebastian armero':^59s}|\n"
        text += f"| {'Udenar @ 2023':^59s}|\n"
        text += f"{'':-<62s}\n"
        print(text)
