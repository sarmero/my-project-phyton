from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtWidgets import (
    QDialog,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
)

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
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)

        self.but_ok = QPushButton(self)
        self.but_ok.setText("Aceptar")
        self.but_ok.setGeometry(QRect(225, 337, 100, 30))
        self.but_ok.setStyleSheet(
            "QPushButton {background-color: blue; color: white;} QPushButton:hover{background-color : lightgreen; color: black;}"
        )

        self.lab_code = QLabel(self)
        self.lab_code.setText("Código")
        self.lab_code.setGeometry(QRect(80, 20, 50, 25))

        self.tex_code = QLineEdit(self)
        self.tex_code.setGeometry(QRect(120, 20, 70, 25))

        self.but_code = QPushButton(self)
        self.but_code.setText("filtrar")
        self.but_code.setGeometry(QRect(200, 20, 60, 25))
        self.but_code.setStyleSheet(
            "QPushButton {background-color: blue; color: white;} QPushButton:hover{background-color : green; color: black;}"
        )
        self.lab_point = QLabel(self)
        self.lab_point.setText("Punto")
        self.lab_point.setGeometry(QRect(280, 20, 80, 25))

        self.tex_point = QLineEdit(self)
        self.tex_point.setGeometry(QRect(310, 20, 70, 25))

        self.but_point = QPushButton(self)
        self.but_point.setText("filtrar")
        self.but_point.setGeometry(QRect(390, 20, 60, 25))
        self.but_point.setStyleSheet(
            "QPushButton {background-color: blue; color: white;} QPushButton:hover{background-color : green; color: black;}"
        )

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
        self.tab_polygons.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

    def __launch_Events(self):
        self.but_ok.clicked.connect(self.__ok)
        self.but_code.clicked.connect(self.__search_code)
        self.but_point.clicked.connect(self.__search_point)
        self.tex_point.textChanged.connect(self.__validate_line)

    def __validate_line(self):
        tex_point = self.tex_point.text()
        for i in range(len(tex_point)):
            if (
                ord(tex_point[i : i + 1]) < 48 or ord(tex_point[i : i + 1]) > 57
            ) and tex_point[i : i + 1] != " ":
                tex_point = tex_point.replace(tex_point[i : i + 1], " ", 1)

        tex_point = tex_point.replace(" ", "", tex_point.count(" "))
        self.tex_point.setText(tex_point)

    def __search_code(self):
        if self.__vector_polygon.get_size() > 0:
            if self.tex_code != "":
                polygon = self.__vector_polygon.search_polygon_code(
                    self.tex_code.text()
                )

                if polygon != None:
                    self.__list_polygon(polygon)
                else:
                    QMessageBox.information(
                        self, "Gestor polígonos", "el código no existe!", QMessageBox.Ok
                    )
            else:
                QMessageBox.information(
                    self,
                    "Gestor polígonos",
                    "por favor ingrese un código",
                    QMessageBox.Ok,
                )
        else:
            QMessageBox.information(
                self,
                "Gestor polígonos",
                "No se encuentra ningún polígono listado",
                QMessageBox.Ok,
            )

    def __search_point(self):
        if self.__vector_polygon.get_size() > 0:
            if self.tex_point.text() != "":
                polygon = self.__vector_polygon.search_polygon_point(
                    int(self.tex_point.text())
                )

                if len(polygon) > 0:
                    self.__list_polygon(polygon)
                else:
                    QMessageBox.information(
                        self,
                        "Gestor polígonos",
                        "no se encontró ningún polígono con la cantidad de puntos!",
                        QMessageBox.Ok,
                    )
            else:
                QMessageBox.information(
                    self,
                    "Gestor polígonos",
                    "por favor ingrese una cantidad valida",
                    QMessageBox.Ok,
                )

        else:
            QMessageBox.information(
                self,
                "Gestor polígonos",
                "No se encuentra ningún polígono listado",
                QMessageBox.Ok,
            )

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
            self.tab_polygons.setItem(table_size - 1, 0, code)
            self.tab_polygons.setItem(table_size - 1, 1, points)
            self.tab_polygons.setItem(table_size - 1, 2, perimeter)
            self.tab_polygons.setItem(table_size - 1, 3, area)

    def __ok(self):
        self.setVisible(False)
