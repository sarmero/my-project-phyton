from PyQt5.QtCore import QRect, Qt
from PyQt5.QtWidgets import *
from component.StyleWidget import StyleWidget

from controller.ListSuggestion import ListSuggestion
from controller.ListUser import ListUser


class ListPccsView(QDialog):
    __list_pccs = ListSuggestion()
    __list_user = ListUser()

    def __init__(self, list_pccs, list_user):
        super().__init__()
        self.__list_pccs = list_pccs
        self.__list_user = list_user
        self.__styleWidget = StyleWidget()

        self.__launch_widgets()
        self.__launch_Events()

    def __launch_widgets(self):
        self.setWindowTitle("Gestor de polígono")
        self.setFixedSize(570, 400)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        style = self.__styleWidget.styleDialog("#13293d")

        self.lab_id = QLabel(self)
        self.lab_id.setText("Identificación: ")
        self.lab_id.setGeometry(40, 20, 87, 25)
        self.lab_id.setObjectName("labelId")
        style += self.__styleWidget.styleLabel("labelId", "orange", "#4e91cd", "Arial", 13, "bold")

        self.tex_id = QLineEdit(self)
        self.tex_id.setGeometry(QRect(132, 20, 150, 25))
        self.tex_id.setObjectName("texId")
        style += self.__styleWidget.styleLine("texId", "Arial", 12)

        self.but_search = QPushButton(self)
        self.but_search.setText("Buscar")
        self.but_search.setGeometry(QRect(287, 20, 65, 25))
        self.but_search.setObjectName("buttonSearch")
        style += self.__styleWidget.styleButton("buttonSearch", "#4e91cd", "white", "Arial", 12, "bold", 12)

        self.lab_guy = QLabel(self)
        self.lab_guy.setText("Tipo: ")
        self.lab_guy.setGeometry(372, 20, 40, 25)
        self.lab_guy.setObjectName("labelGuy")
        style += self.__styleWidget.styleLabel("labelGuy", "orange", "#4e91cd", "Arial", 13, "bold")


        self.com_guy = QComboBox(self)
        self.com_guy.setGeometry(QRect(410, 20, 110, 25))
        self.com_guy.setObjectName("com")
        style += self.__styleWidget.styleLine("com", "Arial", 12)

        self.tab_point = QTableWidget(self)
        self.tab_point.setGeometry(QRect(25, 55, 520, 290))
        self.tab_point.setColumnCount(5)
        self.tab_point.setRowCount(0)
        self.tab_point.setColumnWidth(0, 93)
        self.tab_point.setColumnWidth(1, 150)
        self.tab_point.setColumnWidth(2, 70)
        self.tab_point.setColumnWidth(3, 100)
        self.tab_point.setColumnWidth(4, 100)

        ite_code = QTableWidgetItem("Código")
        self.tab_point.setHorizontalHeaderItem(0, ite_code)
        ite_id = QTableWidgetItem("Identificación")
        self.tab_point.setHorizontalHeaderItem(1, ite_id)
        ite_guy = QTableWidgetItem("Tipo")
        self.tab_point.setHorizontalHeaderItem(2, ite_guy)
        ite_state = QTableWidgetItem("Estado")
        self.tab_point.setHorizontalHeaderItem(3, ite_state)
        ite_date = QTableWidgetItem("Fecha")
        self.tab_point.setHorizontalHeaderItem(4, ite_date)

        self.but_detail = QPushButton(self)
        self.but_detail.setText("Mostrar detalle")
        self.but_detail.setGeometry(QRect(205, 360, 160, 30))
        self.but_detail.setObjectName("buttonDetail")
        style += self.__styleWidget.styleButton("buttonDetail", "orange", "#13293d", "Arial", 12, "bold", 12)

        self.setStyleSheet(str(style))


    def __launch_Events(self):
        pass
