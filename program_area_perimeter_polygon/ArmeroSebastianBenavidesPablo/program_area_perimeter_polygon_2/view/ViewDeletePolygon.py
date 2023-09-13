from PyQt5 import QtGui
from PyQt5.QtCore import QRect, Qt
from PyQt5.QtWidgets import QComboBox, QDialog, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox
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

        self.tab_point = QTableWidget(self)
        self.tab_point.setGeometry(QRect(50, 80, 170, 260))
        self.tab_point.setColumnCount(2)
        self.tab_point.setRowCount(0)
        self.tab_point.setColumnWidth(0, 75)
        self.tab_point.setColumnWidth(1, 75)

        self.but_delete_polygon = QPushButton(self)
        self.but_delete_polygon.setText("Eliminar")
        self.but_delete_polygon.setGeometry(QRect(40, 350, 100, 30))

        self.but_cancel = QPushButton(self)
        self.but_cancel.setText("Cancelar")
        self.but_cancel.setGeometry(QRect(150, 350, 100, 30))

    def __launch_Events(self):
        self.but_delete_polygon.clicked.connect(self.__ok)
        self.but_cancel.clicked.connect(self.__cancel)
        self.tab_point.itemSelectionChanged.connect(self.__selected_point)
        self.com_code.currentTextChanged.connect(self.__search_polygon)

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

    def __ok(self):

        res = QMessageBox.question(self,
                                   "Gestor polígonos", "Esta seguro que desea eliminar este polígono", QMessageBox.Yes, QMessageBox.No)
        if res == 16384:
            code = self.com_code.currentText()
            self.__vector_polygon.delete_polygon(code)
            QMessageBox.information(
                self, "Gestor polígonos", "Polígono eliminado correctamente", QMessageBox.Ok)
            self.setVisible(False)

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
                self.tab_point.setItem(self.tab_point.rowCount()-1, 0, ite_x)
                self.tab_point.setItem(self.tab_point.rowCount()-1, 1, ite_y)

    def __update(self):
        self.com_code.clear()

        for i in range(self.__vector_polygon.get_size()):
            self.com_code.addItem(
                str(self.__vector_polygon.array_polygon[i].code))
