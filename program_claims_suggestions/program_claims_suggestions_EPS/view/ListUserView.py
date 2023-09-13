from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import QRect, QRegExp, Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *
from component.StyleWidget import StyleWidget

from controller.ListSuggestion import ListSuggestion
from controller.ListUser import ListUser


class ListUserView(QDialog):
    __list_user = ListUser()

    def __init__(self, list_user):
        super().__init__()
        self.__list_user = list_user
        self.__styleWidget = StyleWidget("Comic Sans MS")

        self.__launch_widgets()
        self.__launch_Events()

    def __launch_widgets(self):
        self.setWindowTitle("Listado de usuarios")
        self.resize(800, 500)
        self.setWindowIcon(QIcon("images/icon.png"))
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        style = self.__styleWidget.styleDialog("white")

        canvas = QPixmap("images/fondo_list_user.png")
        self.lab_background = QLabel(self)
        self.lab_background.setGeometry(QRect(0, 0, 800, 500))
        self.lab_background.setPixmap(canvas)

        self.lab_id = QLabel(self)
        self.lab_id.setText("Identificación:")
        self.lab_id.setObjectName("labelId")
        self.lab_id.setGeometry(QRect(186, 30, 100, 25))
        style += self.__styleWidget.styleLabel("labelId", "white", "#351C75", 13, "bold")

        self.tex_id = QLineEdit(self)
        self.tex_id.setGeometry(QRect(279, 30, 150, 25))
        self.tex_id.setObjectName("texId")
        self.tex_id.setAlignment(Qt.AlignHCenter)
        self.tex_id.setValidator(QtGui.QRegExpValidator(QRegExp("[0-9]{1,10}"), self))
        style += self.__styleWidget.styleLine("texId",13)

        self.but_search_id = QPushButton(self)
        self.but_search_id.setText("Buscar")
        self.but_search_id.setGeometry(QRect(436, 30, 65, 25))
        self.but_search_id.setObjectName("buttonSearch")
        style += self.__styleWidget.styleButton("buttonSearch", "#4e91cd", "white", 12, "bold", 12)

        self.but_show_all = QPushButton(self)
        self.but_show_all.setText("Mostrar Todo")
        self.but_show_all.setGeometry(QRect(509, 30, 110, 25))
        self.but_show_all.setObjectName("buttonAll")
        style += self.__styleWidget.styleButton("buttonAll", "white", "#351C75", 12, "bold", 12)

        self.tab_users = QTableWidget(self)
        self.tab_users.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tab_users.setGeometry(QRect(30, 70, 740, 370))
        self.tab_users.setColumnCount(5)
        self.tab_users.setRowCount(0)
        self.tab_users.setColumnWidth(0, 90)
        self.tab_users.setColumnWidth(1, 200)
        self.tab_users.setColumnWidth(2, 150)
        self.tab_users.setColumnWidth(3, 90)
        self.tab_users.setColumnWidth(4, 200)
    

        ite_id = QTableWidgetItem("Identificación")
        # ite_code.setSizeHint(QSize(100,30))
        self.tab_users.setHorizontalHeaderItem(0, ite_id)
        ite_name = QTableWidgetItem("Nombre")
        self.tab_users.setHorizontalHeaderItem(1, ite_name)
        ite_address = QTableWidgetItem("Dirección")
        self.tab_users.setHorizontalHeaderItem(2, ite_address)
        ite_phone = QTableWidgetItem("Celular")
        self.tab_users.setHorizontalHeaderItem(3, ite_phone)
        ite_email = QTableWidgetItem("Email")
        self.tab_users.setHorizontalHeaderItem(4, ite_email)
    

        self.tab_users.setAlternatingRowColors(True)
        self.tab_users.setObjectName("table")
        style += self.__styleWidget.styleTable("table", 12, "lightgreen", "white")

        self.but_acepte = QPushButton(self)
        self.but_acepte.setText("Aceptar")
        self.but_acepte.setGeometry(QRect(366, 456, 90, 30))
        self.but_acepte.setObjectName("buttonAcepte")
        style += self.__styleWidget.styleButton("buttonAcepte", "green", "white",  13, "bold", 12)

        self.setStyleSheet(str(style))


    def __launch_Events(self):
        self.but_acepte.clicked.connect(self. __ok)
        self.but_search_id.clicked.connect(self. __show_by_id)
        self.but_show_all.clicked.connect(self. __show_all)

    def __ok(self):
        self.setVisible(False)

    def __show_by_id(self):
        self.tab_users.setRowCount(0)
        if self.tex_id.text() != "":
            user = self.__list_user.search_by_id(self.tex_id.text())

            if user != None:
                self.__addRow(user)
            else:
                QMessageBox.warning(self,"Benavides EPS","No se encontraron registros",QMessageBox.Ok,)
        else:
            QMessageBox.critical(self,"Benavides EPS","Por favor ingrese una identificación",QMessageBox.Ok,)

    def __show_all(self):
        self.tab_users.setRowCount(0)
        list = self.__list_user.get_list()
        

        if list.size() > 0:
            i = list.front()
            while i != None:
                print("usuario: ", )
                self.__addRow(i.value)
                i = i.next
        else:
            QMessageBox.warning(self,"Benavides EPS","No se encontraron registros ",QMessageBox.Ok,)
        
    def __addRow(self, user):
        ite_id = QTableWidgetItem(user.get_id())
        ite_name = QTableWidgetItem(user.get_name())
        ite_address = QTableWidgetItem(user.get_address())
        ite_phone = QTableWidgetItem(user.get_phone())
        ite_mail = QTableWidgetItem(user.get_mail())

        self.tab_users.insertRow(self.tab_users.rowCount())
        self.tab_users.setItem(self.tab_users.rowCount() - 1, 0, ite_id)
        self.tab_users.setItem(self.tab_users.rowCount() - 1, 1, ite_name)
        self.tab_users.setItem(self.tab_users.rowCount() - 1, 2, ite_address)
        self.tab_users.setItem(self.tab_users.rowCount() - 1, 3, ite_phone)
        self.tab_users.setItem(self.tab_users.rowCount() - 1, 4, ite_mail)
    
    def init_window(self):
        self.tex_id.clear()
        self.tab_users.setRowCount(0)



