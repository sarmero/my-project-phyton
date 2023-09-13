from PyQt5.QtCore import QRect, Qt
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QMessageBox, QPushButton, QTableWidget, QTableWidgetItem
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
        self.but_ok.setGeometry(QRect(225, 330, 100, 30))

        self.lab_code = QLabel(self)
        self.lab_code.setText("Código")
        self.lab_code.setGeometry(QRect(20, 20, 50, 25))

        self.tex_code = QLineEdit(self)
        self.tex_code.setGeometry(QRect(60, 20, 70, 25))

        self.but_code = QPushButton(self)
        self.but_code.setText("filtrar")
        self.but_code.setGeometry(QRect(130, 20, 70, 25))

        self.lab_point = QLabel(self)
        self.lab_point.setText("Punto")
        self.lab_point.setGeometry(QRect(220, 20, 80, 25))

        self.tex_point = QLineEdit(self)
        self.tex_point.setGeometry(QRect(250, 20, 70, 25))

        self.but_point = QPushButton(self)
        self.but_point.setText("filtrar")
        self.but_point.setGeometry(QRect(320, 20, 70, 25))

        self.tab_polygons = QTableWidget(self)
        self.tab_polygons.setGeometry(QRect(20, 50, 510, 280))
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
        self.but_code.clicked.connect(self.__search_code)
        self.but_point.clicked.connect(self.__search_point)

    def __search_code(self):
        polygon = self.__vector_polygon.search_polygon_code(
            self.tex_code.text())

        if len(polygon) > 0:
            self.__list_polygon(polygon)
        else:
            QMessageBox.information(
                self, "Gestor polígonos", "el código no existe!", QMessageBox.Ok)

    def __search_point(self):
        polygon = self.__vector_polygon.search_polygon_point(
            int(self.tex_point.text()))

        if len(polygon) > 0:
            self.__list_polygon(polygon)
        else:
            QMessageBox.information(
                self, "Gestor polígonos", "no se encontró ningún polígono con la cantidad de puntos!", QMessageBox.Ok)

    def __list_polygon(self, polygon):
        self.tab_polygons.setRowCount(0)
        # self.__vector_polygon.show_polygons()
        for i in range(0, len(polygon)):

            code = QTableWidgetItem(polygon[i].code)
            points = QTableWidgetItem(str(polygon[i].points_count()))
            perimeter = QTableWidgetItem(str(polygon[i].calculate_perimeter()))
            area = QTableWidgetItem(str(polygon[i].calculate_area()))

            table_size = self.tab_polygons.rowCount()
            self.tab_polygons.insertRow(table_size)
            table_size = self.tab_polygons.rowCount()
            self.tab_polygons.setItem(table_size-1, 0, code)
            self.tab_polygons.setItem(table_size-1, 1, points)
            self.tab_polygons.setItem(table_size-1, 2, perimeter)
            self.tab_polygons.setItem(table_size-1, 3, area)

    def __ok(self):
        self.setVisible(False)
