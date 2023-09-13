from PyQt5.QtCore import QRect, Qt
from PyQt5.QtWidgets import QDialog, QPushButton, QTableWidget, QTableWidgetItem
from controller.ListPolygon import ListPolygon


class ViewListPolygon(QDialog):
    __vector_polygon = ListPolygon()

    def __init__(self, vector_polygon):
        super().__init__()
        self.__vector_polygon = vector_polygon
        self.__launch_widgets()
        self.__launch_Events()

    def __launch_widgets(self):
        self.setWindowTitle("Listar polígono")
        self.setFixedSize(550, 370)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)

        self.but_ok = QPushButton(self)
        self.but_ok.setText("Aceptar")
        self.but_ok.setGeometry(QRect(225, 320, 100, 30))

        self.tab_polygons = QTableWidget(self)
        self.tab_polygons.setGeometry(QRect(20, 20, 510, 280))
        self.tab_polygons.setColumnCount(4)
        self.tab_polygons.setRowCount(0)
        self.tab_polygons.setColumnWidth(0, 125)
        self.tab_polygons.setColumnWidth(1, 125)
        self.tab_polygons.setColumnWidth(2, 130)
        self.tab_polygons.setColumnWidth(3, 130)

        ite_code = QTableWidgetItem("Código")
        self.tab_polygons.setHorizontalHeaderItem(0, ite_code)
        ite_point = QTableWidgetItem("Puntos")
        self.tab_polygons.setHorizontalHeaderItem(1, ite_point)
        ite_perimeter = QTableWidgetItem("Perímetro")
        self.tab_polygons.setHorizontalHeaderItem(2, ite_perimeter)
        ite_area = QTableWidgetItem("Area")
        self.tab_polygons.setHorizontalHeaderItem(3, ite_area)

    def __launch_Events(self):
        self.but_ok.clicked.connect(self.__ok)

    def list_polygon(self):
        self.tab_polygons.setRowCount(0)
        # self.__vector_polygon.show_polygons()
        for i in range(0, self.__vector_polygon.get_size()):
            polygon = self.__vector_polygon.array_polygons[i]

            code = QTableWidgetItem(polygon.code)
            points = QTableWidgetItem(str(polygon.points_count()))
            perimeter = QTableWidgetItem(str(polygon.calculate_perimeter()))
            area = QTableWidgetItem(str(polygon.calculate_area()))

            table_size = self.tab_polygons.rowCount()
            self.tab_polygons.insertRow(table_size)
            table_size = self.tab_polygons.rowCount()
            self.tab_polygons.setItem(table_size-1, 0, code)
            self.tab_polygons.setItem(table_size-1, 1, points)
            self.tab_polygons.setItem(table_size-1, 2, perimeter)
            self.tab_polygons.setItem(table_size-1, 3, area)

    def __ok(self):
        self.setVisible(False)
