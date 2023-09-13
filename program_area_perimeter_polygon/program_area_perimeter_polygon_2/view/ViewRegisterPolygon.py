from PyQt5 import QtGui
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

from classes.Polygon import Polygon
from controller.ListPolygon import ListPolygon


class ViewRegisterPolygon(QDialog):
    __vector_polygon = ListPolygon()
    #  __search_button = Button()

    def __init__(self, vector_polygon):
        super().__init__()
        self.__vector_polygon = vector_polygon
        self.__launch_widgets()
        self.__launch_Events()

    def __launch_widgets(self):
        self.setWindowTitle("Gestor de polígono")
        self.setFixedSize(270, 390)
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)

        self.lab_code = QLabel(self)
        self.lab_code.setText("código")
        self.lab_code.setGeometry(20, 10, 50, 25)

        self.lab_listado = QLabel(self)
        self.lab_listado.setText("Listado de puntos")
        self.lab_listado.setGeometry(QRect(20, 45, 100, 25))

        self.tex_code = QLineEdit(self)
        self.tex_code.setGeometry(QRect(80, 10, 50, 25))

        self.but_add_point = QPushButton(self)
        self.but_add_point.setText("+")
        self.but_add_point.setGeometry(QRect(210, 220, 30, 30))
        self.but_add_point.setStyleSheet(
            "QPushButton {background-color: lightgreen; color: black;} QPushButton:hover{background-color : green;color: black;}"
        )

        self.lab_x = QLabel(self)
        self.lab_x.setText("X")
        self.lab_x.setGeometry(200, 80, 50, 25)

        self.tex_x = QLineEdit(self)
        self.tex_x.setGeometry(QRect(200, 115, 50, 25))

        self.lab_y = QLabel(self)
        self.lab_y.setText("Y")
        self.lab_y.setGeometry(200, 150, 50, 25)

        self.tex_y = QLineEdit(self)
        self.tex_y.setGeometry(QRect(200, 185, 50, 25))

        self.tab_point = QTableWidget(self)
        self.tab_point.setGeometry(QRect(20, 80, 170, 260))
        self.tab_point.setColumnCount(2)
        self.tab_point.setRowCount(0)
        self.tab_point.setColumnWidth(0, 75)
        self.tab_point.setColumnWidth(1, 75)

        ite_x = QTableWidgetItem("x")
        self.tab_point.setHorizontalHeaderItem(0, ite_x)
        ite_y = QTableWidgetItem("y")
        self.tab_point.setHorizontalHeaderItem(1, ite_y)

        self.but_ok = QPushButton(self)
        self.but_ok.setText("Aceptar")
        self.but_ok.setGeometry(QRect(40, 350, 100, 30))
        self.but_ok.setStyleSheet(
            "QPushButton {background-color: lightgreen; color: black;} QPushButton:hover{background-color : green; color: white;}"
        )

        self.but_cancel = QPushButton(self)
        self.but_cancel.setText("Cancelar")
        self.but_cancel.setGeometry(QRect(150, 350, 100, 30))
        self.but_cancel.setStyleSheet(
            "QPushButton {background-color: red; color: white;} QPushButton:hover{background-color : white; color: red;}"
        )

    def __launch_Events(self):
        self.but_ok.clicked.connect(self.__ok)
        self.but_cancel.clicked.connect(self.__cancel)
        self.but_add_point.clicked.connect(self.__add_points)
        self.tex_y.textChanged.connect(self.__validate_line_y)
        self.tex_x.textChanged.connect(self.__validate_line_x)

    def __validate_line_x(self):
        self.tex_x.setText(self.__validator_line(self.tex_x.text()))

    def __validate_line_y(self):
        self.tex_y.setText(self.__validator_line(self.tex_y.text()))

    def __validator_line(self, tex_point):
        size = len(tex_point)
        if size > 0:
            char = ord(tex_point[-1:])

            if char == 46 and size == 1:
                tex_point = tex_point.rstrip(chr(char))
            elif char == 46 and size == 2 and tex_point[:1] == "-":
                tex_point = tex_point.rstrip(chr(char))
            elif char == 46 and tex_point.count(".") > 1:
                if tex_point[(size - 2) : (size - 1)] == ".":
                    tex_point = tex_point.rstrip(chr(char)) + "."
                else:
                    tex_point = tex_point.rstrip(chr(char))
            elif char == 45 and size > 1:
                if size == 2 and tex_point[:1] == "-":
                    tex_point = "-" + tex_point.rstrip(chr(char))
                else:
                    tex_point = tex_point.rstrip(chr(char))
            elif (char < 48 or char > 57) and char != 46 and char != 45:
                tex_point = tex_point.rstrip(chr(char))

            if tex_point.count(".") > 1:
                tex_point = tex_point.replace(".", "", 1)
            if tex_point.count("-") > 1 and tex_point[:1] == "-":
                tex = tex_point[1 : len(tex_point)]
                tex_point = "-" + tex.replace("-", "", 1)
            elif tex_point.count("-") > 0 and tex_point[:1] != "-":
                tex_point = tex_point.replace("-", "", 1)

            if tex_point[:1] == "-" and tex_point[1:2] == ".":
                tex_point = tex_point.replace(".", "", 1)

            for i in range(len(tex_point)):
                print("** ", tex_point[i : i + 1])
                if (
                    (ord(tex_point[i : i + 1]) < 48 or ord(tex_point[i : i + 1]) > 57)
                    and ord(tex_point[i : i + 1]) != 46
                    and ord(tex_point[i : i + 1]) != 45
                    and tex_point[i : i + 1] != " "
                ):
                    tex_point = tex_point.replace(tex_point[i : i + 1], " ", 1)

            tex_point = tex_point.replace(" ", "", tex_point.count(" "))

            return tex_point

    def __add_points(self):
        if self.tex_x.text() != "" and self.tex_y.text() != "":
            x = self.tex_x.text()
            y = self.tex_y.text()
            ite_x = QTableWidgetItem(x)
            ite_y = QTableWidgetItem(y)

            self.tab_point.insertRow(self.tab_point.rowCount())
            self.tab_point.setItem(self.tab_point.rowCount() - 1, 0, ite_x)
            self.tab_point.setItem(self.tab_point.rowCount() - 1, 1, ite_y)

            self.tex_x.setText("")
            self.tex_y.setText("")
        else:
            QMessageBox.information(
                self,
                "Gestor polígonos",
                "Error, por favor ingrese una cifra en las casillas bacías  ",
                QMessageBox.Ok,
            )

    def __ok(self):
        if self.tab_point.rowCount() > 0:
            if self.tex_code.text() != "":
                code = self.tex_code.text()
                if self.__vector_polygon.search_code(code) == False:
                    point_x = []
                    point_y = []
                    quantity_points = self.tab_point.rowCount()

                    for i in range(quantity_points):
                        ite_x = self.tab_point.item(i, 0)
                        ite_y = self.tab_point.item(i, 1)
                        x = float(ite_x.text())
                        y = float(ite_y.text())
                        point_x.append(x)
                        point_y.append(y)

                    polygon = Polygon(code, quantity_points, point_y, point_x)
                    self.__vector_polygon.add_polygon(polygon)

                    QMessageBox.information(
                        self,
                        "Gestor polígonos",
                        "Polígono registrado correctamente",
                        QMessageBox.Ok,
                    )
                    self.setVisible(False)
                else:
                    QMessageBox.information(
                        self,
                        "Gestor polígonos",
                        "El código ya existe, por favor escriba otro código",
                        QMessageBox.Ok,
                    )

            else:
                QMessageBox.information(
                    self,
                    "Gestor polígonos",
                    "Error, por favor inserte un código",
                    QMessageBox.Ok,
                )
        else:
            QMessageBox.information(
                self, "Gestor polígonos", "Error, la tabla esta bacía  ", QMessageBox.Ok
            )

    def __cancel(self):
        self.setVisible(False)

    def initWindow(self):
        self.tex_x.setText("")
        self.tex_y.setText("")
        self.tex_code.setText("")
        self.tab_point.setRowCount(0)
