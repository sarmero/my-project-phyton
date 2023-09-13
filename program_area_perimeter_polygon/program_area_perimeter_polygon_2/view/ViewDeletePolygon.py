from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtWidgets import (
    QComboBox,
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


class ViewDeletePolygon(QDialog):
    __vector_polygon = ListPolygon()
    __row_table = 0
    #  __search_button = Button()

    def __init__(self, vector_polygon):
        super().__init__()
        self.__vector_polygon = vector_polygon
        self.__launch_widgets()
        self.__launch_Events()

    def __launch_widgets(self):
        self.setWindowTitle("Eliminar polígono")
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setFixedSize(270, 390)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)

        self.lab_code = QLabel(self)
        self.lab_code.setText("código")
        self.lab_code.setGeometry(50, 10, 50, 25)

        self.lab_listado = QLabel(self)
        self.lab_listado.setText("Listado de puntos")
        self.lab_listado.setGeometry(QRect(50, 45, 100, 25))

        self.com_code = QComboBox(self)
        self.com_code.setGeometry(QRect(110, 10, 80, 25))

        self.tab_point = QTableWidget(self)
        self.tab_point.setGeometry(QRect(50, 80, 170, 260))
        self.tab_point.setColumnCount(2)
        self.tab_point.setRowCount(0)
        self.tab_point.setColumnWidth(0, 75)
        self.tab_point.setColumnWidth(1, 75)
        self.tab_point.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        self.but_delete_polygon = QPushButton(self)
        self.but_delete_polygon.setText("Eliminar")
        self.but_delete_polygon.setGeometry(QRect(40, 350, 100, 30))
        self.but_delete_polygon.setStyleSheet(
            "QPushButton {background-color: green; color: white;} QPushButton:hover{background-color : white; color: green;}"
        )

        self.but_cancel = QPushButton(self)
        self.but_cancel.setText("Cancelar")
        self.but_cancel.setGeometry(QRect(150, 350, 100, 30))
        self.but_cancel.setStyleSheet(
            "QPushButton {background-color: red; color: white;} QPushButton:hover{background-color : white; color: red;}"
        )

    def __launch_Events(self):
        self.but_delete_polygon.clicked.connect(self.__ok)
        self.but_cancel.clicked.connect(self.__cancel)
        self.com_code.currentTextChanged.connect(self.__search_polygon)

    def __ok(self):
        if self.__vector_polygon.get_size() > 0:
            res = QMessageBox.question(
                self,
                "Gestor polígonos",
                "Esta seguro que desea eliminar este polígono",
                QMessageBox.Yes,
                QMessageBox.No,
            )
            if res == 16384:
                code = self.com_code.currentText()
                self.__vector_polygon.delete_polygon(code)
                QMessageBox.information(
                    self,
                    "Gestor polígonos",
                    "Polígono eliminado correctamente",
                    QMessageBox.Ok,
                )
                self.setVisible(False)
        else:
            QMessageBox.information(
                self, "Gestor polígonos", "Error, seleccione un código", QMessageBox.Ok
            )

    def __cancel(self):
        self.setVisible(False)

    def initWindow(self):
        self.tab_point.setRowCount(0)
        self.__update()

    def __search_polygon(self):
        self.tab_point.setRowCount(0)
        item = self.com_code.currentText()
        polygon = self.__vector_polygon.show_polygon(item)

        if polygon != None:
            for i in range(polygon.points_count()):
                x = polygon.point_x[i]
                y = polygon.point_y[i]

                ite_x = QTableWidgetItem(str(x))
                ite_y = QTableWidgetItem(str(y))

                self.tab_point.insertRow(self.tab_point.rowCount())
                self.tab_point.setItem(self.tab_point.rowCount() - 1, 0, ite_x)
                self.tab_point.setItem(self.tab_point.rowCount() - 1, 1, ite_y)

    def __update(self):
        self.com_code.clear()

        for i in range(self.__vector_polygon.get_size()):
            self.com_code.addItem(str(self.__vector_polygon.array_polygon[i].code))
