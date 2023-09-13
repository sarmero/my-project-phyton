from PyQt5 import QtGui
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtWidgets import QComboBox, QDialog, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox
from classes.Polygon import Polygon


from controller.ListPolygon import ListPolygon


class ViewUpdatePolygon(QDialog):
    __vector_polygon = ListPolygon()
    __row_table = 0
  #  __search_button = Button()

    def __init__(self, vector_polygon):
        super().__init__()
        self.__vector_polygon = vector_polygon
        self.__launch_widgets()
        self.__launch_Events()

    def __launch_widgets(self):
        self.setWindowTitle("Modificar polígono")
        self.setFixedSize(270, 390)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)

        self.lab_code = QLabel(self)
        self.lab_code.setText("código")
        self.lab_code.setGeometry(20, 10, 50, 25)

        self.lab_listado = QLabel(self)
        self.lab_listado.setText("Listado de puntos")
        self.lab_listado.setGeometry(QRect(20, 45, 100, 25))

        self.com_code = QComboBox(self)
        self.com_code.setGeometry(QRect(80, 10, 50, 25))

        self.but_add_point = QPushButton(self)
        self.but_add_point.setText("+")
        self.but_add_point.setGeometry(QRect(210, 220, 30, 30))

        self.but_update = QPushButton(self)
        self.but_update.setText("/")
        self.but_update.setGeometry(QRect(210, 260, 30, 30))

        self.but_delete = QPushButton(self)
        self.but_delete.setText("-")
        self.but_delete.setGeometry(QRect(210, 300, 30, 30))

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

        self.but_cancel = QPushButton(self)
        self.but_cancel.setText("Cancelar")
        self.but_cancel.setGeometry(QRect(150, 350, 100, 30))

    def __launch_Events(self):
        self.but_ok.clicked.connect(self.__ok)
        self.but_delete.clicked.connect(self.__delete_point)
        self.but_update.clicked.connect(self.__update_point)
        self.but_cancel.clicked.connect(self.__cancel)
        self.but_add_point.clicked.connect(self.__add_points)
        self.tab_point.itemSelectionChanged.connect(self.__selected_point)
        self.com_code.currentTextChanged.connect(self.__search_polygon)
        #self.tex_x.validator

    def __selected_point(self):
        if self.tab_point.rowCount() > 0:
            items = self.tab_point.selectedItems()
            if items != []:
                self.__row_table = items[0].row()

                ite_x = self.tab_point.item(items[0].row(), 0)
                ite_y = self.tab_point.item(items[0].row(), 1)

                self.tex_x.setText(ite_x.text())
                self.tex_y.setText(ite_y.text())
                self.tab_point.clearSelection()

    def __add_points(self):
        x = self.tex_x.text()
        y = self.tex_y.text()
        ite_x = QTableWidgetItem(x)
        ite_y = QTableWidgetItem(y)

        self.tab_point.insertRow(self.tab_point.rowCount())
        self.tab_point.setItem(self.tab_point.rowCount()-1, 0, ite_x)
        self.tab_point.setItem(self.tab_point.rowCount()-1, 1, ite_y)

        self.tex_x.setText("")
        self.tex_y.setText("")

    def __delete_point(self):
        self.tab_point.clearSelection()
        QMessageBox.information(
            self, "Gestor polígonos", "Punto eliminado correctamente", QMessageBox.Ok)

    def __update_point(self):
        x = self.tex_x.text()
        y = self.tex_y.text()
        ite_x = QTableWidgetItem(x)
        ite_y = QTableWidgetItem(y)

        self.tab_point.setItem(self.__row_table, 0, ite_x)
        self.tab_point.setItem(self.__row_table, 1, ite_y)
        self.tex_x.setText("")
        self.tex_y.setText("")

        QMessageBox.information(
            self, "Gestor polígonos", "Punto modificado correctamente", QMessageBox.Ok)

    def __ok(self):
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

        code = self.com_code.currentText()
        polygon = Polygon(code, quantity_points, point_y, point_x)
        self.__vector_polygon.update_polygon(polygon)

        QMessageBox.information(
            self, "Gestor polígonos", "Polígono modificado correctamente", QMessageBox.Ok)
        self.setVisible(False)

    def __cancel(self):
        self.setVisible(False)

    def initWindow(self):
        self.tex_x.setText("")
        self.tex_y.setText("")
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
                self.tab_point.setItem(self.tab_point.rowCount()-1, 0, ite_x)
                self.tab_point.setItem(self.tab_point.rowCount()-1, 1, ite_y)

    def __update(self):
        self.com_code.clear()

        for i in range(self.__vector_polygon.get_size()):
            self.com_code.addItem(
                str(self.__vector_polygon.array_polygon[i].code))
