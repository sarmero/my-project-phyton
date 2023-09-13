from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtCore import QRect, QRegExp, Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *
from component.StyleWidget import StyleWidget
from controller.ListSuggestion import ListSuggestion
from view.DetailView import DetailView


class ListSuggestionView(QDialog):
    __list_suggestion = ListSuggestion()

    def __init__(self, list_suggestion, list_user):
        super().__init__()
        self.__list_suggestion = list_suggestion
        self.__window_show_detail = DetailView(list_suggestion, list_user)
        self.__code = ""
        self.__styleWidget = StyleWidget("Comic Sans MS")

        self.__launch_widgets()
        self.__launch_Events()

    def __launch_widgets(self):
        self.setWindowTitle("Listado de sugestión")
        self.resize(710, 450)
        self.setWindowIcon(QIcon("images/icon.png"))
        self.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)
        style = self.__styleWidget.styleDialog("white")

        canvas = QPixmap("images/fondo_list_suggestion.png")
        self.lab_background = QLabel(self)
        self.lab_background.setGeometry(QRect(0, 0, 710, 450))
        self.lab_background.setPixmap(canvas)

        self.lab_search_code = QLabel(self)
        self.lab_search_code.setText("Código:")
        self.lab_search_code.setGeometry(35, 25, 50, 25)
        self.lab_search_code.setObjectName("labelCodeSearch")
        style += self.__styleWidget.styleLabel("labelCodeSearch", "#351C75", "green", 13, "bold")

        self.tex_code = QLineEdit(self)
        self.tex_code.setGeometry(QRect(30, 48, 93, 25))
        self.tex_code.setObjectName("texCode")
        self.tex_code.setAlignment(Qt.AlignHCenter)
        self.tex_code.setValidator(QtGui.QRegExpValidator(QRegExp("[A-Z0-9]{1,10}"), self))
        style += self.__styleWidget.styleLine("texCode",  13)

        self.but_search_code = QPushButton(self)
        self.but_search_code.setText("Buscar")
        self.but_search_code.setGeometry(QRect(130, 48, 65, 25))
        self.but_search_code.setObjectName("buttonSearch")
        style += self.__styleWidget.styleButton("buttonSearch", "#4e91cd", "white", 12, "bold", 12)

        self.lab_id = QLabel(self)
        self.lab_id.setText("Identificación:")
        self.lab_id.setObjectName("labelId")
        self.lab_id.setGeometry(QRect(237, 25, 100, 25))
        style += self.__styleWidget.styleLabel("labelId", "white", "#351C75", 13, "bold")

        self.tex_id = QLineEdit(self)
        self.tex_id.setGeometry(QRect(232, 48, 150, 25))
        self.tex_id.setObjectName("texId")
        self.tex_id.setAlignment(Qt.AlignHCenter)
        self.tex_id.setValidator(QtGui.QRegExpValidator(QRegExp("[0-9]{1,10}"), self))
        style += self.__styleWidget.styleLine("texId",13)

        self.but_search_id = QPushButton(self)
        self.but_search_id.setText("Buscar")
        self.but_search_id.setGeometry(QRect(391, 48, 65, 25))
        self.but_search_id.setObjectName("buttonSearch")
        style += self.__styleWidget.styleButton("buttonSearch", "#4e91cd", "white", 12, "bold", 12)

        self.lab_guy = QLabel(self)
        self.lab_guy.setText("Tipo:")
        self.lab_guy.setGeometry(507, 25, 35, 25)
        self.lab_guy.setObjectName("labelGuy")
        style += self.__styleWidget.styleLabel("labelGuy", "white", "#351C75",  13, "bold")

        self.com_guy = QComboBox(self)
        self.com_guy.setGeometry(QRect(502, 48, 178, 25))
        self.com_guy.setObjectName("texGuy")
        self.com_guy.addItems(["Petición", "Queja", "Reclamo", "Sugerencia"])
        style += self.__styleWidget.styleLine("texGuy", 12)

        self.tab_suggestions = QTableWidget(self)
        self.tab_suggestions.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.tab_suggestions.setGeometry(QRect(30, 92, 650, 300))
        self.tab_suggestions.setColumnCount(7)
        self.tab_suggestions.setRowCount(0)
        self.tab_suggestions.setColumnWidth(0, 50)
        self.tab_suggestions.setColumnWidth(1, 80)
        self.tab_suggestions.setColumnWidth(2, 180)
        self.tab_suggestions.setColumnWidth(3, 80)
        self.tab_suggestions.setColumnWidth(4, 80)
        self.tab_suggestions.setColumnWidth(5, 100)
        self.tab_suggestions.setColumnWidth(6, 50)

        ite_code = QTableWidgetItem("Código")
        # ite_code.setSizeHint(QSize(100,30))
        self.tab_suggestions.setHorizontalHeaderItem(0, ite_code)
        ite_id = QTableWidgetItem("Identificación")
        self.tab_suggestions.setHorizontalHeaderItem(1, ite_id)
        ite_description = QTableWidgetItem("Descripción")
        self.tab_suggestions.setHorizontalHeaderItem(2, ite_description)
        ite_guy = QTableWidgetItem("Tipo")
        self.tab_suggestions.setHorizontalHeaderItem(3, ite_guy)
        ite_state = QTableWidgetItem("Estado")
        self.tab_suggestions.setHorizontalHeaderItem(4, ite_state)
        ite_date = QTableWidgetItem("Fecha")
        self.tab_suggestions.setHorizontalHeaderItem(5, ite_date)
        ite_hour = QTableWidgetItem("Hora")
        self.tab_suggestions.setHorizontalHeaderItem(6, ite_hour)

        self.tab_suggestions.setAlternatingRowColors(True)
        self.tab_suggestions.setObjectName("table")
        style += self.__styleWidget.styleTable("table", 12, "lightgreen", "white")
        
        self.but_detail = QPushButton(self)
        self.but_detail.setText("Mostrar detalle")
        self.but_detail.setGeometry(QRect(30, 409, 115, 30))
        self.but_detail.setObjectName("buttonDetail")
        style += self.__styleWidget.styleButton("buttonDetail", "#4e91cd", "white", 13, "bold", 12)

        self.but_acepte = QPushButton(self)
        self.but_acepte.setText("Aceptar")
        self.but_acepte.setGeometry(QRect(321, 409, 80, 30))
        self.but_acepte.setObjectName("buttonAcepte")
        style += self.__styleWidget.styleButton("buttonAcepte", "green", "white",  13, "bold", 12)

        self.setStyleSheet(str(style))

    def __launch_Events(self):
        self.but_search_code.clicked.connect(self. __report_by_code)
        self.but_search_id.clicked.connect(self. __report_by_id)
        self.com_guy.currentTextChanged.connect(self. __report_by_guy)
        self.but_acepte.clicked.connect(self. __ok)
        self.but_detail.clicked.connect(self. __show_detail)
        self.tab_suggestions.itemSelectionChanged.connect(self.__selected_row)


    def __report_by_code(self):
        self.tab_suggestions.setRowCount(0)
        if self.tex_code.text() != "":
            suggestion = self.__list_suggestion.search_by_code(self.tex_code.text())

            if suggestion != None:
                self.__addRow(suggestion)
            else:
                QMessageBox.warning(self,"Benavides EPS","No hay registros",QMessageBox.Ok,)
        else:
            QMessageBox.critical(self,"Benavides EPS","Por favor ingrese un código",QMessageBox.Ok,)

    def __report_by_id(self):
        self.tab_suggestions.setRowCount(0)
        if self.tex_id.text() != "":
            list = self.__list_suggestion.search_by_id(self.tex_id.text())

            if list.size() > 0:
                i = list.front()
                while i != None:
                    self.__addRow(i.value)
                    i = i.next
            else:
                QMessageBox.warning(self,"Benavides EPS","No hay registros",QMessageBox.Ok,)
        else:
            QMessageBox.critical(self,"Benavides EPS","Por favor ingrese una identificación",QMessageBox.Ok,)

    def __report_by_guy(self):
        if self.isVisible() == True:
            self.tab_suggestions.setRowCount(0)
            if self.com_guy.currentText() != "":
                list = self.__list_suggestion.search_by_guy(self.com_guy.currentText())

                if list.size() > 0:
                    i = list.front()
                    while i != None:
                        self.__addRow(i.value)
                        i = i.next
                else:
                    QMessageBox.warning(self,"Benavides EPS","No hay registros",QMessageBox.Ok,)
            else:
                QMessageBox.critical(self,"Benavides EPS","No hay ningún registro",QMessageBox.Ok,)

    def __addRow(self, suggestion):
        ite_code = QTableWidgetItem(suggestion.get_code())
        ite_id = QTableWidgetItem(suggestion.get_id_user())
        ite_description = QTableWidgetItem(suggestion.get_description())
        ite_guy = QTableWidgetItem(suggestion.get_guy())
        ite_state = QTableWidgetItem("Revisado" if suggestion.get_state() == True else "Pendiente")
        ite_date = QTableWidgetItem(suggestion.get_date())
        ite_hour = QTableWidgetItem(suggestion.get_hour())

        self.tab_suggestions.insertRow(self.tab_suggestions.rowCount())
        self.tab_suggestions.setItem(self.tab_suggestions.rowCount() - 1, 0, ite_code)
        self.tab_suggestions.setItem(self.tab_suggestions.rowCount() - 1, 1, ite_id)
        self.tab_suggestions.setItem(self.tab_suggestions.rowCount() - 1, 2, ite_description)
        self.tab_suggestions.setItem(self.tab_suggestions.rowCount() - 1, 3, ite_guy)
        self.tab_suggestions.setItem(self.tab_suggestions.rowCount() - 1, 4, ite_state)
        self.tab_suggestions.setItem(self.tab_suggestions.rowCount() - 1, 5, ite_date)
        self.tab_suggestions.setItem(self.tab_suggestions.rowCount() - 1, 6, ite_hour)

    def __ok(self):
        self.setVisible(False)

    def __show_detail(self):
        if self.__code != "":
            self.__window_show_detail.init_window()
            self.__window_show_detail.set_data(self.__code)
            self.__window_show_detail.setVisible(True)

    def init_window(self):
        self.tex_code.clear()
        self.tex_id.clear()
        self.tab_suggestions.setRowCount(0)
        
    
    def __selected_row(self):
        if self.tab_suggestions.rowCount() > 0:
            items = self.tab_suggestions.selectedItems()
            if items != []:
                ite_code = self.tab_suggestions.item(items[0].row(), 0)
                
                self.__code = ite_code.text()
                print("el código es: ",self.__code)
                self.tab_suggestions.clearSelection()
        else:
            QMessageBox.critical(self,"Benavides EPS","Aun no ha seleccionado una fila",QMessageBox.Ok,)



